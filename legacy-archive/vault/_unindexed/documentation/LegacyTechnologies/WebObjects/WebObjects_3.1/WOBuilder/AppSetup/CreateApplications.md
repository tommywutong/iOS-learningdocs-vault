---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/AppSetup/CreateApplications.html
archived_at: '2026-07-15T07:50:12.948184Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](AppSetup.book.md)

Creating Applications

# Creating Applications

__Note:__ To create an application that has compiled code, use Project Builder instead of WebObjects Builder. See "[Creating a Compiled WebObjects Application](../../GettingStarted/Compiled/compiled.book.md)" in _Getting Started_.

To create a new application in WebObjects Builder:

Choose File->New Application.

The panel that opens shows you the contents of ___<DocumentRoot>___/WebObjects (unless you have previously saved into a different directory). ___<DocumentRoot>___ is your HTTP server's document root, which you specified when you installed WebObjects.

Enter a name for the application.

Click Save to create the application directory.

!

WebObjects Builder creates the application directory _AppName___.woa__, where _AppName_ is the name you specified. Under _AppName___.woa__, WebObjects Builder creates another directory called __Main.wo__ for your first page, or _component_. (See "[Layout of Application in the File System](AppLayout.md#apple-kjcumnjxgy2ds).")

An empty editing window for __Main.wo__ opens along with an [application window](AppWindow.md) that lists all the components in your application. At first only __Main.wo__ is listed in the application window.

[!Table of Contents](AppSetup.book.md)
[!Next Section](AppLayout.md)
