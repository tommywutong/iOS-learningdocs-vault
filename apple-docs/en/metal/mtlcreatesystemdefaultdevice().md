---
title: MTLCreateSystemDefaultDevice()
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcreatesystemdefaultdevice()
source_url: 'https://developer.apple.com/documentation/metal/mtlcreatesystemdefaultdevice()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcreatesystemdefaultdevice%28%29.json'
content_hash: 'sha256:d2eedb690f7cb1f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCreateSystemDefaultDevice()

<sub>Function</sub>

Returns the device instance Metal selects as the default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLCreateSystemDefaultDevice() -> (any MTLDevice)?
```

## Return Value

A device object.

## Discussion

In macOS, in order for the system to provide a default Metal device object, you need to link to the [Core Graphics](../coregraphics.md) framework. You usually need to do this explicitly if you’re writing apps that don’t use graphics by default, such as command line tools.

## See Also

### Locating and inspecting a GPU device

- [Getting the default GPU](getting-the-default-gpu.md) — Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) — Use the device object’s properties to determine how you perform tasks in Metal.
- [MTLDevice](mtldevice.md) — The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
- [Multi-GPU systems](multi-gpu-systems.md) — Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.
