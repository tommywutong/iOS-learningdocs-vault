---
title: 'init(cspHand:clHand:serialNumber:numSubjectNames:subjectNames:numIssuerNames:issuerNames:issuerNameX509:certPublicKey:issuerPrivateKey:signatureAlg:signatureOid:notBefore:notAfter:numExtensions:extensions:challengeString:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/cssm_apple_tp_cert_request/init(csphand:clhand:serialnumber:numsubjectnames:subjectnames:numissuernames:issuernames:issuernamex509:certpublickey:issuerprivatekey:signaturealg:signatureoid:notbefore:notafter:numextensions:extensions:challengestring:)'
source_url: 'https://developer.apple.com/documentation/security/cssm_apple_tp_cert_request/init(csphand:clhand:serialnumber:numsubjectnames:subjectnames:numissuernames:issuernames:issuernamex509:certpublickey:issuerprivatekey:signaturealg:signatureoid:notbefore:notafter:numextensions:extensions:challengestring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_apple_tp_cert_request/init%28csphand%3Aclhand%3Aserialnumber%3Anumsubjectnames%3Asubjectnames%3Anumissuernames%3Aissuernames%3Aissuernamex509%3Acertpublickey%3Aissuerprivatekey%3Asignaturealg%3Asignatureoid%3Anotbefore%3Anotafter%3Anumextensions%3Aextensions%3Achallengestring%3A%29.json'
content_hash: 'sha256:2092225294b1281e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [CSSM_APPLE_TP_CERT_REQUEST](../cssm_apple_tp_cert_request.md)

# init(cspHand:clHand:serialNumber:numSubjectNames:subjectNames:numIssuerNames:issuerNames:issuerNameX509:certPublicKey:issuerPrivateKey:signatureAlg:signatureOid:notBefore:notAfter:numExtensions:extensions:challengeString:)

<sub>Initializer</sub>

<sub>macOS</sub>

```swift
init(cspHand: CSSM_CSP_HANDLE, clHand: CSSM_CL_HANDLE, serialNumber: uint32, numSubjectNames: uint32, subjectNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, numIssuerNames: uint32, issuerNames: UnsafeMutablePointer<CSSM_APPLE_TP_NAME_OID>!, issuerNameX509: UnsafeMutablePointer<cssm_x509_name>!, certPublicKey: UnsafePointer<cssm_key>!, issuerPrivateKey: UnsafePointer<cssm_key>!, signatureAlg: CSSM_ALGORITHMS, signatureOid: SecAsn1Oid, notBefore: uint32, notAfter: uint32, numExtensions: uint32, extensions: UnsafeMutablePointer<__CE_DataAndType>!, challengeString: UnsafePointer<CChar>!)
```
