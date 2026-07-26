---
title: SecIdentityGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secidentitygettypeid()
source_url: 'https://developer.apple.com/documentation/security/secidentitygettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitygettypeid%28%29.json'
content_hash: 'sha256:aa3d1466e702e9af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentityGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which an identity object belongs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecIdentityGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecIdentity](secidentity.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecIdentity](secidentity.md) object. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function on a specific object. These values might change from release to release or platform to platform.
