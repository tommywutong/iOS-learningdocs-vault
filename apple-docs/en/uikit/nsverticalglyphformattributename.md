---
title: NSVerticalGlyphFormAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nsverticalglyphformattributename
source_url: 'https://developer.apple.com/documentation/uikit/nsverticalglyphformattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsverticalglyphformattributename.json'
content_hash: 'sha256:1aab6d391b4310d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSVerticalGlyphFormAttributeName

<sub>Global Variable</sub>

The vertical glyph form of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSVerticalGlyphFormAttributeName;
```

## Discussion

The value of this attribute is an [NSNumber](../foundation/nsnumber.md) object containing an integer. The value `0` indicates horizontal text. The value `1` indicates vertical text. In iOS, horizontal text is always used and specifying a different value is undefined.

## See Also

### Deprecated keys

- [NSExpansionAttributeName](nsexpansionattributename.md) — The expansion factor of the text. _(deprecated)_
- [NSObliquenessAttributeName](nsobliquenessattributename.md) — The obliqueness of the text. _(deprecated)_
