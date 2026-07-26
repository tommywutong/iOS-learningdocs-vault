---
title: NSUbiquitousKeyValueStoreChangeReasonKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsubiquitouskeyvaluestorechangereasonkey
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestorechangereasonkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestorechangereasonkey.json'
content_hash: 'sha256:cca3a48166a16740'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUbiquitousKeyValueStoreChangeReasonKey

<sub>Global Variable</sub>

A key that indicates the reason why the key-value store changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSUbiquitousKeyValueStoreChangeReasonKey: String
```

## Discussion

When the iCloud key-value store changes due to an external source, the system generates a [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) notification. That notification can include this key. The value of this key is an [NSNumber](nsnumber.md) that indicates the reason for the change. Possible values include one of the constants [NSUbiquitousKeyValueStoreServerChange](nsubiquitouskeyvaluestoreserverchange.md), [NSUbiquitousKeyValueStoreInitialSyncChange](nsubiquitouskeyvaluestoreinitialsyncchange.md), [NSUbiquitousKeyValueStoreQuotaViolationChange](nsubiquitouskeyvaluestorequotaviolationchange.md), or [NSUbiquitousKeyValueStoreAccountChange](nsubiquitouskeyvaluestoreaccountchange.md).

## See Also

### Detecting changes to values

- [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) — Posted when the value of one or more keys changes due to incoming data from iCloud.
- [NSUbiquitousKeyValueStoreChangedKeysKey](nsubiquitouskeyvaluestorechangedkeyskey.md) — A key that indicates which keys changed in the iCloud key-value store.
- [NSUbiquitousKeyValueStoreServerChange](nsubiquitouskeyvaluestoreserverchange.md) — A constant that indicates a value changed in iCloud.
- [NSUbiquitousKeyValueStoreInitialSyncChange](nsubiquitouskeyvaluestoreinitialsyncchange.md) — A constant that indicates the initial attempt to load keys and values from iCloud is in progress.
- [NSUbiquitousKeyValueStoreQuotaViolationChange](nsubiquitouskeyvaluestorequotaviolationchange.md) — A constant that indicates an attempt to write data exceeded the quota limits.
- [NSUbiquitousKeyValueStoreAccountChange](nsubiquitouskeyvaluestoreaccountchange.md) — A constant that indicates the current Apple account changed.
