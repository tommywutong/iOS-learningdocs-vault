---
title: SecRequirementGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secrequirementgettypeid()
source_url: 'https://developer.apple.com/documentation/security/secrequirementgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secrequirementgettypeid%28%29.json'
content_hash: 'sha256:28eac52471bfa03e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecRequirementGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a code requirement object belongs.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecRequirementGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecRequirement](secrequirement.md) object.

## Discussion

You can compare the value returned by this function to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function on a specific object. These values might change from release to release or platform to platform.

## See Also

### Related Documentation

- [SecRequirementCreateWithString](<secrequirementcreatewithstring(______).md>) — Creates a code requirement object by compiling a valid text representation of a code requirement.
- [SecRequirementCreateWithStringAndErrors](<secrequirementcreatewithstringanderrors(________).md>) — Creates a code requirement object by compiling a valid text representation of a code requirement and returns detailed error information in the case of failure.
