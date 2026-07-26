---
title: 'init(mtlDevice:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/init(mtldevice:)-swey'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init(mtldevice:)-swey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28mtldevice%3A%29-swey.json'
content_hash: 'sha256:3718c72d66075c1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init(mtlDevice:)

<sub>Initializer</sub>

Creates a Core Image context using the specified Metal device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(mtlDevice device: any MTLDevice)
```

## Parameters

- `device` — The Metal device object to use for rendering.

## Return Value

A Core Image context.

## Discussion

Use this method to choose a specific Metal device for rendering when a system contains multiple Metal devices. To create a Metal-based context using the system’s default Metal device, use the [contextWithOptions:](contextwithoptions_.md) method.

## See Also

### Creating a Context for GPU-Based Rendering

- [+ contextWithMTLDevice:options:](<init(mtldevice_options_)-26usb.md>) — Creates a Core Image context using the specified Metal device and options.
- [+ contextWithMTLCommandQueue:](<init(mtlcommandqueue_)-7dtqk.md>)
- [+ contextWithMTLCommandQueue:options:](<init(mtlcommandqueue_options_)-6i3me.md>)
