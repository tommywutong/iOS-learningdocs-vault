---
title: SecIdentitySearchCopyNext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secidentitysearchcopynext
source_url: 'https://developer.apple.com/documentation/security/secidentitysearchcopynext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitysearchcopynext.json'
content_hash: 'sha256:a090e110c5117f1a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentitySearchCopyNext

<sub>Function</sub>

Finds the next identity matching specified search criteria

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecIdentitySearchCopyNext(SecIdentitySearchRef searchRef, SecIdentityRef*identity);
```

## Parameters

- `searchRef` — An identity search object specifying the search criteria for this search. You create the identity search object by calling the [SecIdentitySearchCreate](secidentitysearchcreate.md) function.

- `identity` — On return, points to the identity object of the next matching identity (if any). In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). When there are no more identities that match the parameters specified to [SecIdentitySearchCreate](secidentitysearchcreate.md), [errSecItemNotFound](errsecitemnotfound.md) is returned.
