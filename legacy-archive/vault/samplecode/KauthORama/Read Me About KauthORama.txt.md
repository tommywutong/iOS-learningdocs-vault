---
title: KauthORama
apple_id: DTS10003633
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2014-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/KauthORama/Listings/Read_Me_About_KauthORama_txt.html
archived_at: '2026-07-18T03:13:21.503637Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [KauthORama](KauthORama.md)


[Next](Document%20Revision%20History.md)[Previous](KauthORama.c.md)

# Read Me About KauthORama.txt

```swift
Read Me About KauthORama
========================
1.4

KauthORama is a sample that demonstrates the use of the Kernel Authorization (Kauth) subsystem.  KauthORama allows you to register a listener for any scope.  The listener has no effect on authorization decisions, but it prints a record of each authorization request so that you can see how Kauth interacts with high-level operations, like listing directories or copying files.

KauthORama requires OS X 10.9, but the core techniques used by the sample are compatible all the way back to Mac OS X 10.4.

Packing List
------------
The sample contains the following items:

o Read Me About KauthORama.txt -- This file.

o KauthORama.c -- C source code for the kernel extension.

o Info.plist -- Property list for the kernel extension.

o KauthORama.xcodeproj -- An Xcode project for the kernel extension.

Building the Sample
-------------------
The sample was built using Xcode 5.1 on OS X 10.9.2.  You should be able to just open the project and choose Product > Build.

OS X 10.9 and later require that KEXTs be code signed.  For more information about this, watch WWDC 2013 Session 707 "What's New in Kext Development".

<https://developer.apple.com/videos/>

The sample comes pre-configured to sign the KEXT using your Developer ID code signing identity.  Such an identity must be enabled for KEXT development.  To determine if that's the case, look in the certificate for a custom extension with OID 1.2.840.113635.100.6.1.18.  If it's present, you're all set.  Otherwise, to enable your Developer ID code signing identity for KEXT development, follow the instructions on the page below.

<https://developer.apple.com/contact/kext/>

Finally, if you have more than one Developer ID, make sure you select the right one via the CODE_SIGN_IDENTITY build setting.

Using the Sample
----------------
To use the sample, first change into the directory containing the newly-built extension and install it as follows.

$ sudo cp -R KauthORama.kext /Library/Extensions/
Password: ********
$ sudo kextutil /Library/Extensions/KauthORama.kext

To confirm that it is installed, take a look at the system log.  You should see a startup message from the sample.

$ grep KauthORama /var/log/system.log
[...]
Feb 21 16:31:10 [...] kernel[0]: KauthORama_start: Hello Cruel World!
[...]

You can also dump the sysctl tree to confirm that the KauthORama node is present.

$ sysctl -a | grep Kauth
kern.com_example_apple_samplecode_kext_KauthORama: 

Once the sample is loaded, you have to configure it.  For this example we're going to use KauthORama to monitor file operations within a specific directory.  To prevent our output being lost in the general background noise, we do all of our operations within the "KauthTest" directory in the root directory.  So we start by creating the target directory.

$ sudo mkdir /KauthTest

Then we configure KauthORama using sysctl.

$ sudo sysctl -w kern.com_example_apple_samplecode_kext_KauthORama="add com.apple.kauth.fileop /KauthTest"
kern.com_example_apple_samplecode_kext_KauthORama:  -> add com.apple.kauth.fileop /KauthTest

The value of the kern.com_example_apple_samplecode_kext_KauthORama sysctl variable is a string that represents KauthORama's configuration.  In this case the string says to "install a listener for the com.apple.kauth.fileop scope and dump out any information that occurs within the /KauthTest directory".

To test this, make a copy of the "echo" command in the "/KauthTest" directory and then execute it.

$ sudo cp /bin/echo /KauthTest/NewEcho
$ /KauthTest/NewEcho 'Hello Cruel World!'
Hello Cruel World!
$ sudo rm /KauthTest/NewEcho

If you dump the system log again, you'll see a bunch of entries.  There's a typical example below, with the various system log prefixes (the date and time, and so on) stripped off to make things clearer.

scope=com.apple.kauth.fileop, action=KAUTH_FILEOP_OPEN, uid=0, vnode=0xffffff80129ea610, path=/KauthTest/NewEcho

scope=com.apple.kauth.fileop, action=KAUTH_FILEOP_CLOSE, uid=0, vnode=0xffffff80129ea610, path=/KauthTest/NewEcho, dirty=true

scope=com.apple.kauth.fileop, action=KAUTH_FILEOP_OPEN, uid=89, vnode=0xffffff80129ea610, path=/KauthTest/NewEcho

scope=com.apple.kauth.fileop, action=KAUTH_FILEOP_CLOSE, uid=89, vnode=0xffffff80129ea610, path=/KauthTest/NewEcho, dirty=false

scope=com.apple.kauth.fileop, action=KAUTH_FILEOP_EXEC, uid=501, vnode=0xffffff80129ea610, path=/KauthTest/NewEcho

scope=com.apple.kauth.fileop, action=KAUTH_FILEOP_DELETE, uid=0, vnode=0xffffff80129ea610, path=/KauthTest/NewEcho

As you can see, copying the file as root involved opening and closing it as root (UID 0).  The close is interesting because you can see that the dirty flag is set.  The second open / close pair is Spotlight indexing the file (UID 89 is _spotlight).  This time the file isn't dirty when it's closed.  Next you see the KAUTH_FILEOP_EXEC operation generated by running the "NewEcho" command.  Finally, there's a KAUTH_FILEOP_DELETE operation generated by the "rm".

How it Works
------------
For a detailed discussion of Kauth, see DTS Technote 2127 "Kernel Authorization".

<https://developer.apple.com/library/mac/technotes/tn2127/_index.html>

When you load KauthORama, it installs a sysctl oid (a node in the sysctl tree) called "kern.com_example_apple_samplecode_kext_KauthORama".  When you modify that oid, the SysctlHandler routine calls ConfigureKauth to interpret the new configuration string.  If the string is an "add" command, it installs a scope listener for the specified Kauth scope.  When an action is authorized within the scope, the kernel calls Kauth's scope listener.  This prints the action and its parameters, and then returns KAUTH_RESULT_DEFER to indicate that it has no information about whether this operation should be allowed.

Caveats
-------
In general, writing kernel code is hard.  Writing a Kauth listener is especially hard because it's intimately tied into critical kernel subsystems.   DTS Technote 2127 "Kernel Authorization" describes the Kauth technology in detail.  I strongly recommend that you read this technote before starting any Kauth development.

<https://developer.apple.com/library/mac/technotes/tn2127/_index.html>

KauthORama was coded for simplicity, not efficiency.  A production Kauth listener should be much more careful about its impact on system performance.

Credits and Version History
---------------------------
If you find any problems with this sample, please file a bug against it.

<https://developer.apple.com/bug-reporting/>

1.0 (May 2005) was the first shipping version.

1.1 (Jul 2005) was updated to include an Xcode 2.1 project to produce universal binaries.  There were no code changes required for it to run correctly on the Developer Transition Systems.  However, I did modify the code slightly to eliminate some new warnings produced by GCC 4.0.

1.2 (Jan 2007) added a workaround to the kernel bug.  I also tweaked the project a little to make it easier to update, and to bring in into line with my current coding standards.

1.3 (Apr 2007) included minor editorial changes.

1.4 (Mar 2014) was updated to support the latest tools and techniques (64-bit, Developer ID code signing, Xcode 5, and so on) (r. 16127581) (r. 9272790).  It also added support for the KAUTH_FILEOP_DELETE operation (r. 6511762).

Share and Enjoy

Apple Developer Technical Support
Networking, Communications, Hardware

26 Mar 2014
```

[Next](Document%20Revision%20History.md)[Previous](KauthORama.c.md)

