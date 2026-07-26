---
title: 'locationForCharacter(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlinefragment/locationforcharacter(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment/locationforcharacter(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment/locationforcharacter%28at%3A%29.json'
content_hash: 'sha256:05d8ee11958902e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLineFragment](../nstextlinefragment.md)

# locationForCharacter(at:)

<sub>Instance Method</sub>

Returns the location of the character at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func locationForCharacter(at index: Int) -> CGPoint
```

## Parameters

- `index` — An integer that represents the position in the text.

## Return Value

A [CGPoint](../../corefoundation/cgpoint.md) that’s on the upstream edge of the glyph. It’s in the coordinate system relative to the line fragment origin.

## See Also

### Finding specific text

- [- characterIndexForPoint:](<characterindex(for_).md>) — Returns character index for a point inside the line fragment coordinate system.
- [- fractionOfDistanceThroughGlyphForPoint:](<fractionofdistancethroughglyph(for_).md>) — Returns character index for a point inside the line fragment coordinate system.
