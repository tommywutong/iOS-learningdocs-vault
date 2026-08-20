---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Creating/Creating_th_ger_Project.html
archived_at: '2026-07-15T08:14:00.974162Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Creating_the_Movies_Model.md)[![Next](attachments/JavaClient/Images/next.gif)](The_Ingredi_ent_Project.md)

## Creating the StudioManager Project

Every Java Client application starts out as a project. A project
is a repository for all the elements that go into the application,
such as source code files, frameworks, libraries, packages, the
application's user interface, sounds, and images. You use the
Project Builder application to create and manage projects.

1. Start Project
   Builder.

   Navigate to `/Developer/Applications` and
   launch Project Builder.

   ![[image: ../Art/pbicon.gif]](../Art/pbicon.gif)
2. Start a new project.

   Choose File > New Project

   Select
   Java Client Application.

   Click Next.

   ![[image: ../Art/pbnewprojecttype.gif]](../Art/pbnewprojecttype.gif)
3. Name the project.

   Name the project StudioManager.

   Click
   Set and select the folder where you want the project placed.

   Click
   Next.

   ![[image: ../Art/pbnewprojectlocation.gif]](../Art/pbnewprojectlocation.gif)
4. Add the necessary frameworks to the project.

   The Choose
   Frameworks pane allows you to add frameworks to your project, but
   no additional frameworks are required for this tutorial.

   Click
   Next.

   ![[image: ../Art/pbnewprojectframeworks.gif]](../Art/pbnewprojectframeworks.gif)
5. Choose the model to be used in the project.

   The Choose
   EOModels pane allows you to add the model to be used in your project.

   Click
   Add.

   If you defined your own Movies model, navigate
   to the folder where you stored it. Otherwise, you can use the Movies
   model included in one of the example projects. Navigate to `/Developer/Examples/JavaWebObjects/JavaClient/JavaClientMovies`.

   Select `Movies.eomodeld` and
   click Choose.

   Click Next.

   ![[image: ../Art/pbnewprojecteomodels.gif]](../Art/pbnewprojecteomodels.gif)
6. Name the interface file.

   The Interface Controller Class
   Name pane lets you change the class name and package name of the
   interface controller. You'll use the default name so click Next.

   ![[image: ../Art/pbnewprojectinterfaceclass.gif]](../Art/pbnewprojectinterfaceclass.gif)
7. Select the application skeleton template.The Select a Template
   pane allows you to choose the application template to use for your project.

   Make
   sure that the EOF Application Skeleton template is selected.

   Click
   Finish to create the project.

   ![[image: ../Art/pbnewprojecttemplate.gif]](../Art/pbnewprojecttemplate.gif)

[![Previous](attachments/JavaClient/Images/previous.gif)](Creating_the_Movies_Model.md)[![Next](attachments/JavaClient/Images/next.gif)](The_Ingredi_ent_Project.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
