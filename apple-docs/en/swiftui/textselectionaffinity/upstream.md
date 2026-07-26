---
title: TextSelectionAffinity.upstream
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselectionaffinity/upstream
source_url: 'https://developer.apple.com/documentation/swiftui/textselectionaffinity/upstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselectionaffinity/upstream.json'
content_hash: 'sha256:6729da8b5cda0f9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextSelectionAffinity](../textselectionaffinity.md)

# TextSelectionAffinity.upstream

<sub>Case</sub>

An upstream selection affinity. In this case, the cursor is associated with the character immediately before it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case upstream
```

## Discussion

In the context of our example  `hello|مرحبا`, with an upstream affinity, the cursor would be associated with the “o” from “hello”. If you were to type in English, the characters would continue to be added after the “o” in “hello”.
