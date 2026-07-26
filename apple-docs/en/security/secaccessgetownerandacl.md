---
title: SecAccessGetOwnerAndACL
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaccessgetownerandacl
source_url: 'https://developer.apple.com/documentation/security/secaccessgetownerandacl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccessgetownerandacl.json'
content_hash: 'sha256:a9e132fc13d24f93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessGetOwnerAndACL

<sub>Function</sub>

Retrieves the owner and the access control list of a given access object.

> [!warning] Deprecated
> Use [SecAccessCopyOwnerAndACL](<secaccesscopyownerandacl(__________).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAccessGetOwnerAndACL(SecAccessRef accessRef, CSSM_ACL_OWNER_PROTOTYPE_PTR*owner, uint32 *aclCount, CSSM_ACL_ENTRY_INFO_PTR*acls);
```

## Parameters

- `accessRef` — An access object from which to retrieve the owner and access control list.

- `owner` — On return, a pointer to a CSSM access control list owner.

- `aclCount` — On return, a pointer to an unsigned 32-bit integer representing the number of items in the access control list.

- `acls` — On return, a pointer to the CSSM access control list.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use [SecAccessCopyOwnerAndACL](<secaccesscopyownerandacl(__________).md>) instead.

This function returns CSSM structures for use with CSSM API functions.

### Special Considerations

This function is deprecated in macOS 10.7 and later. Use [SecAccessCopyOwnerAndACL](<secaccesscopyownerandacl(__________).md>) instead.
