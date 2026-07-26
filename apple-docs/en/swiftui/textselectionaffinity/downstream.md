---
title: TextSelectionAffinity.downstream
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselectionaffinity/downstream
source_url: 'https://developer.apple.com/documentation/swiftui/textselectionaffinity/downstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselectionaffinity/downstream.json'
content_hash: 'sha256:11033b80be292a76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextSelectionAffinity](../textselectionaffinity.md)

# TextSelectionAffinity.downstream

<sub>Case</sub>

An downstream selection affinity. In this case, the cursor is associated with the character immediately after it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case downstream
```

## Discussion

In the context of our example `hello|مرحبا`, with a downstream affinity, the cursor would be associated with the first character of “مرحبا”. If you were to type in Arabic, the characters would be added before the “م” in “مرحبا”, since Arabic is written right-to-left.
