---
title: Rendering a scene with forward plus lighting using tile shaders
framework: Metal
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 26.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders
source_url: 'https://developer.apple.com/documentation/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/rendering-a-scene-with-forward-plus-lighting-using-tile-shaders.json'
content_hash: 'sha256:39645ca0220eac42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Metal sample code library](metal-sample-code-library.md)

# Rendering a scene with forward plus lighting using tile shaders

<sub>Sample Code</sub>

Implement a forward plus renderer using the latest features on Apple GPUs.

## Overview

> [!note] Note
> This sample code project is associated with WWDC 2019 session [601: Modern Rendering with Metal](https://developer.apple.com/videos/play/wwdc19/601/).

### Configure the sample code project

To run the app:

- Build the project with Xcode 11 or later.
- Target an iOS device with an A11 chip or later and iOS 11 or later.

## See Also

### Lighting techniques

- [Rendering a scene with deferred lighting in Objective-C](rendering-a-scene-with-deferred-lighting-in-objective-c.md) — Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering a scene with deferred lighting in Swift](rendering-a-scene-with-deferred-lighting-in-swift.md) — Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering a scene with deferred lighting in C++](rendering-a-scene-with-deferred-lighting-in-c++.md) — Avoid expensive lighting calculations by implementing a deferred lighting renderer optimized for immediate mode and tile-based deferred renderer GPUs.
- [Rendering reflections with fewer render passes](rendering-reflections-with-fewer-render-passes.md) — Use layer selection to reduce the number of render passes needed to generate an environment map.

## Download

- [RenderingASceneWithForwardPlusLightingUsingTileShaders.zip](https://docs-assets.developer.apple.com/published/73528988a5ff/RenderingASceneWithForwardPlusLightingUsingTileShaders.zip)
