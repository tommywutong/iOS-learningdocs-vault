---
title: Application Menu and Pop-up List Programming Topics
apple_id: 10000032i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/Articles/RemovingMenu.html
archived_at: '2026-07-15T07:16:45.237817Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Menu and Pop-up List Programming Topics](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)


[Next](Setting%20a%20Menu%20Item%E2%80%99s%20Key%20Equivalent.md)[Previous](Enabling%20Menu%20Items.md)

# Removing a Menu

To remove a menu item from a menu, you send [removeItem:](https://developer.apple.com/documentation/appkit/nsmenu/1518257-removeitem) or [removeItemAtIndex:](https://developer.apple.com/documentation/appkit/nsmenu/1518207-removeitematindex) to the `NSMenu` object managing the menu item.

To remove an entire menu from the menu bar, you use the same technique. The menus in the menu bar are themselves items of another menu: the root menu, or main menu. To get the main menu, send [mainMenu](https://developer.apple.com/documentation/appkit/nsapplication/1428634-mainmenu) to [NSApp](https://developer.apple.com/documentation/appkit/nsapp), the global application instance. Then send `removeItem:` to the main menu; or find the index of the menu to be removed and send `removeItemAtIndex:` to the main menu. Listing 1 illustrates the latter procedure.

__Listing 1__  Removing a menu from the menu bar

```objc
- (IBAction)removeMenu:(id)sender {
    NSMenu* rootMenu = [NSApp mainMenu];
    // sender is an NSMenuItem
    [rootMenu removeItemAtIndex:[rootMenu indexOfItemWithSubmenu:[sender menu]]];
}
```

[Next](Setting%20a%20Menu%20Item%E2%80%99s%20Key%20Equivalent.md)[Previous](Enabling%20Menu%20Items.md)

