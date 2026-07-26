---
title: NSExpansionAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nsexpansionattributename
source_url: 'https://developer.apple.com/documentation/uikit/nsexpansionattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsexpansionattributename.json'
content_hash: 'sha256:40e301922759fb95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSExpansionAttributeName

<sub>Global Variable</sub>

The expansion factor of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSExpansionAttributeName;
```

## Overview

The value of this attribute is an [NSNumber](../foundation/nsnumber.md) object containing a floating point value indicating the log of the expansion factor to be applied to glyphs. The default value is `0`, indicating no expansion.

## See Also

### Deprecated keys

- [NSObliquenessAttributeName](nsobliquenessattributename.md) — The obliqueness of the text. _(deprecated)_
- [NSVerticalGlyphFormAttributeName](nsverticalglyphformattributename.md) — The vertical glyph form of the text. _(deprecated)_
