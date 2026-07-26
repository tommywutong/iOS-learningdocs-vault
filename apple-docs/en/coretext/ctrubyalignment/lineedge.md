---
title: CTRubyAlignment.lineEdge
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrubyalignment/lineedge
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyalignment/lineedge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyalignment/lineedge.json'
content_hash: 'sha256:56371703defb13b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRubyAlignment](../ctrubyalignment.md)

# CTRubyAlignment.lineEdge

<sub>Case</sub>

Aligns the ruby text to an adjacent line edge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case lineEdge
```

## Discussion

If the ruby text is adjacent to a line edge, Core Text aligns the end of the ruby text adjacent to the line edge to that line edge. This only applies if the width of the ruby text is greater than the width of the base text; otherwise, the alignment is [kCTRubyAlignmentAuto](auto.md).

If the ruby text isn’t adjacent to a line edge, the alignment is [kCTRubyAlignmentAuto](auto.md).

## See Also

### Constants

- [kCTRubyAlignmentAuto](auto.md) — Core Text automatically determines the alignment.
- [kCTRubyAlignmentStart](start.md) — Aligns the ruby text with the starting edge of the base text.
- [kCTRubyAlignmentCenter](center.md) — Centers the ruby text within the width of the base text.
- [kCTRubyAlignmentEnd](end.md) — Aligns the ruby text with the ending edge of the base text.
- [kCTRubyAlignmentDistributeLetter](distributeletter.md) — Distributes the ruby text evenly over the width of the base text, aligning the first and last characters of the ruby text with the first and last characters of the base text.
- [kCTRubyAlignmentDistributeSpace](distributespace.md) — Distributes the ruby text evenly over the width of the base text, adding space before the first and after the last character.
- [kCTRubyAlignmentInvalid](invalid.md) — The alignment is invalid.
