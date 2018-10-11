#! /bin/bash
# StudentNetworkTools Version 0.5
# There is no license on this bit of scripting.
# It would be rediculous if we claim a license 
# as this script is just "glueing" together
# known Bash and Linux commands. 

# Files
	user=/home/pi/.net_tools/txt_files

	file_dhcp_conf=/etc/dhcpcd.conf
	file_dhcp_template=/etc/dhcpcd.conf.template
	file_eth0=$user/eth0_status

	file_wifi_conf=/etc/wpa_supplicant/wpa_supplicant.conf
	file_wifi_template=/etc/wpa_supplicant/wpa_supplicant.conf.template 

	file_menu=$user/menu.txt
	file_eth0_menu=$user/eth0_menu.txt
	file_wlan0_menu=$user/wlan0_menu.txt
	file_net_menu=$user/net_menu.txt

	file_about=$user/about.txt
	file_readme=$user/readme.txt

restart_network () {
	sudo ifconfig eth0 down
	sudo ifconfig eth0 up
	sudo service networking restart
}

eth0_menu () {
	echo " "
	cat $file_eth0_menu
	printf "%s\n" "" " Enter a number from the above IP Menu"
	printf " " 
	read eth0_menu_number
	return $eth0_menu_number
}

eth0_menu_eval () {
	case $1 in
	1)	# hostname
		clear
		hostname="$(ifconfig eth0)"
		printf '%s\n' " " "$hostname" " "
	;;
	2)	# status
		clear
		printf "%s\n" " " " Warning!" \
				" Just because your Pi is in either of the IP modes," \
				" does not mean your Pi has an IP address" 
	    eth0_status=$(<$file_eth0)
	    if [[ $eth0_status == "dhcp" ]]
			then
				printf "%s\n" " " " Your Pi is in DHCP mode" " "
		elif [[ $eth0_status == "static" ]]
			then
				printf "%s\n" " " " Your Pi is in static mode" " " 
		else
				printf "%s\n" " "" Sorry, something went wrong" " "
		fi
	;;
	3)	# Change to DHCP
		clear
		cp /dev/null $file_eth0
		printf "%s\n\n" '' " Change IP to DHCP:"
		sudo rm $file_dhcp_conf
		sudo cp $file_dhcp_template $file_dhcp_conf
		echo "dhcp" >> $file_eth0
		printf '%s\n' " " " Processing, please wait!" " "
		restart_network
	;;
	4)	# Change to static
		clear
		# enter static IP and gateway
			cp /dev/null $file_eth0
			printf "%s\n" "" " Enter static IP"
			printf " "
			read static
			printf "%s\n" "" " Enter gateway IP"
			printf " "
			read gateway
			echo " "
			sudo rm $file_dhcp_conf
			sudo cp $file_dhcp_template $file_dhcp_conf
			echo " interface eth0" | sudo tee -a $file_dhcp_conf >> /dev/null
			echo " static ip_address=$static" | sudo tee -a $file_dhcp_conf
			echo " static routers=$gateway" | sudo tee -a $file_dhcp_conf		    
			echo "static" >> $file_eth0
			printf '%s\n' " " " Processing, please wait!" " "
		restart_network
	;;
	5)	# Return to main menu
		clear
		echo " "
		menu
	;;
	esac		
}

wlan0_menu () {
	echo " "
	cat $file_wlan0_menu
	printf "%s\n" "" " Enter a number from the above WiFi Menu"
	printf " " 
	read wlan0_menu_number
	return $wlan0_menu_number
}

