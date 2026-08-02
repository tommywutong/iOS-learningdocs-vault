---
title: Text Programming Guide for iOS
apple_id: TP40009542
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/AddingCustomEditMenuItems/AddingCustomEditMenuItems.html
archived_at: '2026-07-18T02:06:52.930809Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Programming Guide for iOS](About%20Text%20Handling%20in%20iOS.md)


[Next](Using%20Text%20Kit%20to%20Draw%20and%20Manage%20Text.md)[Previous](Custom%20Views%20for%20Data%20Input.md)

# Displaying and Managing the Edit Menu

The edit menu is a contextual menu that is displayed to offer commands that can be performed on a selection such as a word in a text view or an image. The edit menu is an integral part of copy, cut, and paste operations, for which it displays (potentially) the commands Copy, Cut, Paste, Select, and Select All. However, you can add custom menu items to the edit menu to perform other kinds of actions on selections.

To copy or cut something in a view, or to do anything else with it, that “something” must be selected. It can be a range of text, an image, a URL, a color, or any other representation of data, including [custom objects](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassDefinition.html#//apple_ref/doc/uid/TP40008195-CH6). You must manage the selection of objects in that view yourself. If the user selects an object in the view by making a certain touch gesture (for example, a double-tap) you must handle that event, internally record the selection (and deselect any previous selection), and perhaps visually indicate the new selection in the view. If it is possible for users to select multiple objects in your view for copy-cut-paste operations, you must implement that multiple-selection behavior.

When your app determines that the user has requested the edit menu—which could be the action of making a selection—you should complete the following steps to display the menu:

1. Call the [sharedMenuController](https://developer.apple.com/documentation/uikit/uimenucontroller/1622831-sharedmenucontroller) class method of [UIMenuController](https://developer.apple.com/documentation/uikit/uimenucontroller) to get the [global](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Singleton.html#//apple_ref/doc/uid/TP40008195-CH49) menu-controller instance.
2. Compute the boundaries of the selection and with the resulting rectangle call the [setTargetRect:inView:](https://developer.apple.com/documentation/uikit/uimenucontroller/1622812-settargetrect) method. The edit menu is displayed above or below this rectangle, depending how close the selection is to the top or bottom of the screen.
3. Call the [setMenuVisible:animated:](https://developer.apple.com/documentation/uikit/uimenucontroller/1622819-setmenuvisible) method (with `YES` for both arguments) to animate the display of the edit menu above or below the selection.

Listing 7-1 illustrates how you might display the edit menu in an implementation of the [touchesEnded:withEvent:](https://developer.apple.com/documentation/uikit/uiresponder/1621084-touchesended) method for handling copy, cut, and paste operations. (Note that the example omits the section of code that handles the selection.) This code snippet also shows the custom view sending itself a [becomeFirstResponder](https://developer.apple.com/documentation/uikit/uiresponder/1621113-becomefirstresponder) message to ensure that it is the first responder for the subsequent copy, cut, and paste operations.

__Listing 7-1__  Displaying the edit menu

```objc
- (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *theTouch = [touches anyObject];

    if ([theTouch tapCount] == 2  && [self becomeFirstResponder]) {

        // selection management code goes here...

        // bring up edit menu.
        UIMenuController *theMenu = [UIMenuController sharedMenuController];
        CGRect selectionRect = CGRectMake (currentSelection.x, currentSelection.y, SIDE, SIDE);
        [theMenu setTargetRect:selectionRect inView:self];
        [theMenu setMenuVisible:YES animated:YES];

    }
}
```

The menu initially includes all commands for which the first responder has corresponding `UIResponderStandardEditActions` method implementations (`copy:`, `paste:`, and so on). Before the menu is displayed, however, the system sends a [canPerformAction:withSender:](https://developer.apple.com/documentation/uikit/uiresponder/1621105-canperformaction) message to the first responder, which in many cases is the custom view itself. In its implementation of this method, the responder evaluates whether the command (indicated by the [selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) in the first argument) is applicable in the current context. For example, if the selector is `paste:` and there is no data in the pasteboard of a type the view can handle, the responder should return `NO` to suppress the Paste command. If the first responder does not implement the `canPerformAction:withSender:` method, or does not handle the given command, the message travels up the responder chain.

Listing 7-2 shows an implementation of the `canPerformAction:withSender:` method that looks for message matching the `cut:`, `copy:`, and `paste:` selectors; it enables or disables the Copy, Cut, and Paste menu commands based on the current selection context and, for paste, the contents of the pasteboard.

__Listing 7-2__  Conditionally enabling menu commands

```objc
- (BOOL)canPerformAction:(SEL)action withSender:(id)sender {
    BOOL retValue = NO;
    ColorTile *theTile = [self colorTileForOrigin:currentSelection];

    if (action == @selector(paste:) )
        retValue = (theTile == nil) &&
             [[UIPasteboard generalPasteboard] containsPasteboardTypes:
             [NSArray arrayWithObject:ColorTileUTI]];
    else if ( action == @selector(cut:) || action == @selector(copy:) )
        retValue = (theTile != nil);
    else
        retValue = [super canPerformAction:action withSender:sender];
    return retValue;
}
```

Note that the final `else` clause in this method calls the superclass implementation to give any superclass a chance to handle commands that the subclass chooses to ignore.

Note that a menu command, when acted upon, can change the context for other menu commands. For example, if the user selects all objects in the view, the Copy and Cut commands should be included in the menu. In this case the responder can, while the menu is still visible, call [update](https://developer.apple.com/documentation/uikit/uimenucontroller/1622815-update) on the menu controller; this results in the reinvocation of `canPerformAction:withSender:` on the first responder.

You can add a custom item to the edit menu. When users tap this item, a command is issued that affects the current target in an app-specific way. The UIKit framework accomplishes this through the [target-action mechanism](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3). The tap of an item results in an action message being sent to the first object in the [responder chain](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1) that can handle the message. Figure 7-1 shows an example of a custom menu item (“Change Color”).

__Figure 7-1__  An edit menu with a custom menu item

!

An instance of the [UIMenuItem](https://developer.apple.com/documentation/uikit/uimenuitem) class represents a custom menu item. `UIMenuItem` objects have two [properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13), a title and an action selector, which you can change at any time. To implement a custom menu item, you must [initialize](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) a `UIMenuItem` instance with these properties, add the instance to the menu controller’s array of custom menu items, and then implement the action method for handling the command in the appropriate responder subclass.

Other aspects of implementing a custom menu item are common to all code that uses the [singleton](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Singleton.html#//apple_ref/doc/uid/TP40008195-CH49) [UIMenuController](https://developer.apple.com/documentation/uikit/uimenucontroller) object. In a custom or overridden view, you set the view to be the first responder, get the shared menu controller, set a target rectangle, and then display the edit menu with a call to [setMenuVisible:animated:](https://developer.apple.com/documentation/uikit/uimenucontroller/1622819-setmenuvisible). The simple example in Listing 7-3 adds a custom menu item for changing a custom view’s color between red and black.

__Listing 7-3__  Implementing a Change Color menu item

```objc
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {}
- (void)touchesMoved:(NSSet *)touches withEvent:(UIEvent *)event {}
- (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *theTouch = [touches anyObject];
    if ([theTouch tapCount] == 2) {
        [self becomeFirstResponder];
        UIMenuItem *menuItem = [[UIMenuItem alloc] initWithTitle:@"Change Color" action:@selector(changeColor:)];
        UIMenuController *menuCont = [UIMenuController sharedMenuController];
        [menuCont setTargetRect:self.frame inView:self.superview];
        menuCont.arrowDirection = UIMenuControllerArrowLeft;
        menuCont.menuItems = [NSArray arrayWithObject:menuItem];
        [menuCont setMenuVisible:YES animated:YES];
    }
}
- (void)touchesCancelled:(NSSet *)touches withEvent:(UIEvent *)event {}

- (BOOL)canBecomeFirstResponder { return YES; }

- (void)changeColor:(id)sender {
    if ([self.viewColor isEqual:[UIColor blackColor]]) {
        self.viewColor = [UIColor redColor];
    } else {
        self.viewColor = [UIColor blackColor];
    }
    [self setNeedsDisplay];
}
```


When your implementation of a system or custom command returns, the edit menu is automatically hidden. You can keep the menu visible with the following line of code:

```
[UIMenuController sharedMenuController].menuVisible = YES;
```

The system may hide the edit menu at any time. For example, it hides the menu when an alert is displayed or the user taps in another area of the screen. If you have state or a display that depends on whether the edit menu is visible, you should listen for the notification named `UIMenuControllerWillHideMenuNotification` and take an appropriate action.

[Next](Using%20Text%20Kit%20to%20Draw%20and%20Manage%20Text.md)[Previous](Custom%20Views%20for%20Data%20Input.md)

