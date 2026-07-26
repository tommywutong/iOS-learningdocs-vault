---
title: SecTrustedApplicationGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectrustedapplicationgettypeid()
source_url: 'https://developer.apple.com/documentation/security/sectrustedapplicationgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustedapplicationgettypeid%28%29.json'
content_hash: 'sha256:0db27d3d51681c42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustedApplicationGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a trusted app instance belongs.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecTrustedApplicationGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecTrustedApplication](sectrustedapplication.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecTrustedApplication](sectrustedapplication.md) instance. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) method on a specific instance. These values might change from release to release or platform to platform.
