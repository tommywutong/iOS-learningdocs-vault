---
title: Revocation Policy Constants
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/revocation-policy-constants
source_url: 'https://developer.apple.com/documentation/security/revocation-policy-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/revocation-policy-constants.json'
content_hash: 'sha256:8f8c50bdbee9bf0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Policies](policies.md)

# Revocation Policy Constants

<sub>API Collection</sub>

Use these flags to create a revocation policy object.

## Overview

Use these flags with a call to the [SecPolicyCreateRevocation](<secpolicycreaterevocation(__).md>) function to characterize the constructed policy.

## Topics

### Constants

- [kSecRevocationCRLMethod](ksecrevocationcrlmethod.md) — Perform revocation checking using the CRL (Certification Revocation List) method.
- [kSecRevocationNetworkAccessDisabled](ksecrevocationnetworkaccessdisabled.md) — Consult only locally cached replies; do not use network access.
- [kSecRevocationOCSPMethod](ksecrevocationocspmethod.md) — Perform revocation     checking using OCSP (Online Certificate Status Protocol).
- [kSecRevocationPreferCRL](ksecrevocationprefercrl.md) — Prefer CRL revocation checking over OCSP; by default, OCSP is preferred.
- [kSecRevocationRequirePositiveResponse](ksecrevocationrequirepositiveresponse.md) — Require a positive response to pass the policy.
- [kSecRevocationUseAnyAvailableMethod](ksecrevocationuseanyavailablemethod.md) — Perform either OCSP or CRL checking.
