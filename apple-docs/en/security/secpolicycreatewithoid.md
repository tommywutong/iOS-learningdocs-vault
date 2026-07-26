---
title: SecPolicyCreateWithOID
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpolicycreatewithoid
source_url: 'https://developer.apple.com/documentation/security/secpolicycreatewithoid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicycreatewithoid.json'
content_hash: 'sha256:50cd62c3e96aa947'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyCreateWithOID

<sub>Function</sub>

Returns a policy object for the specified policy type object identifier.

<sub>macOS</sub>

```objc
SecPolicyRefSecPolicyCreateWithOID(CFTypeRef policyOID);
```

## Parameters

- `policyOID` — The object identifier (OID) of the policy type for this policy.
