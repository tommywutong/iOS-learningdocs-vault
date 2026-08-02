---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.f.html
archived_at: '2026-07-15T08:11:28.235841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Supporting%20Files.md) [!](Libraries.md)

---

#   Frameworks

A _framework_
is a collection of classes and resources that an application can use. By storing items such as components and images in frameworks, you can reuse them in multiple projects without having to create multiple copies.

Every WebObjects Application project includes several frameworks by default. When you build, your application links with these frameworks. They are:

- 

  WebObjects: The basic WebObjects classes.
- 

  WOExtensions: Extensions to the WebObjects framework.
- 

  EOAccess: The Enterprise Objects Access Layer.
- 

  EOControl: The Enterprise Objects Control Layer.
- 

  Foundation: Basic object classes that most applications use (for example, strings, numbers, and arrays).

You can include additional system frameworks in your project if you need to. To add an existing framework to your project:

1. 

   Double-click Frameworks in the first column of the browser.
2. 

   In the Add Frameworks panel that appears, select a framework to add and click Open.

In addition, you can create your own frameworks in order to share WebObjects components and resources across multiple applications. To create a WebObjects Framework:

1. 

   Choose Project !
   New.
2. 

   Select Webobjectsframework from the pop-up menu.
3. 

   Select the path where you want to create the framework.

Once you have created a framework, you can add components, images, and other items to it in the same way that you would add them to a project. To make your framework accessible to other applications, you must install it (see [Installing Your Application](Installing%20Your%20Application.md#apple-gi4dimbq)
for more information). See [Reusable Components](Reusable%20Components.md#apple-geytamzw)
for more information on using components that live in frameworks.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Supporting%20Files.md) [!](Libraries.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
