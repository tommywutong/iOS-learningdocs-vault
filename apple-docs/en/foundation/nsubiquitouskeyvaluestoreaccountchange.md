---
title: NSUbiquitousKeyValueStoreAccountChange
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsubiquitouskeyvaluestoreaccountchange
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestoreaccountchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestoreaccountchange.json'
content_hash: 'sha256:1504b42e80c8c058'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUbiquitousKeyValueStoreAccountChange

<sub>Global Variable</sub>

A constant that indicates the current Apple account changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSUbiquitousKeyValueStoreAccountChange: Int { get }
```

## Discussion

When someone changes the Apple account of the current device, the system removes any previous iCloud data and replaces it with data from the new account. Use the new data to configure your app.

## See Also

### Detecting changes to values

- [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) — Posted when the value of one or more keys changes due to incoming data from iCloud.
- [NSUbiquitousKeyValueStoreChangeReasonKey](nsubiquitouskeyvaluestorechangereasonkey.md) — A key that indicates the reason why the key-value store changed.
- [NSUbiquitousKeyValueStoreChangedKeysKey](nsubiquitouskeyvaluestorechangedkeyskey.md) — A key that indicates which keys changed in the iCloud key-value store.
- [NSUbiquitousKeyValueStoreServerChange](nsubiquitouskeyvaluestoreserverchange.md) — A constant that indicates a value changed in iCloud.
- [NSUbiquitousKeyValueStoreInitialSyncChange](nsubiquitouskeyvaluestoreinitialsyncchange.md) — A constant that indicates the initial attempt to load keys and values from iCloud is in progress.
- [NSUbiquitousKeyValueStoreQuotaViolationChange](nsubiquitouskeyvaluestorequotaviolationchange.md) — A constant that indicates an attempt to write data exceeded the quota limits.
