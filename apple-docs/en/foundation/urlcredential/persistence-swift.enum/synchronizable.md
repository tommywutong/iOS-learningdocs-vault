---
title: URLCredential.Persistence.synchronizable
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/persistence-swift.enum/synchronizable
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum/synchronizable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/persistence-swift.enum/synchronizable.json'
content_hash: 'sha256:09468ba2d61bfe96'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLCredential](../../urlcredential.md) · [Persistence](../persistence-swift.enum.md)

# URLCredential.Persistence.synchronizable

<sub>Case</sub>

The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case synchronizable
```

## See Also

### Persistence strategies

- [NSURLCredentialPersistenceNone](none.md) — The credential should not be stored.
- [NSURLCredentialPersistenceForSession](forsession.md) — The credential should be stored only for this session.
- [NSURLCredentialPersistencePermanent](permanent.md) — The credential should be stored in the keychain.
