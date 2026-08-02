---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/SettingUp17.html
archived_at: '2026-07-18T01:27:46.555952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](SettingUp16.md)

# Rapid Turnaround Mode

For the most part, WebObjects is an interpreted environment. The HTML templates, declarations files, and WebScript files each represent interpreted languages. One of the main benefits of an interpreted environment is that you don't need to recompile every time you make a change to the project. The ability to test your changes without rebuilding the project is called "rapid turnaround" and, when using the rapid turnaround features, you're said to be in "rapid turnaround mode."
WebObjects supports rapid turnaround of __.html__, __.wod__, and __.wos__ files within application projects, framework projects, and subprojects of either applications or frameworks.
To support rapid turnaround, WebObjects must be able to locate the resources of your application and its associated frameworks within your system's projects rather than the built products (the __.woa__ or __.framework__ wrappers). To tell WebObjects where to look for your system's projects you must define the NSProjectSearchPath user default. Set this default to an array of paths where your projects may be found. (Relative paths are taken relative to the executable of your project.) The order of the entries in the array defines the order in which projects will be located. The default NSProjectSearchPath is ("../.."), which causes WebObjects to look in the directory where your application's project resides for any other applicable projects. For example, if your application's executable resides in:

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

## Rapid Turnaround and Direct Connect Mode

Direct connect mode allows you to test your application without involving a web server. This means that you don't have to install your WebServerResources under the document root of your web server. The result is that rapid turnaround is even more convenient when in direct connect mode because you don't need to rebuild to install WebServerResources changes to the document root.

## Testing With a Web Server

When you're working in direct connect mode, few issues arise with respect to rapid turnaround. If your application has features which require a web server be used even for testing, however, there are a couple of things to know to make rapid turnaround work for you. Specifically, since you are relying on the web server to locate files within WebServerResources, you must follow these guidelines:

- Your projects must reside somewhere below your web server's document root.
- NSProjectSearchPath should point to all projects of interest.
- For application projects, the WOApplicationBaseURL user default should specify the directory containing the application project. For example, if your application's project folder is:

```
c:\web\docroot\WebObjects\MyApp
```


then the WOApplicationBaseURL user default must be "/WebObjects".

- For framework projects, the WOFrameworksBaseURL user default should specify the directory containing all framework projects used by the application. For example, if your application uses MyFramework.framework and that project resides in:

```
c:\web\docroot\WebObjects\Frameworks\MyFramework
```


then the WOFrameworksBaseURL user default must be "/WebObjects/Frameworks".

Conveniently, the two examples above use the default locations for WOApplicationBaseURL and WOFrameworksBaseURL; if your projects reside in these default locations, you need only set NSProjectSearchPath.
Also, while it is possible to point WOApplicationBaseURL and WOFrameworksBaseURL to other locations, it is not suggested that WOFrameworksBaseURL be moved since all WebObjects applications use WOExtensions.framework, which resides in the default location. If you set WOFrameworksBaseURL to point elsewhere, one side effect will be that the images in the "Raised Exception" panel will not render.
[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Editing%20With%20WebObjects%20Builder.md)
