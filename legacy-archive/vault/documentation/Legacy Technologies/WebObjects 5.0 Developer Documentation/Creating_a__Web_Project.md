---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/Creating_a__Web_Project.html
archived_at: '2026-07-15T08:12:26.019744Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](An_Introduc_rect_To_Web.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Structu_Web_Project.md)

## Creating a Direct to Web Project

To create a Direct to Web application, begin by using Project
Builder to create a WebObjects application project. Follow these
steps:

1. Launch Project
   Builder.
2. Choose File > New Project.
3. Select WebObjects/Direct to Web Application.
4. Set the name and location of your project.

   Enter `D2WTutorial` in
   the Project Name field.

   Click Set and select a location
   for your project.
5. Add additional frameworks to the project.

   No additional
   frameworks are required for this tutorial, so click Next.
6. Choose a model file.

   You'll use one of the models defined
   in the sample projects.

   Click Add.

   Navigate
   to the /Developer/Examples/JavaWebObjects/JavaClient/JavaClientMovies directory.

   Select Movies.eomodeld and
   click Choose.

   Click Next.
7. Select a look for the user-interface.

   This pane offers
   a selection of user-interface styles ("looks") for your Direct
   to Web application; see ["The Different Looks for WebObjects Applications"](#apple-ijbusskfjjeeg) for more information.

   Select
   Basic Look from the Direct To Web Looks list and click Next.
8. Build and run the project.

   This pane asks if you would
   like to build and launch your application immediately. If you choose
   not to have the wizard build and launch your application, see ["Using Your Direct to Web Application"](Using_Your__Application.md#apple-ijbusr2iifbuu), which tells you how to launch your WebObjects application
   and describes what you see when you launch it. For information about building
   a project, see _WebObjects Tools and Techniques_.

   For
   the purposes of this tutorial, make sure "Build and launch project
   now" is selected and click Finish.

### The Different Looks for WebObjects Applications

In this release, Direct to Web offers three different user-interface
styles, or looks, for WebObjects applications: Basic, Neutral, and
WebObjects. Currently the only simple way to change the look of
an application is to re-create a project using Project Builder.
Therefore it is advisable to know which look you want in advance.

All the looks provide the same functions for the user. They
only differ in the style and placement of their user-interface elements.The
Neutral look and the WebObjects look are very similar but the Neutral
look does not display the Apple logo, which makes it easier if you
want to use your own logo.

The login page for the Basic look has a panel-like submit
form for the entry of user name and password:

![[image: ../Art/basiclook.gif]](../Art/basiclook.gif)

The login page for the Neutral look is much simpler:

![[image: ../Art/neutrallook.gif]](../Art/neutrallook.gif)

This is the login page for the WebObjects look:

![[image: ../Art/webobjectslook.gif]](../Art/webobjectslook.gif)

In the dynamically-generated pages (query, list, inspect,
and so on), the Basic look differs from the Neutral and WebObjects
looks even more strikingly. In the Basic look the control header
runs across the top of the page whereas in the Neutral and WebObjects
looks it appears on the left side of the page. In addition, the
Basic look is more tabular while the Neutral and WebObjects looks
tends to present records in visual "blocks." For example, the
following is an example of a list page in the Basic look:

![[image: ../Art/basiclooklist.gif]](../Art/basiclooklist.gif)

The list page in the Neutral look appears like this:

![[image: ../Art/neutralllooklist.gif]](../Art/neutralllooklist.gif)

The following illustrates what a list page looks like in the
WebObjects look.

![[image: ../Art/wolooklist.gif]](../Art/wolooklist.gif)

[![Previous](attachments/DirectToWeb/Images/previous.gif)](An_Introduc_rect_To_Web.md)[![Next](attachments/DirectToWeb/Images/next.gif)](The_Structu_Web_Project.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
