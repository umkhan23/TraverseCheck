# TraverseCheck

### About
TraverseCheck is a tool that can be used to check for directory traversal in vulnerable web applications.
### Getting Started
#### Clone the repository
```Bash
git clone https://github.com/umkhan23/TraverseCheck.git
cd TraverseCheck
```
#### Install required dependancies
`pip3 install -r requirements.txt`
### Usage

``` python 3


   /=\                             /=\ |           |
    |  /= /=| | | /=\ /= /== /=\   |   |=\ /=\ /=: =/
    |  |  \=| \/  \=  |  ==/ \=    \=/ | | \=  \=: |\

  ####################################################
                Author: Usman Q Khan

usage: python3 TraverseCheck.py -u URL -p PATH

example: python3 TraverseCheck.py -u http://10.10.10.10/ -p /etc/passwd

Check for Directory Traversal vulnerability

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Enter a URL
  -p PATH, --path PATH  Enter the full path of the file you'd like to find
```
