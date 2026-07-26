---
title: 'init(request:scale:content:placeholder:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/asyncimage/init(request:scale:content:placeholder:)'
source_url: 'https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:content:placeholder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/asyncimage/init%28request%3Ascale%3Acontent%3Aplaceholder%3A%29.json'
content_hash: 'sha256:69661c1a8fec1073'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AsyncImage](../asyncimage.md)

# init(request:scale:content:placeholder:)

<sub>Initializer</sub>

Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<I, P>(request: URLRequest?, scale: CGFloat = 1, @ContentBuilder content: @escaping (Image) -> I, @ContentBuilder placeholder: @escaping () -> P) where Content == _AsyncImageConditionalContent<I, P>, I : View, P : View
```

## Parameters

- `request` — The [URLRequest](../../foundation/urlrequest.md) of the image to display.

- `scale` — The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.

- `content` — A closure that takes the loaded image as an input, and returns the view to show. You can return the image directly, or modify it as needed before returning it.

- `placeholder` — A closure that returns the view to show until the load operation completes successfully.

## Discussion

Until the image loads, SwiftUI displays the placeholder view that you specify. When the load operation completes successfully, SwiftUI updates the view to show content that you specify, which you create using the loaded image. For example, you can show a green placeholder, followed by a tiled version of the loaded image:

```swift
AsyncImage(request: URLRequest(url: imageURL)) { image in
    image.resizable(resizingMode: .tile)
} placeholder: {
    Color.green
}
```

If the load operation fails, SwiftUI continues to display the placeholder. To be able to display a different view on a load error, use the [init(url:scale:transaction:content:)](<init(url_scale_transaction_content_).md>) initializer instead.

## See Also

### Loading an image with a URL request

- [init(request:scale:)](<init(request_scale_).md>) — Loads and displays an image from the specified URL load request. _(beta)_
- [init(request:scale:transaction:content:)](<init(request_scale_transaction_content_).md>) — Loads and displays a modifiable image from the specified URL load request in phases. _(beta)_
