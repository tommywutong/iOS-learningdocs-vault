---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Tasks/CreatingBundles.html
archived_at: '2026-07-15T07:16:30.486643Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Building%20Applications%20with%20Multiple%20Bundles.md)[Previous](Loading%20Bundles.md)

# Creating Loadable Bundles

This section describes how to create a Cocoa loadable bundle—an application component or plug-in—with Xcode.

Xcode provides graphical tools for creating loadable bundles. Building loadable bundles is very similar to building an application. The process consists of three basic steps:

1. Create a new project from a Xcode template.
2. Set up and edit source files.
3. Modify project settings with information about your bundle.

The following sections describe this process in detail.

Creating a loadable bundle project is just like creating an application—you just need to pick the appropriate project template. To create a loadable bundle project, perform the following steps:

1. Launch Xcode.
2. Choose New Project… from the File menu.
3. From the template list, select Cocoa Bundle.
4. Click Next.
5. Choose the location for the project and click Finish.

A new project built from the Cocoa Bundle template contains one source file, `main.c`, and a reference to the Cocoa framework. In most cases, you can just delete this file and begin adding your own sources. You can add new Cocoa classes and other source files, as well as resources and frameworks, just as with a Cocoa application.

The minimal loadable bundle in Cocoa contains one class in two files—one for the interface (`MyClass.h`) and one for the implementation (`MyClass.m`). One class in the bundle should be set as the principal class, as described in Modifying Target Settings. If the principal class is not selected, NSBundle will use the first class in the project (as shown in the Xcode window) as the principal class.

If your loadable bundle is a plug-in, the host application developer usually provides an interface for the plug-in architecture in a framework. This framework typically contains a class that all plug-in principal classes inherit from, or a protocol (formal or informal) for the plug-in’s principal class to adopt.

You need to set two settings in the bundle’s information property list for the bundle to be a good citizen:

1. Bundle identifier
2. Principal class

The bundle identifier serves as a unique identifier for all bundles on the system: applications, kernel extensions, all loadable bundles, and other types of bundles. The bundle identifier should be a reverse DNS-style name, such as `com.apple.screensaver.Abstract`.

The principal class serves as the entry point into a Cocoa bundle. It should be named in a globally unique way, as described in [Preventing Name Conflicts](Preventing%20Name%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tolkdjjbemr2di5dq). If no principal class is selected, NSBundle chooses one for you.

To modify these settings, perform the following steps:

1. Open the project’s Targets pane.
2. Select the bundle target listed under the Targets group.
3. Under Info.plist Entries > Simple View, select Basic Information.
4. Enter the desired bundle identifier into the text field labeled “Identifier:”.
5. Also under Info.plist Entries > Simple View, select Cocoa-Specific.
6. Enter the name of the principal class into the text field labeled “Principal class:”.

[Next](Building%20Applications%20with%20Multiple%20Bundles.md)[Previous](Loading%20Bundles.md)

