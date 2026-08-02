---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook1.html
archived_at: '2026-07-15T07:53:13.491009Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBookTOC.md)

# Creating a WebObjects Application Project

A WebObjects application project contains all the files needed to build and maintain your application. You use Project Builder to create a new project.

- Launch Project Builder.

On Windows NT, you can launch Project Builder from the WebObjects program group in the Start menu. On other platforms, you can launch the application by navigating to the directory _NeXT_ROOT___/NextDeveloper/Apps/__ and launching __ProjectBuilder.app__. _NeXT_ROOT_ is an environment variable defined when you installed WebObjects. On Windows NT systems, it is __C:\NeXT__ by default. On Mach systems, it is the root directory __/__.

- Choose Project !New.
  !
- In the New Project panel, select WebObjectsApplication from the Project Type pop-up list.
- Click Browse.
  !
- In the Save panel, navigate to the _DocumentRoot___/WebObjects__ directory.

_DocumentRoot_ is your HTTP server's document root, which you specified when you installed WebObjects.

- Type the name of the project you want to create (GuestBook).
- Click Save.

The New Project panel shows the path you specified.

- Click OK.

The WebObjects Application Wizard starts.

!- For Available Assistance, choose None.

If you are developing an application that accesses a database, you may wish to use one of the levels of assistance that WebObjects provides. For more information on these options, see ["Creating a WebObjects Database Application"](../Movies/MoviesTOC.md#apple-gi3dq).

[!Table of Contents](GuestBookTOC.md) [!Next Section](GuestBook2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
