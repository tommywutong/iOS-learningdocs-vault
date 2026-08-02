---
title: High Level Toolbox Release Notes (10.5.2)
apple_id: TP40007068
resource_type: Release Note
platform: macOS
topic: null
technology: Carbon
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-HIToolbox10-5-2/index.html
archived_at: '2026-07-18T02:50:22.255015Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# HIToolbox Release Notes for OS X v10.5.2

This release note describes changes to the HIToolbox framework in OS X v10.5.2.

#### Contents:

- [Appearance Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [HIShape](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [HIToolbar](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [HIViews](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [IBCarbonRuntime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [Keyboard Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)
- [Menus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ny)
- [MLTE](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oa)
- [Text Services Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oi)
- [Windows](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanryfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjq)

### Appearance Manager

- The ApplyThemeBackground API no longer leaks a PixPat each time it is called (rdar://5576789).

### HIShape

- In OS X v10.5.0, the HIShape APIs were moved from the HIToolbox framework to the HIServices framework. This introduced a compatibility problem when linking an application that used the HIShape APIs against the 10.5 SDK; the application would not launch on earlier versions of OS X because the linker would look for the HIShape symbols in the HIServices framework (which would not have them) rather than the HIToolbox framework. OS X v10.5.2 contains a fix for this problem (rdar://5631372), but in order to link successfully, you must link against Current Mac OS rather than using the 10.5 SDK. The 10.5 SDK has not yet been updated to include this fix.

### HIToolbar

- The toolbar configuration sheet now repositions appropriately when a toolbar’s icon size or text/icon style is changed while the sheet is open (rdar://5533317).

### HIViews

- The Clock view now properly supports input in 24-hour mode (rdar://5532315).
- The HIImageViewCopyImage API now returns a valid CGImageRef, rather than NULL, when the image view’s content has been set to a CGImageRef (rdar://5570580).
- Views that display images no longer crash for certain image types (rdar://5544084).

### IBCarbonRuntime

- A compatibility problem that caused versions 5.0 and 5.1 of the Sibelius application to crash at launch has been fixed (rdar://5553794).

### Keyboard Resources

- The ‘KCHR’ resources for Canadian, Russian, Italian, and Swiss keyboards have been updated to match those used in OS X v10.4 (rdar://5564950). This fixes a regression in command key handling when using these keyboards.

### Menus

- It is now possible for the user to choose an opaque menu bar appearance in the Desktop preferences pane.
- Menus are now less transparent than they were in OS X v10.5.0. This improves legibility on some LCD panels, particularly those included in portable Macs.
- Switching some games from full-screen to windowed mode now properly resizes the menu bar to the full width of the screen (rdar://5450976).
- Dynamic menu items that are in the system-provided section of the application menu in a Carbon application (from the Preferences item on down) are now properly displayed when the menu first opens (rdar://5571248). There is still a known issue with dynamic menu items not responding to modifier key presses. This issue will be fixed in a future software update.

### MLTE

- Horizontal scrolling with a mouse wheel over a single-line MLTE control has been disabled (rdar://5575778). Horizontal scrolling in a single-line control isn’t typically necessary or useful and can cause user confusion when the text in the control disappears.

### Text Services Manager

- The Text Services Manager now establishes autorelease pools before calling into IMKit, which fixes an incompatibility with the Canon Printer Setup application (rdar://5508690).

### Windows

- Sheets now have the same appearance as in Cocoa applications, with a shadow cast onto the sheet by the parent window. The implementation of this appearance requires ShowSheetWindow to add a new window to the window list when showing the sheet; the new window is used to draw the sheet shadow. This new window is positioned above the sheet in the window list. We’ve noticed that the presence of this window causes compatibility issues with some applications that expect the sheet to be the frontmost window in the window list. To improve compatibility with these applications, the FrontWindow API has been modified to ignore this extra window. However, your application will still see the window if iterating manually over the window list. We recommend tagging your windows with a window property using the SetWindowProperty API in order to distinguish your own windows from windows provided by the toolbox; this will help avoid confusion with the many other types of windows provided automatically for your application, such as help tags, menus, the menu bar, in-place edit windows for DataBrowser, and combo box lists.
- The HIWindowConstrain API now behaves properly when a NULL value is passed for the inScreenBounds parameter (rdar://5554240). Previously, it would attempt to constrain the window position against an uninitialized screen bounds.
