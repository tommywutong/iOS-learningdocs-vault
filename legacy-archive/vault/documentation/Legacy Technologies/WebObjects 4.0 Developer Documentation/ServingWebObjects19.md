---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects19.html
archived_at: '2026-07-18T01:23:38.701848Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](Administrative%20Tasks.md)

## Installing Applications

You can use the developer application Project Builder to deploy WebObjects applications. When an application is ready to be deployed, do the following in Project Builder:

- Click the inspector button to open the Build Attributes Inspector. In the Install in field, type `$(NEXT_ROOT)/Library/WebObjects/Applications`.

If you're installing a framework, type `$(NEXT_ROOT)/Library/Frameworks`

- If your project contains web server resources, go to the __Makefile.preamble__ file under Supporting Files. Uncomment the following macro:

INSTALLDIR_WEBSERVER

- In the Project Build panel, click the checkmark button to bring up the Build Options panel.
- Choose __install__ as the build target, and close the Build Options panel.
- Click the Build button to start the build and installation process.

Assuming that your application is named __MyApp.woa__, this procedure installs these directories:

```
NEXT_ROOT/Library/WebObjects/MyApp.woa
    MyApp[.exe]
    Resources/
    WebServerResources/
<DocRoot>/WebObjects/MyApp.woa
    WebServerResources/
```


As discussed in the section "[Adaptor Modes](ServingWebObjects3.md#apple-gq3dcmq)," when the client tries to contact an application, the adaptor first looks for a public configuration file that names the application, then for a private configuration file that names the application, and then for an executable in _<DocRoot>___/WebObjects__ and _NEXT_ROOT___/Library/WebObjects/Applications__. Thus, you can install the entire directory under _<DocRoot>___/WebObjects__, but doing so presents a security problem if you have scripted components. Any client can access any file under the document root, which means that if you install scripted components under the document root, you are exposing source code to outside users.

Instead, it is recommended that you install most of the application in _NEXT_ROOT___/Library/WebObjects/Applications__ and install only the web server resources under the document root. It is also recommended that you install the application directly in the _<DocRoot>___/WebObjects__ directory rather than in a subdirectory. If you install in a subdirectory, your application can still run but cannot find image files unless you provide the application's base URL (WOApplicationBaseURL) on the command line. For more information, see "[Starting Up Applications From the Command Line](ServingWebObjects21.md#apple-gq4timi)" in this guide.

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects20.md)
