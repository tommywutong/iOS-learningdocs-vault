---
title: perItemMetadataProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfiguration/peritemmetadataprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/peritemmetadataprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfiguration/peritemmetadataprovider.json'
content_hash: 'sha256:328110f3cc720c2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfiguration](../uiactivityitemsconfiguration.md)

# perItemMetadataProvider

<sub>Instance Property</sub>

A closure that provides metadata for each activity item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var perItemMetadataProvider: ((Int, UIActivityItemsConfigurationMetadataKey) -> Any?)? { get set }
```

## See Also

### Managing the configuration

- [localObject](localobject.md) — A local object that represents the configuration.
- [metadataProvider](metadataprovider.md) — A closure that provides metadata for the activity items.
- [applicationActivitiesProvider](applicationactivitiesprovider.md) — A closure that provides application acitivites for the activity items.
- [UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md) — A structure that defines keys for the metadata associated with an activity items configuration.
