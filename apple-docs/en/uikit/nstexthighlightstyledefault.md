---
title: NSTextHighlightStyleDefault
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstexthighlightstyledefault
source_url: 'https://developer.apple.com/documentation/uikit/nstexthighlightstyledefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexthighlightstyledefault.json'
content_hash: 'sha256:22c133d73e0c2697'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextHighlightStyleDefault

<sub>Global Variable</sub>

The default highlight style to apply to text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSTextHighlightStyle const NSTextHighlightStyleDefault;
```

## Overview

Use this constant as the value for the [NSTextHighlightStyleAttributeName](nstexthighlightstyleattributename.md) attribute. The system applies the default highlight color to your text. To specify a different highlight color, add the [NSTextHighlightColorSchemeAttributeName](nstexthighlightcolorschemeattributename.md) attribute to your text and set its value to the color you want.
