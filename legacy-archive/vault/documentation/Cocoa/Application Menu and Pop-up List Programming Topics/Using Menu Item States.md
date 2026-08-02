---
title: Application Menu and Pop-up List Programming Topics
apple_id: 10000032i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/Articles/MenuItemStates.html
archived_at: '2026-07-15T07:16:45.002468Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Menu and Pop-up List Programming Topics](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)


[Next](Enabling%20Menu%20Items.md)[Previous](How%20Menus%20Work.md)

# Using Menu Item States

Menu items can have a state: on (`NSOnState`), off (`NSOffState`), or mixed (`NSMixedState`). These are useful if the menu item represents a setting in your application. The menu item automatically displays its state, as follows. If the state is `NSOnState`, a checkmark appears beside it. If the state is `NSMixedState`, a dash appears beside it. If the state is `NSOffState`, nothing appears beside it. To set the menu item’s state, use [setState:](https://developer.apple.com/documentation/appkit/nsmenuitem/1514804-state).

The mixed state is useful if the setting is true for only some items in the application or the current selection. For example, if some of the selected characters in a word processor document are italic and others are not, the Italic menu item would have a dash beside it. If the menu item is in the mixed state, then choosing it should cycle through all three states. Going back to the mixed state should leave the selection as it was.

You can use states to implement a group of mutually exclusive menu items, much like a group of radio buttons. For example, a game could have three menu items to show the level of play: Beginner, Intermediate, and Advanced. To implement a such a group, create one action message that they all use. This action message changes the appropriate setting, and then reflects that change by unchecking the currently checked item and checking the newly selected item.

In an action method that responds to all commands in the group use `setState:` to uncheck the menu item that is currently marked:

```
[currentItem setState:NSOffState];
```

Then mark the newly selected command:

```
[sender setState:NSOnState];
```

[Next](Enabling%20Menu%20Items.md)[Previous](How%20Menus%20Work.md)

