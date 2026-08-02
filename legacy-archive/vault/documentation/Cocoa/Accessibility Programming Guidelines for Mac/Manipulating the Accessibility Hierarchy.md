---
title: Accessibility Programming Guidelines for Mac
apple_id: 10000118i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Accessibility/cocoaAXManipulateHierarchy/cocoaAXManipulateHier.html
archived_at: '2026-07-15T05:25:25.765515Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Mac](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Supporting%20Actions.md)

# Manipulating the Accessibility Hierarchy

As described in [The Accessibility Hierarchy](Accessibility%20Objects%20and%20the%20Accessibility%20Hierarchy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2toljxge3dgoa), some accessibility objects are uninteresting to assistive applications and are designated as ignored. An ignored accessibility object is never exposed to an assistive application, but it does participate in the accessibility hierarchy. As you develop your Cocoa application, you may find that you need to adjust the accessibility hierarchy to present a cleaner representation to assistive applications. This article describes how to manipulate the accessibility hierarchy.

Any object indicates that it should not be visible to assistive applications by implementing the `accessibilityIsIgnored` method and returning `YES`. Because an ignored object still participates in the internal parent-child hierarchy, however, it must implement the `NSAccessibilityParentAttribute` and `NSAccessibilityChildrenAttribute` attributes to provide a link between the objects above and below it.

When an attribute value, hit-test, or focus test would otherwise return an ignored object, the object must be replaced by an unignored object. Depending on the situation, the object should be replaced either by an ancestor or by one or more descendants. The search for replacement objects iterates through the internal hierarchy until all ignored objects are eliminated. For example, when an object’s children are requested, a child that is ignored is replaced by the child’s children. If one of those children is also ignored, it is replaced by its children, and so on. Likewise, when asking for an object’s parent, an ignored parent is skipped and the first unignored ancestor is returned.

To help manage ignored objects, Cocoa provides several functions that perform the necessary search-and-replace procedures. The following two functions test whether the given object is ignored and returns either that object, if not ignored, or the first unignored parent (ancestor) or child (descendant), if the object is ignored:

```
id NSAccessibilityUnignoredDescendant(id element);
id NSAccessibilityUnignoredAncestor(id element);
```

You use these utility functions to ensure that you return an unignored object in response to, for example, a request for the value of the `NSAccessibilityChildrenAttribute` attribute. The `NSAccessibilityUnignoredDescendant` function returns the first unignored object it finds as it checks the accessibility object passed to it and works its way down the object’s descendant chain. If an ignored object has either no unignored children or multiple unignored children, this function fails and returns `nil`.

This does not mean that you should return `nil` in response to a hit-testing or focus-testing method, however. For hit-testing and focus-testing, you should return either an unignored child or `self`.

Similarly, the `NSAccessibilityUnignoredAncestor` function returns the first unignored object it finds as it checks the accessibility object passed to it and works its way up the object’s ancestor chain.

Cocoa also provides the following two convenience functions that replace ignored objects with their unignored children:

```
NSArray *NSAccessibilityUnignoredChildren(NSArray *originalChildren);
NSArray *NSAccessibilityUnignoredChildrenForOnlyChild(id originalChild);
```

The `NSAccessibilityUnignoredChildren` function takes a set of accessibility objects and replaces any ignored objects with their children, recursing if necessary. The `NSAccessibilityUnignoredChildrenForOnlyChild` function replaces a single child with its unignored children. It is equivalent to the following usage of the `NSAccessibilityUnignoredChildren` function:

```
NSAccessibilityUnignoredChildren( [NSArray arrayWithObject:originalChild] )
```

You can use these convenience functions to make it easier to respect the ignored status of the accessibility objects you return to assistive applications. Listing 1 shows one way to do this.

__Listing 1__  Returning attribute values for unignored children

```objc
- (id)accessibilityAttributeValue:(NSString *)attribute
{
    if ( [attribute isEqualToString:NSAccessibilityChildrenAttribute] )
        return NSAccessibilityUnignoredChildren( _children );

    else if ( [attribute isEqualToString:NSAccessibilityParentAttribute] )
        return NSAccessibilityUnignoredAncestor( _parent );

    else
        return [super accessibilityAttributeValue:attribute];
}
```

In the code in Listing 1, __children_ and __parent_ represent the objects immediately above and below the given object, regardless of their ignored status. For an NSView object, for example, these are the subviews and superview, respectively.

[Next](Document%20Revision%20History.md)[Previous](Supporting%20Actions.md)

