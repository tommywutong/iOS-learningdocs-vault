---
title: 'UIGraphicsBeginImageContext(_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uigraphicsbeginimagecontext(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsbeginimagecontext%28_%3A%29.json'
content_hash: 'sha256:a809113cb26bec86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsBeginImageContext(_:)

<sub>Function</sub>

Creates a bitmap-based graphics context and makes it the current context.

> [!warning] Deprecated
> Use [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsBeginImageContext(_ size: CGSize)
```

## Parameters

- `size` — The size of the new bitmap context. This represents the size of the image returned by the [UIGraphicsGetImageFromCurrentImageContext](<uigraphicsgetimagefromcurrentimagecontext().md>) function.

## Discussion

This function is equivalent to calling the [UIGraphicsBeginImageContextWithOptions](<uigraphicsbeginimagecontextwithoptions(______).md>) function with the opaque parameter set to [false](../swift/false.md) and a scale factor of `1.0`.

This function may be called from any thread of your app.

## See Also

### Deprecated functions

- [UIApplicationMain(_:_:_:_:)](<uiapplicationmain(________)-9jjn8.md>) — Creates the application object and the application delegate and sets up the event cycle. _(deprecated)_
- [UIGraphicsGetImageFromCurrentImageContext](<uigraphicsgetimagefromcurrentimagecontext().md>) — Returns an image from the contents of the current bitmap-based graphics context. _(deprecated)_
- [UIGraphicsEndImageContext](<uigraphicsendimagecontext().md>) — Removes the current bitmap-based graphics context from the top of the stack. _(deprecated)_
