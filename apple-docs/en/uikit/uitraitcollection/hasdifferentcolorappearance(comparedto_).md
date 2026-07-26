---
title: 'hasDifferentColorAppearance(comparedTo:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/hasdifferentcolorappearance(comparedto:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/hasdifferentcolorappearance(comparedto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/hasdifferentcolorappearance%28comparedto%3A%29.json'
content_hash: 'sha256:65ca20c08e5b67b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# hasDifferentColorAppearance(comparedTo:)

<sub>Instance Method</sub>

Queries whether changing between the specified and current trait collections would affect color values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func hasDifferentColorAppearance(comparedTo traitCollection: UITraitCollection?) -> Bool
```

## Parameters

- `traitCollection` — A trait collection that you want to compare to the current trait collection.

## Return Value

[true](../../swift/true.md) if the colors in the two trait collections differ, or [false](../../swift/false.md) if they have the same component values.

## Discussion

Use this method to determine whether changing the traits of the current environment would also change the colors in your interface. For example, changing the [userInterfaceStyle](userinterfacestyle.md) or [accessibilityContrast](accessibilitycontrast.md) property usually changes the colors of your interface.

## See Also

### Comparing trait collections

- [- containsTraitsInCollection:](<containstraits(in_).md>) — Queries whether a trait collection contains all of another trait collection’s values. _(deprecated)_
