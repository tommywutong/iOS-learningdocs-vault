---
title: 'init(user:password:persistence:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredential/init(user:password:persistence:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/init(user:password:persistence:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/init%28user%3Apassword%3Apersistence%3A%29.json'
content_hash: 'sha256:c6a0940174a35da7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# init(user:password:persistence:)

<sub>Initializer</sub>

Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(user: String, password: String, persistence: URLCredential.Persistence)
```

## Parameters

- `user` — The user for the credential.

- `password` — The password for `user`.

- `persistence` — A [Persistence](persistence-swift.enum.md) value indicating whether the credential should be stored permanently, for the duration of the current session, or not at all.

## Return Value

An instance of [URLCredential](../urlcredential.md), initialized with user name `user`, password `password`, and using persistence setting `persistence`.

## Discussion

If `persistence` is [NSURLCredentialPersistencePermanent](persistence-swift.enum/permanent.md), the credential is stored in the keychain. If `persistence` is [NSURLCredentialPersistenceSynchronizable](persistence-swift.enum/synchronizable.md), it is also stored to the user’s other devices.

## See Also

### Creating a credential

- [init(forTrust:)](<init(fortrust_).md>) — Creates a URL credential instance for server trust authentication with a given accepted trust.
- [- initWithIdentity:certificates:persistence:](<init(identity_certificates_persistence_).md>) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithTrust:](<init(trust_).md>) — Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
