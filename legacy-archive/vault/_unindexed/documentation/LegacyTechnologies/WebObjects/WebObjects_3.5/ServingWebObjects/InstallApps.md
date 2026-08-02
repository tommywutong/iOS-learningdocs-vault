---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/InstallApps.html
archived_at: '2026-07-15T07:55:58.978733Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](AdminTasks.md)[Previous
Section](AdminTasks.md) 

## Installing Applications

You can use the developer application Project Builder
to deploy WebObjects applications. When an application is ready to be deployed,
do the following in Project Builder:

1. Click the inspector button to open the Build Attributes Inspector.
   In the Install in field, type __$(NEXT_ROOT)/NextLibrary/WOApps__. 

If you're installing a framework, type __$(NEXT_ROOT)/NextLibrary/Frameworks__

2. If your project contains web server resources, go to the __Makefile.preamble__
   file under Supporting Files. Uncomment the following macro: 

INSTALLDIR_WEBSERVER

3. In the Project Build panel, click the checkmark button to bring up
   the Build Options panel. 
4. Choose __install__ as the build target, and close the Build Options
   panel. 
5. Click the Build button to start the build and installation process.

Assuming that your application is named __MyApp.woa__,
this procedure installs these directories:

```
NeXT_ROOT/NextLibrary/WOApps/MyApp.woa

        MyApp[.exe]

        Resources/

        WebServerResources/

<DocRoot>/WebObjects/MyApp.woa

        WebServerResources/
```

As discussed previously in the section "[Adaptor
Modes](AdaptorModes.md#apple-gq3dcmq)," when the client tries to contact an application, the adaptor
first looks for a public configuration file that names the application,
then for a private configuration file that names the application, and then
for an executable in _<DocRoot>___/WebObjects__ and _NeXT_ROOT___/NextLibrary/WOApps__.
Thus, you can install the entire directory under _<DocRoot>___/WebObjects__,
but doing so presents a security problem if you have scripted components.
Any client can access any file under the document root, which means that
if you install scripted components under the document root, you are exposing
source code to outside users.

Instead, it is recommended that you install most
of the application in _NeXT_ROOT___/NextLibrary/WOApps__ and install
only the web server resources under the document root. It is also recommended
that you install the application directly in the _<DocRoot>___/WebObjects__
directory rather than in a subdirectory. If you install in a subdirectory,
your application can still run but cannot find image files unless you provide
the application path on the command line. For more information, see "[Starting
Up Applications From the Command Line](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/ServingWebObjects/ManualStarting.html#4941)" in this guide.

[!](ServingWebObjectsTOC.md)[Table
of Contents](ServingWebObjectsTOC.md) [!](StartApps.md)[Next
Section](StartApps.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
