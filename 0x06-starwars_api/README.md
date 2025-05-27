# Star Wars API

This project contains a script that interacts with the Star Wars API to retrieve and display character information from Star Wars films.

## Requirements

- Node.js 10.14.x
- Ubuntu 20.04 LTS
- Semistandard style compliant code
- Request module

## Installation

### Node 10

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Semistandard

```bash
sudo npm install semistandard --global
```

### Request module

```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Task 0: Star Wars Characters

The script prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: 3 = "Return of the Jedi"
- Display one character name per line in the same order as the "characters" list in the /films/ endpoint
- Uses the Star Wars API: <https://swapi-api.alx-tools.com/api/>

### Usage

```bash
./0-starwars_characters.js <Movie ID>
```

### Example

```bash
./0-starwars_characters.js 3
```
