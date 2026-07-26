---
title: UIGraphicsGetImageFromCurrentImageContext()
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uigraphicsgetimagefromcurrentimagecontext()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsgetimagefromcurrentimagecontext()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsgetimagefromcurrentimagecontext%28%29.json'
content_hash: 'sha256:05db85423482c759'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsGetImageFromCurrentImageContext()

<sub>Function</sub>

Returns an image from the contents of the current bitmap-based graphics context.

> [!warning] Deprecated
> Use [currentImage](uigraphicsimagerenderercontext/currentimage.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?
```

## Return Value

A image object containing the contents of the current bitmap graphics context.

## Discussion

You should call this function only when a bitmap-based graphics context is the current graphics context. If the current context is `nil` or was not created by a call to [UIGraphicsBeginImageContext](<uigraphicsbeginimagecontext(__).md>), this function returns `nil`.

This function may be called from any thread of your app.

## See Also

### Deprecated functions

- [UIApplicationMain(_:_:_:_:)](<uiapplicationmain(________)-9jjn8.md>) — Creates the application object and the application delegate and sets up the event cycle. _(deprecated)_
- [UIGraphicsBeginImageContext](<uigraphicsbeginimagecontext(__).md>) — Creates a bitmap-based graphics context and makes it the current context. _(deprecated)_
- [UIGraphicsEndImageContext](<uigraphicsendimagecontext().md>) — Removes the current bitmap-based graphics context from the top of the stack. _(deprecated)_
