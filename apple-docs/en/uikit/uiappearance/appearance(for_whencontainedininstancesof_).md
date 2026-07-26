---
title: 'appearance(for:whenContainedInInstancesOf:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiappearance/appearance(for:whencontainedininstancesof:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiappearance/appearance(for:whencontainedininstancesof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiappearance/appearance%28for%3Awhencontainedininstancesof%3A%29.json'
content_hash: 'sha256:76bce9fc108619fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAppearance](../uiappearance.md)

# appearance(for:whenContainedInInstancesOf:)

<sub>Type Method</sub>

Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func appearance(for trait: UITraitCollection, whenContainedInInstancesOf containerTypes: [any UIAppearanceContainer.Type]) -> Self
```

## Parameters

- `trait` — The trait collection to use for matching.

- `containerTypes` — An array of appearance container classes, in ascending hierarchical order.

## Return Value

The appearance proxy to use for the object.

## Discussion

Set the `containerTypes` array to an ascending hierarchical list of containing types for the trait collection. For example, if you want a navigation bar to take on a specific appearance when contained in a navigation controller inside a tab bar controller, set `containerTypes` to `[UINavigationController.self, UITabBarController.self]` (Swift) or `@[[UINavigationController class], [UITabBarController class]]` (Objective-C).

Do not set `containerTypes` to an unrelated list of types or to a list that does not match the containment hierarchy of your user interface.

## See Also

### Working with the appearance proxy

- [+ appearance](<appearance().md>) — Returns the appearance proxy for the receiver.
- [+ appearanceForTraitCollection:](<appearance(for_).md>) — Returns the appearance proxy for the receiver that has the passed trait collection.
- [+ appearanceWhenContainedInInstancesOfClasses:](<appearance(whencontainedininstancesof_).md>) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