wlan0_menu_eval () {
	case $1 in
	1)	# WiFi IP address
		clear
		hostname="$(ifconfig wlan0)"
		printf '%s\n' " " "$hostname" " "
	;;
	2)	# Scan wlan0
		clear
		wpa_cli scan
	;;
	3) 	# Scan for WiFi networks
		clear
		sudo iwlist wlan0 scan | less
	;;
	4)	# Connect to WiFi SSID
		printf "%s\n" " "
		read -p " Enter SSID = " ssid
		printf "%s\n" " "
		read -p " Enter Key = " psk
		printf "%s\n" " " " You entered SSID = $ssid"\
			" Network Key = $psk"
		read -p " Is this correct? Answer y or n : " response
		if [[ $response == "y" ]]
		then
			sudo ifconfig wlan0 down
			sudo rm $file_wifi_conf
			sudo cp $file_wifi_template $file_wifi_conf
			echo " network={" | sudo tee -a $file_wifi_conf
			echo " ssid=\"$ssid\"" | sudo tee -a $file_wifi_conf
			echo " psk=\"$psk\"" | sudo tee -a $file_wifi_conf
			echo " }" | sudo tee -a $file_wifi_conf	    
			sudo ifconfig wlan0 up
			wpa_cli reconfigure
		else
			echo " Try Again"
		fi
		;;
	5)	# Disconnect to WiFi 
		clear
		printf '%s\n' "  You can only disconnect"\
				"  if a valid SSID is previously entered"\
				"  and you are connected to that Network."\
				"  Do you want to continue? Answer y or n" " "
		read -p "  " answer
		if [[ $answer == "y" ]]
			then
				wpa_cli disconnect
			else
				clear
				wlan0_menu
		fi
	    ;;
	6)	# Reconnect to Wifi 
		clear
		printf '%s\n' "  You can only reconnect"\
				"  if a valid SSID is previously entered"\
				"  and you disconnected to that Network." \
				"  Do you want to continue? Answer y or n" " "
		read -p "  " answer
		if [[ $answer == "y" ]]
			then
				sudo ifconfig wlan0 up
				wpa_cli reconnect
			else
				clear
				wlan0_menu
		fi
	    ;;
	7)	# Disable wlan0 interface
		clear
		printf '%s\n' "  This will disable the WiFi wlan0 interface."\
				"  SSID and Network Key will be deleted."\
				"  Do you want to continue? Answer y or n" " "
		read -p "  " answer
		if [[ $answer == "y" ]]
			then
				sudo ifconfig wlan0 down
				wpa_cli flush
				sudo rm $file_wifi_conf
				sudo cp $file_wifi_template $file_wifi_conf
			else
				clear
				wlan0_menu
		fi
		;;
	8)	# Enable wlan0 interface
		clear
		printf '%s\n' "  This will enable the WiFi wlan0 interface."\
				"  You might have to enter SSID and Network Key" " "
		sudo ifconfig wlan0 up
		printf '%s\n' "  You should scan if wlan0 is enabled."\
				"  Use menu item 2" " "
		;;
	9)	clear
		echo " "
		menu
		;;
	esac
}

menu () {
	echo " "
	cat $file_menu
	printf "%s\n" "" " Enter a number from the above Main Menu"
	printf " " 
	read menu_number
	return $menu_number
}

menu_eval () {
	msg="$(echo '****** q to quit this reader ******')"
	case $1 in
	1)  # Check IP address
		clear
		#msg="$(echo '****** q to quit this reader ******')"
	    printf "%s\n" " " " Pi's IP address is:" " "
		hostname="$(hostname -I)"
	    printf "%s\n" " $hostname" " " " $msg" " "
		ifconfig | less
	    #read -p " Enter to continue"
	    ;;
	2)  # Ethernet sub menu
		clear
		while true
		do
			clear
			eth0_menu
			eth0_menu_answer=$?
			if [[ $eth0_menu_answer == 5 ]]
				then
				break
			fi
			eth0_menu_eval $eth0_menu_answer
			echo " "
			if [[ $eth0_menu_answer == 3 ]] || [[ $eth0_menu_answer == 4 ]]
				then
				read -p " Enter to continue (You should check new IP)"
			else
				read -p " Enter to continue"
			fi
		done 
		;;
	3)	# WiFi sub menu
		clear
		while true
		do
			clear
			wlan0_menu
			wlan0_menu_answer=$?
			if [[ $wlan0_menu_answer == 9 ]]
			then
				break
			fi
			wlan0_menu_eval $wlan0_menu_answer
			#answer=$net_menu_answer
			echo " "
			read -p " Enter to continue"
		done
		;;		
	4)	# More network tools
		clear
		printf '%s\n' " " " Which IP do you want to ping? "
		read ping
		ping -nc4 $ping
		read -p " Enter to continue"
		clear
		menu
		;;
	5)	# Routing table
		clear
		echo " "
		cat /etc/resolv.conf
		echo " "
		route -ne
		echo " "
		read -p " Enter to continue"
		;;
	6)	# traceroute using nmap
		clear
		printf '%s\n' " " " Which IP do you want to trace? "
		read trace
		sudo nmap --traceroute $trace | less
		read -p " Enter to continue"
		;;
	7)	# Documentation
		clear
		printf '%s\n' " "  " $msg" " "
		cat $file_readme | less
		#read -p " Enter to continue"
		;;
	8)	# Go to command line
		clear
		break
		;;
	9)	# Shutdown Pi
		clear
		printf "%s\n"\
		"            *****Important!*****" " "\
		" When the Pi has shut down all the programs" " "\
		"  ***Disconnect the power from the Pi!****" " "
		read -p " Enter to shut down."
		sudo halt
	esac
}

# Start Main Program
clear
echo " "
cat $file_about
echo " "
read -p " Enter to start the program"

while true 
	do
		clear
		menu
		menu_answer=$?
		if [[ $menu_answer == 8 ]]
		then
			clear
			break
		fi
		menu_eval $menu_answer
	done
