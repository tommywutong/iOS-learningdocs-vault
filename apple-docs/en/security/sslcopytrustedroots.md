---
title: SSLCopyTrustedRoots
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslcopytrustedroots
source_url: 'https://developer.apple.com/documentation/security/sslcopytrustedroots'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopytrustedroots.json'
content_hash: 'sha256:4f9a9b3a51f1f3a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyTrustedRoots

<sub>Function</sub>

Retrieves the current list of trusted root certificates.

> [!warning] Deprecated
> To get the current set of trusted roots, call the [SSLCopyPeerTrust](<sslcopypeertrust(____).md>) function to obtain the [SecTrust](sectrust.md) for the peer certificate chain, and then call the [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) function (see the [Trust](trust.md) section of [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)).

<sub>macOS</sub>

```objc
OSStatus SSLCopyTrustedRoots(SSLContextRef context, CFArrayRef*trustedRoots);
```

## Parameters

- `context` — An SSL session context reference.

- `trustedRoots` — On return, a pointer to a value of type `CFArrayRef`. This array contains values of type `SecCertificateRef` representing the current set of trusted roots. You must call the `CFRelease` function to release this array when you are finished with it.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

You can use the [SSLSetTrustedRoots](sslsettrustedroots.md) function to replace or add to the set of trusted root certificates. If [SSLSetTrustedRoots](sslsettrustedroots.md) has never been called for this session, the [SSLCopyTrustedRoots](sslcopytrustedroots.md) function returns the system’s default set of trusted root certificates.
