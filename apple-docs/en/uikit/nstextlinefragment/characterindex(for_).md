---
title: 'characterIndex(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlinefragment/characterindex(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment/characterindex(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment/characterindex%28for%3A%29.json'
content_hash: 'sha256:4900a1c3195f54e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLineFragment](../nstextlinefragment.md)

# characterIndex(for:)

<sub>Instance Method</sub>

Returns character index for a point inside the line fragment coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func characterIndex(for point: CGPoint) -> Int
```

## Parameters

- `point` — The distance is from the upstream edge.

## Return Value

An integer that represents the character index at `point`.

## See Also

### Finding specific text

- [- fractionOfDistanceThroughGlyphForPoint:](<fractionofdistancethroughglyph(for_).md>) — Returns character index for a point inside the line fragment coordinate system.
- [- locationForCharacterAtIndex:](<locationforcharacter(at_).md>) — Returns the location of the character at the specified index.
