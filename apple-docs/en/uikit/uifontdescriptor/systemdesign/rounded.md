---
title: rounded
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 5.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/systemdesign/rounded
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign/rounded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/systemdesign/rounded.json'
content_hash: 'sha256:0c0199ec5d50a714'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [SystemDesign](../systemdesign.md)

# rounded

<sub>Type Property</sub>

The rounded variant of the default typeface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let rounded: UIFontDescriptor.SystemDesign
```

## Discussion

The returned typeface depends on the system. iOS returns SF Pro Rounded, while watchOS returns SF Compact Rounded.

## See Also

### Typeface designs

- [UIFontDescriptorSystemDesignDefault](default.md) — The default typeface for an app’s user interface.
- [UIFontDescriptorSystemDesignMonospaced](monospaced.md) — The monospace variant of the default typeface.
- [UIFontDescriptorSystemDesignSerif](serif.md) — The serif variant of the default typeface.
