---
title: NSBinaryStoreSecureDecodingClasses
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbinarystoresecuredecodingclasses
source_url: 'https://developer.apple.com/documentation/coredata/nsbinarystoresecuredecodingclasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbinarystoresecuredecodingclasses.json'
content_hash: 'sha256:a2c741a6f842d4c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBinaryStoreSecureDecodingClasses

<sub>Global Variable</sub>

An additional set of classes to use while decoding a binary store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSBinaryStoreSecureDecodingClasses: String
```

## Discussion

This option is preferable to using [NSBinaryStoreInsecureDecodingCompatibilityOption](nsbinarystoreinsecuredecodingcompatibilityoption.md).

## See Also

### Persistent Store Metadata Keys

- [NSBinaryStoreInsecureDecodingCompatibilityOption](nsbinarystoreinsecuredecodingcompatibilityoption.md) — A flag that indicates Core Data decodes the binary store insecurely.
- [NSPersistentStoreRemoteChangeNotificationPostOptionKey](nspersistentstoreremotechangenotificationpostoptionkey.md) — A key that indicates a persistent store posts a remote change notification for every write to the store, including writes by other processes.
- [NSPersistentStoreModelVersionChecksumKey](nspersistentstoremodelversionchecksumkey.md)
