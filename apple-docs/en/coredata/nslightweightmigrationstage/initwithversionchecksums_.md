---
title: 'initWithVersionChecksums:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nslightweightmigrationstage/initwithversionchecksums:'
source_url: 'https://developer.apple.com/documentation/coredata/nslightweightmigrationstage/initwithversionchecksums:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nslightweightmigrationstage/initwithversionchecksums%3A.json'
content_hash: 'sha256:41c1d2e1441cfc46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSLightweightMigrationStage](../nslightweightmigrationstage.md)

# initWithVersionChecksums:

<sub>Instance Method</sub>

Creates a lightweight migration stage with the specified version checksums.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithVersionChecksums:(NSArray<NSString *> *) versionChecksums;
```

## Parameters

- `versionChecksums` — The array of version checksums.

## Return Value

An initialized lightweight migration manager, or `nil` if Core Data can’t create one.

## Discussion

To determine an object model’s version checksum, use its [versionChecksum](../nsmanagedobjectmodel/versionchecksum.md) property. Alternatively, you can find the checksum in the versioned model’s `VersionInfo.plist` file or in Xcode’s build log.
