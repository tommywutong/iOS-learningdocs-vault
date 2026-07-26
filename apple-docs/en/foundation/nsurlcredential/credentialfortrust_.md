---
title: 'credentialForTrust:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlcredential/credentialfortrust:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcredential/credentialfortrust:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcredential/credentialfortrust%3A.json'
content_hash: 'sha256:8fc83b3cc0bfae46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredential](../urlcredential.md)

# credentialForTrust:

<sub>Type Method</sub>

Creates a URL credential instance for server trust authentication with a given accepted trust.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSURLCredential *) credentialForTrust:(SecTrustRef) trust;
```

## Parameters

- `trust` — The accepted trust.

## Return Value

A new URL credential object, containing the accepted server trust.

## Discussion

Before creating a server trust credential, it is the responsibility of the delegate of an [NSURLConnection](../nsurlconnection.md) instance or an [NSURLDownload](../nsurldownload.md) instance to evaluate the trust. Do this by calling `SecTrustEvaluate`, passing it the trust obtained from the `serverTrust` method of the server’s [URLProtectionSpace](../urlprotectionspace.md) instance. If the trust is invalid, the authentication challenge should be cancelled with the [URLAuthenticationChallengeSender](../urlauthenticationchallengesender.md) protocol’s `cancelAuthenticationChallenge:` method.
