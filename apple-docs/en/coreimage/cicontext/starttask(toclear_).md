---
title: 'startTask(toClear:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/starttask(toclear:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/starttask(toclear:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/starttask%28toclear%3A%29.json'
content_hash: 'sha256:60d4f48569b41970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# startTask(toClear:)

<sub>Instance Method</sub>

Fills the entire destination with black or clear depending on its [alphaMode](../cirenderdestination/alphamode.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startTask(toClear destination: CIRenderDestination) throws -> CIRenderTask
```

## Parameters

- `destination` — The [CIRenderDestination](../cirenderdestination.md) to clear.

## Return Value

The asynchronous [CIRenderTask](../cirendertask.md) for clearing the destination.

## Discussion

If the destination’s [alphaMode](../cirenderdestination/alphamode.md) is [CIRenderDestinationAlphaNone](../cirenderdestinationalphamode/none.md), this command fills the entire destination with black `(0, 0, 0, 1)`.

If the destination’s [alphaMode](../cirenderdestination/alphamode.md) is [CIRenderDestinationAlphaPremultiplied](../cirenderdestinationalphamode/premultiplied.md) or [CIRenderDestinationAlphaUnpremultiplied](../cirenderdestinationalphamode/unpremultiplied.md), this command fills the entire destination with clear `(0, 0, 0, 0)`.

## See Also

### Customizing Render Destination

- [- prepareRender:fromRect:toDestination:atPoint:error:](<preparerender(__from_to_at_).md>) — An optional call to warm up a [CIContext](../cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [- startTaskToRender:fromRect:toDestination:atPoint:error:](<starttask(torender_from_to_at_).md>) — Renders a portion of an image to a point in the destination.
- [- startTaskToRender:toDestination:error:](<starttask(torender_to_).md>) — Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.
