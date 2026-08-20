---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Creating_a__ent_Project.html
archived_at: '2026-07-15T08:12:21.031938Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Getting_Sta_Java_Client.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Building_an_Application.md)

## Creating a Direct to Java Client Project

The Project Builder Assistant creates a Direct to Java Client
project for you using a model you specify. For this tutorial, you
use the Movies and Rentals models included in the example JavaBusinessLogic
framework that's installed with WebObjects.

1. Launch Project
   Builder.

   The Project Builder application is located in the `/Developer/Applications` directory. Navigate
   to that directory and launch the application.
2. Create a new project.

   Choose File > New Project.
3. Select the kind of project to create.

   Select WebObjects/Direct
   to Java Client Application.

   Click Next.
4. Name the project.

   Name the project D2JCTutorial.

   Click
   Set and choose a location for the project.

   Click Next.
5. Select the frameworks to use.

   The Assistant includes
   the frameworks necessary for Direct to Java Client applications. For
   the tutorial, you add the JavaBusinessLogic framework. It provides
   client- and server-side business logic implemented in custom enterprise
   objects.

   Click Add.

   Navigate to the `/Library/Frameworks` directory.

   Select `JavaBusinessLogic.framework` and
   click Choose.

   Click Next.
6. Select the model(s) that the project is to based upon.

   Direct
   to Java Client technology uses model files to generate applications.
   To make models available to Direct to Java Client, you add them
   to your project. You can add models directly to your project by
   adding them to the Resources group, or you can add them indirectly
   by adding frameworks that contain your models.

   The JavaBusinessLogic
   framework that you added in the previous step already includes the
   appropriate models, `Movies.eomodeld` and `Rentals.eomodeld`.

   Click
   Next.
7. Build the project.

   At this point the Assistant has all
   the information it needs to create the project. It offers to build
   and launch the application for you. However, in this tutorial you
   do that manually.

   Deselect "Build and launch project
   now" and click Finish.

### What's in a Direct to Java Client Project?

The project that the Project Builder Assistant created for
you is very similar to a normal Java Client project. It has the
typical Application, Session, and Main classes for the Server target.
The Client target, however, has no files associated to it. It has
no interface controller class or nib file, because Direct to Java
Client applications generate their user interfaces dynamically.

The project's `Main.wo` component
contains a WOJavaClientApplet that is configured in a special way.
It's `width` and `height` are
set to `0`, and the `applicationClassName` is
set to "com.webobjects.eogeneration.EODynamicApplication". The
application class is important because it's responsible for initiating
the user interface generation process.

The Resources group of the project contains a `user.d2wmodel` file.
The Direct to Java Client Assistant uses this file to store user
interface configuration information.

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Getting_Sta_Java_Client.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Building_an_Application.md)

© 2001 Apple Computer, Inc.
