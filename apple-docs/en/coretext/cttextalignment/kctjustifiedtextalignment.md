---
title: kCTJustifiedTextAlignment
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.11 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coretext/cttextalignment/kctjustifiedtextalignment
source_url: 'https://developer.apple.com/documentation/coretext/cttextalignment/kctjustifiedtextalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttextalignment/kctjustifiedtextalignment.json'
content_hash: 'sha256:8d7786a446cc95c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTTextAlignment](../cttextalignment.md)

# kCTJustifiedTextAlignment

<sub>Type Property</sub>

Text is fully justified.

> [!warning] Deprecated
> Use [kCTTextAlignmentJustified](justified.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var kCTJustifiedTextAlignment: CTTextAlignment { get }
```

## Discussion

The last line in a paragraph is naturally aligned.

## See Also

### Deprecated

- [kCTLeftTextAlignment](kctlefttextalignment.md) — Text is visually left-aligned. _(deprecated)_
- [kCTRightTextAlignment](kctrighttextalignment.md) — Text is visually right-aligned. _(deprecated)_
- [kCTCenterTextAlignment](kctcentertextalignment.md) — Text is visually center-aligned. _(deprecated)_
- [kCTNaturalTextAlignment](kctnaturaltextalignment.md) — Text uses the natural alignment of the text’s script. _(deprecated)_
