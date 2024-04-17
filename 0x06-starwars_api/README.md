# Star Wars Characters

This script prints all characters of a Star Wars movie based on the Movie ID.

## Description

The script takes the Movie ID as the first positional argument and retrieves the list of characters from the Star Wars API for that movie. It then prints each character's name on a separate line.

## Requirements

- Node.js (version 10.14.x)
- request module (installed globally)
- semistandard module (installed globally)

## Installation

1. Install Node.js 10:

   ```bash
   $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   $ sudo apt-get install -y nodejs
Install semistandard:

bash
Copy code
$ sudo npm install semistandard --global
Install request module:

bash
Copy code
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
Usage
Run the script with the Movie ID as the first argument:

bash
Copy code
$ ./0-starwars_characters.js <Movie ID>
Example:

bash
Copy code
$ ./0-starwars_characters.js 3
Author
Jae Ncube