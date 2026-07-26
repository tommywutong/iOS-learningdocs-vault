---
title: rendererContextClass()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsrenderer/renderercontextclass()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderer/renderercontextclass()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderer/renderercontextclass%28%29.json'
content_hash: 'sha256:21458d43baeba82e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRenderer](../uigraphicsrenderer.md)

# rendererContextClass()

<sub>Type Method</sub>

Specifies the drawing context class used by this graphics renderer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func rendererContextClass() -> AnyClass
```

## Return Value

A subclass of [UIGraphicsRendererContext](../uigraphicsrenderercontext.md) suitable for the current renderer.

## Discussion

Each subclass of `UIGraphicsRenderer` can define its own subclass of [UIGraphicsRendererContext](../uigraphicsrenderercontext.md). The graphics renderer calls this method whenever it needs to create a new graphics renderer context.

Override this method to specify the context class that the graphics renderer should use.

## See Also

### Managing graphics contexts

- [+ contextWithFormat:](<context(with_).md>) — Creates a Core Graphics context configured according to the supplied format object.
- [+ prepareCGContext:withRendererContext:](<prepare(__with_).md>) — Applies the configuration specified in the renderer context to the Core Graphics context.
