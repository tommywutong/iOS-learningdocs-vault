---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.059.html
archived_at: '2026-07-15T07:59:00.519958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.058.md)

# Rapid Turnaround Mode

For the most part, WebObjects is an interpreted environment. The HTML templates, declarations files, and WebScript files each represent interpreted languages. One of the main benefits of an interpreted environment is that you needn't recompile every time you make a change to the project. The ability to test your changes without rebuilding the project is called "rapid turnaround" and, when using rapid turnaround capability, you're said to be in "rapid turnaround mode."
WebObjects has always supported rapid turnaround of __.html__, __.wod__, and __.wos__ files within the application project. WebObjects 4.0 adds support for rapid turnaround of these files within framework projects and within subprojects of either application or framework projects.
To support rapid turnaround, WebObjects must be able to locate the resources of your application and its associated frameworks within your system's projects rather than the built products (the __.woa__ or __.framework__ wrappers). To tell WebObjects where to look for your system's projects you must define the NSProjectSearchPath user default. Set this default to an array of paths where your projects may be found. (Relative paths are taken relative to the executable of your project.) The order of the entries in the array defines the order in which projects will be located. The default NSProjectSearchPath is ("../.."), which causes WebObjects to look for any other applicable projects in the directory where your application's project resides. For example, if your application's executable resides within:

```
c:\web\docroot\WebObjects\Projects\MyProject\MyProject.woa
```


then from the executable's directory, "../.." would point to:

```
c:\web\docroot\WebObjects\Projects
```


If you've set your project's "Build In" directory to something other than the default, "../.." isn't likely to be appropriate; you should set your NSProjectSearchPath to point to the directories where you keep your projects while you work on them.
When your application is starting up, pay close attention to those log messages which indicate that a given project is found and will be used instead of the built product. Many problems can be solved by understanding how to interpret this output. If no such log message is seen for a given project, it won't be possible to use rapid turnaround for that project. As well, if you have several projects with the same name in the same directory, a conflict will be reported. This often happens when you have several copies of the same project as backups in your project directory. For example, you might have:

```
c:\web\docroot\WebObjects\Projects\MyApp
c:\web\docroot\WebObjects\Projects\Copy of MyApp
c:\web\docroot\WebObjects\Projects\MyAppOld
```


Even though the folders containing the projects have different names, the __PB.project__ files within them might be identical. WebObjects uses the PROJECTNAME attribute inside your project's __PB.project__ file to determine the name of the project, not the name of the directory for the project. If this happens, you'll need to move the backups to another directory to avoid the conflict.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.060.md)
