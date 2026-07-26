---
title: SecAccessCreateFromOwnerAndACL
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaccesscreatefromownerandacl
source_url: 'https://developer.apple.com/documentation/security/secaccesscreatefromownerandacl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscreatefromownerandacl.json'
content_hash: 'sha256:1ce7b933f60b5a9c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessCreateFromOwnerAndACL

<sub>Function</sub>

Creates a new access object using the owner and access control list you provide.

> [!warning] Deprecated
> Use [SecAccessCreateWithOwnerAndACL](<secaccesscreatewithownerandacl(__________).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecAccessCreateFromOwnerAndACL(const CSSM_ACL_OWNER_PROTOTYPE *owner, uint32 aclCount, const CSSM_ACL_ENTRY_INFO *acls, SecAccessRef*accessRef);
```

## Parameters

- `owner` — A pointer to a CSSM access control list owner.

- `aclCount` — An unsigned 32-bit integer representing the number of items in the access control list.

- `acls` — A pointer to the CSSM access control list.

- `accessRef` — On return, points to the new access object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use [SecAccessCreateWithOwnerAndACL](<secaccesscreatewithownerandacl(__________).md>) instead.

This function creates an access object from CSSM structures. You can use this function to create an access object for use with other Certificate, Key, and Trust API functions if you want to use CSSM to create the access control list. CSSM allows more complex access controls than you can construct with the Certificate, Key, and Trust API. For more information about the CSSM API, see _Common Security: CDSA and CSSM, version 2 (with corrigenda)_ from The Open Group ([http://www.opengroup.org/security/cdsa.htm](http://www.opengroup.org/security/cdsa.htm)).

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [SecAccessCreateWithOwnerAndACL](<secaccesscreatewithownerandacl(__________).md>) instead.
