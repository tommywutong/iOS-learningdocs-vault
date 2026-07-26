---
title: 'fractionOfDistanceThroughGlyph(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlinefragment/fractionofdistancethroughglyph(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment/fractionofdistancethroughglyph(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment/fractionofdistancethroughglyph%28for%3A%29.json'
content_hash: 'sha256:54bbb727c01e92c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLineFragment](../nstextlinefragment.md)

# fractionOfDistanceThroughGlyph(for:)

<sub>Instance Method</sub>

Returns character index for a point inside the line fragment coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func fractionOfDistanceThroughGlyph(for point: CGPoint) -> CGFloat
```

## Parameters

- `point` — A [CGPoint](../../corefoundation/cgpoint.md) that represents the point inside the line fragment.

## Return Value

The fraction of distance from the upstream edge.

## See Also

### Finding specific text

- [- characterIndexForPoint:](<characterindex(for_).md>) — Returns character index for a point inside the line fragment coordinate system.
- [- locationForCharacterAtIndex:](<locationforcharacter(at_).md>) — Returns the location of the character at the specified index.
