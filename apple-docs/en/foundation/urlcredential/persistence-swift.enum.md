---
title: URLCredential.Persistence
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredential/persistence-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/persistence-swift.enum.json'
content_hash: 'sha256:f0ca59d07e1f87a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# URLCredential.Persistence

<sub>Enumeration</sub>

Constants that specify how long the credential will be kept.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Persistence
```

## Overview

In iOS, credentials are stored in the app’s keychain, and can be accessed only by that app (and other apps in the same keychain access group, where applicable).

In macOS, credentials are stored in the user’s keychain. The credential’s initial access control list (ACL) allows access only by that app. However, other apps can see that a password exists for a given host, port, and realm combination, and can request that the user grant permission to use that credential.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Persistence strategies

- [NSURLCredentialPersistenceNone](persistence-swift.enum/none.md) — The credential should not be stored.
- [NSURLCredentialPersistenceForSession](persistence-swift.enum/forsession.md) — The credential should be stored only for this session.
- [NSURLCredentialPersistencePermanent](persistence-swift.enum/permanent.md) — The credential should be stored in the keychain.
- [NSURLCredentialPersistenceSynchronizable](persistence-swift.enum/synchronizable.md) — The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.

### Initializers

- [init(rawValue:)](<persistence-swift.enum/init(rawvalue_).md>)

## See Also

### Creating a credential

- [init(forTrust:)](<init(fortrust_).md>) — Creates a URL credential instance for server trust authentication with a given accepted trust.
- [- initWithIdentity:certificates:persistence:](<init(identity_certificates_persistence_).md>) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithTrust:](<init(trust_).md>) — Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [- initWithUser:password:persistence:](<init(user_password_persistence_).md>) — Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
