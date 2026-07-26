---
title: 'transaction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/viewmodifier/transaction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/viewmodifier/transaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewmodifier/transaction%28_%3A%29.json'
content_hash: 'sha256:0594dbb1f1355337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ViewModifier](../viewmodifier.md)

# transaction(_:)

<sub>Instance Method</sub>

Returns a new version of the modifier that will apply the transaction mutation function `transform` to all transactions within the modifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some ViewModifier

```
