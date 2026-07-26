---
title: 'append(repeating:count:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputrawspan/append(repeating:count:as:)-1h8m1'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/append(repeating:count:as:)-1h8m1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/append%28repeating%3Acount%3Aas%3A%29-1h8m1.json'
content_hash: 'sha256:01e3aef6ede3e108'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# append(repeating:count:as:)

<sub>Instance Method</sub>

Appends the given value’s bytes repeatedly to this span’s bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<T>(repeating repeatedValue: T, count: Int, as type: T.Type) where T : BitwiseCopyable
```

## Parameters

- `repeatedValue` — The value to store as raw bytes.

- `count` — The number of copies of `repeatedValue` to append to this span.

- `type` — The type of the instance to store repeatedly.
