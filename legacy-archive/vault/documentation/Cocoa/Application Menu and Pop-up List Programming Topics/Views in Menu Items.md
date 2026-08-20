---
title: Application Menu and Pop-up List Programming Topics
apple_id: 10000032i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/Articles/ViewsInMenuItems.html
archived_at: '2026-07-15T07:16:46.237966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Menu and Pop-up List Programming Topics](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)


[Next](Document%20Revision%20History.md)[Previous](Displaying%20a%20Contextual%20Menu.md)

# Views in Menu Items

You can set the view for a menu item using `NSMenuItem`'s [setView:](https://developer.apple.com/documentation/appkit/nsmenuitem/1514835-view) method (by default, a menu item has a `nil` view)—note, though, that menu item views are not supported in the Dock menu. The following code fragment illustrates how you can create a new menu and add it to your application’s menu bar

```
NSMenuItem* menuBarItem = [[NSMenuItem alloc]
                        initWithTitle:@"Custom" action:NULL keyEquivalent:@""];
// title localization is omitted for compactness
NSMenu* newMenu = [[NSMenu alloc] initWithTitle:@"Custom"];
[menuBarItem setSubmenu:newMenu];
[[NSApp mainMenu] insertItem:menuBarItem atIndex:3];

/*
 Assume that myView1 and myView2 are existing view objects;
 for example, you may have created them in a NIB file.
 */
NSMenuItem* newItem;
newItem = [[NSMenuItem alloc]
               initWithTitle:@"Custom Item 1"
               action:@selector(menuItem1Action:)
               keyEquivalent:@""];
[newItem setView: myView1];
[newItem setTarget:self];
[newMenu addItem:newItem];

newItem = [[NSMenuItem alloc]
               initWithTitle:@"Custom Item 2"
               action:@selector(menuItem2Action:)
               keyEquivalent:@""];
[newItem setView: myView2];
[newItem setTarget:self];
[newMenu addItem:newItem];
```

A menu item with a view does not draw its title, state, font, or other standard drawing attributes, and assigns drawing responsibility entirely to the view. Keyboard equivalents and type-select continue to use the key equivalent and title as normal.

A view in a menu item can receive all mouse events as normal, but keyboard events are not supported. During “non-sticky” menu tracking (that is, manipulating menus with the mouse button held down), a view in a menu item receives `mouseDragged:` events.

You can add animation to a menu item view as you would any other view (you set a timer to call [setNeedsDisplay:](https://developer.apple.com/documentation/appkit/nsview/1483360-needsdisplay) or [display](https://developer.apple.com/documentation/appkit/nsview/1483487-display)), but because menu tracking occurs in the `NSEventTrackingRunLoopMode`, you must add the timer to the run loop in that mode.

When the menu is opened, the view is added to a window; when the menu is closed the view is removed from the window. If you are using a custom view, you can therefore override [viewDidMoveToWindow](https://developer.apple.com/documentation/appkit/nsview/1483329-viewdidmovetowindow) as a convenient place to start or stop animation, reset tracking rectangles and so on, but you should not attempt to move or otherwise modify the window

A menu item with a view sizes itself according to the view's frame, and the width of the other menu items. The menu item will always be at least as wide as its view, but it may be wider. If you want your view to auto-expand to fill the menu item, then make sure that its autoresizing mask has `NSViewWidthSizable` set. A menu item will resize itself as the view's frame changes, but resizing during menu tracking is not supported.

When a menu item is copied using `NSCopying`, any attached view is copied using archiving and unarchiving.

[Next](Document%20Revision%20History.md)[Previous](Displaying%20a%20Contextual%20Menu.md)

