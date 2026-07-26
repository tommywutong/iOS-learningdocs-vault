---
title: 'init(forTrust:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredential/init(fortrust:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/init(fortrust:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/init%28fortrust%3A%29.json'
content_hash: 'sha256:e572cbcfa4d9c451'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# init(forTrust:)

<sub>Initializer</sub>

Creates a URL credential instance for server trust authentication with a given accepted trust.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forTrust trust: SecTrust)
```

## Parameters

- `trust` — The accepted trust.

## Return Value

A new URL credential object, containing the accepted server trust.

## Discussion

Before creating a server trust credential, it is the responsibility of the delegate of an [NSURLConnection](../nsurlconnection.md) instance or an [NSURLDownload](../nsurldownload.md) instance to evaluate the trust. Do this by calling [SecTrustEvaluate(_:_:)](<../../security/sectrustevaluate(____).md>), passing it the trust obtained from the `serverTrust` method of the server’s [URLProtectionSpace](../urlprotectionspace.md) instance. If the trust is invalid, the authentication challenge should be cancelled with [- cancelAuthenticationChallenge:](<../urlauthenticationchallengesender/cancel(__).md>).

## See Also

### Creating a credential

- [- initWithIdentity:certificates:persistence:](<init(identity_certificates_persistence_).md>) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithTrust:](<init(trust_).md>) — Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [- initWithUser:password:persistence:](<init(user_password_persistence_).md>) — Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
