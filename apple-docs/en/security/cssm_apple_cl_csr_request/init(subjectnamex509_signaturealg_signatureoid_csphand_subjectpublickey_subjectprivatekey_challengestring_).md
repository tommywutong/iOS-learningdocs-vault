---
title: 'init(subjectNameX509:signatureAlg:signatureOid:cspHand:subjectPublicKey:subjectPrivateKey:challengeString:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/cssm_apple_cl_csr_request/init(subjectnamex509:signaturealg:signatureoid:csphand:subjectpublickey:subjectprivatekey:challengestring:)'
source_url: 'https://developer.apple.com/documentation/security/cssm_apple_cl_csr_request/init(subjectnamex509:signaturealg:signatureoid:csphand:subjectpublickey:subjectprivatekey:challengestring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_apple_cl_csr_request/init%28subjectnamex509%3Asignaturealg%3Asignatureoid%3Acsphand%3Asubjectpublickey%3Asubjectprivatekey%3Achallengestring%3A%29.json'
content_hash: 'sha256:df9ffb65b442cc3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [CSSM_APPLE_CL_CSR_REQUEST](../cssm_apple_cl_csr_request.md)

# init(subjectNameX509:signatureAlg:signatureOid:cspHand:subjectPublicKey:subjectPrivateKey:challengeString:)

<sub>Initializer</sub>

<sub>macOS</sub>

```swift
init(subjectNameX509: UnsafeMutablePointer<cssm_x509_name>!, signatureAlg: CSSM_ALGORITHMS, signatureOid: SecAsn1Oid, cspHand: CSSM_CSP_HANDLE, subjectPublicKey: UnsafePointer<cssm_key>!, subjectPrivateKey: UnsafePointer<cssm_key>!, challengeString: UnsafePointer<CChar>!)
```
