---
title: Accessibility Programming Guidelines for Mac
apple_id: 10000118i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Accessibility/cocoaAXSupportingAttributes/cocoaAXSupportAttributes.html
archived_at: '2026-07-15T05:25:26.373401Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Mac](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Cocoa.md)


[Next](Supporting%20Actions.md)[Previous](Access%20Enabling%20a%20Cocoa%20Application.md)

# Supporting Attributes

This article describes two techniques you can use to support additional attributes and provide values for individual attributes. For more information on why you might need to do this, see [Access Enabling a Cocoa Application](Access%20Enabling%20a%20Cocoa%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tslkciffeuskcizaq).

OS X version 10.4 introduced the `accessibilitySetOverrideValue:forAttribute:` convenience method, which allows you to add an attribute or change the value of an existing attribute without subclassing the accessibility object. Use this method only for adding attributes and supplying values that are unchanging and pertain to the layout of your application, such as titles, descriptions, and links between conceptually related elements.

Don’t use this method to add attributes that should be settable by an assistive application. Attributes you add using the `accessibilitySetOverrideValue:forAttribute:` method are unsettable by default and will remain unsettable even if you subclass the accessibility object and override the `accessibilityIsAttributeSettable:` method. For information on the methods to override to support attributes that can be settable, see Overriding Methods to Support Attributes.

NSAccessibility defines four methods for accessing an object’s attributes:

- `accessibilityAttributeNames`
- `accessibilityAttributeValue:`
- `accessibilityIsAttributeSettable:`
- `accessibilitySetValue:forAttribute:`

The first method returns an array of attribute names supported by the accessibility object. An assistive application uses this method to determine which attributes an accessibility object supports, so it can later get information about specific ones. The other three methods each operate on an individual attribute, querying or setting the attribute’s value.

When supporting an additional attribute in a subclass, you must override the `accessibilityAttributeNames` method and append the attribute to the array of attributes already supported by the superclass. For example, if your accessibility object needs to support the `NSAccessibilityLinkedUIElementsAttribute`, you override this method and insert the attribute into the array. This method is likely to be called numerous times and there could be a large number of attributes, so it should be efficient.

Listing 1 shows an implementation that adds the `@"MyAttribute"` attribute, initializing a static variable with the array of attribute names the first time the method is invoked:

__Listing 1__  Supporting an additional attribute

```objc
static NSString *MyAttributeName = @"MyAttribute";

- (NSArray *)accessibilityAttributeNames
{
    static NSArray *attributes = nil;
    if (attributes == nil) {
        attributes = [[[super accessibilityAttributeNames]
                arrayByAddingObject:MyAttributeName] retain];
    }
    return attributes;
}
```

When a subclass supports an additional attribute, it must also override the methods that can get that attribute’s value, determine if it is settable, and set its value. Listing 2 shows possible implementations for these methods, using the `@"MyAttribute"` attribute added in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3delkcijbuoqkfijea).

__Listing 2__  Supplying information about an added attribute

```objc
- (id)accessibilityAttributeValue:(NSString *)attribute
{
    // Determine if the attribute being asked about is the newly added one.
    if ( [attribute isEqualToString:MyAttributeName] )
        return [NSNumber numberWithInt:_MyAttribute];
    else
        // The attribute in question is not the added one, so let
        // the superclass handle it.
        return [super accessibilityAttributeValue:attribute];
}

- (BOOL)accessibilityIsAttributeSettable:(NSString *)attribute
{
    // Determine if the attribute being asked about is the newly added one.
    if ( [attribute isEqualToString:MyAttributeName] )
        return YES; // YES if MyAttribute is settable, NO if it is not.
    else
        // The attribute in question is not the added one, so let
        // the superclass handle it.
        return [super accessibilityIsAttributeSettable:attribute];
}

- (void)accessibilitySetValue:(id)value
                forAttribute:(NSString *)attribute
{
    // Determine if the attribute being asked about is the newly added one.
    if ( [attribute isEqualToString:MyAttributeName] )
        // Call the subclass’s method to set the attribute’s value.
        [self setMyAttributeValue:[value intValue]];
    else
        // The attribute in question is not the added one, so let
        // the superclass handle it.
        [super accessibilitySetValue:value forAttribute:attribute];
}
```

When setting an attribute, the implementation ideally should invoke the same methods that would have been invoked if the attribute was modified directly from the user interface.

[Next](Supporting%20Actions.md)[Previous](Access%20Enabling%20a%20Cocoa%20Application.md)

