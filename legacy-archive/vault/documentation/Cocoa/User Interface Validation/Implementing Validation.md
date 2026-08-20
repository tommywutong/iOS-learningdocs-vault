---
title: User Interface Validation
apple_id: 10000040i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-07-10'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UIValidation/Articles/implementingValidation.html
archived_at: '2026-07-15T07:20:56.808930Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [User Interface Validation](Introduction%20to%20User%20Interface%20Validation.md)


[Next](Implementing%20a%20Validated%20Item.md)[Previous](Introduction%20to%20User%20Interface%20Validation.md)

# Implementing Validation

Before it is displayed, a user interface item checks to see if its target implements `validateUserInterfaceItem:`. If it does, then the enabled status of the item is determined by the return value of the method. You can therefore conditionally enable or disable an item by implementing `validateUserInterfaceItem:` in the target object.

In some situations (typically if you set the target and action in Interface Builder), the target is the object to which the user interface item is connected directly; in other situations (when the user interface item’s target is `nil`—such as if you connected it to First Responder in Interface Builder), the target is the first object in the responder chain that implements its action method. For more details, see “Responder Chain for Action Messages” in _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ > [Event Architecture](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/EventArchitecture/EventArchitecture.html#//apple_ref/doc/uid/10000060i-CH3). In either case, the important thing to realize is that _the target is the object that implements the user interface item’s action method_. (The target is also the object that has the suitable context to know whether the action is appropriate.) Hence _the object that must implement_ `validateUserInterfaceItem:` _is the same object that implements the action method_.

For example, suppose you have a controller object that implements a `paste:` method. When the `paste:` method is invoked, it retrieves a value from the pasteboard and then pastes it into the current selection. It can only do this if there is a valid value on the pasteboard. The controller object therefore also implements `validateUserInterfaceItem:`. The `validateUserInterfaceItem:` checks to see if the pasteboard contains useable data, and if it does it returns `YES` otherwise it returns `NO`. If the pasteboard does not contain useable data, the user interface item is disabled.

If in your application you have more than one controller that implements `paste:`—each responsible for pasting different data—then each should have its own implementation of `validateUserInterfaceItem:` that checks to see if the pasteboard contains data useable by it.

The implementation of `validateUserInterfaceItem:` should follow these steps:

1. To decide whether or not an item should be enabled, you need to know what it will do if the user selects it. The sender implements the `NSValidatedUserInterfaceItem` protocol, so you can find out what tag and action are associated with it. You typically first therefore check to see what _action_ is associated with the item (you need to test for each of the actions you’re interested in).

   Checking the action rather than the tag means you avoid the fragility of having to remember to use the same tag for each user interface element that invokes the same method on the target.
2. If the action is something you’re interested in, then return a Boolean value appropriate for the current context.
3. If the action is not something you’re interested in, then either:

   1. If your superclass implements the validation method (for example, `NSDocument` and `NSObjectController` implement `validateUserInterfaceItem:`), invoke super’s implementation; otherwise
   2. Return a default value (typically `YES`).

The following example illustrates the implementation of `validateUserInterfaceItem:` in a subclass of `NSDocument`.

```objc
- (BOOL)validateUserInterfaceItem:(id <NSValidatedUserInterfaceItem>)anItem
{
    SEL theAction = [anItem action];

    if (theAction == @selector(copy:))
    {
        if ( /* there is a current selection and it is copyable */ )
        {
            return YES;
        }
        return NO;
    } else if (theAction == @selector(paste:))
    {
        if ( /* there is a something on the pasteboard we can use and
                the user interface is in a configuration in which it makes sense to paste */ )
        {
            return YES;
        }
        return NO;
    } else
        /* check for other relevant actions ... */
    }
    // subclass of NSDocument, so invoke super's implementation
    return [super validateUserInterfaceItem:anItem];
}
```

[Next](Implementing%20a%20Validated%20Item.md)[Previous](Introduction%20to%20User%20Interface%20Validation.md)

