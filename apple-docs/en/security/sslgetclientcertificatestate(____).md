---
title: 'SSLGetClientCertificateState(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.3+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslgetclientcertificatestate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslgetclientcertificatestate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetclientcertificatestate%28_%3A_%3A%29.json'
content_hash: 'sha256:331fcc20426d6650'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetClientCertificateState(_:_:)

<sub>Function</sub>

Retrieves the exchange status of the client certificate.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLGetClientCertificateState(_ context: SSLContext, _ clientState: UnsafeMutablePointer<SSLClientCertificateState>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `clientState` — On return, a pointer to a value indicating the state of the client certificate exchange. See [SSLClientCertificateState](sslclientcertificatestate.md) for a list of possible values.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The value returned reflects the latest change in the state of the client certificate exchange. If either peer initiates a renegotiation attempt, Secure Transport resets the state to `kSSLClientCertNone`.
