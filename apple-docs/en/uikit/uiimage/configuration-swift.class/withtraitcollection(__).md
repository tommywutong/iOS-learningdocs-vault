---
title: 'withTraitCollection(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/configuration-swift.class/withtraitcollection(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class/withtraitcollection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/configuration-swift.class/withtraitcollection%28_%3A%29.json'
content_hash: 'sha256:5fa8282ff438c72f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Configuration](../configuration-swift.class.md)

# withTraitCollection(_:)

<sub>Instance Method</sub>

Returns a new configuration object that merges the current traits with the traits from the specified trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func withTraitCollection(_ traitCollection: UITraitCollection?) -> Self
```

## Parameters

- `traitCollection` — The traits to insert or apply to the configuration object. The trait values in this parameter take precedence over the ones in the current configuration object, unless you left the trait with an unspecified value.

## Return Value

A configuration object with the merged set of traits.

## Discussion

Use this method to augment or change the traits in the current configuration object. This method prefers the values from `traitCollection` over the values in the current configuration object. If the value of the trait is unspecified in both collections, it remains unspecified in the new collection.

## See Also

### Modifying a configuration object

- [- configurationByApplyingConfiguration:](<applying(__).md>) — Returns a configuration object that applies the specified configuration values on top of the current object’s values.
