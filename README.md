# Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Application view](#application-view)

## General info
<details>
    <summary><b>Click here to see general information about application!</b></summary>
        <br>
        This application based on flask allows user to connect to chosen raspberry pi via ssh.
        After connect user can see real time chart with temperature near by raspberry pi.
        Personally, I use this application to check the temperature in the server room.
</details>

## Technologies
<details>
    <summary><b>Click here to see the technologies used!</b></summary>
        <ul>
            <li>Python 3.8.5</li>
            <li>Flask 1.1.2</li>
            <li>Docker 20.10.5</li>
            <li>Docker-compose 1.29.0</li>
            <li>Raspberry Pi 4 model B</li>
            <li>KAmodLM75A</li>
        </ul>
</details>

## Setup
<details>
    <summary><b>Configuration Steps!</b></summary>
    <ol type="1">
        <li>Connect the KAmodLM75A module with the Raspberry pi.</li>
        <li>Configure Raspberry pi.</li>
        <li>Configure the application with "run_config.py".</li>
        <li>Run app using "run_app.py".</li> 
    </ol>
</details>
<details>
    <summary><b>Click here to see how to connect KAmodLM75A with Raspberry pi!</b></summary>

### Cables connection diagram
![Przechwytywanie](https://user-images.githubusercontent.com/57534862/116564470-4c99a380-a905-11eb-9a40-74e4b4be3e36.PNG)
    </details>
    <details>
    <summary><b>Click here to see how to configure Raspberry pi!</b></summary>
        <ol type="1">
            <li>Turn on SSH in your rassbery pi (use raspi-config)</li>
            <li>Set static ip address in your rassbery pi</li> 
        </ol>

### Setting static ip in Raspberry pi   
    sudo nano /etc/dhcpcd.conf
If your are in nano editor just add this lines below(use the correct addressing of course). 
![image](https://user-images.githubusercontent.com/57534862/116561729-deec7800-a902-11eb-8b8b-10d4daa47749.png)
    </details>
    <details>
    <summary><b>Click here to see how to configure app!</b></summary>

#### The app will guide you through the setup. Just run "run_config.py"</li>
   </details>
    <details>
    <summary><b>Click here to see how to set up docker-compose!</b></summary>

        docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d & docker compose ps -a
   </details>



## Application view

### Chart view 
![temperature_example](https://user-images.githubusercontent.com/57534862/116559776-0e01ea00-a901-11eb-8608-c2d63d33bc48.png)

