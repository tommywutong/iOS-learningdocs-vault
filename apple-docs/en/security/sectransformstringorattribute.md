---
title: SecTransformStringOrAttribute
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformstringorattribute
source_url: 'https://developer.apple.com/documentation/security/sectransformstringorattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformstringorattribute.json'
content_hash: 'sha256:da09676569cfebf6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformStringOrAttribute

<sub>Type Alias</sub>

A type that may be either a string or an attribute reference.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
typealias SecTransformStringOrAttribute = CFTypeRef
```

## Discussion

Use a value of this type in place of either a [CFString](../corefoundation/cfstring.md) or a [SecTransformAttribute](sectransformattribute.md) when referring to transform attributes, such as with the `attribute` parameter in calls to the [SecTransformCustomSetAttribute](<sectransformcustomsetattribute(________).md>)  and [SecTransformCustomGetAttribute](<sectransformcustomgetattribute(______).md>) functions. When using a name, see [Transform Attributes](transform-attributes.md) for a list of valid key names.
