---
title: previewProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfiguration/previewprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/previewprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfiguration/previewprovider.json'
content_hash: 'sha256:f41f07b483ec9119'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfiguration](../uiactivityitemsconfiguration.md)

# previewProvider

<sub>Instance Property</sub>

A closure that provides previews for the activity items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var previewProvider: ((Int, UIActivityItemsConfigurationPreviewIntent, CGSize) -> NSItemProvider?)? { get set }
```

## See Also

### Managing previews

- [UIActivityItemsConfigurationPreviewIntent](../uiactivityitemsconfigurationpreviewintent.md) — A structure that specifies the types of activity item previews.
