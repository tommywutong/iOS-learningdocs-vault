---
title: 'SSLSetCertificate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetcertificate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetcertificate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetcertificate%28_%3A_%3A%29.json'
content_hash: 'sha256:13fd53a675999fa3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetCertificate(_:_:)

<sub>Function</sub>

Specifies this connection’s certificate or certificates.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetCertificate(_ context: SSLContext, _ certRefs: CFArray?) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `certRefs` — The certificates to set. This array contains items of type `SecCertificateRef`, except for `certRefs[0]`, which is of type `SecIdentityRef`.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Setting the certificate or certificates is mandatory for server connections, but is optional for clients. Specifying a certificate for a client enables SSL client-side authentication. You must place in `certRefs[0]` a `SecIdentityRef` object that identifies the leaf certificate and its corresponding private key. Specifying a root certificate is optional; if it’s not specified, the root certificate that verifies the certificate chain specified here must be present in the system wide set of trusted anchor certificates.

This function must be called before calling [SSLHandshake](<sslhandshake(__).md>), or immediately after [SSLHandshake](<sslhandshake(__).md>) has returned `errSSLClientCertRequested` (that is, before the handshake is resumed by calling [SSLHandshake](<sslhandshake(__).md>) again).

Secure Transport assumes the following:

- The certificate references remain valid for the lifetime of the session.
- The identity specified in `certRefs[0]` is capable of signing.

The required capabilities of the identity specified in `certRefs[0]`—and of the optional certificate specified in the [SSLSetEncryptionCertificate](<sslsetencryptioncertificate(____).md>) function—are highly dependent on the application. For example, to work as a server with Netscape clients, the identity specified here must be capable of both signing and encrypting. Use the [SSLCopyDistinguishedNames](<sslcopydistinguishednames(____).md>) function to get a list of certificates acceptable to the server.
