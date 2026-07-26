---
title: 'estimateRender(_:from:to:at:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/coreimage/cicontext/estimaterender(_:from:to:at:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/estimaterender(_:from:to:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/estimaterender%28_%3Afrom%3Ato%3Aat%3A%29.json'
content_hash: 'sha256:97c58bad74925362'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# estimateRender(_:from:to:at:)

<sub>Instance Method</sub>

Returns a task with estimated resource statistics for a render, without executing the render.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func estimateRender(_ image: CIImage, from fromRect: CGRect, to destination: CIRenderDestination, at atPoint: CGPoint) throws -> CIRenderTask
```

## Parameters

- `image` — The [CIImage](../ciimage.md) to estimate the render for.

- `fromRect` — The region of [CIImage](../ciimage.md) to render.

- `destination` — The [CIRenderDestination](../cirenderdestination.md) to estimate the render to.

- `atPoint` — The point in the destination where the origin of `fromRect` is placed.

## Return Value

A [CIRenderTask](../cirendertask.md) you can query for estimated statistics, or `nil` if `fromRect` doesn’t intersect `image.extent` or if estimation fails.

## Discussion

Call this method to analyze the cost of a render before you execute it. Query the returned task’s `plannedPixelsProcessed`, `plannedPixelsOverdrawn`, `plannedPassCount`, and `plannedPeakMemory` properties to get the estimated statistics.

The method renders as if the image is cropped to `fromRect` and places the origin of `fromRect` at `atPoint` in the destination.
