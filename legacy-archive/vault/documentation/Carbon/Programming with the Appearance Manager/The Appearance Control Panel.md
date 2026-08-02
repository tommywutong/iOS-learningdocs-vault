---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.3.html
archived_at: '2026-07-15T05:23:56.612503Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.2.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.4.md)

---

#   The Appearance Control Panel

The 

Appearance control panel is the user interface for the Appearance Manager. Through the Appearance control panel, users can adapt their experience of the system's look and sound by changing the current theme. The changes that the user makes to the current theme apply not just to the Mac OS itself, but also to all theme-compliant programs that the user is currently running.

[Figure 2-1](#apple-giytkojs)
shows the same desktop, before and after a change of themes.

__Figure 2-1__  

The same desktop in two different themes

!

As [Figure 2-1](#apple-giytkojs)
shows, changing a theme can mean changing various user preferences. A 

__theme__
can contain preferences for the current desktop picture or pattern, the system fonts, any interface-related sounds, the current appearance, and other options.

Each pane of the Appearance control panel allows the user to specify preferences for selected aspects of a theme. As shown in [Figure 2-2](#apple-gm3dmmjt)
, the Themes pane is the first presented to the user. In this pane, the user can select the current theme from among various system-supplied themes, or the user can choose a theme that they themselves have previously created.

__Figure 2-2__  

The Themes pane of the Appearance control panel

!

[Figure 2-3](#apple-gm3denbw)
shows the Appearance pane of the Appearance control panel. In this pane, the user can select highlight and variation colors for an appearance. An __appearance__

unifies the look of human interface objects on the system, including alert icons, controls, background colors, dialog boxes, menus, windows, and state transitions.

__Figure 2-3__  

The Appearance pane of the Appearance control panel

!

In the Fonts pane of the Appearance control panel, shown in [Figure 2-4](#apple-gi4tonbq)
, the user can select the preferences for the system fonts in a theme. Note that the Appearance Manager distinguishes between large and small system fonts, as well as providing the user with the option to choose a separate views font for lists and labels, such as those used in Finder windows.

__Figure 2-4__  

The Fonts pane of the Appearance control panel

!

As shown in [Figure 2-5](#apple-geytombw)
, the user can change the current desktop picture or pattern via the Desktop pane of the Appearance control panel.

__Figure 2-5__  

The Desktop pane of the Appearance control panel

!

[Figure 2-6](#apple-gi3tqmby)
shows the Sound pane of the Appearance control panel. Users can choose a "sound track" for any or all interface aspects in the current theme, or they can choose to eliminate interface sounds from the theme entirely.

__Figure 2-6__  

The Sound pane of the Appearance control panel

!

In the Options pane of the Appearance control panel, shown in [Figure 2-7](#apple-gi4tonbz)
, the user can select scroll bar preferences and choose the window collapsing behavior for a theme.

When the user selects Smart Scrolling, double scroll bar arrows are used at one end of a scroll bar. For vertical scroll bars, the double arrows are located at the lower end of the scroll bar. For horizontal scroll bars, the double arrows are located at the right end of the scroll bar. The scroll box (also known as a "scroll indicator" or "thumb") is proportional in size to the amount of a window's visible content with smart scrolling.

If the user does not select smart scrolling, a single scroll bar arrow is used at each end of a scroll bar and the scroll box is of fixed size.

__Figure 2-7__  

The Options pane of the Appearance control panel

!

While the Appearance control panel allows users to adapt their experience of the system's look and sound, some programs may also wish to set their own theme preferences, thus creating a custom theme environment in which to run. This is useful for some programs, such as games, that need to control the entire user environment while they are active. See [Creating Custom Themes](Creating%20Custom%20Themes.md#apple-gmydenjz)
for more details on this process.

The Appearance Manager saves the preferences that describe a theme in a theme file in the System Folder. The Appearance Manager provides the following functions for working with theme files:

- 

  GetTheme
  obtains a collection containing data describing the current theme.
- 

  SetTheme
  sets a specified collection as the current theme.
- 

  IterateThemes
  iterates over all themes installed on a system.
- 

  IsValidAppearanceFileType
  returns whether the system can interpret files of a given file type as appearance files.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.2.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.2.md) [![Next](attachments/Concepts/images/next.gif)](Appearance.4.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
