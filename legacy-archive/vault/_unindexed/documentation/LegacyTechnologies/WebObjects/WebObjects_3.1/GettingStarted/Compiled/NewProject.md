---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/NewProject.html
archived_at: '2026-07-15T07:48:22.541562Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](SetUp.md)

# Create a project

Now that Project Builder and WebObjects Builder are set up correctly, you are ready to create the application. To create a Java application, you need to create it both as a WebObjects Builder application and as a Project Builder project.

- In WebObjects Builder, choose File ! New Application.
- Type __Registration__ as the application's name, and then press Enter.
!- Relaunch Project Builder, and then choose Project ! New.
- Select WebObjectsApplication from the Project Type pop-up list.
- Click the Browse button.
!- In the Open panel that appears, navigate to the __Registration.woa__ directory (the application you created in step 2), which is under _<DocumentRoot>___/WebObjects__, and click Open.
- Type __PB.project__ in the File name field and click Save. (__PB.project__ is a file Project Builder uses to record information about your project.)
- Click OK.
!

You created __Registration.woa__ in WebObjects Builder first so that Project Builder would know it is a Java application. Because you set the WebObjects Builder language preference to Java, WebObjects Builder creates __.java__ files where it usually creates script files (for example, __Application.java__, __Session.java__, and __Main.wo/Main.java__). When you create a WebObjectsApplication project, Project Builder includes the files created by WebObjects Builder in the project.
If you browse through the project in Project Builder's main window, you'll find these files:

- __Application.java__ and __Session.java__ under Other Resources
- __Application.woo__, __Session.woo__, and __WOProject.plist__ under Other Resources. (These are files maintained by WebObjects and WebObjects Builder.)
- __Main.wo__ under Interfaces
- Project makefiles under Supporting Files

The following sections discuss some other parts of the WebObjects application that are created for you.

[!Table of Contents](compiled.book.md) [!Next Section](mainMethod.md)
