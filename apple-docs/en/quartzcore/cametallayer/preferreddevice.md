---
title: preferredDevice
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/preferreddevice
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/preferreddevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/preferreddevice.json'
content_hash: 'sha256:0f0e77902302b3ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# preferredDevice

<sub>Instance Property</sub>

The device object that the system recommends using for this layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var preferredDevice: (any MTLDevice)? { get }
```

## Discussion

On systems with a single GPU, this method returns the default device object; see [MTLCreateSystemDefaultDevice()](<../../metal/mtlcreatesystemdefaultdevice().md>). On systems with more than one GPU, this method returns the [MTLDevice](../../metal/mtldevice.md) that was last used to composite and present the [CAMetalLayer](../cametallayer.md). This device object usually corresponds to the GPU associated with the screen that’s displaying the layer. If you set the layer’s [device](device.md) property to this device object, you reduce the number of cross-GPU texture copies that Core Animation must perform to present the layer’s contents onscreen.

## See Also

### Configuring the Metal Device

- [device](device.md) — The Metal device responsible for the layer’s drawable resources.
