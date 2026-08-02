---
title: Terminal 2 Release Notes
apple_id: TP40006502
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-Terminal/index.html
archived_at: '2026-07-18T02:50:27.199837Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Terminal 2 Release Notes

> [!IMPORTANT]
> 

#### Contents:

- [User Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Performance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [Emulator Conformance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)
- [International Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ny)
- [Printing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjr)

### User Interface

### Tabbed Windows

Terminal has added support for tabbed windows. A window can contain one or more tabs, which are displayed at the top of the window in a manner similar to Safari’s tabs. Many of the tab menu items and user interface gestures from Safari are available in Terminal, including the tab-related menu items in the Window menu. Option-clicking a tab’s close button will close all other tabs in the window that do not have running processes.

### Settings

Terminal’s support for user settings has been greatly enhanced. Settings are now managed from the application preferences panel under _Settings_. Users can manage multiple sets of settings, and have fine control over how settings are used. In addition, all settings are now managed in the application preferences instead of in individual `.term` files as in Tiger and earlier releases. Existing `.term` files can be imported by double-clicking them in the Finder, importing them using the _Import_ item in the File menu, or by dragging them into the Window Settings preferences.

Groups of multiple windows are now managed in the application preferences as well, under _Window Groups_. Window groups consist of one or more windows and their tabs, the loaded settings for each tab, and the size, position, shortcut key and title of each window. Tabs can be imported and exported from the preferences either by drag-and-drop, or by selecting the corresponding items in the action menu in the Window Groups section of the preferences.

To change the settings for an open window or tab, open the Inspector by pressing ⌘-I and select the _Settings_ tab. Clicking on a thumbnail in the inspector changes the settings of the frontmost window or tab.

### Text Selection

Terminal now fully supports discontiguous and rectangular selection modes, accessible with the Command and Option keys, respectively. To accommodate this change, the path-and-URL selection keyboard shortcut has been changed from Command to Command-Shift.

Tab characters (`ASCII` 9) are no longer copied and selected as multiple spaces; they are treated as proper tabs.

### Performance

Terminal now uses a much more compact representation for text in the user’s scrollback buffer than before. As a result, Terminal uses 60% or less memory in Leopard than in Tiger for long sessions. We have changed the default length for the scrollback buffer to Unlimited, as most users will now be able to use Terminal for long periods of time without running out of memory.

### Emulator Conformance

Terminal now emulates a standard xterm as closely as possible, passing the main portion of the `vttest` emulation test. It has full support for VT-102 emulation and most of the VT-220, VT-320 and ANSI extensions.

### International Support

### Text Layout

Terminal in Leopard has better support for international text layout and input than earlier versions. Instead of relying on a custom width table, Terminal now uses the Unicode East Asian Width property to determine the width of a character. Characters with ambiguous width are treated as narrow characters. For more information, see [Unicode Standard Annex #11: East Asian Width](http://unicode.org/reports/tr11/).

As in previous releases, Terminal does not have complete support for complex scripts, including, but not limited to, Arabic, Persian, Hebrew, and Devanagari. Selecting text in these scripts may not behave as expected, and the cursor will generally not move as expected within a run of complex characters. We will reconsider this support in a future release, but most likely not before a standard for terminal emulation with support for complex scripts is widely accepted.

### Text Input

Editing text in Terminal now behaves similarly to other Cocoa applications:

- Terminal displays the correct background color when entering text using dead keys.
- Unconfirmed text and the corresponding underlines and other styles on unconfirmed text are always laid out correctly.
- Unconfirmed input which wraps across multiple lines is now handled properly in most cases.

### Environment

By default, Terminal now sets the `LANG` environment variable to the appropriate value for your locale, as selected in System Preferences. For most users, this means that most Unix applications will properly handle international text without any further changes to the environment. You can disable this behavior from the Advanced tab of the Settings pane in Terminal’s preferences.

### Printing

All attributes and layout are now preserved when printing from Terminal. Text is always scaled to fit the width of the page, instead of rewrapped, which should improve printing from applications like Emacs and Vim. To simplify the Print panel, the Print Selection behavior has been moved to the File menu.
