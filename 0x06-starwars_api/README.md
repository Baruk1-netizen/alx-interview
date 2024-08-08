# 0x06. Star Wars API

## Description

The "Star Wars Characters" project involves interacting with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. This task requires knowledge of web programming, API interaction, and asynchronous programming in JavaScript.

## Concepts

To successfully complete this project, you need to be familiar with the following key concepts:

### HTTP Requests in JavaScript
- Making HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
- [A Complete Guide to Making HTTP Requests in Node.js](https://nodejs.dev/learn/making-http-requests-with-nodejs)

### Working with APIs
- Understanding the basics of RESTful APIs and how to interact with them.
- Parsing JSON data returned by APIs.
- [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

### Asynchronous Programming
- Managing asynchronous operations with callbacks, promises, and async/await syntax.
- Handling API response data asynchronously.
- [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

### Command Line Arguments in Node.js
- Using the `process.argv` array to access command-line arguments passed to a Node.js script.
- [How to Parse Command Line Arguments in Node.js](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/)

### Array Manipulation and Iteration
- Iterating over arrays and manipulating data structures to format and display character names.
- [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Additional Resources
- [Mock Technical Interview](https://www.example.com/mock-interview)

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should be semistandard compliant (rules of Standard + semicolons on top, reference: AirBnB style)
- All files must be executable
- The length of files will be tested using `wc`
- Do not use `var`

### More Info

#### Install Node 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard
```bash
$ sudo npm install semistandard --global
```

#### Install request module and use it
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Star Wars Characters (mandatory)
Write a script that prints all characters of a Star Wars movie:
- The first positional argument passed is the Movie ID (example: 3 = “Return of the Jedi”)
- Display one character name per line in the same order as the “characters” list in the `/films/` endpoint
- Use the Star Wars API
- Use the `request` module

Example usage:
```bash
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$
```

## Repository
- GitHub repository: `alx-interview`
- Directory: `0x06-starwars_api`
- File: `0-starwars_characters.js`


## Author

- **@waltertaya**
