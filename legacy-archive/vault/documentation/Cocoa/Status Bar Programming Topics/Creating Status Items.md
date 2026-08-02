---
title: Status Bar Programming Topics
apple_id: 10000073i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/StatusBar/Tasks/creatingitems.html
archived_at: '2026-07-15T07:19:23.149873Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Status Bar Programming Topics](Introduction%20to%20Status%20Bars.md)


[Next](Document%20Revision%20History.md)[Previous](About%20Status%20Bars.md)

# Creating Status Items

You obtain the system status bar with the [systemStatusBar](https://developer.apple.com/documentation/appkit/nsstatusbar/1530619-system) class method; do not allocate an instance yourself. Invoke [statusItemWithLength:](https://developer.apple.com/documentation/appkit/nsstatusbar/1532895-statusitem) to create a new status item and allocate space for it in the menu bar. Pass the amount of space in pixels you need to display your status item. You can use the constants `NSSquareStatusItemLength` or `NSVariableStatusItemLength` to make the width the same as the status bar’s thickness (as returned by the method [thickness](https://developer.apple.com/documentation/appkit/nsstatusbar/1534591-thickness)) or variable based on the contents of the item, respectively. Use the former if you are displaying an icon and the latter if you are displaying static text.

Because the system status bar is shared by all applications, it cannot retain references to each application’s status item objects. Instead, each application is responsible for retaining its own status items. Each status item then communicates with the status bar as its configuration changes. When deallocated, the status item removes itself from the status bar. Following normal Cocoa [memory management](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27) rules, you must retain the object returned by `statusItemWithLength:` to keep it around.

Once you have the new status item object, you can assign it a title, a menu, a target-action, a tool tip, and so on.

In the following example, a status item is added to the menu bar and assigned a menu.

```objc
- (void)activateStatusMenu
{
    NSStatusBar *bar = [NSStatusBar systemStatusBar];

    theItem = [bar statusItemWithLength:NSVariableStatusItemLength];
    [theItem retain];

    [theItem setTitle: NSLocalizedString(@"Tablet",@"")];
    [theItem setHighlightMode:YES];
    [theItem setMenu:theMenu];
}
```

In this code example, assume your object has an instance variable, `theMenu`, that holds an NSMenu object, perhaps unarchived from a nib file. Another instance variable, `theItem`, holds the status item, which is retained. When you execute this code, a menu titled “Tablet” (or a localized version if available) is added to the right side of the menu bar. The menu is available from within every application as long as your application is running and the status item exists.

[Next](Document%20Revision%20History.md)[Previous](About%20Status%20Bars.md)

