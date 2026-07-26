---
title: 'SSLHandshake(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslhandshake(_:)'
source_url: 'https://developer.apple.com/documentation/security/sslhandshake(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslhandshake%28_%3A%29.json'
content_hash: 'sha256:581c77653248b2be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLHandshake(_:)

<sub>Function</sub>

Performs the SSL handshake.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLHandshake(_ context: SSLContext) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

On successful return, the session is ready for normal secure communication using the functions [SSLRead](<sslread(________).md>) and [SSLWrite](<sslwrite(________).md>).

If it finds any problems with the peer’s certificate chain, Secure Transport aborts the handshake. You can use the [SSLCopyPeerCertificates](sslcopypeercertificates.md) function to see the peer’s certificate chain. This function can return a wide variety of result codes, including the following:

- `errSSLUnknownRootCert`—The peer has a valid certificate chain, but the root of the chain is not a known anchor certificate.
- `errSSLNoRootCert`—The peer’s certificate chain was not verifiable to a root certificate.
- `errSSLCertExpired`—The peer’s certificate chain has one or more expired certificates.
- `errSSLXCertChainInvalid`—The peer has an invalid certificate chain; for example, signature verification within the chain failed, or no certificates were found.
- `errSSLClientCertRequested`—The server has requested a client certificate. This result is returned only if you called the [SSLSetSessionOption](<sslsetsessionoption(______).md>) function to set the `kSSLSessionOptionBreakOnCertRequested` option. After receiving this result, you must call the [SSLSetCertificate](<sslsetcertificate(____).md>) function to return the client certificate, and then call [SSLHandshake](<sslhandshake(__).md>) again to resume the handshake. Use the [SSLCopyDistinguishedNames](<sslcopydistinguishednames(____).md>) function to obtain a list of certificates acceptable to the server.
- `errSSLServerAuthCompleted`—The server authentication portion of the handshake is complete. This result is returned only if you called the [SSLSetSessionOption](<sslsetsessionoption(______).md>) function to set the `kSSLSessionOptionBreakOnServerAuth` option, and provides an opportunity to perform application-specific server verification before calling [SSLHandshake](<sslhandshake(__).md>) again to continue.

Note that in macOS prior to version 10.8, you must also explicitly call [SSLSetEnableCertVerify](sslsetenablecertverify.md) to disable verification.

A return value of `errSSLWouldBlock` indicates that the [SSLHandshake](<sslhandshake(__).md>) function must be called again until a different result code is returned.
