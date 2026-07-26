---
title: versionChecksums
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nslightweightmigrationstage/versionchecksums
source_url: 'https://developer.apple.com/documentation/coredata/nslightweightmigrationstage/versionchecksums'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nslightweightmigrationstage/versionchecksums.json'
content_hash: 'sha256:f537fbb55658b5e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSLightweightMigrationStage](../nslightweightmigrationstage.md)

# versionChecksums

<sub>Instance Property</sub>

The array of version checksums.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionChecksums: [String] { get }
```

## Discussion

Core Data sets this property to the checksum you specify when creating the lightweight migration stage.
