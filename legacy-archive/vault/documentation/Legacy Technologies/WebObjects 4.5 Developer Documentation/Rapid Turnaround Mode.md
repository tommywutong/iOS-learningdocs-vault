---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.19.html
archived_at: '2026-07-15T08:10:08.396890Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Installing%20Your%20Application.md) [!](Rapid%20Turnaround%20and%20Direct%20Connect%20Mode.md)

---

#   Rapid Turnaround Mode

With the exception of Objective-C and Java code, WebObjects is an interpreted environment. The HTML templates, declarations files, and WebScript files each represent interpreted languages. One of the main benefits of an interpreted environment is that you don't need to recompile every time you make a change to the project. The ability to test your changes without rebuilding the project is called "rapid turnaround" and, when using the rapid turnaround features, you're said to be in "rapid turnaround mode."

In WebObjects you can modify __.html__
, __.wod__
, and __.wos__
files within application projects, framework projects, and subprojects of either applications or frameworks without rebuilding your project.

To support rapid turnaround, WebObjects must be able to locate the resources of your application and its associated frameworks within your system's projects rather than the built products (the __.woa__
or __.framework__
wrappers). To tell WebObjects where to look for your system's projects you must define the NSProjectSearchPath user default. Set this default to an array of paths where your projects may be found. (Relative paths are taken relative to the executable of your project.) The order of the entries in the array defines the order in which projects will be located. The default NSProjectSearchPath is ("../.."), which causes WebObjects to look in the directory where your application's project resides for any other applicable projects. For example, if your application's executable resides in:

c:\web\docroot\WebObjects\Projects\MyProject\MyProject.woa

then from the executable's directory, "../.." would point to:

c:\web\docroot\WebObjects\Projects

If you've set your project's "Build In" directory to something other than the default, "../.." isn't likely to be appropriate; you should set your NSProjectSearchPath to point to the directories where you keep your projects while you work on them.

When your application is starting up, pay close attention to those log messages which indicate that a given project is found and will be used instead of the built product. Many problems can be solved by understanding how to interpret this output. If no such log message is seen for a given project, it won't be possible to use rapid turnaround for that project. As well, if you have several projects with the same name in the same directory, a conflict will be reported. This often happens when you have several copies of the same project as backups in your project directory. For example, you might have:

c:\web\docroot\WebObjects\Projects\MyApp

c:\web\docroot\WebObjects\Projects\Copy of MyApp

c:\web\docroot\WebObjects\Projects\MyAppOld

Even though the folders containing the projects have different names, the __PB.project__
files within them might be identical. WebObjects uses the PROJECTNAME attribute inside your project's __PB.project__
file to determine the name of the project, not the name of the directory for the project. If this happens, you'll need to move the backups to another directory to avoid the conflict.

#### [Rapid Turnaround and Direct Connect Mode](Rapid%20Turnaround%20and%20Direct%20Connect%20Mode.md#apple-obtwmslehuytanruga)

#### [Testing With a Web Server](Testing%20With%20a%20Web%20Server.md#apple-obtwmslehuytanrugi)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Installing%20Your%20Application.md) [!](Rapid%20Turnaround%20and%20Direct%20Connect%20Mode.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
