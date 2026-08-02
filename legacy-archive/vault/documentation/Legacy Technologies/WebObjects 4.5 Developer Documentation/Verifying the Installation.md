---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.29.html
archived_at: '2026-07-15T08:09:32.894576Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Troubleshooting.md) [!](Troubleshooting.md) [!](Troubleshooting-2.md)

---

#  Verifying the Installation

At this point, you should have installed WebObjects as described in the _WebObjects Installation Guide_
(included with the WebObjects 4.5 CD), perform the post-installation steps for your operating system as described in the first part of this document, and rebooted your computer.

After you have completed the installation and the post-installation, verify the installation by performing the following steps:
> __Note:__These steps assume you've installed WebObjects Developer. The examples mentioned below are not installed with WebObjects Deployment. To verify a Deployment installation, you might complete these same steps running other applications.

1. 

   Verify that the WebObjects processes are running.

   On Windows NT, open the Services control panel and verify that "Apple Mach Daemon", "Apple NetName Server", and "Apple WebObjects Task Daemon" are all running (their startup mode should be set to "Automatic").

   On Mac OS X Server, click the icon in the upper left-hand corner of the screen and choose "Show All Processes". Verify that
   nmserver
   ,
   woservice
   , and
   wotaskd
   are all running.

   On Solaris and HP-UX, type "
   ps -eaf
   " in a shell window and verify that
   machd
   ,
   nmserver
   , and
   wotaskd
   are all running.
2. 

   Try to run a simple scripted application.

   Open a command-shell window (on Windows NT, open a Bourne shell window) and enter the following commands:

   > cd
   _NEXT_ROOT_

   /Developer/Examples/WebObjects/WebScript/
   HelloWorld

   >
   _NEXT_ROOT_

   /Library/WebObjects/Executables/
   WODefaultApp[.exe]

   where:

   _NEXT_ROOT_
   is the directory in which you installed WebObjects software (_NEXT_ROOT_
   isn't applicable on Mac OS X systems).

   These commands should run the HelloWorld example application, launch a web browser, and enter HelloWorld's URL in the browser. If this doesn't work, go to the topic _[Troubleshooting](Troubleshooting-2.md#apple-gqyteobt)_
   .

   After you have verified that HelloWorld runs, type Control-C to shut it down.
3. 

   If scripted applications work, try running compiled applications. Enter the following commands:

   > cd ../../Java/Movies/Movies.woa
   > ./Movies[.exe]

   If you have trouble running compiled applications, go to the topic _[Troubleshooting](Troubleshooting-2.md#apple-gqyteobt)_
   .

   After you have verified that Movies or HelloWorldCompiled runs, type Control-C to shut it down.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Troubleshooting.md) [!](Troubleshooting.md) [!](Troubleshooting-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
