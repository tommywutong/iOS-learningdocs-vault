---
title: 'UIGraphicsPushContext(_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicspushcontext(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspushcontext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspushcontext%28_%3A%29.json'
content_hash: 'sha256:911c7680ed426cbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsPushContext(_:)

<sub>Function</sub>

Makes the specified graphics context the current context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsPushContext(_ context: CGContext)
```

## Parameters

- `context` — The graphics context to make the current context.

## Discussion

You can use this function to save the previous graphics state and make the specified context the current context. You must balance calls to this function with matching calls to the [UIGraphicsPopContext](<uigraphicspopcontext().md>) function.

This function may be called from any thread of your app.

## See Also

### Graphics context primitives

- [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) — Returns the current graphics context.
- [UIGraphicsPopContext](<uigraphicspopcontext().md>) — Removes the current graphics context from the top of the stack, restoring the previous context.
- [UIGraphicsBeginImageContextWithOptions](<uigraphicsbeginimagecontextwithoptions(______).md>) — Creates a bitmap-based graphics context with the specified options. _(deprecated)_
- [UIRectClip](<uirectclip(__).md>) — Modifies the current clipping path by intersecting it with the specified rectangle.
