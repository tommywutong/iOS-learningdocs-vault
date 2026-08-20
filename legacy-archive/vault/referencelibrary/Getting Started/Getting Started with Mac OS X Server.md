---
title: Getting Started with Mac OS X Server
apple_id: TP30001141
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_MacOSXServer/_index.html
archived_at: '2026-07-18T02:39:24.371222Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Mac OS X Server combines the most popular open source server technologies with Apple's easy-to-use setup, management, and monitoring tools. It comes with an extensive suite of services for supporting Mac, Windows, and mixed-client environments in businesses, departments, and educational institutions. And because it's all based on open standards, Mac OS X Server integrates easily with existing networks.

### Start Here

Before you begin to write any code, it’s a good idea to become familiar with the features of OS X Server. If you haven’t already done so, read the [product overview](http://www.apple.com/macosx/server/), the [administration guides](http://www.apple.com/server/documentation/), and the [developer introduction](https://developer.apple.com/server/).

### Choose a Learning Path

Mac OS X Server, based on the open source Darwin project and expanded through the integration of many industry-standard open-source services, provides many opportunities for you to add functionality in the form of scripts, plug-ins, and applications, and even to extend the capabilities of the operating system itself.

If you are an in-house developer who, in keeping with the best UNIX traditions, needs to extend or modify the services provided by Mac OS X Server, start by viewing the [Apple Server Solutions](http://www.apple.com/server/resources/) site for Mac OS X Server to see the wide range of options open to you.

#### Providing Access to Network File Services

- If you want your application to take advantage of networked file sharing services, read [Apple Filing Protocol Programming Guide](../../documentation/Networking/Apple%20Filing%20Protocol%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnju) to learn the AFP file system structure and the AFP commands for manipulating files on a server.
- If you want your application to take advantage of Open Directory for centralized LDAP directory-based resource management, read [Open Directory Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Directory/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000917).
- If you want your application to include directory services, read [Open Directory Plug-in Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000918) to learn how to create customized Open Directory plug-in libraries.

#### Providing Access to Network Printing Services

If you want your application to take advantage of Mac OS X Server’s managed network printing services based on the Common UNIX Printing System (CUPS), read [Getting Started with Printing](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Printing/_index.html#//apple_ref/doc/uid/TP30001080).

#### Hosting Web Content

Web hosting services in Mac OS X Server are provided by an Apple-optimized version of the open source Apache web server. Streaming multimedia content over the Web is supported by Apple’s open source QuickTime Steaming Server.

- If you want to embed dynamic logic in your HTML code as server-side includes or common gateway interface (CGI) scripts, see the [Apache documentation site](http://httpd.apache.org/docs-project/). Many good books on CGI scripting are available, among them [CGI Programming with Perl, Second Edition](http://safari.oreilly.com/?XmlId=1-56592-419-3), from O’Reilly & Associates.
- If you prefer to use Java for your dynamic code, you can create JavaServer Pages (JSPs) and Java servlets, both supported by Tomcat and a robust Java virtual machine (JVM). See the [Apache Tomcat site](http://jakarta.apache.org/tomcat) for further information.
- If your application needs to display multimedia content streamed over the Internet from the QuickTime Streaming Server (QTSS), read [QuickTime Streaming Guide](../../documentation/Quick%20Time/QuickTime%20Streaming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbv) for information on creating streams from live sources and on creating, serving, and receiving streamed content, and [QuickTime Streaming Server Modules Programming Guide](../../documentation/Quick%20Time/QuickTime%20Streaming%20Server%20Modules%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbt) for information on adding your own functionality to change or extend the capabilities of QTSS.

### Next Steps

The [Mac OS X Server Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000426) includes the following high-level resource pages, which can be bookmarked for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000426)

  Conceptual and how-to information for Mac OS X Server.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000426)

  Focused, detailed descriptions in reference format for Mac OS X Server.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000421)

  Late-breaking news about new or changed features in technologies related to Mac OS X Server.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000426)

  Examples of small programs to get you started on the right foot with Mac OS X Server.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000426)

  Supplementary documentation on specific Mac OS X Server issues.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000426)

  Design information and FAQs by Apple’s support engineers.
- Mailing Lists

  The Mac OS X Server mailing list ([macos-x-server](http://lists.apple.com/mailman/listinfo/macos-x-server)) is an excellent place to discuss issues surrounding the installation and administration of Mac OS X Server and related technologies. Join the System Imaging discussion list ([system-imaging](http://www.lists.apple.com/mailman/listinfo/system-imaging)) to participate in discussion of the NetBoot and NetInstall system imaging tools included with Mac OS X Server. In addition, there is a mailing list ([client-management](http://www.lists.apple.com/mailman/listinfo/client-management)) devoted to Mac OS X client management and using the Workgroup Manager application included with Mac OS X Server.

