---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/SettingUp10.html
archived_at: '2026-07-18T01:27:33.375353Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](SettingUp9.md)

## Frameworks

A _framework_ is a collection of classes and resources that an application can use. By storing items such as components and images in frameworks, you can reuse them in multiple projects without having to create multiple copies.
Every WebObjects Application project includes several frameworks by default. When you build, your application links with these frameworks. They are:

- WebObjects: The basic WebObjects classes.
- WOExtensions: Extensions to the WebObjects framework.
- EOAccess: The Enterprise Objects Access Layer.
- EOControl: The Enterprise Objects Control Layer.
- Foundation: Basic object classes that most applications use (for example, strings, numbers, and arrays).

You can include additional system frameworks in your project if you need to. To add an existing framework to your project:

- Double-click Frameworks in the first column of the browser.
- In the Add Frameworks panel that appears, select a framework to add and click Open.

In addition, you can create your own frameworks in order to share WebObjects components and resources across multiple applications. To create a WebObjects Framework:

- Choose Project !New.
- Select WebObjectsFramework from the pop-up menu.
- Select the path where you want to create the framework.

Once you have created a framework, you can add components, images, and other items to it in the same way that you would add them to a project. To have your framework be accessible by other applications, you must install it (see ["Installing Your Application"](SettingUp16.md#apple-haytcmy) for more information). See ["Reusable Components"](Reusable%20Components.md#apple-gezdambq)for more information on using components that live in frameworks.

## Libraries

The Libraries suitcase contains libraries that your application links to.

## Non Project Files

The Non Project Files suitcase is used for files that you have opened that aren't part of the current project.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](SettingUp11.md)
