---
title: 'startTask(toRender:from:to:at:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/starttask(torender:from:to:at:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/starttask(torender:from:to:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/starttask%28torender%3Afrom%3Ato%3Aat%3A%29.json'
content_hash: 'sha256:c40f23f7de13ac1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# startTask(toRender:from:to:at:)

<sub>Instance Method</sub>

Renders a portion of an image to a point in the destination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startTask(toRender image: CIImage, from fromRect: CGRect, to destination: CIRenderDestination, at atPoint: CGPoint) throws -> CIRenderTask
```

## Parameters

- `image` — A [CIImage](../ciimage.md) to render.

- `fromRect` — The part of the image to render, as if cropped.

- `destination` — A [CIRenderDestination](../cirenderdestination.md) into which to render the image.

- `atPoint` — An origin point in the destination at which to place the image.

## Return Value

An asynchronous [CIRenderTask](../cirendertask.md) to render the image to the specified destination.

## Discussion

This method crops the image to the specified rectangle and renders the result at the indicated origin point. If the image’s [extent](../ciimage/extent.md) property and `fromRect` argument values are infinite, this call renders the image’s (0, 0) point starting from the origin `atPoint`.

You must use an [MTLTexture](../../metal/mtltexture.md)-backed [CIContext](../cicontext.md) to support an [MTLTexture](../../metal/mtltexture.md)-backed [CIRenderDestination](../cirenderdestination.md). Similarly, you must use `GLContext`-backed [CIContext](../cicontext.md) to support a `GLTexture`-backed [CIRenderDestination](../cirenderdestination.md).

This call returns as soon as it enqueues all work required to render the image on the context’s device. In many situations, after issuing a render, you may need to wait for it to complete. In these cases, use the returned [CIRenderTask](../cirendertask.md) as follows:

**Swift**

```swift
let renderTask = try context.startTask(toRender: image, from: fromRect, to: destination, at: point)

let renderInfo = try renderTask.waitUntilCompleted()
```

**Objective-C**

```objc
CIRenderTask* task = [context startTaskToRender:image fromRect:fromRect toDestination:renderDestination atPoint:point error:&error];

CIRenderInfo* info = [task waitUntilCompletedAndReturnError:&error];
```

## See Also

### Customizing Render Destination

- [- prepareRender:fromRect:toDestination:atPoint:error:](<preparerender(__from_to_at_).md>) — An optional call to warm up a [CIContext](../cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [- startTaskToClear:error:](<starttask(toclear_).md>) — Fills the entire destination with black or clear depending on its [alphaMode](../cirenderdestination/alphamode.md).
- [- startTaskToRender:toDestination:error:](<starttask(torender_to_).md>) — Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.
