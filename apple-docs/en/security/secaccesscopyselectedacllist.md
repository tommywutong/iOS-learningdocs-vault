---
title: SecAccessCopySelectedACLList
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaccesscopyselectedacllist
source_url: 'https://developer.apple.com/documentation/security/secaccesscopyselectedacllist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscopyselectedacllist.json'
content_hash: 'sha256:9001429125e59602'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessCopySelectedACLList

<sub>Function</sub>

Retrieves selected access control lists from a given access object.

> [!warning] Deprecated
> Use [SecAccessCopyMatchingACLList](<secaccesscopymatchingacllist(____).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAccessCopySelectedACLList(SecAccessRef accessRef, CSSM_ACL_AUTHORIZATION_TAG action, CFArrayRef*aclList);
```

## Parameters

- `accessRef` — The access object from which to retrieve the information.

- `action` — An access control list authorization tag; the function returns only those access control list entries that apply to the operation indicated by this tag.

- `aclList` — On return, a pointer to the selected access control lists. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use [SecAccessCopyMatchingACLList](<secaccesscopymatchingacllist(____).md>) instead.

An access object can have any number of access control list (ACL) entries for specific operations or sets of operations. To retrieve all the ACL entries for an access object, use the [SecAccessCopyACLList](<secaccesscopyacllist(____).md>) function.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [SecAccessCopyMatchingACLList](<secaccesscopymatchingacllist(____).md>) instead.
