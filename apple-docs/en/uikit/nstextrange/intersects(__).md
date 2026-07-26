---
title: 'intersects(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextrange/intersects(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextrange/intersects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextrange/intersects%28_%3A%29.json'
content_hash: 'sha256:06d82390f0949141'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextRange](../nstextrange.md)

# intersects(_:)

<sub>Instance Method</sub>

Determines if two ranges intersect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func intersects(_ textRange: NSTextRange) -> Bool
```

## Parameters

- `textRange` — The range used to compare against the current range to evaluate for differences.

## Return Value

Returns `true` if the ranges intersect.

## See Also

### Comparing text ranges

- [- textRangeByIntersectingWithTextRange:](<intersection(__).md>) — Returns the range, if any, where two text ranges intersect.
- [- isEqualToTextRange:](<isequal(to_).md>) — Compares two text ranges.
- [- textRangeByFormingUnionWithTextRange:](<union(__).md>) — Returns a new text range by forming the union with the text range you provide.
