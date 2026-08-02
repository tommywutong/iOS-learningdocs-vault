---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.2e.html
archived_at: '2026-07-15T08:09:35.398121Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Checking%20the%20Installation.md) [!](Solaris%20or%20HP-UX.md) [!](Problems%20With%20Scripted%20Applications.md)

---

#   Mac OS X Server

On Mac OS X Server, these locations should contain the following files or directories:

- 

  Your Apache server's _cgi-bin_
  directory (
  /Local/Library/WebServer/CGI-Executables
  ).
  - 

    WebObjects
    : The WebObjects adaptor
- 

  Your server's _document root_
  directory (
  /Local/Library/WebServer/Documents
  )
  - 

    This directory should contain the following (in addition to any WebObjects applications you may have installed):

    _HTTP_Server_Doc_Root_
    /

        WebObjects/

            Frameworks/

                DirectToJavaClient.framework/

                    WebServerResources/

                DirectToWeb.framework/

                    WebServerResources/

                EOJavaClient.framework/

                    WebServerResources/

                WOExtensions.framework/

                    WebServerResources/

            Java/

                directtoweb.jar

                eojavaclient.jar

                woextensions.jar

                com/

                    apple/

                        client/

                            directtoweb/

                            eoapplication/

                            eocontrol/

                            eodistribution/

                            eogeneration/

                            eointerface/

                            foundation/

                            playback/

                            webobjects/
- 

  /System/Library
  directory

  Check for these files and directories:

  - 

    Frameworks/WebObjects.framework
    : WebObjects library of classes, plus header files (Developer installations only)
  - 

    Frameworks/WOExtensions.framework
    : WebObjects Extensions framework, which contains extra dynamic elements and shared components
  - 

    Java
    :
    The Java interfaces to WebObjects classes.
  - 

    WebObjects/Adaptors
    : Contains WebObjects configuration files and adaptors.
  - 

    WebObjects/Executables
    :
    Contains
    WODefaultApp
    , the default application executable for scripted WebObjects applications

####  Corrective action:

If the WebObjects adaptor is missing from your Apache web server's _cgi-bin_
directory, reinstall it using the instructions found in
/System/Library/WebObjects/Adaptors/Apache/Installation.html
.

If you are missing any of the contents of your server's _document root_
directory, copy the missing files from the following locations, or simply reinstall WebObjects.

|   If you are missing... |   Copy it from... |
| --- | --- |
|   DirectToJavaClient.framework/ WebServerResources |   /System/Library/Frameworks/DirectToJavaClient.framework/ |
|   DirectToWeb.framework/  WebServerResources |   /System/Library/Frameworks/DirectToWeb.framework/ |
|   EOJavaClient.framework/  WebServerResources |   /System/Library/Frameworks/EOJavaClient.framework/ |
|   WOExtensions.framework/  WebServerResources |   /System/Library/Frameworks/WOExtensions.framework/ |
|   Java/directtoweb.jar |   /System/Library/Frameworks/DirectToWeb.framework/  WebServerResources/Java/ |
|   Java/eojavaclient.jar |   /System/Library/Frameworks/EOJavaClient.framework/  WebServerResources/Java/ |
|   Java/woextensions.jar |   /System/Library/Frameworks/WOExtensions.framework/  WebServerResources/Java/ |
|   Java/com/apple/client/\* |   Obtain the contents of the  client directory by combining the  WebServerResources/Java/com/apple/client/ directories of the DirectToWeb, EOJavaClient, DirectToJavaClient, and WOExtensions frameworks (all in  /System/Library/Frameworks ) |

If you are missing any of the contents of your
/System/Library
directory, reinstall WebObjects.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Checking%20the%20Installation.md) [!](Solaris%20or%20HP-UX.md) [!](Problems%20With%20Scripted%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
