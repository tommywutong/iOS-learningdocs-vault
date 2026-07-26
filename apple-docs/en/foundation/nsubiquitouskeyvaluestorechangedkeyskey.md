---
title: NSUbiquitousKeyValueStoreChangedKeysKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsubiquitouskeyvaluestorechangedkeyskey
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestorechangedkeyskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestorechangedkeyskey.json'
content_hash: 'sha256:a6541c000af0cbdf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUbiquitousKeyValueStoreChangedKeysKey

<sub>Global Variable</sub>

A key that indicates which keys changed in the iCloud key-value store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSUbiquitousKeyValueStoreChangedKeysKey: String
```

## Discussion

When the iCloud key-value store changes due to an external source, the system generates a [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) notification. That notification can include this key. The value of this key is an array of strings, each of which contains the name of a key that changed.

## See Also

### Detecting changes to values

- [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) — Posted when the value of one or more keys changes due to incoming data from iCloud.
- [NSUbiquitousKeyValueStoreChangeReasonKey](nsubiquitouskeyvaluestorechangereasonkey.md) — A key that indicates the reason why the key-value store changed.
- [NSUbiquitousKeyValueStoreServerChange](nsubiquitouskeyvaluestoreserverchange.md) — A constant that indicates a value changed in iCloud.
- [NSUbiquitousKeyValueStoreInitialSyncChange](nsubiquitouskeyvaluestoreinitialsyncchange.md) — A constant that indicates the initial attempt to load keys and values from iCloud is in progress.
- [NSUbiquitousKeyValueStoreQuotaViolationChange](nsubiquitouskeyvaluestorequotaviolationchange.md) — A constant that indicates an attempt to write data exceeded the quota limits.
- [NSUbiquitousKeyValueStoreAccountChange](nsubiquitouskeyvaluestoreaccountchange.md) — A constant that indicates the current Apple account changed.
