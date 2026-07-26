---
title: minimumScaleFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentunavailabletextproperties/minimumscalefactor
source_url: 'https://developer.apple.com/documentation/uikit/uicontentunavailabletextproperties/minimumscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentunavailabletextproperties/minimumscalefactor.json'
content_hash: 'sha256:899fe26024eb70e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentUnavailableTextProperties](../uicontentunavailabletextproperties.md)

# minimumScaleFactor

<sub>Instance Property</sub>

The minimum scale factor for the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat minimumScaleFactor;
```

## Discussion

If you set [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) to `YES`, this property defines the smallest multiplier the view uses to fit the text.
