---
title: 'appearanceForTraitCollection:whenContainedIn:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（9.0 起废弃）, iPadOS 8.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiappearance/appearancefortraitcollection:whencontainedin:'
source_url: 'https://developer.apple.com/documentation/uikit/uiappearance/appearancefortraitcollection:whencontainedin:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiappearance/appearancefortraitcollection%3Awhencontainedin%3A.json'
content_hash: 'sha256:f65e10edb97f3f4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAppearance](../uiappearance.md)

# appearanceForTraitCollection:whenContainedIn:

<sub>Type Method</sub>

Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) appearanceForTraitCollection:(UITraitCollection *) trait whenContainedIn:(Class<UIAppearanceContainer> *) ContainerClass;
```

## Parameters

- `trait` — The trait collection to use for matching.

- `ContainerClass` — A nil-terminated list of appearance container classes, in ascending hierarchical order.

## Return Value

The appearance proxy to use for the object.

## Discussion

Set the `ContainerClass` array to an ascending hierarchical list of types where the appearance settings should apply when the caller type is contained within them for the trait collection. For example, if you want a `UINavigationBar` to take on a specific appearance when contained in a `UINavigationController` inside a `UITabBarController`, set `ContainerClass` to `@[[UINavigationController class], [UITabBarController class], nil]`.

Do not set `ContainerClass` to an unrelated list of types or to a list that does not match the containment hierarchy of your user interface.

This method throws an exception for any item in the var-args list that is not a Class object that conforms to the `UIAppearanceContainer` protocol.

## See Also

### Working with the appearance proxy

- [+ appearance](<appearance().md>) — Returns the appearance proxy for the receiver.
- [+ appearanceForTraitCollection:](<appearance(for_).md>) — Returns the appearance proxy for the receiver that has the passed trait collection.
- [+ appearanceWhenContainedInInstancesOfClasses:](<appearance(whencontainedininstancesof_).md>) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [+ appearanceForTraitCollection:whenContainedInInstancesOfClasses:](<appearance(for_whencontainedininstancesof_).md>) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.
- [appearanceWhenContainedIn:](appearancewhencontainedin_.md) — Returns the appearance proxy for object when it’s contained in the hierarchy the specified classes describe. _(deprecated)_
