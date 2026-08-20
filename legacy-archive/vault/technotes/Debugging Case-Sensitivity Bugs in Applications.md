---
title: Debugging Case-Sensitivity Bugs in Applications
apple_id: DTS40009073
resource_type: Technical Note
platform: macOS
topic: Data Management
technology: null
published: '2010-05-19'
source_url: https://developer.apple.com/library/archive/technotes/tn2096/_index.html
archived_at: '2026-07-26T19:54:09.664083Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2096

# Debugging Case-Sensitivity Bugs in Applications

Case-sensitive boot volumes are becoming more prevalent with the advent of case-sensitive HFS Plus, and the file system in iPhone OS is also case sensitive. Unfortunately, many applications do not work correctly on case-sensitive volumes. This technote describes techniques for tracking down case-sensitivity bugs and fixing them. It also provides suggestions for testing techniques to prevent new case sensitivity bugs from appearing in the future. This technote is intended for both Mac OS X and iPhone developers.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbxgmwugsbrfvjukq2ujfhu4mi)[Tracking Down Case-Sensitivity Bugs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbxgmwugsbrfvjukq2ujfhu4mq)[Avoiding Case Sensitivity Problems in the Future](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbxgmwugsbrfvjukq2ujfhu4my)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbxgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Beginning in Mac OS X version 10.5, (or 10.4 Server), Mac OS X supports the case-sensitive HFS Plus volume format. Because case-sensitive HFS Plus performance is comparable to that of standard HFS Plus, case-sensitive boot volumes are becoming much more common. Time Machine and iPhone OS also use case-sensitive volumes, adding further momentum to this trend. With this rise in popularity, it no longer makes sense to assume that only a handful of your application's users will use case-sensitive volumes.

Case sensitivity brings to light many latent bugs in existing software caused by developers using capital letters to access files whose names contain lower-case letters and vice-versa. Case sensitivity also brings with it a number of challenges for application developers, who must now make certain that their applications work correctly in two environments—case-sensitive HFS Plus and case-insensitive HFS Plus. This technote shows you how to fix these problems and tackle these new challenges.

For example, the scripts in this technote can be used to detect if your application would fail (on case-sensitive HFS Plus) to load resources, find its preferences, or correctly read and write preferences shared among a suite of applications.

