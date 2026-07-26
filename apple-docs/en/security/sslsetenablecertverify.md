---
title: SSLSetEnableCertVerify
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslsetenablecertverify
source_url: 'https://developer.apple.com/documentation/security/sslsetenablecertverify'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetenablecertverify.json'
content_hash: 'sha256:71eb5e2b8bfcad40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetEnableCertVerify

<sub>Function</sub>

Enables or disables peer certificate chain validation.

> [!warning] Deprecated
> To disable peer certificate chain validation, you can instead use [SSLSetSessionOption](<sslsetsessionoption(______).md>) to set [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) to true. This will disable verification and cause [SSLHandshake](<sslhandshake(__).md>) to return with an `errSSLServerAuthCompleted` result when the peer certificates have been received. Then you can choose to evaluate peer trust yourself or simply call [SSLHandshake](<sslhandshake(__).md>) again to proceed with the handshake.

<sub>macOS</sub>

```objc
OSStatus SSLSetEnableCertVerify(SSLContextRef context, Boolean enableVerify);
```

## Parameters

- `context` — An SSL session context reference.

- `enableVerify` — A Boolean value specifying whether peer certificate chain validation is enabled. Certificate chain validation is enabled by default. Specify `false` to disable validation.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

By default, Secure Transport attempts to verify the certificate chain during an exchange of peer certificates. If you disable peer certificate chain validation, it is your responsibility to call [SSLCopyPeerCertificates](sslcopypeercertificates.md) upon successful completion of the handshake and then to validate the peer certificate chain before transferring the data.

You can use the [SSLGetEnableCertVerify](sslgetenablecertverify.md) function to determine the current setting of the `enableVerify` flag.
