---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/Installing_Applications.html
archived_at: '2026-07-15T08:12:00.383389Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Setting_Up_Hosts.md)[!](Setting_Up_Applications.md)

## Installing Applications

Before you can deploy applications on your site, you have
to install them on the hosts on which you want to run instances
of them. Most applications have files of two types:

- __application
  files,__ which store the application's logic
- __Web server resources,__ which store resources
  that can be shared among applications

The developer tool Project Builder (used to develop WebObjects
applications) can be used to install an application on a host. With
it, you can create an application bundle (a directory in the file
system) with source code and resources the application needs to
run. All the application files for the application can be included
in the application bundle; however, doing so exposes the application's
source to outside agents.

Instead, you should perform a split install, installing most
of the application in a directory that is not accessible to the
outside world. The nonsensitive resources can be placed on the Web
server's `Document Root` directory.

To perform a split install of your application, navigate to
your project's directory and execute the following command as `root` using
your shell editor:

```
pbxbuild install -buildstyle WebServer DSTROOT=/
```

This places the application files in the /Library/WebObjects/Applications directory
and the Web server resources in the Document Root/WebObjects directory.

### Installing the Application Files

You can place application files in any directory of the application
host.

### Installing the Web Server Resources

You must place Web server resource files in the Web server `Document
Root` directory of the application host. Make
sure that you use the following organization:

```
<Web server Document Root>/
    WebObjects/
        AppName.woa/
            Contents/
                WebServerResources/
                    <resource files>
```

[!](Setting_Up_Hosts.md)[!](Setting_Up_Applications.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
