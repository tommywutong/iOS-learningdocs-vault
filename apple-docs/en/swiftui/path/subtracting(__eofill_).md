---
title: 'subtracting(_:eoFill:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/subtracting(_:eofill:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/subtracting(_:eofill:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/subtracting%28_%3Aeofill%3A%29.json'
content_hash: 'sha256:fe31a45dc9c9a5ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# subtracting(_:eoFill:)

<sub>Instance Method</sub>

Returns a new path with filled regions from this path that are not in the given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subtracting(_ other: Path, eoFill: Bool = false) -> Path
```

## Parameters

- `other` — The path to subtract.

- `eoFill` — Whether to use the even-odd rule for determining which areas to treat as the interior of the paths (if true), or the non-zero rule (if false).

## Return Value

A new path.

## Discussion

The filled region of the resulting path is the filled region of this path with the filled region `other` removed from it.

Any unclosed subpaths in either path are assumed to be closed. The result of filling this path using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on the path

- [addRoundedRect(in:cornerSize:style:transform:)](<addroundedrect(in_cornersize_style_transform_).md>) — Adds a rounded rectangle to the path.
- [intersection(_:eoFill:)](<intersection(__eofill_).md>) — Returns a new path with filled regions common to both paths.
- [lineIntersection(_:eoFill:)](<lineintersection(__eofill_).md>) — Returns a new path with a line from this path that overlaps the filled regions of the given path.
- [lineSubtraction(_:eoFill:)](<linesubtraction(__eofill_).md>) — Returns a new path with a line from this path that does not overlap the filled region of the given path.
- [normalized(eoFill:)](<normalized(eofill_).md>) — Returns a new weakly-simple copy of this path.
- [symmetricDifference(_:eoFill:)](<symmetricdifference(__eofill_).md>) — Returns a new path with filled regions either from this path or the given path, but not in both.
- [union(_:eoFill:)](<union(__eofill_).md>) — Returns a new path with filled regions in either this path or the given path.
