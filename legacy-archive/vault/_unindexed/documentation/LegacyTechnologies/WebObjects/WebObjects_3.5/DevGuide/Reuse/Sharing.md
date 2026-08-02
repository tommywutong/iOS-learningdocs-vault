---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Reuse/Sharing.html
archived_at: '2026-07-15T07:52:06.789187Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ReuseTOC.md) [!Previous Section](Synchronize.md)

# Sharing Reusable Components Across Applications

If a component is in the WebObjects application's directory, it can be used over and over again, but only within that application. This may be fine for some components, but others, you'll want the option to reuse in many applications. If a component is packaged in a framework, it can be used in any WebObjects application.
To package components in a framework for reuse by several applications, do the following:

- Create a project in Project Builder of type WebObjectsFramework.
- Add to this project (under Web Components) all of the components that you want to share across applications.
- Add any resources needed by the components. If the HTTP server needs access to the resource (which is the case for image files and any file that will ultimately be referenced in the HTML file), add it under WebServerResources. Otherwise, add it under Resources.
- Build the framework. If you perform a make install, it installs the framework in _NeXT_ROOT___/NextLibrary/Frameworks__ and the WebServer resources in <DocRoot>__/WebObjects/Frameworks__.

You must build the framework even if it contains only scripted components.

After the framework is installed, you need to set up the applications so that they can use components in that framework. Do the following:

- In Project Builder, add the framework to the application's project under Frameworks.
- Build the application.

The application's executable file must contain all components that your application references, as described in the next section. For this reason, you must build the application even if it contains only scripted components.

[!Table of Contents](ReuseTOC.md) [!Next Section](SearchPath.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
