---
title: SecCertificateGetType
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccertificategettype
source_url: 'https://developer.apple.com/documentation/security/seccertificategettype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificategettype.json'
content_hash: 'sha256:753cef632036a4c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateGetType

<sub>Function</sub>

Retrieves the type of a specified certificate.

<sub>macOS</sub>

```objc
OSStatus SecCertificateGetType(SecCertificateRef certificate, CSSM_CERT_TYPE *certificateType);
```

## Parameters

- `certificate` — A certificate object for the certificate for which to obtain the type.

- `certificateType` — On return, points to the type of the specified certificate. Certificate types are defined in `Security.framework/cssmtype.h`. You must allocate the space for a `CSSM_CERT_TYPE` structure before calling this function.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
