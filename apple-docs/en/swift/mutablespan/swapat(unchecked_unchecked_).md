---
title: 'swapAt(unchecked:unchecked:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablespan/swapat(unchecked:unchecked:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/swapat(unchecked:unchecked:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/swapat%28unchecked%3Aunchecked%3A%29.json'
content_hash: 'sha256:861290823cb7a5d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# swapAt(unchecked:unchecked:)

<sub>Instance Method</sub>

Exchange the elements at the two given indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func swapAt(unchecked i: MutableSpan<Element>.Index, unchecked j: MutableSpan<Element>.Index)
```

## Parameters

- `i` — A valid index into this span.

- `j` — A valid index into this span.

## Discussion

This function does not validate `i` or `j`; this is an unsafe operation.
