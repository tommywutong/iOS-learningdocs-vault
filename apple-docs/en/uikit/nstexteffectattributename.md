---
title: NSTextEffectAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstexteffectattributename
source_url: 'https://developer.apple.com/documentation/uikit/nstexteffectattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexteffectattributename.json'
content_hash: 'sha256:e974092610cad95d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextEffectAttributeName

<sub>Global Variable</sub>

An attribute that applies a text effect to the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSTextEffectAttributeName;
```

## Overview

The value of this attribute is an [NSString](../foundation/nsstring.md) object. Use this attribute to specify a text effect, such as [NSTextEffectLetterpressStyle](nstexteffectletterpressstyle.md). The default value of this property is `nil`, indicating no text effect.

## See Also

### Getting text attribute keys

- [NSLinkAttributeName](nslinkattributename.md) — The link for the text.
- [NSShadowAttributeName](nsshadowattributename.md) — The shadow of the text.
- [NSTextHighlightColorSchemeAttributeName](nstexthighlightcolorschemeattributename.md) — The custom highlight color to apply to the text.
- [NSTextHighlightStyleAttributeName](nstexthighlightstyleattributename.md) — An attribute that adds a highlight color to the text to emphasize it.
- [UITextItemTagAttributeName](uitextitemtagattributename.md) — The name of a custom tag associated with a text item.
- [NSWritingToolsExclusionAttributeName](nswritingtoolsexclusionattributename.md)
