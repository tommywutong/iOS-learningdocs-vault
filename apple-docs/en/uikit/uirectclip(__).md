---
title: 'UIRectClip(_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uirectclip(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uirectclip(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirectclip%28_%3A%29.json'
content_hash: 'sha256:6616afea488ce6ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRectClip(_:)

<sub>Function</sub>

Modifies the current clipping path by intersecting it with the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIRectClip(_ rect: CGRect)
```

## Parameters

- `rect` — The rectangle to intersect with the clipping region. If the width or height of the rectangle are less than 0, this function does not change the clipping path.

## Discussion

Each call to this function permanently shrinks the clipping path of the current graphics context using the specified rectangle. You cannot use this function to expand the clipping region path. If the current graphics context is `nil`, this function does nothing.

If you need to return the clipping path to its original shape in your drawing code, you should save the current graphics context before calling this function. To save the current state of the graphics context, call the [saveGState()](<../coregraphics/cgcontext/savegstate().md>) function before making your modifications. When you are ready to restore the original clipping region, you can then use the [restoreGState()](<../coregraphics/cgcontext/restoregstate().md>) function to restore the previous graphics state.

This function may be called from any thread of your app.

## See Also

### Graphics context primitives

- [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) — Returns the current graphics context.
- [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) — Makes the specified graphics context the current context.
- [UIGraphicsPopContext](<uigraphicspopcontext().md>) — Removes the current graphics context from the top of the stack, restoring the previous context.
- [UIGraphicsBeginImageContextWithOptions](<uigraphicsbeginimagecontextwithoptions(______).md>) — Creates a bitmap-based graphics context with the specified options. _(deprecated)_
