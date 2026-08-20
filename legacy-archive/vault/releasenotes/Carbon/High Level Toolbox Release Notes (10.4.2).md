---
title: High Level Toolbox Release Notes (10.4.2)
apple_id: TP40003380
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-HIToolbox10-4-2/index.html
archived_at: '2026-07-18T02:50:22.146762Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# High Level Toolbox and Navigation Services Release Notes for Mac OS X v10.4.2

> [!IMPORTANT]
> 

The High Level Toolbox is a subsystem of the Carbon framework for Mac OS X. It is composed of three frameworks: HIToolbox, HIServices, and NavigationServices. This document discusses bug fixes in the HIToolbox and NavigationServices frameworks for Mac OS X 10.4.2.

#### Contents:

- [Version Checking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztgobqfvcg63tujruw422fnrsw2zlooreuixzr)
- [HIToolbox Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztgobqfvcg63tujruw422fnrsw2zlooreuixzs)
- [NavigationServices Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztgobqfvcg63tujruw422fnrsw2zlooreuixzz)

### Version Checking

If you need to check for a specific version of the HIToolbox framework, you can use either the kHIToolboxVersionNumber global variable (on 10.3 and later) or the CFBundleShortVersionString in the HIToolbox Info.plist dictionary. kHIToolboxVersionNumber contains the HIToolbox build number, which is incremented each time that HIToolbox is rebuilt during the course of a Mac OS X release; CFBundleShortVersionString contains a separate non-incrementing HIToolbox version for a given Mac OS X release. To test for the HIToolbox included in Mac OS X 10.4.2, check that kHIToolboxVersionNumber is at least 220, or that CFBundleShortVersionString is at least 1.4.2.

To test for the HIToolbox included in Mac OS X 10.4.1, check that kHIToolboxVersionNumber is at least 219.1.

To check for the presence of bug fixes to the NavigationServices framework, you can use the CFBundleShortVersionString in the NavigationServices Info.plist dictionary. To test for the NavigationServices included in Mac OS X 10.4.2, check that CFBundleShortVersionString is at least 3.4.1.

### HIToolbox Framework

### HIView Manager

When destroying a view, the last event sent to the view is now kEventHIObjectDestruct, restoring the behavior of previous versions of Mac OS X (4055506). On Mac OS X 10.4 and 10.4.1, a view could receive other kEventClassControl events after kEventHIObjectDestruct.

The user pane control now sets the current port to the window's port before calling the user pane's tracking procedure, and restores it afterwards (4073540). On Mac OS X 10.4 and 10.4.1, the port was not explicitly set by the user pane; on previous versions of Mac OS X, it was set to the window's port.

### IBCarbonRuntime

Controls that are embedded inside a placard control using Interface Builder are now instantiated at runtime when the placard's window is loaded from the nib (4076443).

### Menu Manager

In BBEdit and Macromedia Fireworks, menu items with submenus now always show the right-pointing arrow indicating the presence of a submenu (4059804).

(Mac OS X 10.4.1 change) The Menu Manager's handling of scroll wheel events has changed. Previously, each scroll wheel event would change the menu highlight up or down by one item. In 10.4.1 and later, scroll wheel events scroll the entire menu content, and the selected item remains under the mouse at all times. Also, scroll wheel events are ignored unless the mouse is over a menu. This makes a scroll wheel or the scrolling trackpad feature available in newer PowerBooks much more usable in menus.

### MLTE

Fixed a crash that occurred when performing an undo with unconfirmed inline input (4085317).

### Text Services Manager

When using an input method that allows a different input source for each TSM document, the proper keyboard layout is now enabled when switching to a new application (4113889).

### Window Manager

Collapsing a drawer parent window no longer causes the drawer to detach from the parent when the parent is uncollapsed, and dragging a drawer closed with the mouse no longer causes all windows in the document window group to move together (4060883).

Window ordering is improved when a Cocoa window is frontmost inside a Carbon application, and the application is deactivated and then reactivated. This fixes a window ordering problem when a Save to PDF dialog is open above a Print sheet (4068534).

(Mac OS X 10.4.1 change) Improved compatibility with the code hints window in Macromedia Dreamweaver 2004 (4098764).

### NavigationServices Framework

Fixed various drawing and navigation problems that occurred when using the command-up-arrow key sequence in column view to move upwards from a selected volume to the "Computer" column (4065226).

Improved compatibility with Adobe Premiere when exporting a file (4071644).
