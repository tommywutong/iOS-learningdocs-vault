---
title: metadataProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfiguration/metadataprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/metadataprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfiguration/metadataprovider.json'
content_hash: 'sha256:90d9f8f22938d25b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfiguration](../uiactivityitemsconfiguration.md)

# metadataProvider

<sub>Instance Property</sub>

A closure that provides metadata for the activity items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var metadataProvider: ((UIActivityItemsConfigurationMetadataKey) -> Any?)? { get set }
```

## See Also

### Managing the configuration

- [localObject](localobject.md) — A local object that represents the configuration.
- [perItemMetadataProvider](peritemmetadataprovider.md) — A closure that provides metadata for each activity item.
- [applicationActivitiesProvider](applicationactivitiesprovider.md) — A closure that provides application acitivites for the activity items.
- [UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md) — A structure that defines keys for the metadata associated with an activity items configuration.
