---
title: User Interface Validation
apple_id: 10000040i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-07-10'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UIValidation/Articles/ValidatingObjects.html
archived_at: '2026-07-15T07:20:56.305910Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [User Interface Validation](Introduction%20to%20User%20Interface%20Validation.md)


[Next](Document%20Revision%20History.md)[Previous](Implementing%20Validation.md)

# Implementing a Validated Item

`NSValidatedUserInterfaceItem` is used by the Application Kit’s standard user interface validation mechanism, and must be implemented by validated objects.

Validated objects send `validateUserInterfaceItem:` to validators that can be determined by `NSApplication`’s `targetForAction:to:from:`.

You can extend this functionality by introducing a new set of protocol pairs that is targeted to your specific validated objects. `NSMenuItem` protocol is one example extending this validation machinery to allow validators to modify menu items being validated. You can extend UI validation by:

1. Declare a protocol that inherits from `NSValidatedUserInterfaceItem`.

   You can add as many features you want for your validated objects in this protocol, for example:

```objc
@protocol NSValidatedToolbarItem <NSValidatedUserInterfaceItem>
- (NSImage *)image;
- (void)setImage:(NSImage *)theImage
- (NSString *)toolTip;
- (void)setToolTip:(NSString *)theToolTip;
@end
```
2. Declare validation method for validators.

   You should declare the new selector that takes your objects as the argument, for example:

```objc
@protocol NSToolbarItemValidations
- (BOOL)validateToolbarItem:(id <NSValidatedToolbarItem>)theItem;
@end
```
3. Implement your `update` method.

   You should, first, check if your current validator responds to your validation method, then, the generic `validateUserInterfaceItem:`. This way, your object can be automatically enabled/disabled by the Application Kit's standard objects like `NSTextView` without any additional coding, for example:

```objc
- (void)update {
    id validator = [NSApp targetForAction:[self action] to:[self target] from:self];

    if ((validator == nil) || ![validator respondsToSelector:[self action]])
    {
         [self setEnabled:NO];
    }
    else if ([validator respondsToSelector:@selector(validateToolbarItem:)])
    {
        [self setEnabled:[validator validateToolbarItem:self]];
    }
    else if ([validator respondsToSelector:@selector(validateUserInterfaceItem:)])
    {
        [self setEnabled:[validator validateUserInterfaceItem:self]];
    }
    else
    {
         [self setEnabled:YES];
    }
}
```
4. Optionally, implement category methods for standard objects .

   Now you can implement default validation methods for standard objects like `NSTextView` or `NSDocument`, for example:

```objc
@implementation NSTextView (NSToolbarValidation)

- (BOOL)validateToolbarItem:(id <NSValidatedToolbarItem>)theItem
{
    BOOL returnValue = [self validateUserInterfaceItem:theItem];
     // Your own validation
     return returnValue;
}
@end
```

[Next](Document%20Revision%20History.md)[Previous](Implementing%20Validation.md)

