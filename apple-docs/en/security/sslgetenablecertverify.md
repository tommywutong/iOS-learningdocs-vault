---
title: SSLGetEnableCertVerify
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslgetenablecertverify
source_url: 'https://developer.apple.com/documentation/security/sslgetenablecertverify'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetenablecertverify.json'
content_hash: 'sha256:a4d9b40618a88471'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetEnableCertVerify

<sub>Function</sub>

Determines whether peer certificate chain validation is currently enabled.

> [!warning] Deprecated
> To check whether peer certificate chain validation is enabled in a context, call [SSLGetSessionOption](<sslgetsessionoption(______).md>) to obtain the value of the [kSSLSessionOptionBreakOnServerAuth](sslsessionoption/breakonserverauth.md) session option flag. If the value of this option flag is [true](../swift/true.md), then verification is disabled.

<sub>macOS</sub>

```objc
OSStatus SSLGetEnableCertVerify(SSLContextRef context, Boolean *enableVerify);
```

## Parameters

- `context` — An SSL session context reference.

- `enableVerify` — On return, a pointer to a Boolean value specifying whether peer certificate chain validation is enabled. If this value is `true`, then Secure Transport automatically attempts to verify the certificate chain during exchange of peer certificates.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Use the [SSLSetEnableCertVerify](sslsetenablecertverify.md) function to set the value of the `enableVerify` flag.
