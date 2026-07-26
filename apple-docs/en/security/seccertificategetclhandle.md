---
title: SecCertificateGetCLHandle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccertificategetclhandle
source_url: 'https://developer.apple.com/documentation/security/seccertificategetclhandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificategetclhandle.json'
content_hash: 'sha256:50525e33dea0db43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateGetCLHandle

<sub>Function</sub>

Retrieves the certificate library handle from a certificate object.

<sub>macOS</sub>

```objc
OSStatus SecCertificateGetCLHandle(SecCertificateRef certificate, CSSM_CL_HANDLE *clHandle);
```

## Parameters

- `certificate` — The certificate object from which to obtain the certificate library handle.

- `clHandle` — On return, points to the certificate library handle of the specified certificate. This handle remains valid until the certificate object is released.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The certificate library handle is the CSSM identifier of the certificate library module that is managing the certificate. The certificate library handle is used as an input to a number of CSSM functions.
