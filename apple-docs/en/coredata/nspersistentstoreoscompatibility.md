---
title: NSPersistentStoreOSCompatibility
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoreoscompatibility
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreoscompatibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreoscompatibility.json'
content_hash: 'sha256:c8c4a2b5aa3b3c90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreOSCompatibility

<sub>Global Variable</sub>

Key to represent the earliest version of the operation system that the persistent store supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSPersistentStoreOSCompatibility: String
```

## Discussion

The corresponding value is an `NSNumber` object that takes the form of the constants defined by the availability macros defined in `/usr/include/AvailabilityMacros.h`; for example `1040` represents OS X version 10.4.0.

Backward compatibility may preclude some features.

## See Also

### Constants

- [NSStoreModelVersionHashesKey](nsstoremodelversionhasheskey.md) — Key to represent the version hash information for the model used to create the store.
- [NSStoreModelVersionIdentifiersKey](nsstoremodelversionidentifierskey.md) — Key to represent the version identifiers for the model used to create the store.
