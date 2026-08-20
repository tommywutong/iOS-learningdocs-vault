---
title: Application Menu and Pop-up List Programming Topics
apple_id: 10000032i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/Articles/DisplayContextMenu.html
archived_at: '2026-07-15T07:16:41.680517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Menu and Pop-up List Programming Topics](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)


[Next](Views%20in%20Menu%20Items.md)[Previous](Managing%20Pop-Up%20Buttons%20and%20Pull-Down%20Lists.md)

# Displaying a Contextual Menu

The Application Kit interprets right-mouse-down events and left-mouse-down events modified by the Control key as commands to display a contextual menu for the clicked view. Your view subclasses have several alternative approaches for displaying a contextual menu:

- __Configure in Interface Builder__: Add a standalone (rootless) menu to a nib file and customize it to suit, including the specification of targets and actions. Then connect it to your custom view’s `menu` outlet, which is inherited from [NSView](https://developer.apple.com/documentation/appkit/nsview).
- __Programmatically assign a generic menu__: Override the [defaultMenu](https://developer.apple.com/documentation/appkit/nsview/1483417-defaultmenu) class method of `NSView` to create and return a menu that’s common to all instances of your subclass. This default menu is also accessible via the `NSResponder` [menu](https://developer.apple.com/documentation/appkit/nsresponder/1533094-menu) method unless some other `NSMenu` object has been associated with the view.
- __Programmatically assign an instance-specific menu__: In the custom view’s `initWithFrame:` or `awakeFromNib` methods, create the menu and associate it with the view by using the [setMenu:](https://developer.apple.com/documentation/appkit/nsresponder/1533094-menu) method (`NSResponder`).

After you complete any of these procedures, the Application Kit displays the contextual menu whenever the user left-Control-clicks or right-clicks the view. Note that the Application Kit automatically also validates the menu items of contextual menus, unless you request it not to.

If you need to customize the contextual menu, you can do so by setting an appropriate object as the menu’s delegate and implementing the [menuWillOpen:](https://developer.apple.com/documentation/appkit/nsmenudelegate/1518156-menuwillopen) method to customize the menu as you see fit just before it appears.

If you want your view to display a contextual menu in response to events other than right-mouse clicks and left-mouse-Control clicks, you can directly handle the event message in the appropriate [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) method. For example, if you want users to be able to left-click an image view to get a menu of export options, you would override the [mouseDown:](https://developer.apple.com/documentation/appkit/nsresponder/1524634-mousedown) method. In your implementation of the method, create a menu and then invoke the `NSMenu` class method [popUpContextMenu:withEvent:forView:](https://developer.apple.com/documentation/appkit/nsmenu/1518170-popupcontextmenu), passing in the event object related to the mouse-down event and the view owning the contextual menu. Listing 1 illustrates this approach.

__Listing 1__  Displaying a contextual menu upon receiving a left-mouse event

```objc
- (void)mouseDown:(NSEvent *)theEvent {

    NSMenu *theMenu = [[NSMenu alloc] initWithTitle:@"Contextual Menu"];
    [theMenu insertItemWithTitle:@"Beep" action:@selector(beep:) keyEquivalent:@"" atIndex:0];
    [theMenu insertItemWithTitle:@"Honk" action:@selector(honk:) keyEquivalent:@"" atIndex:1];

    [NSMenu popUpContextMenu:theMenu withEvent:theEvent forView:self];
}
```

Contextual menus, including any menu you pop up with `popUpContextMenu:withEvent:forView:`, automatically insert menu items from any contextual menu plug-ins that the user has installed into the menu. A contextual menu plug-in, which is `CFPlugIn` bundle installed in a `Library/Contextual Menu Items` directory at the appropriate level of the system, enables applications and other forms of software to extend the list of commands found on contextual menus such as the Finder’s. The applications do not have to be running for their items to appear. If you are trying to programmatically display a menu, you might not want those items to appear. The preferred approach for programmatically displaying a non-contextual menu is to create an [NSPopUpButtonCell](https://developer.apple.com/documentation/appkit/nspopupbuttoncell) object, set its menu, and then call send a [attachPopUpWithFrame:inView:](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/1531648-attachpopupwithframe) message to the pop-up button cell.

[Next](Views%20in%20Menu%20Items.md)[Previous](Managing%20Pop-Up%20Buttons%20and%20Pull-Down%20Lists.md)

