---
title: Policies
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/policies
source_url: 'https://developer.apple.com/documentation/security/policies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/policies.json'
content_hash: 'sha256:0ca59f8647a9e813'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)

# Policies

<sub>API Collection</sub>

Obtain policies for establishing trust.

## Overview

For a certificate that is deemed intact and valid (because the chain of signatures is unbroken back to a trusted root certificate), you evaluate it against a set of rules known as a _trust policy_. The policy indicates how particular fields or extensions of a certificate affect whether it should be trusted for a particular use. For example, the policy may state that a certificate must not be expired or must be marked as valid for encryption, code signing, or some other specific purpose.

Usually you use a standard, predefined policy, such as the basic X509 policy or the SSL policy. You can also create custom policies with the certificate, key, and trust services API.

## Topics

### Standard Policies

- [SecPolicyCreateBasicX509](<secpolicycreatebasicx509().md>) — Returns a policy object for the default X.509 policy.
- [SecPolicyCreateSSL](<secpolicycreatessl(____).md>) — Returns a policy object for evaluating SSL certificate chains.
- [SecPolicyCreateRevocation](<secpolicycreaterevocation(__).md>) — Returns a policy object for checking revocation of certificates.
- [Revocation Policy Constants](revocation-policy-constants.md) — Use these flags to create a revocation policy object.
- [SecPolicy](secpolicy.md) — An object that represents a trust policy.
- [SecPolicyGetTypeID](<secpolicygettypeid().md>) — Returns the unique identifier of the opaque type to which a policy object belongs.

### Advanced Policy Management

- [SecPolicyCreateWithProperties](<secpolicycreatewithproperties(____).md>) — Returns a policy object based on an object identifier for the policy type.
- [SecPolicyCopyProperties](<secpolicycopyproperties(__).md>) — Returns a dictionary containing a policy’s properties.
- [Security Policy Keys](security-policy-keys.md) — Use these dictionary keys to get and set policy properties.
- [Standard Policies for Specific Certificate Types](standard-policies-for-specific-certificate-types.md) — Use special OIDs to cause a certificate to be evaluated based on security policies specific to a given type of certificate.

### Legacy Symbols

- [SecPolicySearch](secpolicysearch.md) — An object that contains information about a policy search.
