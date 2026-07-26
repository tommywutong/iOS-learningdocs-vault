---
title: 'applying(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/configuration-swift.class/applying(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/configuration-swift.class/applying(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/configuration-swift.class/applying%28_%3A%29.json'
content_hash: 'sha256:1574f7c84779845b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [Configuration](../configuration-swift.class.md)

# applying(_:)

<sub>Instance Method</sub>

Returns a configuration object that applies the specified configuration values on top of the current object’s values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func applying(_ otherConfiguration: UIImage.Configuration?) -> Self
```

## Parameters

- `otherConfiguration` — The configuration attributes to apply over the current attributes. Values in this object take precedence over values in the image’s current configuration object.

## Return Value

A configuration object with the specified image configuration attributes and merged traits.

## Discussion

This method merges the traits from `otherConfiguration` with the current object’s trait collection, giving precedence to traits in `otherConfiguration` unless the trait is unspecified. For image-specific traits, this method replaces the current image attributes with the attributes in `otherConfiguration`.

## See Also

### Modifying a configuration object

- [- configurationWithTraitCollection:](<withtraitcollection(__).md>) — Returns a new configuration object that merges the current traits with the traits from the specified trait collection.
