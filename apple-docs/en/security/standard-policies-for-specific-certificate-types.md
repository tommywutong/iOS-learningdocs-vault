---
title: Standard Policies for Specific Certificate Types
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/standard-policies-for-specific-certificate-types
source_url: 'https://developer.apple.com/documentation/security/standard-policies-for-specific-certificate-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/standard-policies-for-specific-certificate-types.json'
content_hash: 'sha256:6be28e24d05de0bf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Policies](policies.md)

# Standard Policies for Specific Certificate Types

<sub>API Collection</sub>

Use special OIDs to cause a certificate to be evaluated based on security policies specific to a given type of certificate.

## Topics

### Constants

- [kSecPolicyAppleX509Basic](ksecpolicyapplex509basic.md) — Basic X509-style certificate evaluation.
- [kSecPolicyAppleSSL](ksecpolicyapplessl.md) — Basic X509 plus host name verification per RFC 2818.
- [kSecPolicyAppleSMIME](ksecpolicyapplesmime.md) — Basic X509 plus email address verification and `KeyUsage` enforcement per RFC 2632.
- [kSecPolicyAppleEAP](ksecpolicyappleeap.md) — Extensible Authentication Protocol. Functionally identical to SSL policy. A separate OID is provided to facilitate per-policy, per-certificate trust settings using the `SecTrust` mechanism.
- [kSecPolicyAppleIPsec](ksecpolicyappleipsec.md) — Policy for use in IPsec communication. Functionally identical to SSL policy. A separate OID is provided to facilitate per-policy, per-certificate trust settings using the `SecTrust` mechanism.
- [kSecPolicyApplePKINITClient](ksecpolicyapplepkinitclient.md) — Kerberos Pkinit client certificate validation.
- [kSecPolicyApplePKINITServer](ksecpolicyapplepkinitserver.md) — Kerberos Pkinit server certificate validation.
- [kSecPolicyAppleCodeSigning](ksecpolicyapplecodesigning.md) — Policy for use in evaluating Apple code signing certificates.
- [kSecPolicyMacAppStoreReceipt](ksecpolicymacappstorereceipt.md) — Policy for use in evaluating Mac App Store receipts.
- [kSecPolicyAppleIDValidation](ksecpolicyappleidvalidation.md) — Policy for use in evaluating Apple ID certificates.
- [kSecPolicyAppleTimeStamping](ksecpolicyappletimestamping.md) — Policy that causes evaluation of the validity of the time stamp on a signature. This can be used to allow verification that a certificate was valid at the time that something was signed with that certificate even if the certificate is no longer valid.
- [kSecPolicyApplePassbookSigning](ksecpolicyapplepassbooksigning.md)
- [kSecPolicyApplePayIssuerEncryption](ksecpolicyapplepayissuerencryption.md)
- [kSecPolicyAppleRevocation](ksecpolicyapplerevocation.md)
