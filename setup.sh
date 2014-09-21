## Setup a virtual environment to run the web server
## Your computer will appreciate it ;)


# Define project values
VIRTUALENV=~/cool-player/play-server
PROJECT=play/*

# Install virtualenv
echo " [*] Installing python virtual environment.."
sudo apt-get install python-virtualenv

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

# Install Bootle server
echo " [*] Installing packages into virtual environment.."
pip3 install bottle

echo "Done! The configuration for your server has finished :)"
echo "Checkout $VIRTUALENV"
