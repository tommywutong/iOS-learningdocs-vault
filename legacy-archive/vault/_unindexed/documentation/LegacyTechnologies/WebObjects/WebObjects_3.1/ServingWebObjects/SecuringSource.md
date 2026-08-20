---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/SecuringSource.html
archived_at: '2026-07-15T07:50:01.215164Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](Autostarting.md)

# Securing Application Source Code

Clients can browse source code in _DOCUMENT_ROOT___/WebObjects__ unless you take steps to prevent them. If you don't deny access, a user could submit this URL:

```
    http://host/WebObjects
```

They could get a directory listing of WebObjects applications on your machine and, from there, browse the source code of scripted and compiled applications.

You can take two approaches to prevent this breach of security:

- __Disallowing read access__: Configure your web server to disallow read access to WebObjects-related files (\*.wos, \*.wod, \*.plist, and so on). This configuration won't affect the operation of WebObjects applications, which access the file system directly, but will prevent the server from dispensing these files to browsers.

  Consult you server-administration documentation for procedures on setting read access.
- __Moving applications to NextLibrary/WOApps__: For WebObjects 3.0 or higher, move your WebObjects applications from the server's document root to __NextLibrary/WOApps__. You must move the entire application (that is, the ".woa" directory and everything in it). However, if any of your pages have static links to resources like image or sound files (for example, <IMG src="../Images/logo.gif">), you must leave a "sparse" copy of the application in the document root so that the client's browser can find these resources. In this case, "sparse" means that the application's directory structure is reproduced in the document root, but the only files it contains are the static resources that the server must dispense to a client's browser.

  If you choose to move a scripted application to __NextLibrary/WOApps__, and want to keep the ability for autostarting that application, you must take one further step. Each application in the __WOApps__ directory must contain an executable, but a scripted application located in the server's document root relies on the default application, __WODefaultApp__ (in __NextLibrary/Executables__), as its executable. So, when you move the scripted application into __WOApps__, copy the default application into your scripted application, and then rename this copy with the name of your application.
