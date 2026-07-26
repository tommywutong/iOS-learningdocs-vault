---
title: 'buildEither(first:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/slidertickbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:58f68d3b12624b30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SliderTickBuilder](../slidertickbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Produces content for a conditional statement in a multi-statement closure when the condition is true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where V == T.Value, T : SliderTickContent, F : SliderTickContent, T.Body == F.Body
```
