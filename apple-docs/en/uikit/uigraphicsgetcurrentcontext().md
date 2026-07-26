---
title: UIGraphicsGetCurrentContext()
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicsgetcurrentcontext()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsgetcurrentcontext()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsgetcurrentcontext%28%29.json'
content_hash: 'sha256:0f2a6b7638551a4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsGetCurrentContext()

<sub>Function</sub>

Returns the current graphics context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsGetCurrentContext() -> CGContext?
```

## Return Value

The current graphics context.

## Discussion

The current graphics context is `nil` by default. Prior to calling its `drawRect:` method, view objects push a valid context onto the stack, making it current. If you are not using a `UIView` object to do your drawing, however, you must push a valid context onto the stack manually using the [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) function.

This function may be called from any thread of your app.

## See Also

### Graphics context primitives

- [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) — Makes the specified graphics context the current context.
- [UIGraphicsPopContext](<uigraphicspopcontext().md>) — Removes the current graphics context from the top of the stack, restoring the previous context.
- [UIGraphicsBeginImageContextWithOptions](<uigraphicsbeginimagecontextwithoptions(______).md>) — Creates a bitmap-based graphics context with the specified options. _(deprecated)_
- [UIRectClip](<uirectclip(__).md>) — Modifies the current clipping path by intersecting it with the specified rectangle.
