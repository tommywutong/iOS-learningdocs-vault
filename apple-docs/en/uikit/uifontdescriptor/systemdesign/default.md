---
title: default
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 5.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/systemdesign/default
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/systemdesign/default.json'
content_hash: 'sha256:e94f082ca0a2ece6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [SystemDesign](../systemdesign.md)

# default

<sub>Type Property</sub>

The default typeface for an app’s user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: UIFontDescriptor.SystemDesign
```

## Discussion

The returned typeface depends on the system. In iOS, using this constant with [- fontDescriptorWithDesign:](<../withdesign(__).md>) returns SF Pro, while in watchOS that returns SF Compact.

## See Also

### Typeface designs

- [UIFontDescriptorSystemDesignRounded](rounded.md) — The rounded variant of the default typeface.
- [UIFontDescriptorSystemDesignMonospaced](monospaced.md) — The monospace variant of the default typeface.
- [UIFontDescriptorSystemDesignSerif](serif.md) — The serif variant of the default typeface.
