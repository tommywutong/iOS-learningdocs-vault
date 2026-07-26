---
title: CTRubyPosition.interCharacter
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrubyposition/intercharacter
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyposition/intercharacter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyposition/intercharacter.json'
content_hash: 'sha256:b0dc96042dfcde59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRubyPosition](../ctrubyposition.md)

# CTRubyPosition.interCharacter

<sub>Case</sub>

The ruby text is positioned to the right of the base text, regardless of whether it’s horizontal or vertical.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case interCharacter
```

## Discussion

This is the way that Bopomofo annotations are attached to Chinese text in Taiwan.

## See Also

### Constants

- [kCTRubyPositionBefore](before.md) — The ruby text is positioned before the base text, appearing above horizontal text and to the right of vertical text.
- [kCTRubyPositionAfter](after.md) — The ruby text is positioned after the base text, appearing below horizontal text and to the left of vertical text.
- [kCTRubyPositionInline](inline.md) — The ruby text follows the base text with no special styling.
- [kCTRubyPositionCount](count.md) — A constant that accounts for all ruby positions during ruby annotation creation.
