---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-18.html
archived_at: '2026-07-15T08:04:41.224501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20WebObjects%20Applications.md) [!](Configuration%20File%20DTD.md) [!](Deploying%20With%20Monitor.md)

---

# Installing Applications

You can use the developer application Project Builder to deploy WebObjects applications. When an application is ready to be deployed, do the following in Project Builder:

1. Click the inspector button to open the Build Attributes Inspector. In the Install in field, type the path to the directory in which the application is to be installed, such as
   $(LOCAL_LIBRARY_DIR)/WebObjects/Applications
   .
> If you're installing a framework,
> type
> $(LOCAL_LIBRARY_DIR)/Library/Frameworks

__Note:__You'll need write permission for the directory into which the application is to be installed in order for the build to succeed.

2. If your project contains web server resources, go to the __Makefile.preamble__
   file under Supporting Files. Uncomment the following macro:
> INSTALLDIR_WEBSERVER

__Note:__You'll need write permission for the WebServer's doc root in order for such a "split install" to succeed.

3. In the Project Build panel, click the check-mark button to bring up the Build Options panel.
4. Choose __install__
   as the build target, and close the Build Options panel.
5. Click the Build button to start the build and installation process.

Assuming that your application is named __MyApp.woa__
, and that you installed your application in _LOCAL_LIBRARY_DIR_

/WebObjects/Applications
, the following directories will be created:

`
LOCAL_LIBRARY_DIR
/WebObjects/Applications/MyApp.woa`
`
  MyApp[.exe]`
`
  Resources/`
`
  WebServerResources/`
`
DOC_ROOT
/WebObjects/MyApp.woa`
`
  WebServerResources/`

When the client tries to contact an application, the adaptor first looks for a configuration file that names the application, and then for an executable in  ___DOC_ROOT___
__/WebObjects__
and  ___NEXT_ROOT___
__/Library/WebObjects/Applications__
. Thus, you can install the entire directory under  ___DOC_ROOT___
__/WebObjects__
. However, doing so presents a security problem if you have scripted components, since any client can access any file under the document root. This means that if you install scripted components under the document root, you're exposing source code to outside users.

Instead, it is recommended that you do a "split install", installing most of the application in  ___NEXT_ROOT___
__/Library/WebObjects/Applications__
and install only the web server resources under the document root. It is also recommended that you install the application directly in the  ___DOC_ROOT___
__/WebObjects__
directory rather than in a subdirectory. If you install in a subdirectory, your application will still run but won't find image files unless you explicitly provide the application's base URL (WOApplicationBaseURL). For more information, see [Starting Up Applications From the Command Line](Deploying-29.md#apple-ge3tkmjv).

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20WebObjects%20Applications.md) [!](Configuration%20File%20DTD.md) [!](Deploying%20With%20Monitor.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
