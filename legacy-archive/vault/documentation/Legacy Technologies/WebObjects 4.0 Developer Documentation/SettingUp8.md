---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/SettingUp8.html
archived_at: '2026-07-18T01:27:54.574208Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](SettingUp7.md)

## Classes

The Classes suitcase contains Java, Web Script and Objective-C classes. For example, if your application's primary language is Java, this suitcase contains the __Application.java__, __Session.java__, __DirectAction.java__, and __Main.java__ files. The files have the extension __.wos__ if the primary language is Web Script and __.m__ if the primary language is Objective-C . There is a class file for each component, as well as any other classes you add to the project

!

You can specify that Java classes are client-side, server-side, or common classes. See ["Subprojects"](SettingUp9.md#apple-gyydeoi)for more information on how to do this.

## Headers

The Headers suitcase contains header files for projects that use Objective-C.

## Other Sources

The Other Sources suitcase contains compiled code that doesn't belong to a particular class.

## Resources

The Resources suitcase contains files that are needed by your application at run time, but which do not need to be in the web server's document root (and hence will not be accessible to users). It includes:

- Configuration files
- EOModel files
- APIfiles containing the keys defined by a component (for example, __Main.api__) that other components can bind to (see ["Reusable Components"](Reusable%20Components.md#apple-gezdambq)).

## Web Server Resources

The Web Server Resources suitcase contains files, such as images and sounds that must be under the web server's document root at run time. When developing your application, you place these files in your project directory and add them to the project (see ["Adding or Deleting Items From a Project"](SettingUp6.md#apple-g44dqoi)). When you build your project, Project Builder copies the files in this suitcase into the WebServerResources folder of your application wrapper (see ["The Application Wrapper"](Building%20Your%20Application.md#apple-hazdmmq)).

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](SettingUp9.md)
