---
title: UIGraphicsPopContext()
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicspopcontext()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspopcontext()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspopcontext%28%29.json'
content_hash: 'sha256:303a55ba19cfc55c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsPopContext()

<sub>Function</sub>

Removes the current graphics context from the top of the stack, restoring the previous context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsPopContext()
```

## Discussion

Use this function to balance calls to the [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) function.

This function may be called from any thread of your app.

## See Also

### Graphics context primitives

- [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) — Returns the current graphics context.
- [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) — Makes the specified graphics context the current context.
- [UIGraphicsBeginImageContextWithOptions](<uigraphicsbeginimagecontextwithoptions(______).md>) — Creates a bitmap-based graphics context with the specified options. _(deprecated)_
- [UIRectClip](<uirectclip(__).md>) — Modifies the current clipping path by intersecting it with the specified rectangle.
