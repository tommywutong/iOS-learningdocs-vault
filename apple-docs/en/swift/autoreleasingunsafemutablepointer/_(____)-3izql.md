---
title: '>(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/autoreleasingunsafemutablepointer/_(_:_:)-3izql'
source_url: 'https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer/_(_:_:)-3izql'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/autoreleasingunsafemutablepointer/_%28_%3A_%3A%29-3izql.json'
content_hash: 'sha256:2f9607ba4560f6bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AutoreleasingUnsafeMutablePointer](../autoreleasingunsafemutablepointer.md)

# \>(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func > (lhs: borrowing Self, rhs: borrowing Self) -> Bool
```

## Parameters

- `lhs` — A value to compare.

- `rhs` — Another value to compare.

## Discussion

This is the default implementation of the greater-than operator (`>`) for any type that conforms to `Comparable`.
