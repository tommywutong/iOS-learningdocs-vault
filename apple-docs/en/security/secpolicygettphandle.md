---
title: SecPolicyGetTPHandle
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpolicygettphandle
source_url: 'https://developer.apple.com/documentation/security/secpolicygettphandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicygettphandle.json'
content_hash: 'sha256:6a6d2e82f06d1950'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyGetTPHandle

<sub>Function</sub>

Retrieves the trust policy handle for a policy object.

<sub>macOS</sub>

```objc
OSStatus SecPolicyGetTPHandle(SecPolicyRef policyRef, CSSM_TP_HANDLE *tpHandle);
```

## Parameters

- `policyRef` — The policy object from which to obtain the trust policy handle.

- `tpHandle` — On return, points to the policy object’s trust policy handle. The handle remains valid until the policy object is released.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The trust policy handle is the CSSM identifier of the trust policy module that is managing the certificate. The trust policy handle is uses as an input to a number of CSSM functions.
