# Introduction :-
JavaScript files some times have a juicy data in the comments so this script automate the parsing of this comment to enable the pen-tester to focus in other missions . This script takes only the domain name you want to parse the comment from its JavaScript files from all subdomains in archive.org website 
# Install :-
git clone https://github.com/smackerdodi/js-comment-parser.git

cd js-comment-parser

pip3 install -r requirements.txt

# Usage :-

This script works only on Linux operating systems and doesn't work on windows because there is sub-process called in this script from Linux system 

# Ex :-

python3 js-comment-parser.py snapchat.com 

# Output files :-

This script generate 3 txt files as below :-
1. [ urllinks.txt ] this file contain all url for the subdomains of the given domain from archive.org website
2. [ final-links.txt ] this file contain all url for JavaScript files for all subdomains " you could use it for end points parsing using nahamsec js-parser tool https://github.com/nahamsec/JSParser
3. [ js-comment.txt ] this file contain all JavaScript comments parsed from the above files organized by file url then the comment for each 


