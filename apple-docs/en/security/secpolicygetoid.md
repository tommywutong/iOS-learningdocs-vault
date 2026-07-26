---
title: SecPolicyGetOID
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpolicygetoid
source_url: 'https://developer.apple.com/documentation/security/secpolicygetoid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicygetoid.json'
content_hash: 'sha256:6c6dae6a9565eb3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyGetOID

<sub>Function</sub>

Retrieves a policy’s object identifier.

<sub>macOS</sub>

```objc
OSStatus SecPolicyGetOID(SecPolicyRef policyRef, SecAsn1Oid *oid);
```

## Parameters

- `policyRef` — The policy object for which to obtain the object identifier. You can obtain a policy object with the [SecPolicySearchCopyNext](secpolicysearchcopynext.md) function.

- `oid` — On return, points to the policy’s object identifier. This identifier is owned by the policy object and remains valid until that object is destroyed; do not release it separately.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The policy’s object identifier, in the form of a `CSSM_OID` structure, is used in the CSSM API together with the policy’s value. Use the [SecPolicyGetValue](secpolicygetvalue.md) function to obtain the value that corresponds to this object identifier.
