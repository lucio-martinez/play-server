## Setup a virtual environment to run the web server
## Your computer will appreciate it ;)


# Define project values
VIRTUALENV=~/cool-player/play-server
PROJECT=play/*

echo "WARNING! Make sure that you do not have a folder already on $VIRTUALENV"
echo "Otherwise any information stored there will be deleted."
echo ""
echo "Do you want to continue? Y/n"
read -r doit

if [[ "$doit" != "Y" && "$doit" != "y" ]];
then
	exit;
fi

# Install virtualenv
echo " [*] Installing python virtual environment.."
sudo apt-get install python-virtualenv

# Remove possible old environment
echo " [*] Trying to remove possible obsolete environment.."
rm -R $VIRTUALENV

# Generate the virtual environment
echo " [*] Generating the virtual environment.."
virtualenv --python=python3 --system-site-packages $VIRTUALENV

# Copy the project into the virtual environment
echo " [*] Copying the project into the virtual environment.."
cp -R $PROJECT $VIRTUALENV

# Go to the new environment
cd $VIRTUALENV

# Enable the environment
echo " [*] Enabling environment.."
source bin/activate

# Install server
echo " [*] Installing packages into virtual environment.."
pip install bottle cherrypy

echo "Done! The configuration for your server has finished :)"
echo "Checkout $VIRTUALENV"
