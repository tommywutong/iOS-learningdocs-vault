---
title: URLCredential.Persistence.permanent
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/persistence-swift.enum/permanent
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum/permanent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/persistence-swift.enum/permanent.json'
content_hash: 'sha256:e2a1d9e3dce3caff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLCredential](../../urlcredential.md) · [Persistence](../persistence-swift.enum.md)

# URLCredential.Persistence.permanent

<sub>Case</sub>

The credential should be stored in the keychain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case permanent
```

## See Also

### Persistence strategies

- [NSURLCredentialPersistenceNone](none.md) — The credential should not be stored.
- [NSURLCredentialPersistenceForSession](forsession.md) — The credential should be stored only for this session.
- [NSURLCredentialPersistenceSynchronizable](synchronizable.md) — The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.
