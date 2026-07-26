---
title: makeSharedContext()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/previewmodifier/makesharedcontext()-4zi8r
source_url: 'https://developer.apple.com/documentation/swiftui/previewmodifier/makesharedcontext()-4zi8r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewmodifier/makesharedcontext%28%29-4zi8r.json'
content_hash: 'sha256:0e7de7e8533fd5f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreviewModifier](../previewmodifier.md)

# makeSharedContext()

<sub>Type Method</sub>

Create shared context to apply to previews. The context returned here will be cached and passed into the `body` method for every preview that applies a modifier of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor static func makeSharedContext() async throws -> Self.Context
```
