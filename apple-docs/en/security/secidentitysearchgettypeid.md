---
title: SecIdentitySearchGetTypeID
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secidentitysearchgettypeid
source_url: 'https://developer.apple.com/documentation/security/secidentitysearchgettypeid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitysearchgettypeid.json'
content_hash: 'sha256:0a0584e4a53f29dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentitySearchGetTypeID

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a `SecIdentitySearch` object belongs.

<sub>Mac Catalyst, macOS</sub>

```objc
CFTypeID SecIdentitySearchGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [SecIdentitySearch](secidentitysearch.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecIdentitySearch](secidentitysearch.md) object. You can compare this value to the `CFTypeID` identifier obtained by calling the `CFGetTypeID` function on a specific object. These values might change from release to release or platform to platform.
