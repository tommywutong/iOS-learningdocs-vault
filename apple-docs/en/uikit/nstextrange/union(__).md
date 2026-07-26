---
title: 'union(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextrange/union(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextrange/union(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextrange/union%28_%3A%29.json'
content_hash: 'sha256:ca21e40bf5a56a07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextRange](../nstextrange.md)

# union(_:)

<sub>Instance Method</sub>

Returns a new text range by forming the union with the text range you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func union(_ textRange: NSTextRange) -> Self
```

## Parameters

- `textRange` — The range to use to create the union.

## Return Value

An [NSTextRange](../nstextrange.md) that represent the union of the two ranges.

## See Also

### Comparing text ranges

- [- textRangeByIntersectingWithTextRange:](<intersection(__).md>) — Returns the range, if any, where two text ranges intersect.
- [- intersectsWithTextRange:](<intersects(__).md>) — Determines if two ranges intersect.
- [- isEqualToTextRange:](<isequal(to_).md>) — Compares two text ranges.
