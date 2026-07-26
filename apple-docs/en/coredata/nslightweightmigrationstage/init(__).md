---
title: 'init(_:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+, Swift 5.8+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nslightweightmigrationstage/init(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nslightweightmigrationstage/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nslightweightmigrationstage/init%28_%3A%29.json'
content_hash: 'sha256:9f3319530a56751d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSLightweightMigrationStage](../nslightweightmigrationstage.md)

# init(_:)

<sub>Initializer</sub>

Creates a lightweight migration stage with the specified version checksums.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(_ checksums: [String])
```

## Parameters

- `checksums` — The array of version checksums.

## Discussion

To determine an object model’s version checksum, use its [versionChecksum](../nsmanagedobjectmodel/versionchecksum.md) property. Alternatively, you can find the checksum in the versioned model’s `VersionInfo.plist` file or in Xcode’s build log.
