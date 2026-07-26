---
title: SSLSetAllowsAnyRoot
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsetallowsanyroot
source_url: 'https://developer.apple.com/documentation/security/sslsetallowsanyroot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetallowsanyroot.json'
content_hash: 'sha256:501ad7a089881162'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetAllowsAnyRoot

<sub>Function</sub>

Specifies whether root certificates from unrecognized certification authorities are allowed.

> [!warning] Deprecated
> To ignore unknown root certificate errors, first disable Secure Transport’s automatic verification of peer certificates by calling [SSLSetSessionOption](<sslsetsessionoption(______).md>) to set [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) to [true](../swift/true.md). When [SSLHandshake](<sslhandshake(__).md>) subsequently returns an `errSSLServerAuthCompleted` result, obtain the [SecTrust](sectrust.md) for the peer’s certificates and perform a custom trust evaluation with [SecTrust](sectrust.md) APIs (see the [Trust](trust.md) section of [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)). Note that an unknown root certificate will cause [SecTrustEvaluate](<sectrustevaluate(____).md>) to report [kSecTrustResultRecoverableTrustFailure](sectrustresulttype/recoverabletrustfailure.md) as the trust result.

<sub>macOS</sub>

```objc
OSStatus SSLSetAllowsAnyRoot(SSLContextRef context, Boolean anyRoot);
```

## Parameters

- `context` — An SSL session context reference.

- `anyRoot` — A Boolean flag specifying whether root certificates from unrecognized certification authorities (CAs) are allowed. The default for this flag is `false`, specifying that roots from unrecognized CAs are not allowed.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The system maintains a set of root certificates signed by known, trusted root CAs. When the `anyRoot` flag is `true`, Secure Transport does not return an error if one of the following two conditions occurs:

- The peer returns a certificate chain with a root certificate, and the chain verifies to that root, but the CA for the root certificate is not one of the known, trusted root CAs. This results in an `errSSLUnknownRootCert` result code when the `anyRoot` flag is `false`.
- The peer returns a certificate chain that does not contain a root certificate, and the server can’t verify the chain to one of the trusted root certificates. This results in an `errSSLNoRootCert` result code when the `anyRoot` flag is `false`.

Both of these error conditions are ignored when the `anyRoot` flag is `true`, allowing connection to a peer for which trust could not be established.

If you use this function to allow an untrusted root to be used for validation of a certificate—for example, after prompting the user for permission to do so—remember to set the `anyRoot` Boolean value back to `false`. If you don’t, any random root certificate can be used for signing a certificate chain. To add a certificate to the list of trusted roots, use the [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) function.
