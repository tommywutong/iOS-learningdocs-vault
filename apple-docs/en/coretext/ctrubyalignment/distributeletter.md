---
title: CTRubyAlignment.distributeLetter
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrubyalignment/distributeletter
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyalignment/distributeletter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyalignment/distributeletter.json'
content_hash: 'sha256:9d71ab0d891cc2fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRubyAlignment](../ctrubyalignment.md)

# CTRubyAlignment.distributeLetter

<sub>Case</sub>

Distributes the ruby text evenly over the width of the base text, aligning the first and last characters of the ruby text with the first and last characters of the base text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case distributeLetter
```

## Discussion

If the width of the ruby text is less than the width of the base text, Core Text evenly distributes the ruby text over the width of the base text. The first character of the ruby text aligns with the first character of the base text, and the last character of the ruby text aligns with the last character of the base text.

If the width of the base text is less than the width of the ruby text, Core Text evenly distributes the base text over the width of the ruby text.

## See Also

### Constants

- [kCTRubyAlignmentAuto](auto.md) — Core Text automatically determines the alignment.
- [kCTRubyAlignmentStart](start.md) — Aligns the ruby text with the starting edge of the base text.
- [kCTRubyAlignmentCenter](center.md) — Centers the ruby text within the width of the base text.
- [kCTRubyAlignmentEnd](end.md) — Aligns the ruby text with the ending edge of the base text.
- [kCTRubyAlignmentDistributeSpace](distributespace.md) — Distributes the ruby text evenly over the width of the base text, adding space before the first and after the last character.
- [kCTRubyAlignmentLineEdge](lineedge.md) — Aligns the ruby text to an adjacent line edge.
- [kCTRubyAlignmentInvalid](invalid.md) — The alignment is invalid.
