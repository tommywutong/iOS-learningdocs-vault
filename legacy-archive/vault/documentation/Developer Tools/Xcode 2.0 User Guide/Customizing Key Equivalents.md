---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/custom_key_equivalents/custom_key_equivalents.html
archived_at: '2026-07-15T07:29:07.326613Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Xcode%20Preferences.md)[Previous](Customizing%20Xcode.md)

# Customizing Key Equivalents

Xcode lets you change the Command-key equivalents
for its menu items and lets you change the keyboard equivalents
for common editing tasks, such as paging through a document or moving
the cursor. You can choose a pre-defined set of key bindings for menu
items and other tasks, or create your own set. The pre-defined sets
include sets that mimic BBEdit, Metrowerks CodeWarrior, and MPW.

To work with key bindings, choose Preferences from the Xcode
menu, then click Key Bindings. Figure 38-1 shows the Key
Bindings preferences pane, with the key equivalents for the Xcode
menu visible. Menu item key equivalents do not require the Command
key.

You can use the pop-up menu and buttons to choose a predefined
set of key bindings, copy one of the supplied sets and delete sets
you have created. Use the Duplicate button to copy the set that
is currently selected in the Key Binding Sets pop-up menu. You cannot edit
any of the Xcode’s preexisting key bindings sets; to customize
key bindings, duplicate an existing set and modify the copy. Use
the Delete button to delete the currently selected set. You can’t
delete a supplied set, only a set you have created or copied.

__Figure 38-1__  The Key Bindings pane in the Xcode
Preferences window

!

Figure 38-2 shows the supplied sets provided in the Key
Binding Sets pop-up menu, including sets that mimic the menu and
shortcut equivalents of Metrowerks CodeWarrior, and other popular
Macintosh IDEs and text editors.

__Figure 38-2__  Supplied sets of key bindings

!

The Menu Key Bindings pane provides access to almost all of
the menus and menu items in Xcode. The Text Key Bindings pane, which
provides access to key equivalents for common editing tasks, is
described in [Customizing Keyboard Equivalents for Other Tasks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqsdivfekqsd).

Xcode currently lists key equivalents using the traditional
menu glyphs shown in Figure 38-3 (not all glyphs
are shown).

__Figure 38-3__  Some of the glyphs for available
key equivalents

!

The following steps describe how to create a custom set of
key bindings, based on the supplied CodeWarrior set, and how to
add a menu item key equivalent. In this example, the equivalent
automatically opens the release notes, an option available from
the Help menu.

1. Navigate
   to the Key Bindings pane in the Preferences window:

   Xcode >
   Preferences, then click Key Bindings.
2. Choose Metrowerks Compatible in the Key Binding Sets pop-up
   menu, as shown in Figure 38-2.
3. Click the Duplicate button to create a copy of that set. When
   prompted for a name for the set, type `My Custom
   Keys`.
4. Click the Menu Key Bindings tab.
5. Scroll to the Help menu and click the disclosure triangle
   in the Action column to open the menu. Figure 38-4 shows the Help
   menu actions.

   __Figure 38-4__  The Help menu commands

   !
6. Double-click in the Key column next to the Show Release Notes
   menu item to open an editing field, then type Command-Control-H
   (holding the keys down simultaneously). The result is shown in Figure 38-5.

   If
   you try to assign a key equivalent that is already assigned to another
   action in the current key binding set, Xcode displays a message
   indicating which action it is assigned to below the key bindings
   table.

   Note that Xcode displays the letter “h” in
   its capitalized form. Whether or not you include the Shift key as
   part of a menu key equivalent, Xcode shows letters as they appear
   in menus (as capitals).

   You can use the - button (shown
   in Figure 38-5) to clear a menu key equivalent. You can
   use the + button to assign multiple equivalents to a single action
   (where you can use any of the equivalents to initiate the action).

   __Figure 38-5__  Editing the menu key equivalent for
   the Show Release Notes menu item

   !
7. You can repeat the previous step to add or change other menu
   key equivalents.
8. Click the Apply button to apply your changes.
9. You can now type Command-Control-H to choose the Show Release
   Notes menu item, which opens the release notes from the Help menu.
   If you open the Help menu, you will see the keystroke glyphs shown
   in Figure 38-5 next to the Show Release Notes menu item.

You can customize keyboard equivalents for tasks such as editing
and formatting text, cursor movement, and project navigation using
steps similar to those described for menu items in [Customizing Command-Key Equivalents for Menu Items](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqsdjfbesrsg). You can start by copying
one of the predefined sets of key bindings shown in [Figure 38-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqsdjbaucrcg). In
addition to its default settings, Xcode provides sets that are compatible
with BBEdit, Metrowerks CodeWarrior, and MPW.

Figure 38-6 shows the contents of the Text Key Bindings
pane, with some of the key equivalents for Text Editing actions
visible. The current set is the My Custom Keys set, created in [Customizing Command-Key Equivalents for Menu Items](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqsdjfbesrsg).

__Figure 38-6__  Text Key Bindings in the Preferences
window

!

The following steps show how to set a shortcut for the Capitalize
Word action:

1. Navigate
   to the Key Bindings pane in the Preferences window: Xcode > Preferences, then
   click Key Bindings.
2. Choose My Custom Keys (created previously in [Customizing Command-Key Equivalents for Menu Items](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgawueqsdjfbesrsg)) in the Key Binding Sets pop-up menu.
3. Click the Text Key Bindings button.
4. Double-click in the Keys column next to the Capitalize Word
   item to open an editing field, then type Control-Shift-C (holding
   the keys down simultaneously). The result is shown in Figure 38-7.

   You
   can use the - button (shown in Figure 38-5) to clear a keyboard
   equivalent. You can enter more than one key combination for an action
   by clicking the + button.

   __Figure 38-7__  Editing
   the Text Editing shortcut for Capitalize Word

   !
5. You can repeat the previous step to add or change other keyboard
   equivalents for editing actions (or other actions not shown here).
6. Click the Apply button to apply your changes.
7. You can now type Control-Shift-C to capitalize the currently
   selected word in a project.

[Next](Xcode%20Preferences.md)[Previous](Customizing%20Xcode.md)

