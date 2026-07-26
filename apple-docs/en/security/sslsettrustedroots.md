---
title: SSLSetTrustedRoots
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsettrustedroots
source_url: 'https://developer.apple.com/documentation/security/sslsettrustedroots'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsettrustedroots.json'
content_hash: 'sha256:41cc7f39649d1655'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetTrustedRoots

<sub>Function</sub>

Augments or replaces the default set of trusted root certificates for this session.

> [!warning] Deprecated
> To trust specific roots in a session, first disable Secure Transport’s automatic verification of peer certificates by calling [SSLSetSessionOption](<sslsetsessionoption(______).md>) to set [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) to true. When [SSLHandshake](<sslhandshake(__).md>) subsequently returns an errSSLServerAuthCompleted result, obtain the [SecTrust](sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [SecTrust](sectrust.md) APIs (see the [Trust](trust.md) section of [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)). You can call [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) to augment the system’s trusted root set, or [SecTrustSetAnchorCertificatesOnly](<sectrustsetanchorcertificatesonly(____).md>) to make these the only trusted roots, prior to calling [SecTrustEvaluate](<sectrustevaluate(____).md>).

<sub>macOS</sub>

```objc
OSStatus SSLSetTrustedRoots(SSLContextRef context, CFArrayRef trustedRoots, Boolean replaceExisting);
```

## Parameters

- `context` — An SSL session context reference.

- `trustedRoots` — A reference to an array of trusted root certificates of type `SecCertificateRef`.

- `replaceExisting` — A Boolean value indicating whether to replace or append the current trusted root certificate set. If this value is `true`, the specified root certificates become the only roots that are trusted during this session. If this value is `false`, the specified root certificates are added to the current set of trusted root certificates.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Each successive call to this function with the `replaceExisting` parameter set to `false` results in accumulation of additional root certificates. To see the current set of trusted root certificates, call the [SSLCopyTrustedRoots](sslcopytrustedroots.md) function.
