---
title: SecCodeGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodegettypeid()
source_url: 'https://developer.apple.com/documentation/security/seccodegettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodegettypeid%28%29.json'
content_hash: 'sha256:18066c1934d23025'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a code object belongs.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a code object.

## Discussion

You can compare the value returned by this function to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function on a specific object. These values might change from release to release or platform to platform.
