---
title: 'init(request:scale:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/asyncimage/init(request:scale:)'
source_url: 'https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/asyncimage/init%28request%3Ascale%3A%29.json'
content_hash: 'sha256:f90afc097d148d05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AsyncImage](../asyncimage.md)

# init(request:scale:)

<sub>Initializer</sub>

Loads and displays an image from the specified URL load request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(request: URLRequest, scale: CGFloat = 1) where Content == Image
```

## Parameters

- `request` — The [URLRequest](../../foundation/urlrequest.md) of the image to display.

- `scale` — The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.

## Discussion

Until the image loads, SwiftUI displays a default placeholder. When the load operation completes successfully, SwiftUI updates the view to show the loaded image. If the operation fails, SwiftUI continues to display the placeholder. The following example loads and displays an icon from an example server:

```swift
AsyncImage(request: URLRequest(url: imageURL))
```

If you want to customize the placeholder or apply image-specific modifiers — like [resizable(capInsets:resizingMode:)](<../image/resizable(capinsets_resizingmode_).md>) — to the loaded image, use the [init(request:scale:content:placeholder:)](<init(request_scale_content_placeholder_).md>) initializer instead.

## See Also

### Loading an image with a URL request

- [init(request:scale:content:placeholder:)](<init(request_scale_content_placeholder_).md>) — Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads. _(beta)_
- [init(request:scale:transaction:content:)](<init(request_scale_transaction_content_).md>) — Loads and displays a modifiable image from the specified URL load request in phases. _(beta)_
