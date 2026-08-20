---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/Classes.htm
archived_at: '2026-07-15T07:57:35.986316Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](WebComps.md)

## Classes

The Classes suitcase contains Java and Objective-C classes. If your application's primary language is Java, this suitcase contains the __Application.java__ and __Session.java__ files. If the primary language is Objective-C, it contains the files __Application.m__ and __Session.m__. There is a class file for each component that uses Java or Objective-C, as well as any other classes you add to the project.!
You can specify that Java classes are client-side, server-side, or common classes. See ["Subprojects"](Subproj.md#apple-gyydeoi)for more information on how to do this.

## Headers

The Headers suitcase contains header files for projects that use Objective-C.

## Other Sources

The Other Sources suitcase contains compiled code that doesn't belong to a particular class.

## Resources

The Resources suitcase contains files that are needed by your application at run time, but which do not need to be in the web server's document root (and hence will not be accessible to users). It includes:

- The __Application.wos__ and __Session.wos__ files, if your application's primary language is WebScript
- Configuration files
- EOModel files
- Scripted classes

## Web Server Resources

The Web Server Resources suitcase contains files, such as images and sounds that must be under the web server's document root at run time. When developing your application, you place these files in your project directory and add them to the project (see ["Adding or Deleting Items From a Project"](AddorDel.md#apple-g44dqoi)). When you build your project, Project Builder copies the files in this suitcase into the WebServerResources folder of your application wrapper (see ["The Application Wrapper"](Building.md#apple-hazdmmq)).

[!Table of Contents](SetUpTOC.md) [!Next Section](Subproj.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
