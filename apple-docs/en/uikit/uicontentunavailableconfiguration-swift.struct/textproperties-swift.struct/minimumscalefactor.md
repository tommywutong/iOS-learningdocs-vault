---
title: minimumScaleFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailableconfiguration-swift.struct/textproperties-swift.struct/minimumscalefactor
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-swift.struct/textproperties-swift.struct/minimumscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailableconfiguration-swift.struct/textproperties-swift.struct/minimumscalefactor.json'
content_hash: 'sha256:57847c340554eeaf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIContentUnavailableConfiguration](../../uicontentunavailableconfiguration-swift.struct.md) · [TextProperties](../textproperties-swift.struct.md)

# minimumScaleFactor

<sub>Instance Property</sub>

The minimum scale factor for the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumScaleFactor: CGFloat { get set }
```

## Discussion

If you set [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) to `true`, this property defines the smallest multiplier the view uses to fit the text.
