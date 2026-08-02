---
title: AppleScript Studio Programming Guide
apple_id: TP30000889
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/StudioBuildingApps/chapter05/studio_cookbook.html
archived_at: '2026-07-15T05:19:49.423894Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Studio Programming Guide](Introduction%20to%20AppleScript%20Studio%20Programming%20Guide.md)


[Next](Currency%20Converter%20Tutorial.md)[Previous](Programming%20With%20AppleScript%20Studio.md)

# AppleScript Studio Cookbook

This chapter provides step-by-step instructions for performing common AppleScript Studio tasks, in the following sections:

- [Performing User Interface Actions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2telkciffeor2iirba)
- [Specifying Minimum Requirements for an Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2telkcineuqsshirba)
- [Adding AppleScript Studio Support to Your Cocoa Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2telkcineusr2gi5ca)
- [Setting the Keyboard Focus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2telkcijbuerciizea)
- [Obtaining the Path to the Current Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2telkcijbuerciivcq)

AppleScript Studio provides the ability to perform user interface actions directly in scripts, using the `perform action` command (defined in the Control View suite). For example, you can tell an interface object, such as a button, to perform its `clicked` handler, thus providing a way to directly script the user interface (subject to limitations described in [Scripting AppleScript Studio Applications](Programming%20With%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tclkukbmferkgge3tq)). Note, however, that calling the `clicked` handler will not provide the visual feedback a user would see if they actually clicked the button.

Listing 4-1 shows a script that tells the “Drawer” button in the Drawer application to perform its `clicked` handler, which will either open or close the drawer, depending on its current state.

__Listing 4-1__  Manipulating a button in the Drawer application from an external script

```
tell application "Drawer"
    set theButton to button "Drawer" of window "Main"
    tell theButton to perform action
end tell
```

The `perform action` command does nothing unless the specified object has an action handler—a handler such as a `clicked` or `double-clicked` handler in the Action group in the Interface Builder Info window for the object. For example, see the Info window in [Figure 1-15](About%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dslkdivdumr2bi5da).

To use the `perform action` command with menus, you can use syntax like the following:

```
tell menu item 1 of menu 1 of main menu to perform action
```

You can also call application methods directly, as described in [Scripting AppleScript Studio Applications](Programming%20With%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tclkukbmferkgge3tq).

To run AppleScript Studio applications, the target machine must include the AppleScript Studio runtime required for the application. The runtime is available if `AppleScriptKit.framework` is present in `/System/Library/Frameworks`.

For example, an application built with AppleScript Studio 1.2 that uses features added in version 1.2 requires the 1.2 runtime. However, a similar application that doesn’t use any features from AppleScript Studio 1.2 can run with the 1.1 runtime. Note that all 1.1 applications can run with the 1.0 runtime distributed with Mac OS X version 10.1.2. For more information on versions and runtimes, see [AppleScript Studio System Requirements and Version Information](AppleScript%20Studio%20System%20Requirements%20and%20Version%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dalkukbmferkggeydc).

You can install a `will finish launching` handler for your application to check the version. [Connect the Application Object](Mail%20Search%20Tutorial-%20Connect%20the%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tmlkukbmferkgge4de) shows how to add a `will finish launching` handler.

Listing 4-2 shows a simple example of how the `will finish launching` handler might check for the application’s required version of AppleScript Studio. In this case, the application quits if the required version isn’t available. Note that the handler doesn’t check AppleScript Studio’s version number directly. Instead, it checks for the corresponding AppleScript version, as shown in [Table A-1](AppleScript%20Studio%20System%20Requirements%20and%20Version%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dalkciffeuqsdijbq).

__Listing 4-2__  will finish launching handler that checks for required version of AppleScript Studio

```
on will finish launching theObject
    considering numeric strings
    if AppleScript's version as string is less than "1.10.1" then
        display dialog "This application requires AppleScript Studio 1.4 or later."
        quit
    end if
    end considering
end will finish launching
```


You can use the following steps to add AppleScript Studio support to your existing Cocoa application:

1. Add the AppleScriptKit framework to your project. You can do so by navigating to `/System/Library/Frameworks/AppleScriptKit.framework` and dragging the framework into the Frameworks group in the Xcode project for your application.

   In the dialog that appears, do not select the checkbox to copy items, but do check the radio button to recursively create groups. If you have more than one target, you’ll have to select any targets the framework should be added to.
2. Add an AppleScript Studio build phase to the application. To do this, first click the Targets tab, then double-click the desired Target. You should see a pane showing the Files & Build Phases tab.

   Click the section labeled Bundle Resources. You should be able to select the whole section.

   Choose Project > New Build Phase > New AppleScript Build Phase (from the Projects menu).
3. If you’ve already added any `.applescript` files to your application, they’ll be in the Bundle Resources phase, and you’ll have to drag them to the new AppleScript phase you just created.
4. If your application is not already scriptable, make the following modification to its `Info.plist` file to make it scriptable:

   In the Application Settings pane (after clicking the Expert button), add a new string entry to the property list that sets NSAppleScriptEnabled to “YES”. You can add an entry by clicking the New Sibling button. You can double-click any of the entries in the sibling to edit it.
5. If your application has a `.scriptsuite` file, for every class in that file whose superclass belongs to the core suite (NSCoreSuite), change the suite to ASKApplicationSuite. For example, change

```
"Superclass" = "NSCoreSuite.NSApplication"
```

   to

```
"Superclass" = "ASKApplicationSuite.NSApplication"
```


To make a user interface object, such as a text field, have the keyboard focus, set its window’s `first responder` property. For example, the following Tell statement causes a text field to become active and be first in line to respond to keyboard events:

```
tell window "user information"
    set first responder to text field "user name"
end tell
```

Note that without the Tell statement, you would have to specify the window twice:

```
set first responder of window "user information"
    to text field "user name" of window "user information"
```

In many cases, you will not have to set keyboard focus, because it is set automatically as a user tabs between fields, clicks on a text field, and so on.

To obtain the path to the current (running) AppleScript Studio application, you use the standard scripting addition command `path to`. For example:

```
set myPath to (path to me)
display dialog (myPath as string)
-- result, if inserted in on opened handler in Drawer sample application:
-- MacOSX:Developer:Examples:AppleScript Studio:Drawer:build:Drawer.app
```

The Standard Additions are automatically installed with Mac OS X.

[Next](Currency%20Converter%20Tutorial.md)[Previous](Programming%20With%20AppleScript%20Studio.md)

