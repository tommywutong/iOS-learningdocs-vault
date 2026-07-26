---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/app/init()
source_url: 'https://developer.apple.com/documentation/swiftui/app/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/app/init%28%29.json'
content_hash: 'sha256:a4615c40c66c74ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [App](../app.md)

# init()

<sub>Initializer</sub>

Creates an instance of the app using the body that you define for its content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init()
```

## Discussion

Swift synthesizes a default initializer for structures that don’t provide one. You typically rely on the default initializer for your app.

## See Also

### Running an app

- [main()](<main().md>) — Initializes and runs the app.
