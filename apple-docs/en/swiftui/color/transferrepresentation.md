---
title: transferRepresentation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/transferrepresentation
source_url: 'https://developer.apple.com/documentation/swiftui/color/transferrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/transferrepresentation.json'
content_hash: 'sha256:8b87270927c8a02e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# transferRepresentation

<sub>Type Property</sub>

One group of colors–constant colors–created with explicitly specified component values are transferred as is.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var transferRepresentation: some TransferRepresentation { get }
```

## Discussion

Another group of colors–standard colors, like `Color.mint`, and semantic colors, like `Color.accentColor`–are rendered on screen differently depending on the current [Environment](../environment.md). For transferring, they are resolved against the default environment and might produce a slightly different result at the destination if the source of drag or copy uses a non-default environment.
