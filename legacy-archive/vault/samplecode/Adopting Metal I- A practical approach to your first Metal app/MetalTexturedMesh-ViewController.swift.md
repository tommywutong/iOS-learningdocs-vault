---
title: 'Adopting Metal I: A practical approach to your first Metal app'
apple_id: TP40017287
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdoptingMetalI/Listings/MetalTexturedMesh_ViewController_swift.html
archived_at: '2026-07-18T03:00:47.809012Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Adopting Metal I: A practical approach to your first Metal app](Adopting%20Metal%20I-%20A%20practical%20approach%20to%20your%20first%20Metal%20app.md)


[Next](MetalTexturedMesh-Renderer.swift.md)[Previous](MetalTexturedMesh-Shaders.metal.md)

# MetalTexturedMesh/ViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View controller class that manages the MTKView and renderer.
*/

import MetalKit
import Cocoa

class ViewController: NSViewController {

    var renderer: Renderer!

    override func viewDidLoad() {
        super.viewDidLoad()

        let metalView = self.view as! MTKView

        // We initialize our renderer object with the MTKView it will be drawing into
        renderer = Renderer(mtkView:metalView)
    }
}
```

[Next](MetalTexturedMesh-Renderer.swift.md)[Previous](MetalTexturedMesh-Shaders.metal.md)

