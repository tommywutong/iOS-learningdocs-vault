---
title: SecPolicyGetValue
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpolicygetvalue
source_url: 'https://developer.apple.com/documentation/security/secpolicygetvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicygetvalue.json'
content_hash: 'sha256:056d6b26b0ae766c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyGetValue

<sub>Function</sub>

Retrieves a policy’s value.

<sub>macOS</sub>

```objc
OSStatus SecPolicyGetValue(SecPolicyRef policyRef, SecAsn1Item *value);
```

## Parameters

- `policyRef` — The policy object for which to retrieve the value.

- `value` — On return, points to the policy’s value. This value is owned by the policy object and remains valid until that object is destroyed; do not release it separately.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A policy’s value is defined and interpreted by the policy. If you are using CSSM, you can specify object-identifier–policy-value pairs as input to the `CSSM_TP_POLICYINFO` function. Use the [SecPolicyGetOID](secpolicygetoid.md) function to obtain the object identifier (OID) for a policy.

Depending on how the policy uses the value, the value can be specific to a transaction. Because some other process might be using this policy object, it is best not to assign a new value to the policy using the same policy object. Instead, obtain a new policy object before assigning a new value to the policy.
