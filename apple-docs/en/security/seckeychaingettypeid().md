---
title: SecKeychainGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychaingettypeid()
source_url: 'https://developer.apple.com/documentation/security/seckeychaingettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingettypeid%28%29.json'
content_hash: 'sha256:ac17bb34653190c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a keychain object belongs.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecKeychain](seckeychain.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecKeychain](seckeychain.md) object. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function on a specific object. These values might change from release to release or platform to platform.
