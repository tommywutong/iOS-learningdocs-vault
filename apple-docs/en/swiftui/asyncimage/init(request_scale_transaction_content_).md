---
title: 'init(request:scale:transaction:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/asyncimage/init(request:scale:transaction:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/asyncimage/init(request:scale:transaction:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/asyncimage/init%28request%3Ascale%3Atransaction%3Acontent%3A%29.json'
content_hash: 'sha256:9f7171fbed1d588a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AsyncImage](../asyncimage.md)

# init(request:scale:transaction:content:)

<sub>Initializer</sub>

Loads and displays a modifiable image from the specified URL load request in phases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(request: URLRequest?, scale: CGFloat = 1, transaction: Transaction = Transaction(), @ContentBuilder content: @escaping (AsyncImagePhase) -> Content)
```

## Parameters

- `request` — The [URLRequest](../../foundation/urlrequest.md) of the image to display.

- `scale` — The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.

- `transaction` — The transaction to use when the phase changes.

- `content` — A closure that takes the load phase as an input, and returns the view to display for the specified phase.

## Discussion

If you set the asynchronous image’s [URLRequest](../../foundation/urlrequest.md) to `nil`, or after you set the request to a value but before the load operation completes, the phase is [AsyncImagePhase.empty](../asyncimagephase/empty.md). After the operation completes, the phase becomes either [AsyncImagePhase.failure(_:)](<../asyncimagephase/failure(__).md>) or [AsyncImagePhase.success(_:)](<../asyncimagephase/success(__).md>). In the first case, the phase’s [error](../asyncimagephase/error.md) value indicates the reason for failure. In the second case, the phase’s [image](../asyncimagephase/image.md) property contains the loaded image. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

```swift
AsyncImage(request: URLRequest(url: imageURL)) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

To add transitions when you change the [URLRequest](../../foundation/urlrequest.md), apply an identifier to the [AsyncImage](../asyncimage.md).

You can specify the cache policy and timeout interval via `request`.

## See Also

### Loading an image with a URL request

- [init(request:scale:)](<init(request_scale_).md>) — Loads and displays an image from the specified URL load request. _(beta)_
- [init(request:scale:content:placeholder:)](<init(request_scale_content_placeholder_).md>) — Loads and displays a modifiable image from the specified URL load request using a custom placeholder until the image loads. _(beta)_
