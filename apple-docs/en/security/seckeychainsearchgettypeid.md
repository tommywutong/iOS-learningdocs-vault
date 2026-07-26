---
title: SecKeychainSearchGetTypeID
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychainsearchgettypeid
source_url: 'https://developer.apple.com/documentation/security/seckeychainsearchgettypeid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsearchgettypeid.json'
content_hash: 'sha256:2a207a6f608e0216'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSearchGetTypeID

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a keychain search object belongs.

<sub>Mac Catalyst, macOS</sub>

```objc
CFTypeID SecKeychainSearchGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [SecKeychainSearch](seckeychainsearch.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecKeychainSearch](seckeychainsearch.md) object. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function on a specific object. These values might change from release to release or platform to platform.
