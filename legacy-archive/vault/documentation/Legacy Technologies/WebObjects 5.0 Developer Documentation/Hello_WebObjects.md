---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/IntroductionToWO/Hello_WebObjects.html
archived_at: '2026-07-15T08:13:21.726880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Project_Builder.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/index.html)

## Hello WebObjects

There is a place for breaking with tradition, but this is
not it: your first WebObjects application will display "Hello
World!" in your browser. Though this project is trivial, it does
serve as an example with which to examine the interface of Project
Builder. Also, a successful build and launch verifies that your
development environment is correctly installed and configured.

### Launch Project Builder

1. Navigate
   to the /Developer/Applications directory.
2. Double-click the Project Builder icon.
    ![[image: ../Art/projectbuildericon.gif]](../Art/projectbuildericon.gif)

   The first time
   you run Project Builder, you are greeted by a setup assistant that
   walks you through some of the basic configuration settings of Project
   Builder. At this point, you could customize the build system used
   to compile your projects, but for now, accept the default options
   on each pane.

### Using the New Project Assistant

When you first launch Project Builder, you see only its menu
bar. To create a project to work in, choose New Project from the
File menu. The Project Builder Assistant appears, walking you through
a few steps to create a new project.

__Figure
3-1 The New Project Assistant__

![[image: ../Art/pbassistantnewproject.gif]](../Art/pbassistantnewproject.gif)

There are several project types to choose from. Each starts
out with a slightly different set of files and configuration to
facilitate particular types of applications, from command-line tools
to desktop applications. The following are two types of WebObjects
project you can develop:

- __WebObjects
  Application__ This project type is the basic starting
  point for WebObjects applications. It provides one Web page, a system
  for moving resources like images to your Web server's document
  root during installation, and other basic components like the Session
  and Application classes.
- __WebObjects Framework__ A framework is
  a bundle of related code, resources such as sounds and graphics,
  and more. You can make your applications dependent on your frameworks
  as a means of sharing code between applications. Your WebObjects applications
  are based on the JavaWebObjects framework, and you can write your
  own as well.

Follow these steps to build your first WebObjects application
project.

1. Select WebObjects
   Application from the list of templates and click Next.
2. Type `HelloWebObjects` in
   the Project Name text input field.

   If you don't want to use
   the default project location, click Set and navigate to the directory
   where you want to store your project.

   __Figure 3-2 Choosing
   a location for the project__

   ![[image: ../Art/intronewprojectassistant.gif]](../Art/intronewprojectassistant.gif)
3. Click Finish to create the project.

   A window similar
   to the one in [Figure 3-3](#apple-ijauersijffei) appears.

### The Main Window

__Figure
3-3 Project Builder's main window__

![[image: ../Art/pbhellowo.gif]](../Art/pbhellowo.gif)

The Project Builder main window organizes all the files in
your project and provides all the tools you need to edit, build,
and debug them.

When you first create a project, Project Builder displays
the release notes in the code editor, which is the pane where you
usually edit files. This document contains information about the
latest release of Project Builder. You should read it carefully.

The left pane is a tabbed pane used for organization. In the
Groups & Files pane, which is initially visible, there are several
groups of files, each with a disclosure triangle.

- Classes

  This
  group initially contains the `.java` files
  for the Application, Session, and DirectAction classes that your
  application uses. You can customize your application by changing
  these files. In addition, when you add new classes to your project,
  they are stored here by default.
- Web Components

  Each Web page or component you create
  is stored within its own subgroup in the Web Components group. Each
  subgroup contains the files that define the HTML representation
  and WebObjects behavior for each component. Initially, only the
  Main subgroup is present.

  Inside the Main subgroup you
  find three items: Main.wo, Main.java ,
  and Main.api. They define the look and behavior
  of the Main component.
- Resources

  Graphics, sounds, and movies for your components
  are stored in this folder. In database-enabled applications, the
  model files (with the extension `.eomodeld`)
  are stored here.
- Web Server Resources

  Some resources may be referenced
  not only by your WebObjects applications but also by static pages
  in other parts of the site. Resources in this folder are moved to
  a location outside of the application wrapper, where they can be
  accessed by other means as well.
- Frameworks

  Every WebObjects project is dependent on at
  least the JavaWebObjects framework, which contains the code behind
  WebObjects. You can add additional frameworks to your project by
  choosing Project > Add Files.
- Documentation

  Documentation for your project can be organized
  by Project Builder.
- Products

  The actual files created by compiling your application
  are listed under this group. It includes the executable, an organized
  tree of resources for components, and localized versions of the
  components themselves.

The other three panes, Bookmarks, Targets, and Breakpoints,
are explained in greater detail later in the book.

### Modifying the Main Component

Now you'll use WebObjects Builder to modify the Main component.

1. Open `Main.wo`.
   ![[image: ../Art/pbmainwosel.gif]](../Art/pbmainwosel.gif)

   Double-click
   the `Main.wo` component
   in the Main subgroup in the Web Components group in the Groups &
   Files list in Project Builder. The WebObjects Builder application opens
   and displays a window for Main.wo.
2. Modify `Main.wo`.

   Enter `Hello
   World!` in the content pane.

   ![[image: ../Art/wobmainhello.gif]](../Art/wobmainhello.gif)
3. Save `Main.wo`.

   Choose
   File > Save.

### Building the Project

All that remains is to compile the project and run it. When
you start the build process, Project Builder does more than compile
the Java bytecode from your files. First, only files that have changed
since the last build are compiled, to save time. Project Builder
also gathers all the resources required for your project, organizes
them for your Web server, and compresses your Java class files into
a JAR (Java Archive) file.

When you choose Build from the Build menu, the build pane
appears so you can watch the progress of the build. This is also
the pane that displays Java compilation errors if your project has
any, but its output is frequently very useful even when it doesn't
contain error messages.

In Project Builder, choose Build > Build or click
![[image: ../Art/buildicon.gif]](../Art/buildicon.gif)
in the main
window.

Because you didn't modify any Java code, you shouldn't
encounter any compilation errors. When the compilation progress
bar is complete, you're ready to run your project.

### Running the Project

Unless you changed the default location when you first ran
Project Builder, you now have a bundle called HelloWebObjects.woa in
the build directory at the top level of your
project's directory.

Choose Debug > Run Executable or click
![[image: ../Art/launchicon.gif]](../Art/launchicon.gif)
in Project
Builder's main window.

Since your application is already built, the Run pane appears
immediately, displaying the output from your application as it runs:

```
Reading MacOSClassPath.txt ...
Launching HelloWebObjects.woa ...
```

. . .

```
Creating adaptor of class WODefaultAdaptor listening on port -1 with a listen queue  size of 128 and 2 WOWorkerThreads.
Creating LifebeatThread now with: HelloWebObjects -1 1085 30000
Welcome to HelloWebObjects!
Opening application's URL in browser: http://localhost:49189/cgi-bin/WebObjects/HelloWebObjects
Waiting for requests...
```

After the last line appears, the URL shown opens automatically
in your default browser.

__Figure
3-4 The HelloWebObjects application in
action__

![[image: ../Art/iehellowo.gif]](../Art/iehellowo.gif)

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Project_Builder.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
