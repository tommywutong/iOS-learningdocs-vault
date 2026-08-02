---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/Developing__Application.html
archived_at: '2026-07-15T08:15:13.189385Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](WebObjects_Architecture.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__ed_Approach.md)

## Developing a WebObjects HTML Application

Developing a WebObjects application is a matter of creating
your templates, bindings, and Java code files. Although these files
are text based and thus could be created using a text editor, WebObjects
provides graphical tools that simplify the entire process. The sequence of
tasks used to create a WebObjects HTML application with these tools
is as follows:

- Create a
  project using Project Builder.
- Create a model using EOModeler.
- Edit your components with WebObjects Builder.

You have already been introduced to EOModeler. Project Builder
and WebObjects Builder are discussed in the following sections.

### Project Builder

As its name implies, Project Builder manages all of the constituent
parts of your application, including source code files, WebObjects
components, frameworks, makefiles, graphics and sound files, and
the like. You use Project Builder to edit your code files, compile,
debug, and launch your application for development testing. Project
Builder's assistants help you create new WebObjects components.
You also can launch the other development tools from within Project
Builder.

[Figure 4-4](#apple-ineuercjjbbeo) shows Project Builder in use.

__Figure
4-4 Project Builder__

![[image: ../Art/ProjectBuilder.gif]](../Art/ProjectBuilder.gif)

### WebObjects Builder

You use WebObjects Builder to edit your application's components.
WebObjects Builder allows you to graphically edit a component's
HTML template. If you prefer, you can switch to the source view
from which you can edit the template as an HTML text file. WebObjects
Builder also allows you to graphically bind the dynamic elements
on your template to variables and methods within your code; you
simply drag from a variable to the dynamic element as shown in [Figure 4-5](#apple-ineuercfivcug).

__Figure
4-5 WebObjects Builder__

![[image: ../Art/WOB.gif]](../Art/WOB.gif)

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](WebObjects_Architecture.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__ed_Approach.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
