---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/UsingCVS/UsingCVS.html
archived_at: '2026-07-15T07:28:50.821131Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Using%20Subversion.md)[Previous](Using%20Scripts%20To%20Customize%20Xcode.md)

# Using CVS

This appendix provides instructions on performing
a few essential version control operations using the CVS client
tool. It doesn’t offer detailed guidance on using CVS. Consult
the CVS documentation for in-depth explanations.

CVS is installed in Mac OS X. Max OS X version 10.4 includes
two versions of CVS: the legacy version (version 1.10), which supports
wrappers and the current version (version 1.11.18), which doesn’t
support wrappers. CVS with wrapper support is required when you
work on projects that contain bundles, such as nibs, which are directories
that group a set of files as a discrete package (see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ for
details). When you use CVS with wrappers, bundles are compressed
into a single file before they are placed in the repository and
decompressed when they are checked out to local copies.

In Mac OS X v10.4, the CVS tool that supports wrappers is `/usr/bin/ocvs`,
(this is the same version of the tool that shipped on earlier versions
of Mac OS X). The current version of the CVS tool is `/usr/bin/cvs`.
It incorporates fixes to security problems in earlier versions of
CVS. Xcode is initially configured to use `ocvs`.

You must use the `ocvs` tool
when working on projects hosted on repositories created using CVS
1.10 or earlier. Also, you must host new projects containing bundles
in repositories created using CVS 1.10 or earlier. You should host
new projects that don’t use bundles in repositories created using
CVS version 1.11.18 or later.

Most developers don’t need to worry about creating or managing
repositories. This task is usually handled by system administrators.
However, if you’re a member of a very small team or the sole programmer
in your organization, you may have to create and maintain the repository
that holds your company’s source code. Or you may create a local
repository to experiment with version control in your computer.

To create a CVS repository, create the CVS root directory
(the directory that contains the repository) and initialize the
repository. If you want others to access the repository, you should
create a group containing their user names and assign the group
to the root directory.

To create the CVS users group, execute these commands in Terminal:

```shell
% sudo nicl . -create /groups/cvsusers // 1
% sudo nicl . -append /groups/cvsusers gid 600 // 2
% sudo nicl . -append /groups/cvsusers users <user1> <user2>  ... <userN> // 3
% lookupd -flushcache // 4
% memberd -r // 5
```

This is what the commands do:

1. Creates the `cvsusers` group.
2. Assigns an ID number to the `cvsusers` group.
   You can use any unused group ID number.
3. Assigns a list of user names to the `cvsusers` group.
4. Flushes the directory information cache.
5. Resolves the memberships of the new group.

To create the repository’s root directory, execute the following
commands:

```shell
% sudo mkdir /cvsrep // 1
% sudo chgrp cvsusers /cvsrep // 2
% sudo chmod g+w /cvsrep // 3
```

This is what the commands do:

1. Creates the `/cvsrep` directory.
2. Assigns the `cvsusers` group
   to the directory.
3. Gives write permission to the `cvsusers` group
   for the directory.

To initialize the repository, execute the following commands:

```shell
% setenv CVSROOT /cvsrep         # 'export CVSROOT=/cvsrep' in bash
% sudo cvs init
```


You can access local repositories (that is, repositories that
reside on the same computer on which you develop) directly. For
repositories located in remote computers, however, CVS uses secure
connection methods, such as SSH. See the CVS documentation for information on
other secure connection methods.

This section shows how to configure environment variables
to enable SSH-based access to a CVS repository. For information
on how to set up the required private and public keys, see [Configuring Your SSH Environment](Configuring%20Your%20SSH%20Environment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrxgqwueqkci5fegq2i).

To access a CVS repository through SSH, you need to configure
the `CVSROOT` and `CVS_RSH` environment
variables for your user account:

1. Set `CVSROOT` so
   that it defines the user under which to log in, the computer the repository
   resides in, and the path to the repository's root directory, using
   the following format:

```
:ext:<user>@<host><repository_path>
```

   For example:

```
setenv CVSROOT :ext:ming@server.apple.com:/cvsrep
```
2. Set `CVS_RSH` to `ssh`:

```
setenv CVS_RSH ssh
```

For more information on using SSH to access a remote CVS repository,
consult the CVS documentation.

To add a project directory to a CVS repository, use the `cvs
import` command, which operates on the current
working directory. You must have the `CVSROOT` environment
variable set to the CVS root directory (see [Creating a CVS Repository](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrsgywueq2ji5cumscf)).
The command’s syntax is:

```
cvs import -m "<import_comment>" <module_name>  <tag> start
```

For example, to import the project directory `/Developer/Examples/Networking/Echo`,
you issue the following commands in Terminal:

```shell
% cd /Developer/Examples/Networking/Echo
% cvs import -m "Echo added to repository" Echo Echo_1  start
```

Before adding a project directory to a repository, you should
move or delete the `build` directory
if it resides in the project directory. You should also move or
delete any other directories you don’t want to add to the repository.
Otherwise, changes to files in those directories are tracked by
your version control system and added to the repository.

To check out a project in a CVS repository, use the `cvs
checkout` command. The command's syntax is:

```
cvs checkout <module_name>
```

For example:

```shell
% cd ~/src
% cvs checkout Echo
```


When Xcode is unable to open a project because its project
file (`project.pbxproj`)
is corrupted, you must use the `cvs update` command
to get the latest version from the repository. For example, to update
the project package in a project named Grape using `cvs`,
you execute the `cvs update` command
on the project file, as shown here:

```
% cvs update -C Grape.xcode/project.pbxproj
(Locally modified project.pbxproj moved to .#project.pbxproj.1.4)
U Grape.xcode/project.pbxproj
```

To do the same using `ocvs`,
execute the following commands:

```shell
% mv Grape.xcode/project.pbxproj /tmp
% ocvs update Grape.xcode/project.pbxproj
ocvs update: warning: Grape.xcode/project.pbxproj was lost
U Grape.xcode/project.pbxproj
```

[Next](Using%20Subversion.md)[Previous](Using%20Scripts%20To%20Customize%20Xcode.md)

