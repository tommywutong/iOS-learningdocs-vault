---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/WhereThingsGo.html
archived_at: '2026-07-15T07:47:13.399098Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](RoleOfExecutable.md)

# Where Things Go

!Figure 7. WebObjects Directories
_NeXT_ROOT_, the installation directory, depends on the platform you are using:

| __ Platform__ | __ Installation Directory__ |
|  Mach |  / |
|  Solaris |  Defined at installation time. |
|  Windows NT |  Defined at installation time. |

```
```


After you install WebObjects, you'll find the following items:

- __NextDeveloper/Apps/WebObjectsBuilder.app__ contains the WebObjects Builder application (WebObjects Pro or Enterprise only).
- __NextDeveloper/Examples/WebObjects__ contains several sample WebObjects applications.
- __NextLibrary/WOAdaptors__ contains the WebObjects adaptors. If you have WebObjects Pro or Enterprise, this directory also contains adaptor source code, which you can compile for additional platforms.

Your HTTP server does not access the adaptor in this directory. Instead, it accesses a link or copy of it in the server's __<cgi-bin>__ directory.

- __NextLibrary/WOApps__ is an empty directory when first installed. If you create applications that contain compiled code, you place the application's executable in this directory.

If the application's executable is in __WOApps__, you can also place the application's entire __.woa__ directory in __WOApps__. This ensures the __.woa__ directory's privacy; if you place the __.woa__ under the document root and outside users have read access on __.wos__ and __.wod__ files, they have access to the application's source. However, if the application imports any images or sounds, you must leave a "sparse" copy of the application in the document root so that the client's browser can find these resources. In this case "sparse" means that the application's directory structure is reproduced in the document root, but the only files it contains are the static resources that the server must dispense to a client's browser.

__Note:__ Applications in __WOApps__ must include the executable file. If you have a WebObjects application that relies on the generic application executable (__NextLibrary/Executables/WODefaultApp__) and you want to place it in __WOApps__, you can still do so. Copy __WODefaultApp__ into that application's directory and name the copy after your application.

- __NextLibrary/Executables__ contains __WODefaultApp__, the generic application executable.
- __NextLibrary/Frameworks__ contains the WebObjects framework, the library of WebObjects classes. This is also where you find header files.
- __NextLibrary/Java__ contains the Java classes provided by Sun and the Java interfaces to the classes in the WebObjects framework.

To run the WebObjects applications you write, your web server must be able to access the adaptor and the application's code or script. Therefore, after installing WebObjects, make sure your web server's directories contain the following links or copies:

- _<cgi-bin>/WebObjects_ is a copy of or link to the CGI adaptor __NextLibrary/WOAdaptors/CGI/WebObjects__ (or __WebObjects.exe__).
- _<DocumentRoot>/WebObjects/Examples_ is a copy of or link to __NextDeveloper/Examples/WebObjects__.

[Figure 8](#apple-g44ds) shows the resources that should be present in your web server after the WebObjects installation process is completed. If any of these links or copies are missing, check the instructions in "[About WebObjects."](../../PostInstall.md)!Figure 8. The Contents of Your Web Server's Directories After Installing WebObjects

[!Table of Contents](Start.book.md) [!Next Section](Summary.md)
