---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/ConfigFiles.html
archived_at: '2026-07-15T07:55:54.041939Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.md) [!Previous Section](HTTPAdaptors.md)

## Configuration Files

WebObjects HTTP adaptors use configuration files to locate WebObjects application processes. There are two types of configuration files: public and private.

- The _public configuration file_ is _NeXT_ROOT___/NextLibrary/WOAdaptors/Configuration/WebObjects.conf__. (_NeXT_ROOT_ is defined at system installation time.) This file tells the adaptor what applications are (or should be) running and allows the adaptor to balance transactions among different instances of the same application. You create the public configuration file using the Monitor application as described in the section "[Initial Monitor Setup](InitialSetup.md#apple-gq3temi)" in this guide.

In general, you want one public configuration file per site. That means if you have multiple machines running WebObjects, you should access all WebObjects applications through a single machine that is running the HTTP server and that contains the public configuration file.

If you have multiple HTTP servers running on a single machine, they all share the public configuration file. If you want each server to have its own configuration file, you can install one __WebObjects.conf__ file in each server's configuration directory.

- A _private configuration file_ is also named __WebObjects.conf__ and is located in the temporary directory of the system (__/tmp__ for Mach, Solaris, and HP-UX platforms or the directory specified by the TEMP environment variable on the Windows NT platform). If the WebObjects adaptor cannot find the public configuration file or if it cannot find the requested WebObjects application in the public configuration file, it searches the private configuration file.

A new private configuration file is created automatically any time a WebObjects application is started and a private configuration file doesn't exist. The adaptor contacts only one instance of an application in the private configuration file; if you manually start HelloWorld and it's already been started, the entry for HelloWorld in the file is overwritten. (The old process will continue to run, but cannot be contacted.) The adaptor also cannot contact a remote instance of an application using the private configuration file.

The contents of the private configuration file are essentially the same as those of the public configuration file, except that the contents are stored as C structures and so cannot be directly modified. This file should only be modified by the WebObjects adaptor itself.

[!Table of Contents](ServingWebObjectsTOC.md) [!Next Section](AdaptorModes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
