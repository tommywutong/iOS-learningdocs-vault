---
title: Accessibility Programming Guidelines for Mac
apple_id: 10000118i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Accessibility/cocoaAXSupportingActions/cocoaAXSupportActions.html
archived_at: '2026-07-15T05:25:26.367319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Mac](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Cocoa.md)


[Next](Manipulating%20the%20Accessibility%20Hierarchy.md)[Previous](Supporting%20Attributes.md)

# Supporting Actions

NSAccessibility defines three methods for accessing an object’s actions:

- `accessibilityActionNames`
- `accessibilityActionDescription:`
- `accessibilityPerformAction:`

The first method returns an array of action names supported by the accessibility object, the second returns a localized string describing a particular action, and the third performs a particular action.

When supporting an action in a subclass, you need to override all three methods. In the `accessibilityActionNames` method, you need to invoke the superclass’s implementation and append your new action. This allows an assistive application to get an accurate list of all actions you support. In the other two methods, compare the action name to those your subclass supports; if no match is found, invoke the superclass’s implementation. Listing 1 shows sample implementations of these methods that add a new action named `@"Boing"`.

__Listing 1__  Supporting a new action

```objc
static NSString *MyBoingActionName = @"Boing";

- (NSArray *)accessibilityActionNames
{
    static NSArray *actions = nil;
    if (actions == nil) {
        actions = [[[super accessibilityActionNames]
                arrayByAddingObject:MyBoingActionName] retain];
    }
    return actions;
}

- (NSString *)accessibilityActionDescription:(NSString *)action
{
    if ( [action isEqualToString:MyBoingActionName] )
        return NSLocalizedString(@"BoingDescription",
                    @"Performs the Boing action");
    else
        return [super accessibilityActionDescription:action];
}

- (void)accessibilityPerformAction:(NSString *)action
{
    if ( [action isEqualToString:MyBoingActionName] )
        [self doBoing];
    else
        [super accessibilityPerformAction:action];
}
```

When performing an action, the subclass’s implementation ideally should invoke the same methods that are invoked if the action is performed directly from the user interface.

[Next](Manipulating%20the%20Accessibility%20Hierarchy.md)[Previous](Supporting%20Attributes.md)

