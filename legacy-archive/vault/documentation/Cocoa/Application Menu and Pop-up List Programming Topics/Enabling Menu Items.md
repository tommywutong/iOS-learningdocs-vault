---
title: Application Menu and Pop-up List Programming Topics
apple_id: 10000032i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/Articles/EnablingMenuItems.html
archived_at: '2026-07-15T07:16:42.178262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Menu and Pop-up List Programming Topics](Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md)


[Next](Removing%20a%20Menu.md)[Previous](Using%20Menu%20Item%20States.md)

# Enabling Menu Items

By default, every time a user event occurs, `NSMenu` automatically enables and disables each visible menu item. You can also force a menu to update using `NSMenu`’s `update` method.

There are two ways to enable menus:

- [Automatic Menu Enabling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi3dcljxgq3dkmy): `NSMenu` updates every menu item whenever a user event occurs. A menu item is enabled if `NSMenu` can find an appropriate object that responds to the menu item’s action. If you want a menu item to remain disabled even though an object responds to the menu item’s action, define a `validateMenuItem:` method for that object.
- [Manual Menu Enabling](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi3dcljxgqzdonq): You use `setEnabled:` to enable or disable every menu item individually.

To choose a system, use `NSMenu`’s `setAutoenablesItems:` with an argument of `YES` (for automatic menu enabling) or `NO` (for manual menu enabling). Automatic menu enabling is on by default.

When you use automatic menu enabling, `NSMenu` updates the status of every menu item whenever a user event occurs. To update the status of a menu item, `NSMenu` first determines the target of the item and then determines whether the target implements [validateMenuItem:](https://developer.apple.com/documentation/objectivec/nsobject/1518160-validatemenuitem) or [validateUserInterfaceItem:](https://developer.apple.com/documentation/appkit/nsuserinterfacevalidations/1528162-validateuserinterfaceitem) (in that order). In more detail:

- If the menu item’s target is set, then `NSMenu` first checks to see if that object implements the item’s action method. If it does not, then the item is disabled. If the target does implement the item’s action method, `NSMenu` first checks to see if that object implements `validateMenuItem:` or `validateUserInterfaceItem:` method. If it does not, then the menu item is enabled. If it does, then the enabled status of the menu item is determined by the return value of the method.
- If the menu item’s target is not set (that is, if it is `nil`—typically if the menu item is connected to First Responder) and the `NSMenu` object is not a contextual menu, then `NSMenu` uses the responder chain (described in [The Responder Chain](../Cocoa%20Event%20Handling%20Guide/Event%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedglktk4za)) to determine the target. If there is no object in the responder chain that implements the item’s action, the item is disabled.

  If there is an object in the responder chain that implements the item’s action, `NSMenu` then checks to see if that object implements the `validateMenuItem:` or `validateUserInterfaceItem:` method. If it does not, then the menu item is enabled. If it does, then the enabled status of the menu item is determined by the return value of the method.
- If the menu item’s target is not set and the `NSMenu` object _is_ a contextual menu, `NSMenu` goes through the same steps as before but the search order for the responder chain is different:

  1. The responder chain for the window in which the view that triggered the context menu resides, starting with the view.
  2. The window itself.
  3. The window’s delegate.
  4. The `NSApplication` object.
  5. The `NSApplication` object’s delegate.

As noted above, before it is displayed a menu item checks to see if its target implements `validateMenuItem:` or `validateUserInterfaceItem:`. If it does, then the enabled status of the menu item is determined by the return value of the method. You can therefore conditionally enable or disable a menu item by implementing either of these methods in the menu’s target (see [Choosing validateMenuItem: or validateUserInterfaceItem:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi3dclktk4yq) to determine which is the most appropriate). The implementation strategy is the same whichever you choose:

1. To decide whether or not an item should be enabled, you need to know what it will do if the user selects it. You typically first therefore check to see what _action_ is associated with the item (you need to test for each of the actions you’re interested in).

   Checking the action rather than, say, the title makes sure that: (a) your code works with different localizations and is robust against changes in the title due to changes in the user interface, and (b) you avoid the fragility of having to remember to use the same tag for each user interface element that invokes the same method on the target. (In the case of `validateUserInterfaceItem:`, you can only check the action or the tag.)
2. If the action is something you’re interested in, then return a Boolean value appropriate for the current context.
3. If the action is not something you’re interested in, then either:

   1. If your superclass implements the validation method (for example, `NSDocument` and `NSObjectController` implement `validateUserInterfaceItem:`, and `NSObjectController` implements `validateMenuItem:`), invoke super’s implementation; otherwise
   2. Return a default value of `YES` to indicate that you handle the validation method, even if you don’t implement the action.

The following example illustrates the implementation of `validateUserInterfaceItem:` in a subclass of `NSDocument`.

```objc
- (BOOL)validateUserInterfaceItem:(id <NSValidatedUserInterfaceItem>)anItem
{
    SEL theAction = [anItem action];

    if (theAction == @selector(copy:)) {
        if ( /* there is a current selection and it is copyable */ )
        {
            return YES;
        }
        return NO;
    }
    else {
        if (theAction == @selector(paste:)) {
            if ( /* there is a something on the pasteboard we can use and
                the user interface is in a configuration in which it makes sense to paste */ ) {
                return YES;
            }
            return NO;
        }
        else {
        /* check for other relevant actions ... */
        }
    }
    // Subclass of NSDocument, so invoke super's implementation
    return [super validateUserInterfaceItem:anItem];
}
```


Typically you should use `validateUserInterfaceItem:` instead of `validateMenuItem:` because the former will also work for toolbar items which have the same target and action. If, however, there is additional work that you want to do that is specific to a menu item, use `validateMenuItem:`—for example, `validateMenuItem:` is also a good place to toggle titles or set state on menu items to make sure they're always correct.

Here is an example of using `validateUserInterfaceItem:` to override automatic enabling. If your application has a Copy menu item that sends the `copy:` action message to the first responder, that menu item is automatically enabled any time an object that responds to `copy:`, such as an `NSText` object, is the first responder of the key or main window. If you create a class whose instances might become the first responder, and which doesn’t support copying of everything it allows the user to select, you should implement `validateUserInterfaceItem:` in that class. `validateUserInterfaceItem:` should then return `NO` if items that can’t be copied are selected (or if no items are selected) and `YES` if all items in the selection can be copied. By implementing `validateUserInterfaceItem:`:, you can have the Copy menu item disabled even though the target object does implement the `copy:` method. If a class never permits copying, then you simply omit an implementation of `copy:` in that class, and the Copy menu item is disabled automatically whenever an instance of that class is the first responder.

When you use manual menu enabling, you use `setEnabled:` to enable or disable every menu item individually. None of the menu items, even those controlled by Application Kit classes like `NSTextView`, are updated automatically.

To turn on manual menu enabling, use `NSMenu`’s `setAutoenablesItems:` with an argument of `NO`.

[Next](Removing%20a%20Menu.md)[Previous](Using%20Menu%20Item%20States.md)

