---
title: applicationActivitiesProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemsconfiguration/applicationactivitiesprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/applicationactivitiesprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsconfiguration/applicationactivitiesprovider.json'
content_hash: 'sha256:abd4af3e8be4cb93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemsConfiguration](../uiactivityitemsconfiguration.md)

# applicationActivitiesProvider

<sub>Instance Property</sub>

A closure that provides application acitivites for the activity items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var applicationActivitiesProvider: (() -> [UIActivity])? { get set }
```

## See Also

### Managing the configuration

- [localObject](localobject.md) — A local object that represents the configuration.
- [metadataProvider](metadataprovider.md) — A closure that provides metadata for the activity items.
- [perItemMetadataProvider](peritemmetadataprovider.md) — A closure that provides metadata for each activity item.
- [UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md) — A structure that defines keys for the metadata associated with an activity items configuration.
