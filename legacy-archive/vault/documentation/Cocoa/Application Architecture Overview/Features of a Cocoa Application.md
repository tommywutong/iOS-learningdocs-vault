---
title: Application Architecture Overview
apple_id: 10000005i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2011-06-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppArchitecture/Concepts/AppFeatures.html
archived_at: '2026-07-15T05:25:28.830672Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Architecture Overview](Introduction%20to%20Application%20Architecture.md)


[Next](Document%20Architecture.md)[Previous](Introduction%20to%20Application%20Architecture.md)

# Features of a Cocoa Application

A Cocoa application has behind it the powerful resources of the Cocoa frameworks, particularly the Application Kit. These software resources—along with Xcode, Interface Builder, and the rest of the Cocoa development environment—make possible the speedy development of robust, full-featured applications.

The simplest Cocoa application, even one without a line of code added to it, includes a wealth of features that you get “for free.” In other words, you either do not have to program these features yourself or the programming effort is trivial. You can simply create an application project with Xcode, create a graphical user interface with Interface Builder, and build the application to get the following features:

- _Window Management and Workspace Integration_. In response to user actions, an application takes care of closing, miniaturizing, and resizing its windows. In coordination with the Finder, the application handles its own deactivation and reactivation, hiding and exposing its windows and doing all necessary redraws.
- _Event Handling_. The application creates its event loop and, in coordination with the window system, receives and distributes events to the windows and views in which user actions occurred. Many user actions are handled automatically, but you can implement your own handling of events.
- _Menu Management_. As with an application’s windows, an application menu is automatically displayed and removed from the menu bar as the application is started, deactivated, reactivated, and terminated. The application takes care of menu-item tracking and highlighting, submenu display, and accelerator keys. In many instances, an application triggers actions in expected objects when menu items are disabled and it enables or disables items appropriately. Of course, you can customize menu behavior to more sophisticated requirements.
- _Text and Font Support_. When you add the necessary objects to your user interface in Interface Builder, your application automatically gains many capabilities related to text editing: menu selection of font families, sizes, and styles and textual attributes such as alignment, kerning and ligatures; a text object with a ruler, automatic scrolling, and wrapping, built–in support for displaying simple text, RTF, and HTML (and writing simple text and RTF). (Although much of the behavior is free, you still must programmatically provide for saving and reading text files.)
- _Control Behavior_. Applications automatically handle control highlighting, cursor display, pop-up list display, radio-button coordination, and many other aspects of control appearance and behavior. You can customize most of these aspects in Interface Builder. Applications also handle the invocation of actions (methods) in target objects when controls are activated (you set these associations in Interface Builder). You can create your own custom controls.

Cocoa applications are distributed as application bundles. An application bundle is a special type of a bundle: a directory that presents itself to the user in the Finder as a single file. In the case of an application bundle, the file is an executable. Double-clicking it causes the Finder to launch the application. Application bundles have an extension of `.app`.

An application bundle contains the application executable and the resources needed by that executable. For more information about bundles and application packaging, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

[Next](Document%20Architecture.md)[Previous](Introduction%20to%20Application%20Architecture.md)

