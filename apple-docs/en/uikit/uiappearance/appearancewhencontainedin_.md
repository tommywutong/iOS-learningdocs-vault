---
title: 'appearanceWhenContainedIn:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+（9.0 起废弃）, iPadOS 5.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiappearance/appearancewhencontainedin:'
source_url: 'https://developer.apple.com/documentation/uikit/uiappearance/appearancewhencontainedin:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiappearance/appearancewhencontainedin%3A.json'
content_hash: 'sha256:ca03a6021930162b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAppearance](../uiappearance.md)

# appearanceWhenContainedIn:

<sub>Type Method</sub>

Returns the appearance proxy for object when it’s contained in the hierarchy the specified classes describe.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) appearanceWhenContainedIn:(Class<UIAppearanceContainer> *) ContainerClass;
```

## Parameters

- `ContainerClass` — A nil-terminated list of appearance container classes, in ascending hierarchical order.

## Return Value

The appearance proxy to use for the object.

## Discussion

Set the `ContainerClass` array to an ascending hierarchical list of containing types. For example, if you want a navigation bar to take on a specific appearance when contained in a navigation controller inside a tab bar controller, set `ContainerClass` to `@[[UINavigationController class], [UITabBarController class], nil]`.

Do not set `ContainerClass` to an unrelated list of types or to a list that does not match the containment hierarchy of your user interface.

This method throws an exception for any item in the var-args list that is not a Class object that conforms to the `UIAppearanceContainer` protocol.

## See Also

### Working with the appearance proxy

- [+ appearance](<appearance().md>) — Returns the appearance proxy for the receiver.
- [+ appearanceForTraitCollection:](<appearance(for_).md>) — Returns the appearance proxy for the receiver that has the passed trait collection.
- [+ appearanceWhenContainedInInstancesOfClasses:](<appearance(whencontainedininstancesof_).md>) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [+ appearanceForTraitCollection:whenContainedInInstancesOfClasses:](<appearance(for_whencontainedininstancesof_).md>) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.
- [appearanceForTraitCollection:whenContainedIn:](appearancefortraitcollection_whencontainedin_.md) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection. _(deprecated)_
