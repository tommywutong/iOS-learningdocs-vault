---
title: 'init(trust:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredential/init(trust:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredential/init(trust:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredential/init%28trust%3A%29.json'
content_hash: 'sha256:c40c71a0000cd6eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# init(trust:)

<sub>Initializer</sub>

Creates a URL credential instance for server trust authentication, initialized with a accepted trust.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(trust: SecTrust)
```

## Parameters

- `trust` — The accepted trust.

## Return Value

A new URL credential object, containing the provided server trust.

## Discussion

Before your implementation of [- URLSession:task:didReceiveChallenge:completionHandler:](<../urlsessiontaskdelegate/urlsession(__task_didreceive_completionhandler_).md>) uses this initializer to create a server trust credential, you are responsible for evaluating the received [SecTrust](../../security/sectrust.md) instance. You get this [serverTrust](../urlprotectionspace/servertrust.md) from the [protectionSpace](../urlauthenticationchallenge/protectionspace.md) of the [URLAuthenticationChallenge](../urlauthenticationchallenge.md) parameter that is passed to your delegate method. Pass the trust instance to [SecTrustEvaluate(_:_:)](<../../security/sectrustevaluate(____).md>) to evaluate it. If this call indicates the trust is invalid, you should cancel the challenge by passing the [NSURLSessionAuthChallengeCancelAuthenticationChallenge](../urlsession/authchallengedisposition/cancelauthenticationchallenge.md) disposition to the completion handler.

## See Also

### Creating a credential

- [init(forTrust:)](<init(fortrust_).md>) — Creates a URL credential instance for server trust authentication with a given accepted trust.
- [- initWithIdentity:certificates:persistence:](<init(identity_certificates_persistence_).md>) — Creates a URL credential instance for resolving a client certificate authentication challenge.
- [- initWithUser:password:persistence:](<init(user_password_persistence_).md>) — Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [Persistence](persistence-swift.enum.md) — Constants that specify how long the credential will be kept.
