---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/Framewrk.htm
archived_at: '2026-07-15T07:57:41.519864Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](Subproj.md)

## Frameworks

A _framework_ is a collection of classes and resources that an application can use. By storing items such as components and images in frameworks, you can reuse them in multiple projects without having to create multiple copies.
Every WebObjects Application project includes several frameworks by default. When you build, your application links with these frameworks. They are:

- WebObjects: The basic WebObjects classes.
- WOExtensions: Extensions to the WebObjects framework.
- Foundation: Basic object classes that most applications use.
- EOAccess: The Enterprise Objects Access Layer.
- EOControl: The Enterprise Objects Control Layer.

You can include additional frameworks in your project if you need to. To add an existing framework to your project:

- Double-click Frameworks in the first column of the browser.
- In the Add Frameworks panel that appears, select a framework to add and click Open.

Frameworks are generally installed in the directory _NeXT_ROOT_/__NextLibrary__/__Frameworks__.

In addition, you can create your own frameworks in order to share WebObjects components and resources across multiple applications. To create a WebObjects Framework:

- Choose Project !New.
- Select WebObjectsFramework from the pop-up menu.
- Select the path where you want to create the framework.

Once you have created a framework, you can add components, images, and other items to it in the same way that you would add them to a project. To have your framework be accessible by other applications, you must install it (see ["Installing Your Application"](Install.md#apple-haytcmy) for more information). See ["Reusable Components"](../DynamicElements/ReuseCmp.md#apple-gezdambq)for more information on using components that live in frameworks.

## Libraries

The Libraries suitcase contains libraries that your application links to.

## Non Project Files

The Non Project Files suitcase is used for files that you have opened that aren't part of the current project.

[!Table of Contents](SetUpTOC.md) [!Next Section](Existing.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
