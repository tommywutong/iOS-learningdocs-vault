---
title: 'buildEither(first:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontentbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontentbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontentbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:9de60a9916ca8e52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContentBuilder](../tabcontentbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where TabValue == T.TabValue, T : TabContent, F : TabContent, T.TabValue == F.TabValue
```
