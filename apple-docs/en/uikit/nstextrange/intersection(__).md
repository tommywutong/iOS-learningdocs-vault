---
title: 'intersection(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextrange/intersection(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextrange/intersection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextrange/intersection%28_%3A%29.json'
content_hash: 'sha256:a7bb8d0acf46ce4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextRange](../nstextrange.md)

# intersection(_:)

<sub>Instance Method</sub>

Returns the range, if any, where two text ranges intersect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func intersection(_ textRange: NSTextRange) -> Self?
```

## Parameters

- `textRange` — The range used to compare against the current range to evaluate for differences.

## Return Value

An [NSRange](../../foundation/nsrange-c.struct.md) that represents the intersection of the ranges, or `nil` if they don’t intersect.

## See Also

### Comparing text ranges

- [- intersectsWithTextRange:](<intersects(__).md>) — Determines if two ranges intersect.
- [- isEqualToTextRange:](<isequal(to_).md>) — Compares two text ranges.
- [- textRangeByFormingUnionWithTextRange:](<union(__).md>) — Returns a new text range by forming the union with the text range you provide.
