---
title: Trust Result Dictionary Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/trust-result-dictionary-keys
source_url: 'https://developer.apple.com/documentation/security/trust-result-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/trust-result-dictionary-keys.json'
content_hash: 'sha256:e35ee69f74bc19a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Trust](trust.md)

# Trust Result Dictionary Keys

<sub>API Collection</sub>

Recognize the keys that appear in a dictionary containing information about an evaluated certification chain.

## Overview

These keys appear in the dictionary returned from a call to the [SecTrustCopyResult](<sectrustcopyresult(__).md>) function and provide information about the evaluated trust.

## Topics

### Constants

- [kSecTrustCertificateTransparency](ksectrustcertificatetransparency.md) — A key whose value is a Boolean used to indicate Certificate Transparency.
- [kSecTrustCertificateTransparencyWhiteList](ksectrustcertificatetransparencywhitelist.md) — A key whose value is a Boolean used to indicate the chain satisfies Certificate Transparency by being on the allow list. _(deprecated)_
- [kSecTrustEvaluationDate](ksectrustevaluationdate.md) — A key whose value indicates the time that the trust evaluation took place.
- [kSecTrustExtendedValidation](ksectrustextendedvalidation.md) — A key whose value is a Boolean used to indicate Extended Validation.
- [kSecTrustOrganizationName](ksectrustorganizationname.md) — A key whose value is the organization name field of the subject of the leaf certificate.
- [kSecTrustResultValue](ksectrustresultvalue.md) — A key whose value represents the trust evaluation result.
- [kSecTrustRevocationChecked](ksectrustrevocationchecked.md) — A key whose value indicates the outcome of revocation checking during trust evaluation.
- [kSecTrustRevocationValidUntilDate](ksectrustrevocationvaliduntildate.md) — A key whose value indicates the earliest date at which revocation information becomes stale.
