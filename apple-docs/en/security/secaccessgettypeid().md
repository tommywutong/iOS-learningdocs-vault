---
title: SecAccessGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaccessgettypeid()
source_url: 'https://developer.apple.com/documentation/security/secaccessgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccessgettypeid%28%29.json'
content_hash: 'sha256:c625839683144d45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which an access instance belongs.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecAccessGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecAccess](secaccess.md) instance.

## Discussion

This method returns a value that uniquely identifies the opaque type of a [SecAccess](secaccess.md) instance. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) method on a specific object. These values might change from release to release or platform to platform.
