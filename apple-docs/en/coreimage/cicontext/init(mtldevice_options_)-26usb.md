---
title: 'init(mtlDevice:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/init(mtldevice:options:)-26usb'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init(mtldevice:options:)-26usb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28mtldevice%3Aoptions%3A%29-26usb.json'
content_hash: 'sha256:9881c6852f92f9e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init(mtlDevice:options:)

<sub>Initializer</sub>

Creates a Core Image context using the specified Metal device and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(mtlDevice device: any MTLDevice, options: [CIContextOption : Any]? = nil)
```

## Parameters

- `device` — The Metal device object to use for rendering.

- `options` — A dictionary that contains options for creating a [CIContext](../cicontext.md) object. You can pass any of the keys defined in [CIContextOption](../cicontextoption.md) along with the appropriate value.

## Return Value

A Core Image context.

## Discussion

Use this method to choose a specific Metal device for rendering when a system contains multiple Metal devices. To create a Metal-based context using the system’s default Metal device, use the [contextWithOptions:](contextwithoptions_.md) method.

## See Also

### Creating a Context for GPU-Based Rendering

- [+ contextWithMTLDevice:](<init(mtldevice_)-swey.md>) — Creates a Core Image context using the specified Metal device.
- [+ contextWithMTLCommandQueue:](<init(mtlcommandqueue_)-7dtqk.md>)
- [+ contextWithMTLCommandQueue:options:](<init(mtlcommandqueue_options_)-6i3me.md>)
