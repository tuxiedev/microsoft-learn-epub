# mslearn-epub

![](https://docs.microsoft.com/en-us/media/learn/home/hero_background_light.svg)

Generate epubs of [Microsoft Learn Learning Paths](https://docs.microsoft.com/en-us/learn/browse/?resource_type=learning%20path)


## Table of Contents
* [Running](#running)
* [Example usages](#example-usages)
* [Contact or Contribute](#contact-or-contribute)

## Running
* Clone this repository
```
$ git clone git@github.com:tuxiedev/mslearn-epub
```
* cd into the directory
```
$ cd mslearn-epub
```
* Install requirements to run the script
```
$ pip install -r requirements.txt
```
* Go to [Microsoft Learn Learning Paths](https://docs.microsoft.com/en-us/learn/browse/?resource_type=learning%20path) and pick the learning path you want to download
* Copy the URL of the learning path
* Use the command like this 
```
python mslearn-epub.py -u <learning-path-url> -d <destination-directory>
```
## Example usages
1. To get the Learning Path [Introduce DevOps Dojo: Create efficiencies that support your business](https://docs.microsoft.com/en-us/learn/paths/devops-dojo-white-belt-foundation/) ebooks downloaded to a folder `./devops-dojo-whitebelt`, run the following command
```
$ python mslearn-epub.py -u https://docs.microsoft.com/en-us/learn/paths/devops-dojo-white-belt-foundation/ -d ./devops-dojo-whitebelt
Generating ebook for title Introduce the foundation pillars of DevOps: Culture and Lean Product
Waiting ebook to finish for title Introduce the foundation pillars of DevOps: Culture and Lean Product
...
```
2. Check if the ebooks are ready in the folder `devops-dojo-whitebelt`
```
$ ls ./devops-dojo-whitebe
0-Introduce the foundation pillars of DevOps: Culture and Lean Product.epub
1-Define the foundation pillars of DevOps: Architecture and Technology.epub
2-Analyze DevOps Continuous Planning and Continuous Integration.epub
3-Explain DevOps Continuous Delivery and Continuous Quality.epub
4-Explore DevOps Continuous Security and Continuous Operations.epub
5-Characterize DevOps Continuous Collaboration and Continuous Improvement.epub
```
## Contact or Contribute
Questions? Raise an [Issue](https://github.com/tuxiedev/mslearn-epub/issues)

Contributions can be made via [Pull Requests](https://github.com/tuxiedev/mslearn-epub/pulls)

## Credits
[EpubPress](https://epub.press)
