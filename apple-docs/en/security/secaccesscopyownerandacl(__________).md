---
title: 'SecAccessCopyOwnerAndACL(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaccesscopyownerandacl(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaccesscopyownerandacl(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscopyownerandacl%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8c50668e18acd5d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessCopyOwnerAndACL(_:_:_:_:_:)

<sub>Function</sub>

Retrieves the owner and the ACL entries of a given access instance.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecAccessCopyOwnerAndACL(_ accessRef: SecAccess, _ userId: UnsafeMutablePointer<uid_t>?, _ groupId: UnsafeMutablePointer<gid_t>?, _ ownerType: UnsafeMutablePointer<SecAccessOwnerType>?, _ aclList: UnsafeMutablePointer<CFArray?>?) -> OSStatus
```

## Parameters

- `accessRef` — An access instance from which to retrieve the owner and ACL entries.

- `userId` — On return, the user ID that owns the access instance.

- `groupId` — On return, the group ID that owns the access instance.

- `ownerType` — On return, flags that indicate whether the specified user ID or group ID owns the resulting ACL entries. See [SecAccessOwnerType](secaccessownertype.md) for details.

- `aclList` — On return, an array of [SecACL](secacl.md) instances associated with the access instance.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
