---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects2.html
archived_at: '2026-07-18T01:23:38.756813Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](WebObjects%20HTTP%20Adaptors.md)

## Configuration Files

WebObjects HTTP adaptors use configuration files to locate WebObjects application processes. There are two types of configuration files: public and private.

- The _public configuration file_ is _NEXT_ROOT___/Library/WebObjects/Configuration/WebObjects.conf__. (_NEXT_ROOT_ is defined at system installation time on Windows NT systems; on Mac OS X Server and similar systems, it is always __/System__.) This file tells the adaptor what applications are (or should be) running and allows the adaptor to balance transactions among different instances of the same application. You create the public configuration file using the Monitor application as described in the section "[Setting Up the Monitor Application](Deploying%20With%20the%20Monitor%20Application.md#apple-gu4tgmi)" in this guide.

In general, you want one public configuration file per site. That means if you have multiple machines running WebObjects, you should access all WebObjects applications through a single machine that is running the HTTP server and that contains the public configuration file.

If you have multiple HTTP servers running on a single machine, they all share the public configuration file. If you want each server to have its own configuration file, you can install one __WebObjects.conf__ file in each server's configuration directory if you a using an API adaptor, or in each server's __cgi-bin__ or __scripts__ directory if you are using the CGI adaptor.

- A _private configuration file_ is also named __WebObjects.conf__ and is located in the temporary directory of the system (__/tmp__ for Mac OS X Server, Solaris, and HP-UX platforms or the directory specified by the TEMP environment variable on the Windows NT platform). If the WebObjects adaptor cannot find the public configuration file, it searches the private configuration file. Thus the public configuration file ensures security in deployment mode because only the applications you list are accessible.

A new private configuration file is created automatically any time a WebObjects application is started and a private configuration file doesn't exist. The adaptor contacts only one instance of an application in the private configuration file; if you manually start HelloWorld and it's already been started, the entry for HelloWorld in the file is overwritten. (The old process will continue to run, but cannot be contacted.) The adaptor also cannot contact a remote instance of an application using the private configuration file.

The contents of the private configuration file are essentially the same as those of the public configuration file. This file should only be directly modified by the WebObjects adaptor itself.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects3.md)
