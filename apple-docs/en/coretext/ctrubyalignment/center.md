---
title: CTRubyAlignment.center
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrubyalignment/center
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyalignment/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyalignment/center.json'
content_hash: 'sha256:ff93a9f3cd2ae8ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRubyAlignment](../ctrubyalignment.md)

# CTRubyAlignment.center

<sub>Case</sub>

Centers the ruby text within the width of the base text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case center
```

## Discussion

If the ruby text is wider than the base text, Core Text centers the base text within the width of the ruby text.

## See Also

### Constants

- [kCTRubyAlignmentAuto](auto.md) — Core Text automatically determines the alignment.
- [kCTRubyAlignmentStart](start.md) — Aligns the ruby text with the starting edge of the base text.
- [kCTRubyAlignmentEnd](end.md) — Aligns the ruby text with the ending edge of the base text.
- [kCTRubyAlignmentDistributeLetter](distributeletter.md) — Distributes the ruby text evenly over the width of the base text, aligning the first and last characters of the ruby text with the first and last characters of the base text.
- [kCTRubyAlignmentDistributeSpace](distributespace.md) — Distributes the ruby text evenly over the width of the base text, adding space before the first and after the last character.
- [kCTRubyAlignmentLineEdge](lineedge.md) — Aligns the ruby text to an adjacent line edge.
- [kCTRubyAlignmentInvalid](invalid.md) — The alignment is invalid.
