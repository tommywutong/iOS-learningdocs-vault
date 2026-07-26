---
title: 'appearance(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiappearance/appearance(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiappearance/appearance(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiappearance/appearance%28for%3A%29.json'
content_hash: 'sha256:6a2ea3015e7b8b34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAppearance](../uiappearance.md)

# appearance(for:)

<sub>Type Method</sub>

Returns the appearance proxy for the receiver that has the passed trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func appearance(for trait: UITraitCollection) -> Self
```

## Parameters

- `trait` — The trait collection used for matching.

## Return Value

The appearance proxy for the receiver.

## See Also

### Working with the appearance proxy

- [+ appearance](<appearance().md>) — Returns the appearance proxy for the receiver.
- [+ appearanceWhenContainedInInstancesOfClasses:](<appearance(whencontainedininstancesof_).md>) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe.
- [+ appearanceForTraitCollection:whenContainedInInstancesOfClasses:](<appearance(for_whencontainedininstancesof_).md>) — Returns the appearance proxy for the object when it’s contained in the hierarchy the specified classes describe and has the specified trait collection.
