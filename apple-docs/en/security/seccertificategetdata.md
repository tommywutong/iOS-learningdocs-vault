---
title: SecCertificateGetData
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccertificategetdata
source_url: 'https://developer.apple.com/documentation/security/seccertificategetdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificategetdata.json'
content_hash: 'sha256:5ffb3208b6217abd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateGetData

<sub>Function</sub>

Retrieves the data for a certificate.

<sub>macOS</sub>

```objc
OSStatus SecCertificateGetData(SecCertificateRef certificate, CSSM_DATA_PTR data);
```

## Parameters

- `certificate` — A certificate object for the certificate from which to retrieve the data.

- `data` — On return, points to the data for the certificate specified. You must allocate the space for a `CSSM_DATA` structure before calling this function. This data pointer is only guaranteed to remain valid as long as the certificate remains unchanged and valid.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function requires a certificate object, which can, for example, be created with the [SecCertificateCreateFromData](seccertificatecreatefromdata.md) function, obtained from an identity with the [SecIdentityCopyCertificate](<secidentitycopycertificate(____).md>) function, or obtained over a network (see [Secure Transport](secure-transport.md)).
