---
title: 'formIndex(after:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/utf8view/formindex(after:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/utf8view/formindex(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/utf8view/formindex%28after%3A%29.json'
content_hash: 'sha256:438c6ee4cc7d4bc7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UTF8View](../utf8view.md)

# formIndex(after:)

<sub>Instance Method</sub>

Replaces the given index with its successor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(after i: inout Substring.UTF8View.Index)
```

## Parameters

- `i` — A valid index of the collection. `i` must be less than `endIndex`.
