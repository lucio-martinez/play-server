## Setup the python environment to run the web server.
## Web server: bottle


# Define project values
VIRTUALENVNAME='play-server'

# Install virtualenv
apt-get install python-virtualenv

# Generate the virtual environment
virtualenv --python=python3 --system-site-packages $VIRTUALENVNAME

# Enter the new environment
cd $VIRTUALENVNAME

# Enable the environment
source bin/activate

# Install Bootle server
pip3 install bottle

# Make a directory for the project
mkdir src

# Go to the project
cd src

# Generate views
#...

# Generate the bottle app
#...


