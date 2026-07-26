---
title: 'SecAccessCopyACLList(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaccesscopyacllist(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaccesscopyacllist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscopyacllist%28_%3A_%3A%29.json'
content_hash: 'sha256:6456d1987005fcbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessCopyACLList(_:_:)

<sub>Function</sub>

Retrieves all the ACL entries of a given access instance.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecAccessCopyACLList(_ accessRef: SecAccess, _ aclList: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `accessRef` — The access instance from which to retrieve the information.

- `aclList` — A pointer the method uses to return an array of [SecACL](secacl.md) instances. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release the array when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

An access instance can have any number of ACL entries for specific operations or sets of operations. Use this method to get an array of all the ACL entries of a particular access instance. To retrieve entries corresponding to specific operations, use the [SecAccessCopyMatchingACLList](<secaccesscopymatchingacllist(____).md>) method instead.
