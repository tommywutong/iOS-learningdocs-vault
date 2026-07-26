---
title: NSBinaryStoreInsecureDecodingCompatibilityOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbinarystoreinsecuredecodingcompatibilityoption
source_url: 'https://developer.apple.com/documentation/coredata/nsbinarystoreinsecuredecodingcompatibilityoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbinarystoreinsecuredecodingcompatibilityoption.json'
content_hash: 'sha256:ed2b4bb0ca47a830'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBinaryStoreInsecureDecodingCompatibilityOption

<sub>Global Variable</sub>

A flag that indicates Core Data decodes the binary store insecurely.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSBinaryStoreInsecureDecodingCompatibilityOption: String
```

## Discussion

Use the [NSBinaryStoreSecureDecodingClasses](nsbinarystoresecuredecodingclasses.md) option instead, if possible, to allow Core Data to securely decode the binary store.

If a store has metadata or transformable properties that contain nonstandard classes, this option may be appropriate. Apps linked before the availability date default to using this option.

## See Also

### Persistent Store Metadata Keys

- [NSBinaryStoreSecureDecodingClasses](nsbinarystoresecuredecodingclasses.md) — An additional set of classes to use while decoding a binary store.
- [NSPersistentStoreRemoteChangeNotificationPostOptionKey](nspersistentstoreremotechangenotificationpostoptionkey.md) — A key that indicates a persistent store posts a remote change notification for every write to the store, including writes by other processes.
- [NSPersistentStoreModelVersionChecksumKey](nspersistentstoremodelversionchecksumkey.md)
