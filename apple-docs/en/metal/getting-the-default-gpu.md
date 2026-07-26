---
title: Getting the default GPU
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/getting-the-default-gpu
source_url: 'https://developer.apple.com/documentation/metal/getting-the-default-gpu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/getting-the-default-gpu.json'
content_hash: 'sha256:76ad23b098ca8ed7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md)

# Getting the default GPU

<sub>Article</sub>

Select the system’s default GPU device on which to run your Metal code.

## Overview

To use the Metal framework, start by getting a GPU device. All of the instances your app needs to interact with Metal come from an [MTLDevice](mtldevice.md) that you acquire at runtime. Some devices, such as those with iOS and tvOS have a single GPU that you can access by calling [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>).

```swift
if(!(device = MTLCreateSystemDefaultDevice()))
{
    NSLog(@"Failed to get the system's default Metal device.");
}
```

On macOS devices that have multiple GPUs, such as a MacBook Pro, the system default is the discrete GPU.

## See Also

### Locating and inspecting a GPU device

- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md) — Use the device object’s properties to determine how you perform tasks in Metal.
- [MTLCreateSystemDefaultDevice](<mtlcreatesystemdefaultdevice().md>) — Returns the device instance Metal selects as the default.
- [MTLDevice](mtldevice.md) — The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
- [Multi-GPU systems](multi-gpu-systems.md) — Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.
