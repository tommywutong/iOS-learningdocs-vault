---
title: 'SecACLRemove(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.3+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaclremove(_:)'
source_url: 'https://developer.apple.com/documentation/security/secaclremove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclremove%28_%3A%29.json'
content_hash: 'sha256:4c0ed62951500b0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLRemove(_:)

<sub>Function</sub>

Removes the specified ACL entry from the access instance that contains it.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecACLRemove(_ aclRef: SecACL) -> OSStatus
```

## Parameters

- `aclRef` — An ACL entry to remove.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This method fails if you attempt to remove the owner entry because an access instance must have exactly one such ACL at all times. If you need to change ownership settings, modify the existing owner entry rather than replacing it. In particular, use the [SecAccessCopyMatchingACLList](<secaccesscopymatchingacllist(____).md>) method with the [kSecACLAuthorizationChangeACL](ksecaclauthorizationchangeacl.md) authorization to find the existing entry, and the [SecACLSetContents](<secaclsetcontents(________).md>) method to change it as needed.
