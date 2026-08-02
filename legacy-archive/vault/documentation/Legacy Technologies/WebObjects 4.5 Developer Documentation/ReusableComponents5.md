---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ReusableComponents5.html
archived_at: '2026-07-15T08:06:05.129783Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Creating%20Reusable%20Components.md) [!Previous Section](ReusableComponents4.md)

## Disabling Component Synchronization

Component synchronization can sometimes lead to values being set when you don't want them to be set. You have no control over when, or how often a value is passed to and from the parent.
For these reasons, component synchronization can be disabled. When components are not synchronized, they behave more like dynamic elements in that a value is not resolved with the parent component's settings until that value is needed.
To disable component synchronization, override the method __synchronizesVariablesWithBindings__ in the reusable component's code file to return NO or __false__.
With component synchronization disabled, you must get values from the parent and set values in the parent yourself. The method __valueForBinding:__ gets a value from the parent, and the method __setValue:forBinding:__ (__setValueForBinding__ in Java) set a value in the parent. The argument that you pass to these methods is the name of one of the reusable component's attributes.
For example, consider a reusable component named NonSyncComponent that you declare in a parent component in this way:

```
//parent component's .wod file
Childcomponent : NonSyncComponent {
    stringValue = @"I'm a string!";
}
```


Suppose NonSyncComponent contains a WOTextField element that it declares in this way:

```
// NonSyncComponent.wod
MyString : WOTextField {
    value = someStringValue;
}
```


If NonSyncComponent's script file looks like the following, the value that the parent bound to the __stringValue__ attribute is resolved with WOString's __value__ attribute whenever WOString requests its __value__ attribute. Thus, the WOString in this NonSyncComponent displays "I'm a string!"

```
// NonSyncComponent.wos
- synchronizesVariablesWithBindings {
    return NO;
}

- someStringValue {
    return [self valueForBinding:@"stringValue"];
}

- setSomeStringValue:aValue {
    [self setValue:aValue forBinding:@"stringValue"];
}
```


If NonSyncComponent has no other need for __someStringValue__ than to resolve the __value__ attribute for its WOString, then NonSyncComponent can instead use this shorthand notation in its declarations file:

```
// Alternate NonSyncComponent.wod
MyString : WOString {
    value = ^stringValue;
}
```


The carat (^) syntax means "use the value that my parent bound to my __stringValue__ attribute." This syntax is a convenience that saves you from having to always write cover methods for __valueForBinding:__ and __setValue:forBinding:__. In addition to being more convenient, this syntax is often more efficient because none of your code is invoked to do either the pushing or the pulling.

[!Table of Contents](Creating%20Reusable%20Components.md) [!Next Section](Creating%20a%20-Container-%20Reusable%20Component.md)
