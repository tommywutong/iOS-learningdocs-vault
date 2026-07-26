---
title: 'SSLCopyPeerTrust(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslcopypeertrust(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslcopypeertrust(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopypeertrust%28_%3A_%3A%29.json'
content_hash: 'sha256:9b9a4adbcf1f17b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyPeerTrust(_:_:)

<sub>Function</sub>

Retrieves a trust management object for the certificate used by a session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLCopyPeerTrust(_ context: SSLContext, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `trust` — On return, a trust management object you can use to evaluate trust for the certificate used by the session. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. See [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) for functions to create and evaluate trust management objects. You must call the `CFRelease` function for this object when you are finished with it.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function is valid any time after a handshake attempt.
