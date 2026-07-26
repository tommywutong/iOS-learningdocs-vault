---
title: SecPolicySetProperties
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpolicysetproperties
source_url: 'https://developer.apple.com/documentation/security/secpolicysetproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicysetproperties.json'
content_hash: 'sha256:0244800a34613571'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicySetProperties

<sub>Function</sub>

Sets properties for a policy.

<sub>macOS</sub>

```objc
OSStatus SecPolicySetProperties(SecPolicyRef policyRef, CFDictionaryRef properties);
```

## Parameters

- `policyRef` — The policy to alter

- `properties` — A `CFDictionaryRef` object containing the new set of properties. For a list of valid property keys, see [Security Policy Keys](security-policy-keys.md). > [!note] Note > The property [kSecPolicyOid](ksecpolicyoid.md) is read-only and thus cannot be changed by this function.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
