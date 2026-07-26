---
title: SecPolicySearchGetTypeID
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secpolicysearchgettypeid
source_url: 'https://developer.apple.com/documentation/security/secpolicysearchgettypeid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicysearchgettypeid.json'
content_hash: 'sha256:7281015123758b26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicySearchGetTypeID

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a `SecPolicySearch` object belongs.

<sub>Mac Catalyst, macOS</sub>

```objc
CFTypeID SecPolicySearchGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [SecPolicySearch](secpolicysearch.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecPolicySearch](secpolicysearch.md) object. You can compare this value to the `CFTypeID` identifier obtained by calling the `CFGetTypeID` function on a specific object. These values might change from release to release or platform to platform.
