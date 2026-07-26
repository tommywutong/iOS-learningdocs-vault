---
title: device
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/device
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/device.json'
content_hash: 'sha256:77a17449eb3484b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# device

<sub>Instance Property</sub>

The Metal device responsible for the layer’s drawable resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: (any MTLDevice)? { get set }
```

## Discussion

This property determines which device object Metal uses to create its [MTLTexture](../../metal/mtltexture.md) objects. When you retrieve a drawable object and its associated texture, you must render to the texture using the same device object.

The default value is `nil`—you must set the device for a layer before rendering.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Configuring the Metal Device

- [preferredDevice](preferreddevice.md) — The device object that the system recommends using for this layer.
