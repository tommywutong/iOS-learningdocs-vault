---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/PreferencePanes.html
archived_at: '2026-07-18T02:12:28.200574Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Architecture%20of%20Preference%20Panes.md)

# Introduction

Preference panes are dynamically loaded plug-ins that provide a graphical user interface to the system’s or an application’s user preferences. Preference panes can be presented to the user using the central System Preferences application, using a specialized preferences application, or as the Preferences menu item in an application’s application menu. In System Preferences, each icon in its Show All view represents an individual preference pane plug-in. You can develop preference panes for use by System Preferences or by your own application.

The most common situation for using preference panes is an application that lacks its own user interface (or has a very restricted user interface such as the Mac OS X Login application) but needs to be configurable. Possible cases include a server application that always runs in the background or an application that makes its services available to other applications through the Services menu. To allow configuration of these applications, you must provide a user interface in a separate application. You should not require the user to hand-edit configuration files or execute the application from the command line with special arguments. Instead, create one or more preference pane plug-ins that contain the user interface and the code that can read and write the preference settings. Then, either supply your own “Setup” application or, if appropriate, use System Preferences to display the preference panes.

You should read this document if you are a Cocoa developer who wants to provide a custom preference pane, accessible from the System Preferences applications, to your users. You should have a working knowledge of Cocoa programming with the Application Kit before attempting preference pane programming.

This document describes how to create and manage a preference pane, how to have System Preferences load your own preference pane, and how to load a preference pane in your own application.

Here are the concepts covered:

- [Architecture of Preference Panes](Architecture%20of%20Preference%20Panes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydclkciffekq2ii5aq) describes the plug-in architecture of preference panes and how they interact with applications and the system.
- [The Preference Application](The%20Preference%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydelkdjjbeursbinea) describes the ways the preference pane can be presented to the user: System Preferences, a specialized preferences application, or inside the main application.
- [Managing User Preferences](Managing%20User%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydglkcifbeoscgircq) describes several ways the preference pane can interact with the system for manipulating preferences.
- [Life Cycle of a Preference Pane](Life%20Cycle%20of%20a%20Preference%20Pane.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydilkcineumscgi5cq) describes how the application interacts with the preference pane.
- [Anatomy of a Preference Pane Bundle](Anatomy%20of%20a%20Preference%20Pane%20Bundle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydklkdjjbegqkcifba) describes the structure of a preference pane bundle.
- [Updating Preference Panes](Updating%20Preference%20Panes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4damzzfvjvomq) describes the requirements for preference panes for OS X version 10.6 and later.

Here are the tasks covered:

- [Preventing Name Conflicts](Preventing%20Name%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydmlkciffesqkhizca) recommends a technique to prevent name conflicts between the global symbols in your preference pane and either the application or other preference panes.
- [Wrapping Long Labels](Wrapping%20Long%20Labels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbsfvjvomi) describes how to modify the `.plist` file so that long labels are split across two lines.
- [Using Preference Services](Using%20Preference%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydolkcifbemq2bijfa) describes the methods available for reading and writing preferences to a preference file.
- [Communicating With the Target Application](Communicating%20With%20the%20Target%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydqlkcifbemq2bijfa) provides examples for notifying a separate target application of preference changes.
- [Creating a Preference Pane Bundle](Creating%20a%20Preference%20Pane%20Bundle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydslkcifbemq2bijfa) walks you through the steps of creating a skeletal preference pane bundle in Xcode and Interface Builder.
- [Implementing a Simple Preference Pane](Implementing%20a%20Simple%20Preference%20Pane.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ytalkcifbemq2bijfa) walks you through the source code of a simple preference pane, showing an example of how to implement a working preference pane.
- [Using Preference Panes in Other Applications](Using%20Preference%20Panes%20in%20Other%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ytclkcijbueqkhifea) describes the responsibilities of an application that loads a preference pane.

[Next](Architecture%20of%20Preference%20Panes.md)

