---
title: removeLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/outputspan/removelast()
source_url: 'https://developer.apple.com/documentation/swift/outputspan/removelast()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputspan/removelast%28%29.json'
content_hash: 'sha256:7e0a4de7a716865d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputSpan](../outputspan.md)

# removeLast()

<sub>Instance Method</sub>

Remove the last initialized element from this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast() -> Element
```

## Return Value

The removed element.

## Discussion

Returns the last element. The `OutputSpan` must not be empty.
