---
title: NSURLCredentialStorageRemoveSynchronizableCredentials
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcredentialstorageremovesynchronizablecredentials
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcredentialstorageremovesynchronizablecredentials'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcredentialstorageremovesynchronizablecredentials.json'
content_hash: 'sha256:3917b16c3e4e0aaf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLCredentialStorageRemoveSynchronizableCredentials

<sub>Global Variable</sub>

The corresponding value is an `NSNumber` object representing a Boolean value that indicates whether credentials which contain the [NSURLCredentialPersistenceSynchronizable](urlcredential/persistence-swift.enum/synchronizable.md) attribute should be removed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLCredentialStorageRemoveSynchronizableCredentials: String
```

## Discussion

If the key is missing or the value is `@NO`, then no attempt will be made to remove such a credential.
