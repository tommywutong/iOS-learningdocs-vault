---
title: SecPolicySearchCopyNext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpolicysearchcopynext
source_url: 'https://developer.apple.com/documentation/security/secpolicysearchcopynext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicysearchcopynext.json'
content_hash: 'sha256:f8e6347a4a37f8da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicySearchCopyNext

<sub>Function</sub>

Retrieves a policy object for the next policy matching specified search criteria.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecPolicySearchCopyNext(SecPolicySearchRef searchRef, SecPolicyRef*policyRef);
```

## Parameters

- `searchRef` — A policy search object specifying the search criteria for this search. You create the policy search object by calling the [SecPolicySearchCreate](secpolicysearchcreate.md) function.

- `policyRef` — On return, points to the policy object for the next policy (if any) matching the specified search criteria. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). When there are no more policies that match the parameters specified to [SecPolicySearchCreate](secpolicysearchcreate.md), [errSecPolicyNotFound](errsecpolicynotfound.md) is returned.
