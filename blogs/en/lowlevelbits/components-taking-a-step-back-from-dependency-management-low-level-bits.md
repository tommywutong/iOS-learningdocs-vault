---
title: 'Components: taking a step back from Dependency Management - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/components-taking-a-step-back-from-dependency-management/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0c6a617469f9325b'
translated: false
---

> 原文：[Components: taking a step back from Dependency Management - Low Level Bits 🇺🇦](https://lowlevelbits.org/components-taking-a-step-back-from-dependency-management/)　·　Low Level Bits (Alex Denisov)

# Components: taking a step back from Dependency Management

_Published on Nov 23, 2015_

In this article I will be talking about dependency management, problems we have in this area and will give you a concept that is intended to solve these problems. I will be talking in the context of iOS development, though it might be applied to any OS, language, and platform.

### Acknowledgements

I want to express gratitude to my colleagues and friends [Claudiu-Vlad Ursache](https://twitter.com/ursachec) and [Stanislaw Pankevich](https://twitter.com/sbpankevich) for their help and support in writing this article and building this concept.

### Disclaimer

I do not claim that I invented this approach, it is well known for decades and it is just variation of [FreeBSD ports system](https://en.wikipedia.org/wiki/FreeBSD_Ports). Also, I try not to give any value judgments on approaches suggested by other tools, all mentions here are just for reference, to give the context I have.

### Motivation

I have been working as iOS developer for about 5 years for different companies and on different projects. Sometimes I could start an app from scratch, but usually I had to support existing projects, which were in active development for quite some time. In such projects intervals from previous developer’s last commit and my first commit varied from couple of month to couple of years. Usually such projects use some third-party libraries and the biggest problem besides legacy code and lack of documentation exactly are those dependencies. This problem made me realize that our community is just young and not industrial/enterprise ready, hence the tools are not. I had been thinking about a tool that will work even in a one year without additional modifications and/or fixes and came up with approach FreeBSD uses: [ports](https://en.wikipedia.org/wiki/FreeBSD_Ports).

### Idea

#### Concept

To bring the idea to you let’s first take a step back and think about systems we build and clarify the terms we use. Any big enough system is built from different components, that are composed together. Systems are not built from dependencies.

> Systems are built from **components**, not from **dependencies**.

Of course, usage of a component implies that we depend on it, but psychologically the term `dependency` forces us to think that we depend on something heavily, while term `component` is neutral and lightweight, it also implies replace-ability, while `dependency` doesn’t give you such a spacious vision of the problem, you just **depend** on something.

Having that said, we have built our concept with the question `How to manage components?` in mind.

#### Implementation

The implementation of the concept is pretty simple and robust. Just a few things are needed to make it work:

- directory (`Components`) that will contain ready-for-use components
- directory (`Components.make`) that contains set of makefiles, one for each component (e.g.: `AFNetworking.make`, `BloodMagic.make`, etc.)
- driver script (`components.sh`) that will iterate over those `.make` makefiles and run `make install` (or any other defined rule) for every one of them

##### Ready for use components

Directory `Components` is intended to contain ready for use components in a form defined by maintainer of the component. It might be set of source files, static library, dynamic framework or any other appropriate artefact.

##### Makefiles

Due to our conventions each makefile should provide a set of ‘rules’:

- `install`: installs component into `Components` directory
- `uninstall`: removes component from `Components` directory
- `clean`: removes intermediate files (build artefacts, downloaded sources, etc.)
- `update`: drops current version, installs new one (`uninstall` and `install`)
- `purge`: removes everything related to component (`uninstall` and `clean`)

They are might be extended in the future, but we have found this set sufficient for everyday use.

##### Driver

Driver is responsible for iterating over makefiles and runs particular rule (one of the specified above) against them. Here is couple of examples:

```sh
./components.sh install                # installs every component in the components directory (COMPONENTS_MAKE_PATH)
./components.sh purge Cedar            # cleans and uninstalls Cedar library
./components.sh update BloodMagic      # uninstalls current and installs new version of BloodMagic library
```

`GNU/Make` has a feature called ‘dry-run’ (`man make` look for ‘–dry-run’), that “prints the commands that would be executed, but do not execute them”. We have found it extremely useful and added to driver. To see what will happen during the installation of AFNetworking, simply run:

```sh
$ ./components.sh explain install AFNetworking
[install] AFNetworking:
wget --no-use-server-timestamps https://github.com/AFNetworking/AFNetworking/archive/2.6.3.zip -O /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
unzip /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip -d /Users/alexdenisov/Library/Caches/Components/AFNetworking
touch /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
mkdir ./Components/AFNetworking/
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/AFNetworking/* ./Components/AFNetworking/
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/UIKit+AFNetworking/* ./Components/AFNetworking/
```

It is very useful if you want to debug your component’s installation process, but also if you’re concerned about security and do not want to blindly run a script downloaded from the internet.

### Example

You might already be turned off the whole idea of components because it entails writing Makefiles, but let me show an example of how straight-forward this can be.

We’ll look at a Makefile that installs AFNetworking.

_To make it more clear I will include comment above each line with actual paths instead of variables_

#### Header

Here is a typical header of a component’s makefile:

```makefile
NAME=AFNetworking
VERSION=2.6.3
GH_REPO=AFNetworking/AFNetworking
```

It says that we will work with version 2.6.3 of AFNetworking, the last line specifies the repository on Github. We could reuse `$NAME` here, but it’s not the case for all projects, so we recommend to leave it as is.

#### Paths

Next step is to define paths for all directories that will be involved in the process of the installation:

```makefile
COMPONENTS_BUILD_CACHE_PATH ?= $(HOME)/Library/Caches/Components
COMPONENTS_INSTALL_PATH ?= ./Components
```

These are so called ‘global’ variables provided by the driver script. These variables have default values in case you want to run `make install` without the driver being involved. The cache directory contains all components installed in the system and their corresponding files (such as zip archives, build artefacts and so on). `./Components` is a directory where ready-for-use component will be stored.

```makefile
# $(HOME)/Library/Caches/Components/AFNetworking
COMPONENT_BUILD_PATH=$(COMPONENTS_BUILD_CACHE_PATH)/$(NAME)
# $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
COMPONENT_SOURCE_PATH=$(COMPONENT_BUILD_PATH)/$(NAME)-$(VERSION)
# ./Components/AFNetworking
COMPONENT_INSTALL_PATH=$(COMPONENTS_INSTALL_PATH)/$(NAME)/

# $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
ZIPBALL_PATH=$(COMPONENT_BUILD_PATH)/$(NAME)-$(VERSION).zip
```

These are directories where we store intermediates for the component and where to put installed component.

#### URLs

```makefile
ZIPBALL_URL=https://github.com/$(GH_REPO)/archive/$(VERSION).zip
```

In case of AFNetworking, this URL will be resolved to `https://github.com/AFNetworking/AFNetworking/archive/2.6.3.zip`.

Usually this section contains only one URL, but there might be more. For instance you may want to fetch some patch from other source and apply it before building a component.

#### Targets

There is a set of ‘rules’ our makefile should conform to.

```makefile
.PHONY: install update uninstall clean prepare purge

# install: ./Components/AFNetworking
install: $(COMPONENT_INSTALL_PATH)

uninstall:
  # rm -rf ./Components/AFNetworking
  rm -rf $(COMPONENT_INSTALL_PATH)

update: uninstall install

clean:
  # rm -rf $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
  rm -rf $(COMPONENT_SOURCE_PATH)
  # rm -rf $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
  rm -rf $(ZIPBALL_PATH)

purge: uninstall clean
```

Let’s take a closer look at each line.

##### Phony targets

```makefile
.PHONY: install update uninstall clean prepare purge
```

The nature of makefile is to check if a file or directory with the name of target exists. If it doesn’t, it will run the commands necessary to create that file or directory. Sometimes you want to be able to run commands without that dependency on existing files. For that, you would use ‘control targets’, marked as such with `.PHONY`. So, in this example, even if the file or directory named `install` exists, the makefile will still evaluate the provided commands.

##### install

```makefile
# install: ./Components/AFNetworking
install: $(COMPONENT_INSTALL_PATH)
```

Target `install` doesn’t have any commands to evaluate, though it says that it has a dependency that needs to be resolved first: `$(COMPONENT_INSTALL_PATH)`, which resolves to `./Components/AFNetworking`. This is exactly what we want: after running `make install` we want to have AFNetworking installed to `./Components` directory.

##### uninstall

```makefile
uninstall:
  # rm -rf ./Components/AFNetworking
  rm -rf $(COMPONENT_INSTALL_PATH)
```

`uninstall` doesn’t have any dependencies, but it has one command which just removes installed AFNetworking from the `./Components` directory.

##### update

```makefile
update: uninstall install
```

That’s basically all what update does. It assumes that you have downloaded the newer version of the component and that the old one needs to be replaced.

##### clean

```makefile
clean:
  # rm -rf $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
  rm -rf $(COMPONENT_SOURCE_PATH)
  # rm -rf $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
  rm -rf $(ZIPBALL_PATH)
```

So far clean is our biggest target. It has two simple commands - first one removes sources of AFNetworking (there might be some library/framework/whatnot for other project) and second one cleans up downloaded zip archive with sources. This target is needed only if you want to keep your system clean, though the easiest way to do it is to drop `$(HOME)/Library/Caches/Components/` manually.

##### purge

```makefile
purge: uninstall clean
```

The last phony target we have here. It just cleans and uninstalls the component, nothing special.

#### Artefacts

Finally, the last section of the makefile consists of rules to create artefacts:

```makefile
# ./Components/AFNetworking : $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
$(COMPONENT_INSTALL_PATH): $(COMPONENT_SOURCE_PATH)
  # mkdir ./Components/AFNetworking
  mkdir $(COMPONENT_INSTALL_PATH)
  # $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/AFNetworking/* ./Components/AFNetworking
  cp $(COMPONENT_SOURCE_PATH)/$(NAME)/* $(COMPONENT_INSTALL_PATH)
  # $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/UIKit+AFNetworking/* ./Components/AFNetworking
  cp $(COMPONENT_SOURCE_PATH)/UIKit+$(NAME)/* $(COMPONENT_INSTALL_PATH)

# $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3 : $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
$(COMPONENT_SOURCE_PATH): $(ZIPBALL_PATH)
  # unzip $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip -d $(HOME)/Library/Caches/Components/AFNetworking/
  unzip $(ZIPBALL_PATH) -d $(COMPONENT_BUILD_PATH)
  # touch $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
  touch $(COMPONENT_SOURCE_PATH)

# $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip : $(HOME)/Library/Caches/Components/AFNetworking/
$(ZIPBALL_PATH): $(COMPONENT_BUILD_PATH)
  # wget --no--use-server-timestamps https://github.com/AFNetworking/AFNetworking/archive/2.6.3.zip -O $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
  wget --no-use-server-timestamps $(ZIPBALL_URL) -O $(ZIPBALL_PATH)

#  $(HOME)/Library/Caches/Components/AFNetworking/
$(COMPONENT_BUILD_PATH):
  # mkdir  $(HOME)/Library/Caches/Components/AFNetworking/
  mkdir $(COMPONENT_BUILD_PATH)
```

I will describe each target from top to bottom.

##### COMPONENT_INSTALL_PATH

We start off with `$(COMPONENT_INSTALL_PATH)`, since this is what we actually want to get:

```makefile
# ./Components/AFNetworking : $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
$(COMPONENT_INSTALL_PATH): $(COMPONENT_SOURCE_PATH)
  # mkdir ./Components/AFNetworking
  mkdir $(COMPONENT_INSTALL_PATH)
  # $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/AFNetworking/* ./Components/AFNetworking
  cp $(COMPONENT_SOURCE_PATH)/$(NAME)/* $(COMPONENT_INSTALL_PATH)
  # $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/UIKit+AFNetworking/* ./Components/AFNetworking
  cp $(COMPONENT_SOURCE_PATH)/UIKit+$(NAME)/* $(COMPONENT_INSTALL_PATH)
```

This target has one dependency. We assume that this dependency already resolved and directory `$(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3` contains source files of AFNetworking, to install it we just need to create a resulting directory (`./Components/AFNetworking`) and copy all sources there.

Next time we run `make install` these commands will be evaluated only if `./Components/AFNetworking` doesn’t exist.

##### COMPONENT_SOURCE_PATH

The goal of this target is to provide sources. Again, this target has dependency and we assume that it’s resolved already.

```makefile
# $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3 : $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
$(COMPONENT_SOURCE_PATH): $(ZIPBALL_PATH)
  # unzip $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip -d $(HOME)/Library/Caches/Components/AFNetworking/
  unzip $(ZIPBALL_PATH) -d $(COMPONENT_BUILD_PATH)
  # touch $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
  touch $(COMPONENT_SOURCE_PATH)
```

To provide sources for the next step we need to extract them from an archive. Pretty trivial, though it needs more explanation.

After extraction `unzip` command will create `$(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3` because of internal structure of the archive. We may expect that once we extracted data from archive we will not evaluate these commands again, but `GNU/Make` and `unzip` are smart. `unzip` preserves timestamps of archived files and `make` checks those timestamps: if it sees that directory exists, but it’s ‘old’, then it will still evaluate this step. To avoid this we have to cheat a bit by `touch`‘ing the directory with sources (`touch` changes modification and access times of file or directory).

##### ZIPBALL_PATH

```makefile
# $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip : $(HOME)/Library/Caches/Components/AFNetworking/
$(ZIPBALL_PATH): $(COMPONENT_BUILD_PATH)
  # wget --no--use-server-timestamps https://github.com/AFNetworking/AFNetworking/archive/2.6.3.zip -O $(HOME)/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
  wget --no-use-server-timestamps $(ZIPBALL_URL) -O $(ZIPBALL_PATH)
```

This step is pretty similar to previous one: we also have to take care of access/modification times, but in this case we could avoid `touch`‘ing file, because `wget` can do this for us.

##### COMPONENT_BUILD_PATH

```makefile
#  $(HOME)/Library/Caches/Components/AFNetworking/
$(COMPONENT_BUILD_PATH):
  # mkdir  $(HOME)/Library/Caches/Components/AFNetworking/
  mkdir $(COMPONENT_BUILD_PATH)
```

I don’t think this target requires explanation, but let be explicit: this step creates directory `$(HOME)/Library/Caches/Components/AFNetworking/`.

#### Whole Makefile and tips

Please, take a look at resulting makefile. As you can see it’s not that big and scary at all:

```makefile
NAME=AFNetworking
VERSION=2.6.3
GH_REPO=AFNetworking/AFNetworking

### Paths

COMPONENTS_BUILD_CACHE_PATH ?= $(HOME)/Library/Caches/Components
COMPONENTS_INSTALL_PATH ?= ./Components

COMPONENT_BUILD_PATH=$(COMPONENTS_BUILD_CACHE_PATH)/$(NAME)
COMPONENT_SOURCE_PATH=$(COMPONENT_BUILD_PATH)/$(NAME)-$(VERSION)
COMPONENT_INSTALL_PATH=$(COMPONENTS_INSTALL_PATH)/$(NAME)/

ZIPBALL_PATH=$(COMPONENT_BUILD_PATH)/$(NAME)-$(VERSION).zip

### URLs

ZIPBALL_URL=https://github.com/$(GH_REPO)/archive/$(VERSION).zip

### Targets

.PHONY: install update uninstall clean prepare purge

install: $(COMPONENT_INSTALL_PATH)

uninstall:
  rm -rf $(COMPONENT_INSTALL_PATH)

update: uninstall install

clean:
  rm -rf $(COMPONENT_SOURCE_PATH)
  rm -rf $(ZIPBALL_PATH)

purge: uninstall clean

### Artefacts

$(COMPONENT_INSTALL_PATH): $(COMPONENT_SOURCE_PATH)
  mkdir $(COMPONENT_INSTALL_PATH)
  cp $(COMPONENT_SOURCE_PATH)/$(NAME)/* $(COMPONENT_INSTALL_PATH)
  cp $(COMPONENT_SOURCE_PATH)/UIKit+$(NAME)/* $(COMPONENT_INSTALL_PATH)

$(COMPONENT_SOURCE_PATH): $(ZIPBALL_PATH)
  unzip $(ZIPBALL_PATH) -d $(COMPONENT_BUILD_PATH)
  touch $(COMPONENT_SOURCE_PATH)

$(ZIPBALL_PATH): $(COMPONENT_BUILD_PATH)
  wget --no-use-server-timestamps $(ZIPBALL_URL) -O $(ZIPBALL_PATH)

$(COMPONENT_BUILD_PATH):
  mkdir $(COMPONENT_BUILD_PATH)
```

#### Debugging

To sum up the above example I want to give a small tip about debugging if you still think that makefiles are hard to manage and introduce huge complexity.

You can see what is going on when you run `make` and how `make` is reasoning about its decisions.

Just add two flags `-r` and `-d`. First one disables implicit rules (just to decrease output), second one actually prints debug information, e.g.:

```sh
$ make install -r -d
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-apple-darwin11.3.0
Reading makefiles...
Reading makefile `/Users/alexdenisov/Projects/ComponentsDemo/Components.make/AFNetworking.make'...
Updating makefiles....
 Considering target file `/Users/alexdenisov/Projects/ComponentsDemo/Components.make/AFNetworking.make'.
  Looking for an implicit rule for `/Users/alexdenisov/Projects/ComponentsDemo/Components.make/AFNetworking.make'.
  No implicit rule found for `/Users/alexdenisov/Projects/ComponentsDemo/Components.make/AFNetworking.make'.
  Finished prerequisites of target file `/Users/alexdenisov/Projects/ComponentsDemo/Components.make/AFNetworking.make'.
 No need to remake target `/Users/alexdenisov/Projects/ComponentsDemo/Components.make/AFNetworking.make'.
Updating goal targets....
Considering target file `install'.
 File `install' does not exist.
  Considering target file `Components/AFNetworking'.
   File `Components/AFNetworking' does not exist.
    Considering target file `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3'.
      Considering target file `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip'.
        Considering target file `/Users/alexdenisov/Library/Caches/Components/AFNetworking'.
         Finished prerequisites of target file `/Users/alexdenisov/Library/Caches/Components/AFNetworking'.
        No need to remake target `/Users/alexdenisov/Library/Caches/Components/AFNetworking'.
       Finished prerequisites of target file `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip'.
       Prerequisite `/Users/alexdenisov/Library/Caches/Components/AFNetworking' is older than target `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip'.
      No need to remake target `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip'.
     Finished prerequisites of target file `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3'.
     Prerequisite `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip' is older than target `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3'.
    No need to remake target `/Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3'.
   Finished prerequisites of target file `Components/AFNetworking'.
  Must remake target `Components/AFNetworking'.
mkdir ./Components/AFNetworking/
Putting child 0x7ff3e940a340 (Components/AFNetworking) PID 48450 on the chain.
Live child 0x7ff3e940a340 (Components/AFNetworking) PID 48450
Reaping winning child 0x7ff3e940a340 PID 48450
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/AFNetworking/* ./Components/AFNetworking/
Live child 0x7ff3e940a340 (Components/AFNetworking) PID 48451
Reaping winning child 0x7ff3e940a340 PID 48451
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/UIKit+AFNetworking/* ./Components/AFNetworking/
Live child 0x7ff3e940a340 (Components/AFNetworking) PID 48452
Reaping winning child 0x7ff3e940a340 PID 48452
Removing child 0x7ff3e940a340 PID 48452 from chain.
  Successfully remade target file `Components/AFNetworking'.
 Finished prerequisites of target file `install'.
Must remake target `install'.
Successfully remade target file `install'.
```

Just use these two flags if you ever face any problems with makefiles.

Second tip is `make` parameter `--warn-undefined-variables`. It emits a warning if some variable does not exist. We have found it very helpful to avoid mistakes like `rm -rf $FOO/` when `$FOO` is not set. Also, the `components.sh` driver has this flag enabled. It’s even more helpful when you run `explain`, e.g.:

```sh
$ ./components.sh explain install
[install] AFNetworking:
/Users/alexdenisov/Projects/ComponentsDemo/Components.make/AFNetworking.make:49: warning: undefined variable `ZIPBALL_URL'
wget --no-use-server-timestamps  -O /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
unzip /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip -d /Users/alexdenisov/Library/Caches/Components/AFNetworking
touch /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
mkdir ./Components/AFNetworking/
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/AFNetworking/* ./Components/AFNetworking/
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/UIKit+AFNetworking/* ./Components/AFNetworking/
```

In the output above you may see a warning because I’ve added a typo to `ZIPBALL_URL`

### Key features and goals

Now, when you saw basic implementation, I want to conclude and highlight key features, goals, advantages and disadvantages of the concept.

_**Note:** The order of highlights is alphabetical_

#### Abstraction

We put as much efforts as possible to put abstraction in a first place. We consider `make install` to be a good abstraction that gives a lot of flexibility, hence you can easily use any tool you want under the hood (fetch git-submodules, run `pod/gem install`, etc.)

#### Automatic version updates

Almost every tool for dependency management gives an ability to update version automatically (`~> 1.3.0`, `4.+`, etc.). `Components` does not have such feature.

We strongly believe that you have to have a reason to update third-party component. Updating a library just because a new version available doesn’t seem to be a software engineering.

#### Decentralization

The system is completely decentralized and doesn’t require any server to run (except the servers with components you use).

_Though there is a [repo with examples of Components](https://github.com/AlexDenisov/Components) and we will appreciate if you submit your component there, it might be useful especially in case when maintainer doesn’t provide you with a makefile and you have built one on your own._

#### Dependency Resolution

Implementation of this feature requires more efforts than benefits it gives.

At least in iOS community - for ~5 years I hardly ever had more than 2-3 implicit dependencies. It’s much more time efficient to add such dependency manually once, than wait for it to be resolved automatically every time you hit ‘install’.

Hence, if you use component X in your project and the component X needs another component Y that is not included in the project, then you should include component Y explicitly.

#### Safety

The tool just fetches components and puts them into a directory with your project, it doesn’t touch `.xcodeproj` file or any other files.

#### Semantics

We do care about semantics more, than about nice and fancy syntax or names for tooling.

#### Security

The tool doesn’t make any magic, you can easily explore what will happen when run `make install` for some component. Besides that driver provides a command `explain` to see which commands will be executed, e.g.:

```
$ ./components.sh explain install AFNetworking
[install] AFNetworking:
wget --no-use-server-timestamps https://github.com/AFNetworking/AFNetworking/archive/2.6.3.zip -O /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip
unzip /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3.zip -d /Users/alexdenisov/Library/Caches/Components/AFNetworking
touch /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3
mkdir ./Components/AFNetworking/
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/AFNetworking/* ./Components/AFNetworking/
cp /Users/alexdenisov/Library/Caches/Components/AFNetworking/AFNetworking-2.6.3/UIKit+AFNetworking/* ./Components/AFNetworking/
```

Also, the tool operates only on three directories, which means that you could create an extra user who will only have an access to these directories. Of course it’s not bullet-proof, but it may prevent potential damage by mistakes inside of a makefile.

#### Speed

Our implementation of the concept is fast because:

- the tool doesn’t resolve dependencies, it just installs them
- because of nature of `GNU/Make` each action will be executed only once, so once component was downloaded, extracted or build - any of these actions will not happen again (of course unless you delete those files)
- the tool stores components locally on your machine, once you installed specific version of component it may be reused by other project, hence you don’t need to download and build it again

#### Stability

This is one of the most important things for us: the `GNU/Make` is very stable tool, current version on my machine was released ~10 years ago, if I install newer version it will just work without any problems.

### Summary

We use this approach with our current project by incrementally transforming our ‘open-source’ projects into Components, one by one.

I have to say it works good so far, we haven’t faced any problems yet and it seems that we will use it in the future.

If you interested and want to adopt this approach, then I can recommend you to take a look at another article: [How to build a static iOS framework and distribute it as a Component using Make](http://stanislaw.github.io/2015/11/23/how-to-build-static-framework-using-make.html) and check out [this repository](https://github.com/AlexDenisov/Components) with scripts and sample `.make` makefiles for AFNetworking and CompositeOperations.

One thing I want to ask the community:

**What do you think? Does this `make` thing make any sense?**

I would appreciate any feedback.

Best regards,   
 Alex.
