---
title: 'apply(foreground:background:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciblendkernel/apply(foreground:background:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciblendkernel/apply(foreground:background:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciblendkernel/apply%28foreground%3Abackground%3A%29.json'
content_hash: 'sha256:3fd8ffe9a05feb7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIBlendKernel](../ciblendkernel.md)

# apply(foreground:background:)

<sub>Instance Method</sub>

Creates a new image using the blend kernel and specified foreground and background images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func apply(foreground: CIImage, background: CIImage) -> CIImage?
```

## Parameters

- `foreground` — The first input image to be blended

- `background` — The second input image to be blended

## Return Value

A [CIImage](../ciimage.md) blending the foreground and background images.  Its extent will be the union of the foreground and background image extents.

## Discussion

The foreground and background images are not treated differently in the blending.  You can think of them as equivalents A and B; the foreground is not given any precedence over the background.
