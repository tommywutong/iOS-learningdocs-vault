---
title: High Level Toolbox Release Notes (10.4.3)
apple_id: TP40003381
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-HIToolbox10-4-3/index.html
archived_at: '2026-07-18T02:50:22.190641Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# High Level Toolbox and Navigation Services Release Notes for Mac OS X v10.4.3

> [!IMPORTANT]
> 

The High Level Toolbox is a subsystem of the Carbon framework for Mac OS X. It is composed of three frameworks: HIToolbox, HIServices, and NavigationServices. This document discusses bug fixes in the HIToolbox and NavigationServices frameworks for Mac OS X 10.4.3.

#### Contents:

- [Version Checking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztgobrfvcg63tujruw422fnrsw2zlooreuixzr)
- [HIToolbox Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztgobrfvcg63tujruw422fnrsw2zlooreuixzs)
- [NavigationServices Framework](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztgobrfvcg63tujruw422fnrsw2zlooreuixzrgq)

### Version Checking

If you need to check for a specific version of the HIToolbox framework, you can use either the kHIToolboxVersionNumber global variable (on 10.3 and later) or the CFBundleShortVersionString in the HIToolbox Info.plist dictionary. kHIToolboxVersionNumber contains the HIToolbox build number, which is incremented each time that HIToolbox is rebuilt during the course of a Mac OS X release; CFBundleShortVersionString contains a separate non-incrementing HIToolbox version for a given Mac OS X release. To test for the HIToolbox included in Mac OS X 10.4.3, check that kHIToolboxVersionNumber is at least 222, or that CFBundleShortVersionString is at least 1.4.4.

To check for the presence of bug fixes to the NavigationServices framework, you can use the CFBundleShortVersionString in the NavigationServices Info.plist dictionary. To test for the NavigationServices included in Mac OS X 10.4.3, check that CFBundleShortVersionString is at least 3.4.2.

### HIToolbox Framework

### Appearance Manager

- HIThemeDrawGenericWell now draws a filled center when the kThemeAdornmentDefault bit of the HIThemeButtonDrawInfo.adornment field is set (2605918). This fixes a Tiger regression.
- Fixed a drawing glitch in the background of a scrollbar thumb (3814094).
- DrawThemeFocusRect no longer draws any part of the focus ring inside the specified rectangle (4086442). This fixes a Tiger regression.
- DrawThemeTrack now calls its ThemeEraseProc callback parameter (4107525). This fixes a Tiger regression.
- DrawThemeButton now sets the Quickdraw clip appropriately before calling its ThemeButtonDrawProc callback parameter (4138393). This fixes a Tiger regression.
- A rounded-corner bevel button that is less than 16 pixels high now draws the same way as it did in Panther (4138662). This fixes a Tiger regression.
- The Appearance Manager is now more careful to avoid crashing when the current port is invalid (4166700).
- DrawThemeButton now sets the current port's foreground color appropriately before calling its ThemeButtonDrawProc callback parameter (4193478). This fixes a Tiger regression.

### DataBrowser

- The DataBrowser's support for auto-scrolling in list view during a drag operation has been greatly improved (2794191). It is no longer necessary to continually move the mouse to force auto-scrolling, and the hot area in which scrolling occurs has been expanded.

### Dialog Manager

- GetDialogWindow now provides improved compatibility with the Brother DeviceSelector application and the Palm Desktop application (4163044, 4163706). Note that we have found that many applications incorrectly pass a WindowRef to the GetDialogWindow API; this causes GetDialogWindow to return NULL. Make sure that when calling GetDialogWindow, you pass a DialogRef, not a WindowRef.

### HIArchive

- The HIObject base class now archives its accessibility-ignored and archiving-ignored attributes (4118879).
- HIScrollView now marks its scrollbars as archiving-ignored, and the HIView base class now skips over archiving-ignored views when archiving a view's subviews (4123803). Prior to this fix, it was not possible to correctly archive and unarchive an HIScrollView containing another view, such as an HITextView.
- When an error occurs during unarchiving of an HIObject, the HIArchive implementation now recovers correctly (4195259). Prior to this fix, an error during unarchiving would cause a crash when the decoding HIArchiveRef was released.

### HIView Manager

- Scaling-based HILayouts were incorrectly positioning the view one pixel too far to the right or bottom (3948022). This fixes a Tiger regression.
- Fixed a common source of crashes in the Finder during view drawing (4166700).

### HIWebView

- HIWebViews now redraw properly when displayed in composited windows (4141161). This fixes a Tiger regression. The fix for this problem was actually in WebKit, not HIToolbox.

### IBCarbonRuntime

- When creating a segmented view from a nib, the IBCarbonRuntime view creation code was incorrectly releasing some of its segment data after creating an instance of the segmented view. Therefore, if you tried to create more than one segmented view from the same nib, you would crash. The IB runtime now keeps the segment data in existence until the nib is closed, so it's possible to create more than one segmented view from the same nib reference (4180858). If you need to work around this problem on earlier versions of Mac OS X 10.4, you should release your IBNibRef after creating a window containing a segmented view, and recreate the IBNibRef each time you need to create a new window.

