---
title: SSLCopyPeerCertificates
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslcopypeercertificates
source_url: 'https://developer.apple.com/documentation/security/sslcopypeercertificates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopypeercertificates.json'
content_hash: 'sha256:bf59473c1decc9ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyPeerCertificates

<sub>Function</sub>

Retrieves a peer certificate and its certificate chain.

> [!warning] Deprecated
> To get peer certificates, call [SSLCopyPeerTrust](<sslcopypeertrust(____).md>) to obtain the [SecTrust](sectrust.md) for the peer certificate chain, then use the [SecTrustGetCertificateCount](<sectrustgetcertificatecount(__).md>) and [SecTrustGetCertificateAtIndex](<sectrustgetcertificateatindex(____).md>) functions to retrieve individual certificates in the chain (see the [Trust](trust.md) section of [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)).

<sub>macOS</sub>

```objc
OSStatus SSLCopyPeerCertificates(SSLContextRef context, CFArrayRef*certs);
```

## Parameters

- `context` — An SSL session context reference.

- `certs` — On return, a pointer to an array of values of type `SecCertificateRef` representing the peer certificate and the certificate chain used to validate it. The certificate at index 0 of the returned array is the peer certificate (the subject of the function call—the end certificate in the chain); the root certificate (or the closest certificate to it) is at the end of the returned array. The entire array is created by the Secure Transport library; you must call the `CFRelease` function for this array when you are finished with it.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function is valid any time after a handshake attempt. You can use it to examine a peer certificate, to examine a certificate chain to determine why a handshake attempt failed, or to retrieve the certificate chain in order to validate the certificate yourself. (To disable validation so that you can validate the certificate yourself, use the [SSLSetSessionOption](<sslsetsessionoption(______).md>) function to set the session’s [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) flag.)
