---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyiterator/next()
source_url: 'https://developer.apple.com/documentation/swift/anyiterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyiterator/next%28%29.json'
content_hash: 'sha256:572a4ede4f75f07b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyIterator](../anyiterator.md)

# next()

<sub>Instance Method</sub>

Advances to the next element and returns it, or `nil` if no next element exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func next() -> Element?
```

## Discussion

Once `nil` has been returned, all subsequent calls return `nil`.
