---
title: 'credentialWithIdentity:certificates:persistence:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcredential/credentialwithidentity:certificates:persistence:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcredential/credentialwithidentity:certificates:persistence:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcredential/credentialwithidentity%3Acertificates%3Apersistence%3A.json'
content_hash: 'sha256:4d557755a9316b22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# credentialWithIdentity:certificates:persistence:

<sub>Type Method</sub>

Creates a URL credential instance for resolving a client certificate authentication challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSURLCredential *) credentialWithIdentity:(SecIdentityRef) identity certificates:(NSArray *) certArray persistence:(NSURLCredentialPersistence) persistence;
```

## Parameters

- `identity` — The identity for the credential.

- `certArray` — An array of one or more `SecCertificateRef` objects representing intermediate certificates leading from the identity’s certificate to a trusted root, or `nil` if the server does not need any intermediate certificates to authenticate the client.

- `persistence` — The method ignores this parameter; you should supply a value of [NSURLCredentialPersistenceForSession](../urlcredential/persistence-swift.enum/forsession.md) because that most accurately reflects the actual behaviour.

## Return Value

A new URL credential object, using the provided identity and, optionally, an array of intermediate certificates.

## Discussion

When you receive a client certificate authentication challenge ([NSURLAuthenticationMethodClientCertificate](../nsurlauthenticationmethodclientcertificate.md)) and want to resolve it successfully, you must supply a credential created using this method.

In most cases you should pass `nil` to the `certArray` parameter. You only need to supply an array of intermediate certificates if the server needs those intermediate certificates to authenticate the client. Typically this isn’t necessary because the server already has a copy of the relevant intermediate certificates.

## See Also

### Creating a credential

- [credentialWithUser:password:persistence:](credentialwithuser_password_persistence_.md) — Creates a URL credential instance for internet password authentication with a given user name and password, using a given persistence setting.
- [- initWithIdentity:certificates:persistence:](<../urlcredential/init(identity_certificates_persistence_).md>) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithTrust:](<../urlcredential/init(trust_).md>) — Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [- initWithUser:password:persistence:](<../urlcredential/init(user_password_persistence_).md>) — Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [Persistence](../urlcredential/persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
