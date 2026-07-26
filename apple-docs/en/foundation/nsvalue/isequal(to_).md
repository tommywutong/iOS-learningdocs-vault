---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/isequal%28to%3A%29.json'
content_hash: 'sha256:f6d2cbd5a735b7d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the value object and another value object are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to value: NSValue) -> Bool
```

## Parameters

- `value` — The other value object with which to compare the value object.

## Return Value

[true](../../swift/true.md) if both value objects are equal; otherwise, [false](../../swift/false.md).

## Discussion

The [NSValue](../nsvalue.md) class compares the type and contents of each value object to determine equality.