[Back to Top](#)

## Tracking Down Case-Sensitivity Bugs

With a few shell commands, you can make tracking down case sensitivity bugs relatively straightforward. Before you begin, you will need both a case-insensitive boot volume and a case-sensitive volume or disk image. Install your application in both places before continuing.

The process is very simple. First, boot from the case-insensitive HFS Plus volume, then save the following code as a script:

__Listing 1__  Checking paths accessed by an application

```shell
#!/bin/sh  # Change this to be the volume name of your case-sensitive volume. CSVOLUMENAME="HFSPlusCS"  # Change this to be the doubly quoted path to your application (see note below) APPLICATIONPATH="/Applications/My\ Application/My\ Application.app/Contents/MacOS/My\ Application"  # This command runs your application and records all system calls into the file "fileaccess.log" in the current directory. sudo dtruss "$APPLICATIONPATH" >& fileaccess.log  # The following commands pull out any file accesses from the dtruss # results, then strip off everything but the path itself (which appears # in the dtruss output as a double-quoted string terminated with a # backslash and a zero).  grep 'open(' fileaccess.log | grep -v 'shm_open(' | sed 's/.*open("//g' | sed 's/\\0".*//g' > fileaccesslist grep 'open_nocancel(' fileaccess.log | sed 's/.*open_nocancel("//g' | sed 's/\\0".*//g' >> fileaccesslist grep 'stat(' fileaccess.log |  grep -v 'fstat(' | grep -v 'getfsstat(' | sed 's/.*stat("//g' | sed 's/\\0".*//g' >> fileaccesslist grep 'stat64(' fileaccess.log | grep -v 'fstat64(' | sed 's/.*stat64("//g' | sed 's/\\0".*//g' >> fileaccesslist grep 'getattrlist(' fileaccess.log | sed 's/.*getattrlist("//g' | sed 's/\\0".*//g' >> fileaccesslist   # This checks to see if the file exists in the current boot volume # (case-insensitive), then checks to see if the same file exists on # the case-sensitive volume. for i in $(cat fileaccesslist) ; do     if [ -f "$i" -a ! -f "$CSVOLUMENAME/$i" ] ; then         echo "$i"     fi done
```

Now, fix the following:

- Adjust the path to your application and the name of the volume (if it is not called `HFSPlusCS`). For example, if you are developing an iPhone application, you would set the `APPLICATIONPATH` variable to `"/Developer/Platforms/iPhoneSimulator.platform/Developer/Applications/iPhone\ Simulator.app/Contents/MacOS/iPhone\ Simulator"` (including the double quotes).
- Quote the application name (in)correctly. The path of the application passed to `dtruss` must be doubly quoted, with backslashes before spaces, single quotes, or double quotes, and with an extra set of double quotes around the outside. This is because `dtruss` is a shell script that does not correctly quote these paths internally. If this bug in `dtruss` is fixed in the future, simply remove either the backslashes or the double quotes.

Be certain that you have a newline character (use UNIX line endings) between quotes in the `IFS` assignment statement (and __only__ a newline). Read [Shell Scripting Primer](../documentation/Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrgy) to learn about the internal field separator (`IFS`) variable.

Next, type `chmod a+x testscript.sh` (or whatever you named your copy of the test script) to make it executable. Be sure that the case-sensitive volume or disk image is mounted, then type `./testscript.sh` to run the script.

Test your application as you normally would. When you are done, quit the application. As soon as you quit the application, you should get a list of every single file in your application bundle that was accessed with incorrect case. Now search for each of these in Xcode (with the "Ignore case" option __unchecked__), find the erroneous strings, and fix them. It's that simple.

__Note:__ This script will likely produce a few false positives. Specifically, any files that your application creates from scratch (temporary files, preferences files, files opened or saved by the user, and so on) obviously do not exist on the case-sensitive volume, and thus will be reported as missing files unless you copy them to the case-sensitive volume manually. It should be relatively easy to ignore these, assuming you have a standard naming convention for such files, but the details are specific to your application. To learn how to customize this script, read [Shell Scripting Primer](../documentation/Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrgy).

[Back to Top](#)

## Avoiding Case Sensitivity Problems in the Future

You should always build and test iPhone applications using a case-sensitive volume. Using a case-insensitive file system can lead to new bugs showing up when you move from the simulator to an actual iPhone. And because iPhone OS uses a case-sensitive file system exclusively, there is no benefit to testing iPhone applications on case-insensitive volumes at all.

When developing applications for Mac OS X, the easiest way to avoid case sensitivity problems is simple: do most of your testing on case-sensitive HFS Plus. If you always test on case-sensitive HFS Plus, unless you go out of your way to break things (intentionally creating temporary files that have the same name as open documents, but with different case, for example), the only problem you are likely to encounter is having two different files in your project with the same name and different case. You can trivially check for that as follows:

__Listing 2__  Checking for case collisions

```
# List all the files in your application bundle and store the results in the file "filelist" in your home directory. cd "/Applications/My Application.app" find . > ~/filelist  # Change back to your home directory cd ~  # Sort the files, folding uppercase and lowercase versions together. # The result is stored in the file "filelist2" in your home directory. sort -f filelist > filelist2 # Sort the files, folding uppercase and lowercase versions together and removing duplicates (insensitively) # The result is stored in the file "filelist3" in your home directory. sort -f -u filelist > filelist3  # Compare the two lists. diff -u filelist2 filelist3
```

By performing a case-insensitive (folding) sort and eliminating duplicates, any files that differ only by case will not be in the second copy of the list. Thus, comparing the two lists shows you any files that would collide on a case-insensitive volume. You can also use this technique on other folders to help find the sorts of strange bugs that occur if you open a preferences file or temporary file for writing with the wrong case and later read back an older (stale) copy using the right case.

Alternatively, you can use a case-insensitive volume as the target volume for your builds. If two files have the same name but different case, the files will collide at the build stage instead of during installation. This allows you to focus most of your testing on case-sensitive volumes.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-05-19 | Fixed minor bugs in the scripts. |
| 2009-08-04 | New document that explains how to fix bugs that case-sensitive HFS Plus reveals in applications. |

