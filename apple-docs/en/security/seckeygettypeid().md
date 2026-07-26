---
title: SecKeyGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 4.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeygettypeid()
source_url: 'https://developer.apple.com/documentation/security/seckeygettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygettypeid%28%29.json'
content_hash: 'sha256:777d0969437c56ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a key object belongs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecKey](seckey.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecKey](seckey.md) object. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function on a specific object. These values might change from release to release or platform to platform.
