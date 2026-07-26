---
title: 'SecAccessCopyMatchingACLList(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaccesscopymatchingacllist(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaccesscopymatchingacllist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscopymatchingacllist%28_%3A_%3A%29.json'
content_hash: 'sha256:222f0f6edb1e714d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessCopyMatchingACLList(_:_:)

<sub>Function</sub>

Retrieves selected ACL entries from a given access instance.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecAccessCopyMatchingACLList(_ accessRef: SecAccess, _ authorizationTag: CFTypeRef) -> CFArray?
```

## Parameters

- `accessRef` — The access instance from which to retrieve the information.

- `authorizationTag` — An access control list authorization tag. See [ACL Authorization Keys](acl-authorization-keys.md) for a list of possible values. The method returns only those ACL entries that apply to the operation indicated by this tag.

## Return Value

An array containing the selected access control list entries. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) method to release the array when you are finished using it.

## Discussion

An access instance can have any number of ACL entries for specific operations or sets of operations. This method returns the ACL entries that apply to the given operation. To retrieve all the ACL entries for an access instance, use the [SecAccessCopyACLList](<secaccesscopyacllist(____).md>) method instead.
