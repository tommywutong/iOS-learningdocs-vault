---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Introduction.html
archived_at: '2026-07-15T07:21:11.867874Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](How%20Windows%20Work.md)

# Introduction

An application displays windows on the screen that must be managed and coordinated. A window object corresponds to at most one on-screen window. The two principal functions of windows are to provide an area in which views can be placed and to accept and distribute events the user sends through actions with the mouse and keyboard. The term window sometimes refers to the Application Kit object and sometimes to the window server’s window device; which meaning is intended is made clear in context. Panels are a special kind of window, typically serving an auxiliary function in an application, such as utility windows.

This document is intended for Cocoa developers who need to work with windows and panels in their applications.

This programming topic describes how to use windows and panels. These articles give you basic information on the different types of windows and how they work:

- [How Windows Work](How%20Windows%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdclkcijbukq2girea) describes the classes that define objects that manage and coordinate the windows an application displays.
- [How a Window is Displayed](How%20a%20Window%20is%20Displayed.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdelkcineueskkjjca) describes how window drawing is accomplished.
- [How Modal Windows Work](How%20Modal%20Windows%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdglkdjjbekqkeijaq) describes the behavior of modal windows.
- [How Panels Work](How%20Panels%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdilkcijbuerkbirba) describes the various uses of panels.
- [How Window Controllers Work](How%20Window%20Controllers%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdklkciffegq2jizfa) describes the relationship between a window and its controller.
- [Window Layering and Types of Windows](Window%20Layering%20and%20Types%20of%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztmlkcineuirskizea) describes window layering and the concepts of key and main windows, and how a window can avoid becoming key or main.
- [Window Layers and Levels](Window%20Layers%20and%20Levels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdolkciffeissfiraq) describes window levels, and how to place a window in a specific level, such as the level for document windows, palettes, or tear-off menus.
- [Setting Window Collection Behavior](Setting%20Window%20Collection%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4demzxfvjvomi) describes how to set a window’s behavior with Spaces, Exposé, and window cycles.

These articles describe how to use windows:

- [Opening and Closing Windows](Opening%20and%20Closing%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdmlkdjjbegq2divda) describes how to open and close, or just show and hide, a window.
- [Sizing and Placing Windows](Sizing%20and%20Placing%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdqlkcineugrceifeq) describes how to control a window’s size and position, including how to set its minimum and maximum size, how to constrain it to the screen, how to cascade it so its title bar remains visible, how to zoom it as though the user pressed the zoom button, and how to center it on the screen.
- [Saving a Window’s Position into the User’s Defaults](Saving%20a%20Window%E2%80%99s%20Position%20into%20the%20User%E2%80%99s%20Defaults.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdslkcineuiskiijba) describes how to store a window’s position in the user defaults system, so that it appears in the same location the next time the user starts the application.
- [Minimizing Windows](Minimizing%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztalkcineugq2gifea) describes how to replace a window with a smaller counterpart in the Dock.
- [Using the Window Menu](Using%20the%20Window%20Menu.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztclkcineuessciraq) describes how to place a window’s name in the Windows menu that appears in most Cocoa applications.

These articles describe how to change what a window looks like:

- [Setting a Window’s Appearance](Setting%20a%20Window%E2%80%99s%20Appearance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztelkcijbuircii5cq) describes how to choose whether to display a window’s peripheral elements, including its title bar, close box, zoom box, or size box. It also describes how to set a window’s background color and transparency,
- [Setting a Window’s Title and Represented File](Setting%20a%20Window%E2%80%99s%20Title%20and%20Represented%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztglkcijbuersfinca) describes how to set a window’s title with either a string or the filename of the window’s represented file.
- [Setting Attributes for the Window’s Image](Setting%20Attributes%20for%20the%20Window%E2%80%99s%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztilkciffeerckinaq) describes how to set attributes for the window’s device, which stores the window’s image, including how the image is stored, when the image is created, and the image’s color depth.

These articles describe how to handle a window’s events:

- [Handling Events in Windows](Handling%20Events%20in%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztklkcineugskcifca) gives basic information on how a window handles events.
- [Using Keyboard Interface Control in Windows](Using%20Keyboard%20Interface%20Control%20in%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztolkdjjbeirkjijda) describes how to navigate between a window’s fields using the Tab key and how to use the Return and Escape keys to select default buttons.
- [Using the Window’s Field Editor](Using%20the%20Window%E2%80%99s%20Field%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztqlkciffeirkhjfaq) describes how to use the window’s text object, which is shared for light editing tasks.

These articles describe some advanced features of windows:

- [Using Window Notifications and Delegate Methods](Using%20Window%20Notifications%20and%20Delegate%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgiztslkciffeeq2cijda) describes the notifications and delegate methods used when a window gains or loses key or main window status, minimizes, moves or resizes, becomes exposed, or closes.
- [Dragging Images to and from Windows](Dragging%20Images%20to%20and%20from%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi2dalkdjjbegqsei5da) describes what happens when the user wants to drag an object into or out of a window.
- [Updating the Cursor Image in a Window](Updating%20the%20Cursor%20Image%20in%20a%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi2dclkcineuescfircq) directs you to information on how to change the cursor image when the cursor is over a specified area in a view.
- [Caching Window Images](Caching%20Window%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi2delkciffeiq2finea) describes how to temporarily cache a portion of a window’s image so that it can be restored later. This is useful when highly dynamic drawing must be done over an otherwise static image of the window.

For additional information on specific types of windows and panels, you can also see the following programming topics:

- _[Sheet Programming Topics](../Sheet%20Programming%20Topics/Introduction%20to%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayde2i)_ describes a dialog attached to a specific window, ensuring that a user never loses track of which window the dialog belongs to.
- _[Drawer Programming Topics](../Drawer%20Programming%20Topics/Introduction%20to%20Drawers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaydc2i)_ describes a type of view that slides out from one side of a window.
- _[Toolbar Programming Topics for Cocoa](../Toolbar%20Programming%20Topics%20for%20Cocoa/Introduction%20to%20Toolbars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyds2i)_ describes a standard way to display a toolbar for a titled window below its title bar and provide users with a way to customize toolbars and save those customizations.
- _[Dialogs and Special Panels](../Dialogs%20and%20Special%20Panels/Introduction%20to%20Dialogs%20and%20Special%20Panels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3tc2i)_ describes alert panels and other specialized types of panels, such as Font, Save, and Print panels.
- _[Document-Based App Programming Guide for Mac](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/About%20the%20Cocoa%20Document%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzz)_ describes how to use the architecture supplied by AppKit to create applications that can create, open, load, and save multiple document files.
- _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ discusses the variety of ways your application objects can handle the events they receive.
[Next](How%20Windows%20Work.md)

