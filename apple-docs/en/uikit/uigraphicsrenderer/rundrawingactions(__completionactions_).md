---
title: 'runDrawingActions(_:completionActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsrenderer/rundrawingactions(_:completionactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer/rundrawingactions(_:completionactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer/rundrawingactions%28_%3Acompletionactions%3A%29.json'
content_hash: 'sha256:3d243cef707acae5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRenderer](../uigraphicsrenderer.md)

# runDrawingActions(_:completionActions:)

<sub>Instance Method</sub>

Performs drawing actions on a Core Graphics context that the renderer prepares.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func runDrawingActions(_ drawingActions: (UIGraphicsRendererContext) -> Void, completionActions: ((UIGraphicsRendererContext) -> Void)? = nil) throws
```

## Parameters

- `drawingActions` — A [UIGraphicsDrawingActions](../uigraphicsdrawingactions.md) block that represents a set of drawing instructions that the renderer applies to the Core Graphics context.

- `completionActions` — A [UIGraphicsDrawingActions](../uigraphicsdrawingactions.md) block that the renderer calls after executing the `drawingActions` block.

## Discussion

This method invokes the `drawingActions` block in a Core Graphics context. This context was created by the [+ contextWithFormat:](<context(with_).md>) method, captured in an instance of the class returned by the [+ rendererContextClass](<renderercontextclass().md>) method, and prepared by the [+ prepareCGContext:withRendererContext:](<prepare(__with_).md>) method.

Do not override this method. Instead, consider invoking it from a utility method in your subclass, as the [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md) and [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md) classes do.

## See Also

### Running the drawing actions

- [UIGraphicsDrawingActions](../uigraphicsdrawingactions.md) — A closure that executes a set of drawing instructions that the renderer applies to the Core Graphics context.
