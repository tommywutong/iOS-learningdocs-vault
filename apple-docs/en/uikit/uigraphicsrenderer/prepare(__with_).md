---
title: 'prepare(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsrenderer/prepare(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer/prepare(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer/prepare%28_%3Awith%3A%29.json'
content_hash: 'sha256:a581f042005c4e94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRenderer](../uigraphicsrenderer.md)

# prepare(_:with:)

<sub>Type Method</sub>

Applies the configuration specified in the renderer context to the Core Graphics context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func prepare(_ context: CGContext, with rendererContext: UIGraphicsRendererContext)
```

## Parameters

- `context` — The Core Graphics context that the graphics renderer performs drawing actions on.

- `rendererContext` — The renderer context object that is provided to the [- runDrawingActions:completionActions:error:](<rundrawingactions(__completionactions_).md>) method. This object is of the type returned by the [+ rendererContextClass](<renderercontextclass().md>) static method.

## Discussion

The graphics renderer calls this method when the [- runDrawingActions:completionActions:error:](<rundrawingactions(__completionactions_).md>) method is invoked. Override this method in a subclass to configure the underlying Core Graphics context before the renderer begins renderering.

Core Graphics contexts are reused for repeated calls to the [- runDrawingActions:completionActions:error:](<rundrawingactions(__completionactions_).md>) method. Therefore, be sure to clean up the context to make it ready for reuse.

## See Also

### Managing graphics contexts

- [+ contextWithFormat:](<context(with_).md>) — Creates a Core Graphics context configured according to the supplied format object.
- [+ rendererContextClass](<renderercontextclass().md>) — Specifies the drawing context class used by this graphics renderer.
