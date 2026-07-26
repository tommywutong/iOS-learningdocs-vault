---
title: finalize()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/hasher/finalize()
source_url: 'https://developer.apple.com/documentation/swift/hasher/finalize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/hasher/finalize%28%29.json'
content_hash: 'sha256:39ee8ed738fc9f31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Hasher](../hasher.md)

# finalize()

<sub>Instance Method</sub>

Finalizes the hasher state and returns the hash value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finalize() -> Int
```

## Return Value

The hash value calculated by the hasher.

## Discussion

Finalizing consumes the hasher: it is illegal to finalize a hasher you don’t own, or to perform operations on a finalized hasher. (These may become compile-time errors in the future.)

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.
