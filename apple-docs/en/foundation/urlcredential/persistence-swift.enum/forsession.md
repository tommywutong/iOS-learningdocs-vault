---
title: URLCredential.Persistence.forSession
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/persistence-swift.enum/forsession
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum/forsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/persistence-swift.enum/forsession.json'
content_hash: 'sha256:06b77fa28e537b6d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLCredential](../../urlcredential.md) · [Persistence](../persistence-swift.enum.md)

# URLCredential.Persistence.forSession

<sub>Case</sub>

The credential should be stored only for this session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case forSession
```

## See Also

### Persistence strategies

- [NSURLCredentialPersistenceNone](none.md) — The credential should not be stored.
- [NSURLCredentialPersistencePermanent](permanent.md) — The credential should be stored in the keychain.
- [NSURLCredentialPersistenceSynchronizable](synchronizable.md) — The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.
