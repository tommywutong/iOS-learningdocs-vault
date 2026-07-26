---
title: 'prepareRender(_:from:to:at:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/preparerender(_:from:to:at:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/preparerender(_:from:to:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/preparerender%28_%3Afrom%3Ato%3Aat%3A%29.json'
content_hash: 'sha256:fc36167acf4588f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# prepareRender(_:from:to:at:)

<sub>Instance Method</sub>

An optional call to warm up a [CIContext](../cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func prepareRender(_ image: CIImage, from fromRect: CGRect, to destination: CIRenderDestination, at atPoint: CGPoint) throws
```

## Parameters

- `image` — [CIImage](../ciimage.md) to prepare to render.

- `fromRect` — A [CGRect](../../corefoundation/cgrect.md) defining the region to render.

- `destination` — The [CIRenderDestination](../cirenderdestination.md) to which you are preparing to render.

- `atPoint` — The [CGPoint](../../corefoundation/cgpoint.md) at which you are preparing to render.

## Discussion

By making this call, the Core Image framework ensures that any needed kernels are compiled, and any intermediate buffers are allocated and marked volatile up front.

## See Also

### Customizing Render Destination

- [- startTaskToClear:error:](<starttask(toclear_).md>) — Fills the entire destination with black or clear depending on its [alphaMode](../cirenderdestination/alphamode.md).
- [- startTaskToRender:fromRect:toDestination:atPoint:error:](<starttask(torender_from_to_at_).md>) — Renders a portion of an image to a point in the destination.
- [- startTaskToRender:toDestination:error:](<starttask(torender_to_).md>) — Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.
