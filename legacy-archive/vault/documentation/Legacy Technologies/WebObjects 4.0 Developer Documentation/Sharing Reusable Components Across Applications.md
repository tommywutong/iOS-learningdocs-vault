---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ReusableComponents7.html
archived_at: '2026-07-18T01:20:21.942973Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Creating%20Reusable%20Components.md) [!Previous Section](Creating%20a%20-Container-%20Reusable%20Component.md)

# Sharing Reusable Components Across Applications

If a component is in the WebObjects application's directory, it can be used in many places, but only within that application. This may be fine for some components, but others, you'll want the option to reuse across many applications. If a component is packaged in a framework, it can be used in any WebObjects application.
To package components in a framework for reuse by several applications, do the following:

- Create a project in Project Builder of type WebObjectsFramework.
- Add to this project (under Web Components) all of the components that you want to share across applications.
- Add any resources needed by the components. If the HTTP server needs access to the resource (which is the case for image files and any file that will ultimately be referenced in the HTML file), add it under WebServerResources. Otherwise, add it under Resources.
- Build the framework. If you perform a make install, it installs the framework in __NeXT_ROOT/Library/Frameworks__ and the web server resources in __<___DocRoot___>/WebObjects/Frameworks__.

After the framework is installed, you need to set up the applications so that they can use components in that framework. Do the following:

- In Project Builder, add the framework to the application's project under Frameworks.
- Build the application.

[!Table of Contents](Creating%20Reusable%20Components.md) [!Next Section](Search%20Path%20for%20Reusable%20Components.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
