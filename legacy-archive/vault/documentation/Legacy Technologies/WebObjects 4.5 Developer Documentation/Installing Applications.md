---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Deployment14.html
archived_at: '2026-07-15T08:05:19.496341Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Deployment13.md)

# Installing Applications

When an application is ready to be deployed, do the following in Project Builder:

- Click the inspector button to open the Build Attributes Inspector. In the Install in field, type __$(LOCAL_LIBRARY_DIR)/WebObjects/Applications__.

If you're installing a framework, type __$(LOCAL_LIBRARY_DIR)/Frameworks__.

- If your project contains web server resources, go to the __Makefile.preamble__ file under Supporting Files. Uncomment the line that defines this macro:

```
INSTALLDIR_WEBSERVER
```

- In the Project Build panel, click the checkmark button to bring up the Build Options panel.
- Choose "install" as the build target, and close the Build Options panel.
- Click the Build button to start the build and installation process.

Assuming that your application is named __MyApp.woa__, this procedure installs these directories:

```
NeXT_ROOT/Local/Library/WebObjects/MyApp.woa
    MyApp[.exe]
    Resources/
    WebServerResources/
```


and (assuming that you have web server resources):

```
<DocRoot>/WebObjects/MyApp.woa
    WebServerResources/
```


While you can install the entire directory under __<___DocRoot___>/WebObjects__, doing so presents a security problem if you have scripted components. Any client can access any file under the document root; if you've installed scripted components there, you are exposing source code to outside users. Instead, you should install most of your application in __NeXT_ROOT/Local/Library/WebObjects/Applications__ and install only the web server resources under the document root.
If you install the application in a subdirectory of __<___DocRoot___>/WebObjects__, you should set the WOApplicationBaseURL user default to point to the exact location of the application directory. (As with all user defaults, you can set WOApplicationBaseURL on the command line when launching the application or you can use the __defaults__ command.) For example:

```
defaults write MyApp WOApplicationBaseURL
/WebObjects/MyWebApps
```


If you don't set WOApplicationBaseURL, your application can still run but cannot find image files and other web server resources. For more information, see _[Serving WebObjects](Deploying%20WebObjects%20Applications.md)_.

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Deployment15.md)
