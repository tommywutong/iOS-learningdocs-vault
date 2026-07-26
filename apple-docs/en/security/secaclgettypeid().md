---
title: SecACLGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.3+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaclgettypeid()
source_url: 'https://developer.apple.com/documentation/security/secaclgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclgettypeid%28%29.json'
content_hash: 'sha256:d9a0c66475bc3d4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which an ACL entry belongs.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecACLGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecACL](secacl.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecACL](secacl.md) instance. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) method on a specific instance. These values might change from release to release or platform to platform.
