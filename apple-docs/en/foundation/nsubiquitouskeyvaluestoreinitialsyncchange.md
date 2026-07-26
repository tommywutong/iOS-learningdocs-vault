---
title: NSUbiquitousKeyValueStoreInitialSyncChange
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsubiquitouskeyvaluestoreinitialsyncchange
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreinitialsyncchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestoreinitialsyncchange.json'
content_hash: 'sha256:94f1556351e6c748'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUbiquitousKeyValueStoreInitialSyncChange

<sub>Global Variable</sub>

A constant that indicates the initial attempt to load keys and values from iCloud is in progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSUbiquitousKeyValueStoreInitialSyncChange: Int { get }
```

## Discussion

The system downloads the existing keys and values from iCloud when someone logs into a device using their Apple account. If you try to write a key and value to the iCloud data store while this initial download is in progress, the system generates the [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) notification with this key. Schedule the write operations after a delay to give the system time to download the data and ensure the local copies match the truth in iCloud.

## See Also

### Detecting changes to values

- [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) — Posted when the value of one or more keys changes due to incoming data from iCloud.
- [NSUbiquitousKeyValueStoreChangeReasonKey](nsubiquitouskeyvaluestorechangereasonkey.md) — A key that indicates the reason why the key-value store changed.
- [NSUbiquitousKeyValueStoreChangedKeysKey](nsubiquitouskeyvaluestorechangedkeyskey.md) — A key that indicates which keys changed in the iCloud key-value store.
- [NSUbiquitousKeyValueStoreServerChange](nsubiquitouskeyvaluestoreserverchange.md) — A constant that indicates a value changed in iCloud.
- [NSUbiquitousKeyValueStoreQuotaViolationChange](nsubiquitouskeyvaluestorequotaviolationchange.md) — A constant that indicates an attempt to write data exceeded the quota limits.
- [NSUbiquitousKeyValueStoreAccountChange](nsubiquitouskeyvaluestoreaccountchange.md) — A constant that indicates the current Apple account changed.
