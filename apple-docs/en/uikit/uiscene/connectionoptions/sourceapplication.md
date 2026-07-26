---
title: sourceApplication
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/sourceapplication
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/sourceapplication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/sourceapplication.json'
content_hash: 'sha256:747d600da2d732db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# sourceApplication

<sub>Instance Property</sub>

The bundle ID of the app that originated the request.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sourceApplication: String? { get }
```

## Discussion

If the request originated from another app belonging to your team, UIKit places the bundle ID of that app in this property. If the team identifier of the originating app is different than the team identifier of the current app, this property is `nil`.
