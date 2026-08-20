---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.034.html
archived_at: '2026-07-15T07:58:42.135326Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.033.md)

## Non-Synchronizing Components

By default, a nested component pulls all values from its parent and pushes all values to its parent before and after each phase of the request-response loop. This can lead to problems where values are being set when you don't want them set. In addition, the reusability of components is diminished if you must pre-compute everything a nested component needs before using it inside of another component.
The solution to both of these problems is non-synchronizing components. When components are not synchronized, they behave more like dynamic elements in that values are not pushed or pulled until they are needed.
To create a non-synchronizing nested component, do the following:

- Override the __synchronizesVariablesWithBindings__ method to return __NO__ or __false__.
- Use these two methods to push and pull values:

  |  WOComponent |  |
  |  Method |  Description |
  |  valueForBinding: |  Gets (pulls) the value that the parent component bound to the specified attribute. |
  |  setValue:forBinding: (Objective-C)  setValueForBinding (Java) |  Sets (pushes) the value of the variable that the parent component bound to the specified attribute to the specified value. |

```
```


For example, consider a nested component named NonSyncComponent that you declare in a parent component in this way:

```
//parent component's .wod file
MySubcomponent : NonSyncComponent {
    stringValue = @"I'm a string!";
}
```


Suppose NonSyncComponent contains a WOString element that it declares in this way:

```
// NonSyncComponent.wod
MyString : WOString {
    value = someStringValue;
}
```


If NonSyncComponent's script file looks like the following, the value that the parent bound to the __stringValue__ attribute is pushed and pulled to WOString's __value__ attribute whenever WOString requests it. Thus, the WOString in this NonSyncComponent displays "I'm a string!"

```
// NonSyncComponent.wos
- synchronizesVariablesWithBindings {
    return NO;
}

- someStringValue {
    return [self valueForBinding:@"stringValue"];
}

- setSomeStringValue:aValue {
    [self setValue:aValue ForBinding:@"stringValue"];
}
```


If NonSyncComponent has no other need for __someStringValue__ than to resolve the __value__ attribute for its WOString, then NonSyncComponent can instead use this shorthand notation in its declarations file:

```
// Alternate NonSyncComponent.wod
MyString : WOString {
    value = ^stringValue;
}
```


The carat (^) syntax means "use the value that my parent bound to my __stringValue__ attribute to resolve __value__." This syntax is a convenience that saves you from having to always write cover methods for __valueForBinding:__ and __setValue:forBinding:__. In addition to being more convenient, this syntax is often more efficient because none of your code is invoked to do either the pushing or the pulling.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.035.md)
