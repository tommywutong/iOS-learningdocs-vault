---
title: 'init(url:scale:transaction:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/asyncimage/init(url:scale:transaction:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/asyncimage/init(url:scale:transaction:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/asyncimage/init%28url%3Ascale%3Atransaction%3Acontent%3A%29.json'
content_hash: 'sha256:93052c8288930e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AsyncImage](../asyncimage.md)

# init(url:scale:transaction:content:)

<sub>Initializer</sub>

Loads and displays a modifiable image from the specified URL in phases.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(url: URL?, scale: CGFloat = 1, transaction: Transaction = Transaction(), @ContentBuilder content: @escaping (AsyncImagePhase) -> Content)
```

## Parameters

- `url` — The URL of the image to display.

- `scale` — The scale to use for the image. The default is `1`. Set a different value when loading images designed for higher resolution displays. For example, set a value of `2` for an image that you would name with the `@2x` suffix if stored in a file on disk.

- `transaction` — The transaction to use when the phase changes.

- `content` — A closure that takes the load phase as an input, and returns the view to display for the specified phase.

## Discussion

If you set the asynchronous image’s URL to `nil`, or after you set the URL to a value but before the load operation completes, the phase is [AsyncImagePhase.empty](../asyncimagephase/empty.md). After the operation completes, the phase becomes either [AsyncImagePhase.failure(_:)](<../asyncimagephase/failure(__).md>) or [AsyncImagePhase.success(_:)](<../asyncimagephase/success(__).md>). In the first case, the phase’s [error](../asyncimagephase/error.md) value indicates the reason for failure. In the second case, the phase’s [image](../asyncimagephase/image.md) property contains the loaded image. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

```swift
AsyncImage(url: URL(string: "https://example.com/icon.png")) { phase in
    if let image = phase.image {
        image // Displays the loaded image.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

To add transitions when you change the URL, apply an identifier to the [AsyncImage](../asyncimage.md).
