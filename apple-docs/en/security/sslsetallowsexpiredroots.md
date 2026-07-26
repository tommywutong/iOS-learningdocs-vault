---
title: SSLSetAllowsExpiredRoots
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsetallowsexpiredroots
source_url: 'https://developer.apple.com/documentation/security/sslsetallowsexpiredroots'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetallowsexpiredroots.json'
content_hash: 'sha256:12da36dd4b15e50e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetAllowsExpiredRoots

<sub>Function</sub>

Specifies whether expired root certificates are allowed.

> [!warning] Deprecated
> To ignore expired certificate errors, first disable Secure Transport’s automatic verification of peer certificates by calling [SSLSetSessionOption](<sslsetsessionoption(______).md>) to set [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) to [true](../swift/true.md). When [SSLHandshake](<sslhandshake(__).md>) subsequently returns an `errSSLServerAuthCompleted` result, obtain the [SecTrust](sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [SecTrust](sectrust.md) APIs (see the [Trust](trust.md) section of [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)). The [SecTrustSetOptions](<sectrustsetoptions(____).md>) function allows you to specify that the expiration status of certificates should be ignored for this evaluation. The [kSecTrustOptionAllowExpiredRoot](sectrustoptionflags/allowexpiredroot.md) option can be used instead of [kSecTrustOptionAllowExpired](sectrustoptionflags/allowexpired.md) to allow expired roots only.

<sub>macOS</sub>

```objc
OSStatus SSLSetAllowsExpiredRoots(SSLContextRef context, Boolean allowsExpired);
```

## Parameters

- `context` — An SSL session context reference.

- `allowsExpired` — A Boolean value indicating whether to allow expired root certificates. Pass `true` to allow expired roots.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The default value for the `allowsExpired` flag is `false`. When this flag is `false`, Secure Transport returns an `errSSLCertExpired` result code during handshake if the root certificate is expired.

You can use the [SSLGetAllowsExpiredRoots](sslgetallowsexpiredroots.md) function to determine the current setting of the `allowsExpired` flag.

Use the [SSLSetAllowsExpiredCerts](sslsetallowsexpiredcerts.md) function to set a value that determines whether expired non-root certificates are allowed.
