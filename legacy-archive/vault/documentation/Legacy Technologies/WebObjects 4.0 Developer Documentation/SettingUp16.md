---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/SettingUp16.html
archived_at: '2026-07-18T01:27:43.352436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](SettingUp15.md)

## Installing Your Application

Some files in a web application (such as images and sounds) must be stored under the web server's document root in order for the server to access them. The remaining files (such as your components and source code) must be accessible to your application but not necessarily by the web server itself.
In previous versions of WebObjects, it was typical to store the entire project under the web server's document root. This practice has advantages for turnaround time during development. However, in deployment, it presents the possibility of allowing users access to your source code. WebObjects has a "split installation" feature that allows you to install only those files (such as images) that the web server must have access to under the document root. The remaining files can be stored elsewhere.
The same procedure applies to installing WebObjects applications and frameworks. To install:

- Click ! to open the Project Inspector.
- Under "Install In:", set the path where the application wrapper will be installed.
- In Project Builder's Build panel, click !.
- From the Target pop-up menu, choose __install__. (By default, the target is set to __woapp__.)

!

- Click ! in the Build panel to install your application.

The full application wrapper is copied into the "Install In:" directory, and a wrapper containing only the Web Server Resources is copied into the document root.

See [_Serving WebObject_](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)s for more information about installing your application.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Rapid%20Turnaround%20Mode-2.md)
