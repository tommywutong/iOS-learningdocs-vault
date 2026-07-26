---
title: 'draw(_:in:from:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/draw(_:in:from:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/draw(_:in:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/draw%28_%3Ain%3Afrom%3A%29.json'
content_hash: 'sha256:a037fbdf05340167'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# draw(_:in:from:)

<sub>Instance Method</sub>

Renders a region of an image to a rectangle in the context destination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func draw(_ image: CIImage, in inRect: CGRect, from fromRect: CGRect)
```

## Parameters

- `image` — A Core Image image object.

- `inRect` — The rectangle in the context destination to draw into. The image is scaled to fill the destination rectangle.

- `fromRect` — The subregion of the image that you want to draw into the context, with the origin and target size defined by the `dest` parameter. This rectangle is always in pixel dimensions.

## Discussion

In iOS, this method draws the `CIImage` object into a renderbuffer for the OpenGL ES context. Use this method only if the [CIContext](../cicontext.md) object is created with `contextWithEAGLContext:`  and if you are rendering to a CAEAGLayer. This method is asynchronous for apps linked against the iOS 6 or later SDK.

In macOS, you need to be aware of whether the [CIContext](../cicontext.md) object is created with a `CGContextRef` or a `CGLContext` object. If you create the [CIContext](../cicontext.md) object with a `CGContextRef`, the dimensions of the destination rectangle are in points. If you create the [CIContext](../cicontext.md) object with a `CGLContext` object, the dimensions are in pixels.
