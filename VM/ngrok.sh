sudo apt update
sudo apt install unzip


curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok


unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin
sudo chmod +x /usr/local/bin/ngrok


# in ngrok.yml
authtoken: 2bUsJANW1Au0tOWcXDCiQ4WIkLt_6uf2z7cWeLHpbBiT85Kn3


ngrok config add-authtoken 2bUsJANW1Au0tOWcXDCiQ4WIkLt_6uf2z7cWeLHpbBiT85Kn3


ngrok http http://localhost:8080