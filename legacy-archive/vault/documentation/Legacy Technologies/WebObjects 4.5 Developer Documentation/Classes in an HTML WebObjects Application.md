---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/EOFClasses3.html
archived_at: '2026-07-15T08:03:02.695624Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](Classes%20in%20an%20Application%20Kit%20Client-Server%20Application.md)

# Classes in an HTML WebObjects Application

The major difference between an Application Kit application and an HTML web application is that the web application uses the WebObjects framework instead of the Application Kit. [Figure 17](#apple-geydimbv) shows how the WebObjects framework provides a web application's presentation layer.

The WebObjects box is jagged at the top because not all of the WebObjects classes that participate in user interface management are illustrated. For example, the WebObjects framework provides user interface elements such as WOTextField and WOBrowser for generating web pages that users see in their browsers. None of these classes are shown. Rather, [Figure 17](#apple-geydimbv) shows only the WebObjects framework class that acts as the go-between for Enterprise Objects Framework's control layer and WebObjects user interface: WODisplayGroup.

WODisplayGroup is analogous to the interface layer's EODisplayGroup. They have virtually the same APIs, but EODisplayGroup works with the interface layer's EOAssociation's and WODisplayGroup works with WebObjects framework elements.

!

Figure 17. Classes in an HTML WebObjects Application

Note that you don't have to use WODisplayGroup's in your application. It's primarily useful for managing _batches_ of enterprise objects, so users can page through the first set of objects, then the second, and so on. Additionally, WebObjects Builder has a lot of built-in support for WODisplayGroups. Using them, it's much simpler to construct the user interface for your web application, writing less code than you might if you were to use your own solution.

[!Table of Contents](Enterprise%20Objects%20Framework%20Viewed%20Through%20Its%20Classes.md) [!Next Section](Classes%20in%20a%20Web%20Application%20with%20a%20Java%20Client.md)
