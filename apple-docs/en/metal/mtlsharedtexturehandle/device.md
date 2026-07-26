---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsharedtexturehandle/device
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedtexturehandle/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedtexturehandle/device.json'
content_hash: 'sha256:5a909fdc24344afd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSharedTextureHandle](../mtlsharedtexturehandle.md)

# device

<sub>Instance Property</sub>

The device object that created the texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

A texture is always associated with the [MTLDevice](../mtldevice.md) that created it and can be used only with that device.

## See Also

### Identifying the shared texture handle

- [label](label.md) — A string that identifies the texture.
