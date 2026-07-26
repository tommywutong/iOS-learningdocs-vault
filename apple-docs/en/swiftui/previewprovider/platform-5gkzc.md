---
title: platform
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewprovider/platform-5gkzc
source_url: 'https://developer.apple.com/documentation/swiftui/previewprovider/platform-5gkzc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewprovider/platform-5gkzc.json'
content_hash: 'sha256:8c2d490b70f5fc1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreviewProvider](../previewprovider.md)

# platform

<sub>Type Property</sub>

The platform to run the provider on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static var platform: PreviewPlatform? { get }
```

## Discussion

This default implementation of the [platform](platform.md) computed property returns `nil`. Rely on this implementation unless you have a multiplatform target and want to suggest a particular platform for a preview.
