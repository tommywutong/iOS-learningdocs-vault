---
title: 'startTask(toRender:to:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/starttask(torender:to:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/starttask(torender:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/starttask%28torender%3Ato%3A%29.json'
content_hash: 'sha256:6a32c4f1d26e5f7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# startTask(toRender:to:)

<sub>Instance Method</sub>

Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startTask(toRender image: CIImage, to destination: CIRenderDestination) throws -> CIRenderTask
```

## Parameters

- `image` — [CIImage](../ciimage.md) to prepare to render.

- `destination` — The [CIRenderDestination](../cirenderdestination.md) to which to render.

## Return Value

The asynchronous [CIRenderTask](../cirendertask.md) to render the image to the specified destination.

## See Also

### Customizing Render Destination

- [- prepareRender:fromRect:toDestination:atPoint:error:](<preparerender(__from_to_at_).md>) — An optional call to warm up a [CIContext](../cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [- startTaskToClear:error:](<starttask(toclear_).md>) — Fills the entire destination with black or clear depending on its [alphaMode](../cirenderdestination/alphamode.md).
- [- startTaskToRender:fromRect:toDestination:atPoint:error:](<starttask(torender_from_to_at_).md>) — Renders a portion of an image to a point in the destination.
