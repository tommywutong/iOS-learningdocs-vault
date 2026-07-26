---
title: 'SecAccessCreateWithOwnerAndACL(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaccesscreatewithownerandacl(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaccesscreatewithownerandacl(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscreatewithownerandacl%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3fdd1193db1e6a3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessCreateWithOwnerAndACL(_:_:_:_:_:)

<sub>Function</sub>

Creates a new access instance using the owner and ACL entries you provide.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecAccessCreateWithOwnerAndACL(_ userId: uid_t, _ groupId: gid_t, _ ownerType: SecAccessOwnerType, _ acls: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccess?
```

## Parameters

- `userId` — The user ID that owns this ACL.

- `groupId` — The group ID that owns this ACL.

- `ownerType` — Flags that control whether the specified user ID or group ID owns the resulting ACL. See [SecAccessOwnerType](secaccessownertype.md) for details.

- `acls` — An array of ACL entries to associate with the access instance.

- `error` — The address of an error instance. On error, the return value is `nil`, and the variable referenced by this parameter is overwritten with a [CFError](../corefoundation/cferror.md) instance that provides more information.

## Return Value

The new access instance. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release it when you are finished using it.

## Discussion

Use this method to create a customized access instance from [SecACL](secacl.md) instances that you’ve created with the [SecACLCreateWithSimpleContents](<secaclcreatewithsimplecontents(__________).md>) method. If you want a default access instance, use the [SecAccessCreate](<secaccesscreate(______).md>) method instead.
