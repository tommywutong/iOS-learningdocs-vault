---
title: UIGraphicsEndImageContext()
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uigraphicsendimagecontext()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsendimagecontext()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsendimagecontext%28%29.json'
content_hash: 'sha256:2acb917811d03e52'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsEndImageContext()

<sub>Function</sub>

Removes the current bitmap-based graphics context from the top of the stack.

> [!warning] Deprecated
> Use [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsEndImageContext()
```

## Discussion

You use this function to clean up the drawing environment put in place by the [UIGraphicsBeginImageContext](<uigraphicsbeginimagecontext(__).md>) function and to remove the corresponding bitmap-based graphics context from the top of the stack. If the current context was not created using the [UIGraphicsBeginImageContext](<uigraphicsbeginimagecontext(__).md>) function, this function does nothing.

This function may be called from any thread of your app.

## See Also

### Deprecated functions

- [UIApplicationMain(_:_:_:_:)](<uiapplicationmain(________)-9jjn8.md>) — Creates the application object and the application delegate and sets up the event cycle. _(deprecated)_
- [UIGraphicsBeginImageContext](<uigraphicsbeginimagecontext(__).md>) — Creates a bitmap-based graphics context and makes it the current context. _(deprecated)_
- [UIGraphicsGetImageFromCurrentImageContext](<uigraphicsgetimagefromcurrentimagecontext().md>) — Returns an image from the contents of the current bitmap-based graphics context. _(deprecated)_
