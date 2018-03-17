title:    "Manage Python Packages on Arch Linux"  
date:    2018-03-17  
time:    "14:04"  
location:    Austin, TX  
country:    United States  
author:    Yu Lu  
category:    Linux  
cover:    cover.png  
abstract:  Python package management on arch linux is not trivial, due to the possible confliction between pacman package manager and the pip python package installer. This article introdues the confliction and ways to walk around this issue.  

# Manage Python Packages on Arch Linux  
![cover](/static/posts/manage_python_packages_on_arch_linux/cover.png)  

## Pacman and Pip  
While python is one of the most popular programming language, installing/managing python pacakges could have the risk of package confliction. Pacman, as the pacakge manager on arch linux, tracks packages installed or build through pacman (or related complimentary method like yaourt) and helps to resolve their dependencies as well as keep them update.   

Although a great number of Python packages are readily available in the official repositories and the AUR, it doesn't mean that you could always find what you want from pacman. The Python ecosystem provides its own package managers for use with PyPI, which can be installed through pip. So what should be the preffered way to intall python packages on arch linux ? Arch wiki tells you:  
>"It is always preferred to use pacman to install software".   

But what if one has to use pip for packages not on arch repos ?  

## The Error    
A few month ago I started using python flask package as backend to build dynaic website, since flask will be used frequently on my laptop (with arch linux installed) I decided not to use virtual environment. As always the preference, I first tried to use pacman to query flask from the remote repositories, I got nothing.  

Well, pip is next tool which I was certain that I could find flask package. Here the mistake starts:  

```
sudo pip install flask  
```  

Here I used sudo on top of pip to install python packages, which will install python packages in: `/usr/lib/python3.6/site-packages` directory. It takes only a few seconds compare to looking for packages and build through pacman. Easy!   

However, a few weeks later, when I was doing a regular system update by typing `sudo pacman -Syu`, the error comes:  

```
Pacman "error: failed to commit transaction (conflicting files)"  
```  

With which there was a long list "already exists"  packages in the system site-package path. What's going on ?  

## The Failling Point  
The main reason of this error is that, I was using pip to install python packages system-wide, using sudo. when installing pacman packages which depend on previously installed packages from pip, the later update may fail, since pacman is trying to update packages not documented but turned out these packages already exist in the system.  

This is a general mistake people could make, not restricted to python packages. As every system-wide package you install is build on top of the core arch linux, using third-party package installer will potentially rise confliction. The take-home massage from this lesson is:  
> Be careful when installing packages system-wide if not through pacman.  


## The correct approach  
As mentioned above, the mistake has two aspects: 1) not using pacman; 2) system-wide installation. The correct approaches can also come correspondingly.  


### Build through pacman  
The chance always exists that you have to install some python packages that could not be find through pacman query, such as: flask, frozen-flask, watermark, etc. The general approach is to build from source through pacman build, or if one prefer, can try query yaourt. This keep the package managed by pacman and resolves the dependency and potentially can avoid future conflitions.   
The downside is that this may be time-consuming, and could require more unnecessary packages to build the targeted package you want. This doen't come very handy especially when one what to just get the package ready and enjoy the python joy.  


### Install for user only  
This another way to resolve the confliction, since packages installed only for specific user won't have potential problem with pacman system-wide update. To do this, simply running:   

```
pip install package-name --user  
```  

Make sure to use the `--user` option, otherwise pip by default will try to install the packages system-wide, to `/usr/lib/python3.6/site-packages` and usually will give "permission denied" error during the installation step. Note that one has to be loged in as the end useer and no sudo needed.  

## Python packages  
I had problem to let python find the packages installed for end users, which appears to be `no module named package-name` error when trying import user site packages. So here are a few more works about how python find its packages.  

Similar to pacman, python has its specific system path to search for packages. By default, python search path  `/usr/lib/python3.6/site-packages` for system-wide install packages. One can use `python -m site` in command line to list the system path, for example :  
![pic](/static/posts/manage_python_packages_on_arch_linux/pythonsite.jpg)  

As one can see there are four categories:   
- sys.path: This is a list of system path the python searches for packages   
- USER_BASE: This is where user specific python configuration/package path  
- USER_SITE: The path where user site-packages are installed, when using `pip install package-name --user`  
- ENABLE_USER_SITE: whether the user site package is enabled.  

Usually when one choose to install python packages user-specificly, the installed packages should located in the path given by `USER_SITE`. To view what packages has been install for user, one can either check the above directory or use `pip list`.  

Another way to check where python looks for packages is to use sys module in a python environment:  
![pics](/static/posts/manage_python_packages_on_arch_linux/pythonsite2.jpg)  

Onthing one has to pay attention is that, having "USER_SITE" listed the user site-package path doesn't necessary garantee python will find this packaged installed there. The installed packages has to be under one of the paths listed under "sys.path".   

If your user site-packages path does not appear in "sys.path" list, one can try to assign it to the environment variable "PYTHONPATH" in bash, pratically in .bashrc, add:  

```  
export PYTHONPATH=path_to_user_local_site_packages  
```

One can double check if the user site-package path has been successfully added to the "sys.path" by one of two ways introduced above.  
  
  
  
  
