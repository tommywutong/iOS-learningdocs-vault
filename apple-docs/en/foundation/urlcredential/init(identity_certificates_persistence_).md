---
title: 'init(identity:certificates:persistence:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredential/init(identity:certificates:persistence:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/init(identity:certificates:persistence:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/init%28identity%3Acertificates%3Apersistence%3A%29.json'
content_hash: 'sha256:5978e54b09d52d57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# init(identity:certificates:persistence:)

<sub>Initializer</sub>

Creates a URL credential instance for resolving a client certificate authentication challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(identity: SecIdentity, certificates certArray: [Any]?, persistence: URLCredential.Persistence)
```

## Parameters

- `identity` — The identity for the credential.

- `certArray` — An array of one or more `SecCertificateRef` objects representing intermediate certificates leading from the identity’s certificate to a trusted root, or `nil` if the server does not need any intermediate certificates to authenticate the client.

- `persistence` — The method ignores this parameter; you should supply a value of [NSURLCredentialPersistenceForSession](persistence-swift.enum/forsession.md) because that most accurately reflects the actual behaviour.

## Return Value

A new URL credential object, using the provided identity and, optionally, an array of intermediate certificates.

## Discussion

When you receive a client certificate authentication challenge ([NSURLAuthenticationMethodClientCertificate](../nsurlauthenticationmethodclientcertificate.md)) and want to resolve it successfully, you must supply a credential created using this initializer.

In most cases you should pass `nil` to the `certArray` parameter. You only need to supply an array of intermediate certificates if the server needs those intermediate certificates to authenticate the client. Typically this isn’t necessary because the server already has a copy of the relevant intermediate certificates.

## See Also

### Creating a credential

- [init(forTrust:)](<init(fortrust_).md>) — Creates a URL credential instance for server trust authentication with a given accepted trust.
- [- initWithTrust:](<init(trust_).md>) — Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [- initWithUser:password:persistence:](<init(user_password_persistence_).md>) — Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
