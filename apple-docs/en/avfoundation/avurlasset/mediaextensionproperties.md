---
title: mediaExtensionProperties
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasset/mediaextensionproperties
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/mediaextensionproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/mediaextensionproperties.json'
content_hash: 'sha256:9cb70c77c77387af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# mediaExtensionProperties

<sub>Instance Property</sub>

The properties of the media extension format reader that decodes the asset.

<sub>macOS</sub>

```swift
var mediaExtensionProperties: AVMediaExtensionProperties? { get }
```

## Discussion

If the system decodes the asset using a MediaExtension format reader, the property value contains a valid object that describes the extension. Otherwise, this property value is `nil`.

## See Also

### Accessing Media Extension properties

- [AVMediaExtensionProperties](../avmediaextensionproperties.md) — An object that describes a Media Extension.
