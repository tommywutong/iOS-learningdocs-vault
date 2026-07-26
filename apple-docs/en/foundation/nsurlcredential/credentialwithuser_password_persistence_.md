---
title: 'credentialWithUser:password:persistence:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcredential/credentialwithuser:password:persistence:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcredential/credentialwithuser:password:persistence:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcredential/credentialwithuser%3Apassword%3Apersistence%3A.json'
content_hash: 'sha256:57d2473e0560ad4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# credentialWithUser:password:persistence:

<sub>Type Method</sub>

Creates a URL credential instance for internet password authentication with a given user name and password, using a given persistence setting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSURLCredential *) credentialWithUser:(NSString *) user password:(NSString *) password persistence:(NSURLCredentialPersistence) persistence;
```

## Parameters

- `user` — The user for the credential.

- `password` — The password for `user`.

- `persistence` — A [Persistence](../urlcredential/persistence-swift.enum.md) value indicating whether the credential should be stored permanently, for the duration of the current session, or not at all.

## Return Value

A new URL credential object with user name `user`, password `password`, and using persistence setting `persistence`.

## Discussion

If `persistence` is [NSURLCredentialPersistencePermanent](../urlcredential/persistence-swift.enum/permanent.md), the credential is stored in the keychain. If `persistence` is [NSURLCredentialPersistenceSynchronizable](../urlcredential/persistence-swift.enum/synchronizable.md), it is also synchronized to the user’s other devices.

## See Also

### Creating a credential

- [credentialWithIdentity:certificates:persistence:](credentialwithidentity_certificates_persistence_.md) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithIdentity:certificates:persistence:](<../urlcredential/init(identity_certificates_persistence_).md>) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithTrust:](<../urlcredential/init(trust_).md>) — Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [- initWithUser:password:persistence:](<../urlcredential/init(user_password_persistence_).md>) — Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [Persistence](../urlcredential/persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
