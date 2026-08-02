---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/AppConfs.html
archived_at: '2026-07-15T07:58:14.406209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Top](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

#

# Application Configurations

---

When you use WebObjects Builder or Interface Builder to create the user interface of an Enterprise Objects Framework application, you also set up a network of behind-the-scenes objects including EODatabaseDataSources and EOEditingContexts. Some of these objects don't have representations in the builder applications, so you might not know they're there. Yet when you build and run your application, they're created automatically and they perform many important functions.
You rarely need to intervene in the automatic creation of these
behind-the-scenes objects, but sometimes you need to interact with them. Therefore, it's important to know when they're created and ready to do work. The same is true in applications that don't have a graphical user interface.
The flexibility of Enterprise Objects Framework allows endless configurations, but most are variations on a few basic arrangements. This chapter explains how the plumbing for typical Enterprise Objects Framework applications is established and how to implement variations on the typical configurations. It's organized into the following major sections:
[__Graphical User Interface Applications__](Graphical%20User%20Interface%20Applications.md)
[__Non-Graphical User Interface Applications__](Non-Graphical%20User%20Interface%20Applications.md)
[__Editing Context Configurations__](Editing%20Context%20Configurations.md)
[__Object Store Coordinator Configurations__](Object%20Store%20Coordinator%20Configurations.md)
[__Accessing Multiple Databases__](Accessing%20Multiple%20Databases.md)

[!First Section](Graphical%20User%20Interface%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
