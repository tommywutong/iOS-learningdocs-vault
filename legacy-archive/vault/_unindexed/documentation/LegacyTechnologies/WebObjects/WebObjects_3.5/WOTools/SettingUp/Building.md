---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/Building.htm
archived_at: '2026-07-15T07:57:32.859602Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](SetUpTOC.md)[Table
of Contents](SetUpTOC.md) [!](DecFiles.md)[Previous
Section](DecFiles.md) 

# Building Your Application

You must build your application if your project contains any compiled
code (Java or Objective-C). If your application uses WebScript only, you
do not need to build. In this case, Project Builder runs a default executable
(__WODefaultApp__) when you launch your application.

 

Once you have built your application, you do not need to rebuild unless
you have made changes to your compiled code. You can make changes to your
components (the __.html__, __.wod__, or __.wos__ files) and test
them without rebuilding.

 

__Note:__ When you are developing a framework, you must rebuild after
any change, even for changes to scripts or images. Therefore, when developing
a framework, it is probably best to develop it as an application project,
and once it has been tested, move its reusable pieces into a framework.

 

Project Builder has a toolbar with buttons you use to build and launch
your application.

!

1. Click ! in the toolbar to open the Project
   Build panel. 
2. Click ! in the Project Build panel to build
   your project. 
!

The Project Build panel displays the commands that are being executed
to build your project. If all goes well, it displays the status message
"Build succeeded."

3. Close the panel.

## The Application Wrapper

When you build your project, Project Builder creates
an _application wrapper_, which is a folder whose name is the project
name plus the extension __.woa__.

!

The application wrapper has a structure similar to
that of a framework. It consists of the following:

- The executable application. 
- The application's resources. 

These include the application's components as well as other files that
are needed by your application at run time.

 

- The application's web server resources.

When you build and install your application, Project
Builder copies all the files from your Web Server Resources suitcase to
a folder called WebServerResources inside the application wrapper. If you
have client-side Java components in your project, these are also copied
to the WebServerResources folder.

[!](SetUpTOC.md)[Table
of Contents](SetUpTOC.md) [!](Launchng.md)[Next
Section](Launchng.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
