---
title: default()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+（11.0 起废弃）, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uigraphicsrendererformat/default()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrendererformat/default()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrendererformat/default%28%29.json'
content_hash: 'sha256:fc80c9ff27232291'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRendererFormat](../uigraphicsrendererformat.md)

# default()

<sub>Type Method</sub>

Returns a format that represents the highest fidelity that the current device supports.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func `default`() -> Self
```

## Return Value

An initialized format.

## Discussion

The returned format object always represents the device’s highest fidelity, regardless of the actual fidelity currently employed by the device. A graphics renderer uses this method to create a format at initialization time if you use an initializer that does not have a format argument.

This property doesn’t always return a format that’s optimized for the current configuration of the main screen. If you’re rendering content for immediate display, it’s recommended that you use [+ preferredFormat](<preferred().md>) instead of this property.

## See Also

### Creating a format

- [+ preferredFormat](<preferred().md>) — Returns the most suitable format for the main screen’s current configuration.
