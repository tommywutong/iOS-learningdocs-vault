---
title: Accessibility Programming Guide for OS X
apple_id: TP40001078
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/OSXAXKeyboardShortcuts.html
archived_at: '2026-07-15T03:49:10.136299Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Accessibility Programming Guide for OS X](index.md)



## Accessibility Keyboard Shortcuts

This appendix lists keyboard shortcuts that are reserved for use with the Accessibility features in OS X.

To turn VoiceOver on or off, press Command-F5.

Table A-1 lists the keyboard shortcuts that are reserved for use with screen zooming in OS X. A user turns on the zoom feature in the Zoom pane of Accessibility preferences.

__Table A-1__Key combinations used with screen zooming

| Key combination | Action |
| --- | --- |
| Option-Command-8 | Turns screen zooming on or off |
| Option–Command–Equal Sign (=) | Zooms in |
| Option-Command-Hyphen (-) | Zooms out |
| Control-Option-Command-8 | Inverts the screen colors |
| Command-Option-Control-Comma (,) | Reduces contrast |
| Command-Option-Control-Period (.) | Increases contrast |

OS X provides the option of _full keyboard access mode,_ in which users can navigate through windows, dialogs, menus, toolbars, and the Dock using the keyboard alone, without a mouse or other pointing device.

Users can turn on full keyboard access in the Shortcuts pane of Keyboard preferences. Control-F1 is a reserved keyboard shortcut for turning full keyboard access on or off. Control-F7 toggles between keyboard access for all controls in windows and dialogs and the default state, in which only text fields and scrolling lists are accessed with the keyboard. Don’t use these combinations for any other purpose.

With keyboard access turned on in windows and dialogs, press the arrow keys to move between values within a control. For example, if the user selects a slider with the Tab key, the arrow keys move the slider control along the slider track. For vertically oriented choices, such as menu items, the Up Arrow and Down Arrow keys move the selection. For horizontally oriented choices, such as a row of tabs, the Right Arrow and Left Arrow keys move the selection. In some cases, it makes sense to support both orientations. For example, a vertical slider can use both the Up Arrow and the Right Arrow to increase the value.

In some cases, such as radio buttons, moving the focus to an item selects it as well. In other cases, such as push buttons, the user activates a selected item by pressing the Space bar. In full keyboard access mode, pressing the Space bar is equivalent to clicking the mouse button.

The Esc (Escape) key is used to cancel a dialog and to cancel a selection in a pop-up menu or list. In a Dock menu, pressing Esc dismisses the menu and moves focus to the frontmost window.

The user can also quickly place focus in the menu bar, the Dock, toolbars, and utility windows using the key combinations described in Table A-2.

This behavior is provided for all apps that use the standard controls. If you are implementing your own controls, you need to provide these behaviors for your users.

__Table A-2__Key combinations for moving focus in full keyboard access mode

| Key combination | Action |
| --- | --- |
| Control-F1 | Turns full keyboard access on or off |
| Control-F2 | Moves focus to the menu bar |
| Control-F3 | Moves focus to the Dock |
| Control-F4 | Moves focus to the active (or next) window |
| Shift-Control-F4 | Moves focus to the previous window |
| Control-F5 | Moves focus to the toolbar |
| Control-F6 | Moves focus to the first (or next) utility window |
| Control-Shift-F6 | Moves focus to the previous utility window |
| Control-F7 | Toggles the keyboard access mode in windows and dialogs between all controls and just text fields and scrolling lists |
| Control-Tab | Moves focus to the next grouping of controls in a dialog or the next table (when Tab moves to next cell) |
| Control-Shift-Tab | Moves focus to the previous grouping of controls |
| Command-Tab | Moves focus to the first (or next) open app’s Dock icon |
| Shift-Command-Tab | Moves focus to the previous open app’s Dock icon |
| Arrow Key | Moves focus to the next or previous value in a text field or certain controls, such as menus; also opens Dock menus |
| Control–Arrow Key | Moves focus to another value or cell within a control such as a table |
| Command–Grave Accent (`) | Activates the next open window in the frontmost app |
| Command–Shift–Grave Accent (`) | Activates the previous open window in the frontmost app |
| Command–Option–Grave Accent (`) | Moves focus to the window drawer |
| Space bar | Selects the highlighted control (equivalent to clicking the mouse button) |
| Return (Enter) | Selects the default button |
| Esc | Cancels a dialog or a selection in a pop-up menu or list; in a Dock menu, Esc closes the menu and moves the focus to the frontmost window |

> [!NOTE]
> 

[Testing for Accessibility on OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/OSXAXTestingApps.html#//apple_ref/doc/uid/TP40001078-CH210-TPXREF101)
