---
title: SecCertificateGetAlgorithmID
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccertificategetalgorithmid
source_url: 'https://developer.apple.com/documentation/security/seccertificategetalgorithmid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificategetalgorithmid.json'
content_hash: 'sha256:3566372873a5f460'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateGetAlgorithmID

<sub>Function</sub>

Retrieves the algorithm identifier for a certificate.

<sub>macOS</sub>

```objc
OSStatus SecCertificateGetAlgorithmID(SecCertificateRef certificate, const SecAsn1AlgId **algid);
```

## Parameters

- `certificate` — The certificate object from which to retrieve the algorithm identifier.

- `algid` — On return, points to a struct that identifies the algorithm for this certificate. This pointer remains valid until the certificate reference is released. Do not attempt to free this pointer.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The `CSSM_X509_ALGORITHM_IDENTIFIER` struct is defined in `Security.framework/x509defs.h` and discussed in _Common Security: CDSA and CSSM, version 2 (with corrigenda)_ from [http://www.opengroup.org/security/cdsa.htm](http://www.opengroup.org/security/cdsa.htm). Possible algorithms are enumerated in `Security.framework/oidsalg.h`.