### Menu Manager

- Fixed a crash that commonly occurred in the Dock and other applications when an empty submenu was opened (4062476).
- Improved compatibility with the Cmd-Q and Cmd-, keyboard shortcuts in Palm Desktop (4078419).
- Fixed a window resizing problem visible in the StarMenu sample application that occurred when a window used a custom HIView for its window frame and the HIView did not implement the kEventControlGetFrameMetrics event (4086478). If you are implementing a custom HIView to draw a custom window frame, be sure to implement kEventControlGetFrameMetrics.
- Sending the AXPress accessibility action to an AXMenuBarItem now causes the menu to open, rather than highlighting the Apple menu (4099617). This change also enables Speech Recognition to open a menu by speaking the menu title. This fixes a Tiger regression.
- While the user is using the keyboard to navigate through menus, it is now possible to press Return or Enter to select a menu item that is a parent of a submenu but that also has the kMenuItemAttrSubmenuParentChoosable attribute (4115501). This fixes a Tiger regression.
- Fixed a problem that caused menu items in the BBEdit, Mailsmith, and TextWrangler applications to become disabled when a UIElement application became frontmost (4129011).
- Iconic menu titles are no longer drawn with a disabled appearance when the menu itself is disabled (4126917). This change makes iconic menu title behavior match the behavior of text menu titles in Tiger.

### MLTE

- Fixed a problem that could cause an HITextView in a composited window to ignore mouse clicks (4137938). A workaround for this problem is to install a kEventControlTrack handler on your HITextView. In your Track handler, do the following:

  - call GetPort to get the current port, and then SetPort( NULL )
  - call CallNextEventHandler
  - call SetPort with the saved port
- Selecting text containing a mix of scripts and styles could sometimes overwrite memory not owned by MLTE and cause a crash (4060100).
- Fixed scrollbar behavior when scrolling large amounts of text (extending past 32K vertical coordinate units) in an HITextView (4070933).
- Fixed an error in TXNPaste that was causing frequent crashes in the Finder when showing the clipboard window (4120568).
- Fixed handling of the Page Up/Down, End, and Home keys to provide more reliable behavior when scrolling in an HITextView (4130275).
- Ensured that the correct port is used during click handling and text selection (4161301). This fixes errors during text selection that were commonly seen in Final Cut Pro.
- When a text field is being used for password input, MLTE no longer reports the text field contents in response to requests for the kAXValueAttribute, kAXSelectedTextAttribute, or kAXStringForRangeParameterizedAttribute accessible attributes (4162943). This prevents the screen reader from reading the password. This fix was originally provided in Security Update 2005-007.
- Fixed some drawing issues with edit fields in Final Cut Pro (4161301).

### Text Services Manager

- Improved app startup performance when the user has an input method or palette selected (4172676, 4186011)
- Reduced memory requirements for tracking the active set of input methods (4173363).
- Fixed problems with using input methods in the Spotlight search results window (4173428).
- Fixed problems with using input methods in the Spotlight search results window (4173428).
- Improved performance when opening the Format Text Box dialog in Microsoft Word if an input method is selected (4191919).
- Fixed problems in detection of new input methods that sometimes prevented a newly installed input method from being visible in the Input menu after reboot (4053979).
- Fixed problems that sometimes prevented the palette windows of the current input method from hiding when switching to another input method (4062065).
- The active input method is now used for typing in the Spotlight search results window (4173428).
- Improved performance of NewTSMDocument (4191919).

### Window Manager

- When a Cocoa application containing Carbon windows is activated, the Window Manager no longer orders the Carbon windows to the front of the window list, since AppKit will do this for all windows in the process (3992462). This fixes a common window ordering issue in Safari when a page with a Flash or Quicktime plugin is open.
- When the user clicks on a window in an inactive application, now verify that the window still exists before attempting to select it once the process has become active (4078291). This fixes some common crashes in Adobe Reader, Adobe Illustrator CS, and iTunes.
- Improved compatibility with the Smudge and Shadow color-picker windows in Macromedia Freehand (4095397). The color-picker window is no longer ordered behind the application's tool configuration window. This fixes a Tiger regression.
- Improved compatibility with the Piranesi application when its Tools Manager window is resized (4119915). This fixes a Tiger regression.
- Fixed window dragging errors when dragging a window that uses a custom WDEF that has negative structure widths, such as the CustomWindow sample application (4151906). This fixes a Tiger regression.
- Fixed a regression in Mac OS X 10.4.2 that prevented windows in the DragThing application from being ordered in front of other application windows when DragThing's Dock icon was clicked (4178935).
- When called from a non-foreground application, FindWindow now returns inNoWindow instead of inMenuBar if the specified point is in the menubar area (4218591). This fixes a Tiger regression seen by Cocoa-based applications that use GetEventMonitorTarget to track mouse-down events in other applications; on Tiger, using GetEventMonitorTarget in this way would prevent menu tracking in the active application from working properly.

### NavigationServices Framework

- Improved compatibility with the Mailsmith and TextWrangler applications when attempting to save a file with a '/' in the filename (4149596).
