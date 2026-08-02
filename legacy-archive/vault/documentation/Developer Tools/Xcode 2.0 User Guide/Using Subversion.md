---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/UsingSubversion/UsingSubversion.html
archived_at: '2026-07-15T07:28:50.829282Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Configuring%20Your%20SSH%20Environment.md)[Previous](Using%20CVS.md)

# Using Subversion

This appendix provides instructions on performing
a few essential version control operations using the Subversion
client tool. It doesn’t offer detailed guidance on using Subversion.
Consult the Subversion documentation for in-depth explanations.

This section shows how to install the server and client software
of the Subversion version control system in a computer using Fink.
Fink is an open-source project that simplifies the installation
of UNIX software in several platforms, including Mac OS X.

To install Fink on your computer, go to [http://fink.sourceforge.net](http://fink.sourceforge.net/) and
follow the download instructions.

To install the Subversion server software, execute these commands
in Terminal:

```shell
% sudo apt-get update // 1
Hit us.dl.sourceforge.net 10.3/release/main Packages
Hit us.dl.sourceforge.net 10.3/release/main Release
...
% sudo apt-get install svn // 2
Reading Package Lists... Done
Building Dependency Tree... Done
...
```

This is what the commands do:

1. The `apt-get
   update` command updates Fink’s list of available
   packages.
2. The `apt-get install svn` command
   installs the `svn` package,
   which contains the Subversion server software.

To install the Subversion client software, execute the following
command:

```
% sudo apt-get install svn-client
```


Most developers don’t need to worry about creating or managing
repositories. This task is usually handled by system administrators.
However, if you’re a member of a very small team or the sole programmer
in your organization, you may have to create and maintain the repository
that holds your company’s source code. Or you may create a local
repository to experiment with version control in your computer.

To create a Subversion repository, create its root directory
(the directory that contains the repository) and initialize the
repository. If you want others to access the repository, you should
to create a group containing their usernames and assign the group
to the root directory.

To create the Subversion users group, execute these commands
in Terminal:

```shell
% sudo nicl . -create /groups/svnusers // 1
% sudo nicl . -append /groups/svnusers gid 700 // 2
% sudo nicl . -append /groups/svnusers users <user1> <user2>  ... <userN> // 3
% lookupd -flushcache // 4
% memberd -r // 5
```

This is what the commands do:

1. Creates the `svnusers` group.
2. Assigns an ID number to the `svnusers` group.
   You can use any unused group ID number.
3. Assigns a list of user names to the `svnusers` group.
4. Flushes the directory information cache.
5. Resolves the memberships of the new group.

To create the repository’s root directory, execute the following
commands:

```shell
% sudo svnadmin create /svnrep // 1
% sudo chgrp svnusers /svnrep/db // 2
% sudo chmod -R g+wx /svnrep/db // 3
```

This is what the commands do:

1. Creates and
   initializes the `/svnrep` repository
   directory.
2. Assigns the `svnusers` group
   to the repository’s data directory.
3. Gives write and execute permissions to the `svnusers` group
   for the data directory.

Subversion uses URLs (Uniform Resource Locators) to identify
repositories. Using URLs, you can work with several Subversion repositories
at a time. To access a local repository, you use a URL like the
following:

```
file://<repository_root>/<project_path>
```

For repositories located on remote computers, Subversion offers
a variety of options; one of them is SSH. To access a repository
on a remote computer using SSH, use a URL like the following:

```
svn+ssh://<computer_name>/<repository_root>/<project_path>
```

Before you can access a remote repository using SSH, you have
to configure your SSH environment. See [Configuring Your SSH Environment](Configuring%20Your%20SSH%20Environment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrxgqwueqkci5fegq2i) for
details. Consult the Subversion documentation for information on
other access methods.

To add a project directory to a Subversion repository, use
the `svn import` command.
Its syntax is:

```
svn import -m "<import_comment>" <source>  <repository>
```

For example, to import the project directory `/Developer/Examples/Networking/Echo` into
a local repository, you issue the following commands in Terminal:

```
% svn import -m "Echo added to repository" /Developer/Examples/Networking/Echo  file:///svnrep/Echo
Adding         /Developer/Examples/Networking/Echo/EchoContext.c
Adding         /Developer/Examples/Networking/Echo/main.c
...
Committed revision 1.
```

Before adding a project directory to a repository, you should
move or delete the `build` directory
if it resides in the project directory. You should also move or
delete any other directories you don’t want to add to the repository.
Otherwise, changes to files in those directories are tracked by
your version control system and added to the repository.

To check out a project in a Subversion repository, use the `svn
checkout` command. Its syntax is:

```
svn checkout <repository> <target>
```

For example:

```
% svn checkout file:///svnrep/Echo ~/src/Echo
A  /Users/ernest/src/Echo/EchoContext.c
A  /Users/ernest/src/Echo/main.c
...
Checked out revision 1.
```


When Xcode is unable to open a project because its project
file (`project.pbxproj`)
is corrupted, you must use the `svn revert` command
to restore the project file to the version you last obtained from
the repository. For example, to update the project package in a
project named Sketch, you execute the `svn revert` command
on the project file, as shown here:

```
% svn revert Sketch.xcode/project.pbxproj
Reverted 'Sketch.xcode/project.pbxproj'
```

[Next](Configuring%20Your%20SSH%20Environment.md)[Previous](Using%20CVS.md)

