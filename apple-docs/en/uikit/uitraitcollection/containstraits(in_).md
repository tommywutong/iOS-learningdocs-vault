---
title: 'containsTraits(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（17.0 起废弃）, iPadOS 8.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitraitcollection/containstraits(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/containstraits(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/containstraits%28in%3A%29.json'
content_hash: 'sha256:9375e4914377c3f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# containsTraits(in:)

<sub>Instance Method</sub>

Queries whether a trait collection contains all of another trait collection’s values.

> [!warning] Deprecated
> Compare values for specific traits in the trait collections instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func containsTraits(in trait: UITraitCollection?) -> Bool
```

## Parameters

- `trait` — A trait collection that you want to compare to the current trait collection.

## Return Value

This method returns [true](../../swift/true.md) if the receiver contains all of the trait values in the trait collection passed in the `trait` parameter, and returns [false](../../swift/false.md) otherwise.

## Discussion

Use this method to compare two standalone trait collections, or to compare the iOS interface environment’s trait collection to a standalone trait collection.

## See Also

### Comparing trait collections

- [- hasDifferentColorAppearanceComparedToTraitCollection:](<hasdifferentcolorappearance(comparedto_).md>) — Queries whether changing between the specified and current trait collections would affect color values.
