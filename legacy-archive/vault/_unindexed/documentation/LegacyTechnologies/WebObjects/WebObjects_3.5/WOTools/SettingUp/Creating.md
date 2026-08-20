---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/Creating.htm
archived_at: '2026-07-15T07:57:37.571137Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](Intro.md)

# Creating WebObjects Application Projects

A WebObjects application project contains all the files needed to build and maintain your application. You use Project Builder to create a new project.

- Launch Project Builder.

To do this, launch __ProjectBuilder.app__, which is found in the __NextDeveloper/Apps/__ directory. On Mach systems, this directory is under the root directory __/__. On Windows NT, it is under %_NEXT_ROOT%,_ an environment variable defined when you installed WebObjects (__C:\NeXT__ by default).

On Windows NT, you can launch Project Builder from the WebObjects program group in the Start menu.

- Choose Project !New.
!

The New Project panel has a Project Type pop-up list that lets you choose the type of project you want to create. WebObjectsApplication is shown by default.

- In the Project Type pop-up list, make sure WebObjectsApplication is selected.

Another type of project you may want to create is WebObjectsFramework. See ["Frameworks"](Framewrk.md#apple-gu4tcnq)for more information.

- Click Browse to specify your project's location.

__Note:__ You can also type your project's location and name directly in the Project Path text field.

- Navigate to the directory in which to create your project.

During development, you typically create a project in the _<DocumentRoot>___/WebObjects__ directory. _<DocumentRoot>_ is your HTTP server's document root, which you specified when you installed WebObjects. It is convenient to have your entire project under this directory so project resources can be located without going through the installation process (see ["Installing Your Application"](Install.md#apple-haytcmy)_)_. However, when deploying your application, you can place parts of your project elsewhere, so that only those files needed by the web server are accessible to users.

!- Type the name of the project you want to create.
- Click Save.

The New Project panel shows the path you specified.

- Click OK.

The WebObjects Application Wizard starts.

!

[!Table of Contents](SetUpTOC.md) [!Next Section](Assist.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
