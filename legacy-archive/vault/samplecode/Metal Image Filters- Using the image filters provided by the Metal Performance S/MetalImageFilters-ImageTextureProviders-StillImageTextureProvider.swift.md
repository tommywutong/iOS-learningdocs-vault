---
title: 'Metal Image Filters: Using the image filters provided by the Metal Performance
  Shaders framework.'
apple_id: TP40017535
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal Performance Shaders
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalImageFilters/Listings/MetalImageFilters_ImageTextureProviders_StillImageTextureProvider_swift.html
archived_at: '2026-07-18T03:14:49.021706Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal Image Filters: Using the image filters provided by the Metal Performance Shaders framework.](Metal%20Image%20Filters-%20Using%20the%20image%20filters%20provided%20by%20the%20Metal%20Performance%20S.md)


[Next](MetalImageFilters-ImageTextureProviders-VideoImageTextureProvider.swift.md)[Previous](MetalImageFilters-ImageFilters.swift.md)

# MetalImageFilters/ImageTextureProviders/StillImageTextureProvider.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Still Image Texture Provider for MetalImageFilters.
                Uses the MetalKit texture loader to load an still image into a Metal texture.
 */

import MetalKit

/// Uses the MetalKit texture loader to load a still image into a Metal texture.
class StillImageTextureProvider: NSObject {
    /// The source texture for image filter operations.
    var texture: MTLTexture?

    /// Returns an initialized StillImageTextureProvider object with a source texture, or nil in case of failure.
    required init?(device: MTLDevice, imageName: String) {
        super.init()

        let loader = MTKTextureLoader(device: device)
        let image = UIImage(named: imageName)?.cgImage
        // The still image is loaded directly into GPU-accessible memory that is only ever read from.
        let options = [
            MTKTextureLoaderOptionTextureStorageMode:   MTLStorageMode.private.rawValue,
            MTKTextureLoaderOptionTextureUsage:         MTLTextureUsage.shaderRead.rawValue,
            MTKTextureLoaderOptionSRGB:                 0
        ]
        do {
            let fileTexture = try loader.newTexture(with: image!, options: options as [String : NSObject]?)
            texture = fileTexture
        } catch let error as NSError {
            print("Error loading still image texture: \(error)")
            return nil
        }
    }
}
```

[Next](MetalImageFilters-ImageTextureProviders-VideoImageTextureProvider.swift.md)[Previous](MetalImageFilters-ImageFilters.swift.md)

