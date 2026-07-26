---
title: SecTaskGetTypeID()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectaskgettypeid()
source_url: 'https://developer.apple.com/documentation/security/sectaskgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectaskgettypeid%28%29.json'
content_hash: 'sha256:402db6a78c2889f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTaskGetTypeID()

<sub>Function</sub>

Returns the unique identifier of the opaque type to which a task object belongs.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTaskGetTypeID() -> CFTypeID
```

## Return Value

A value that identifies the opaque type of a [SecTask](sectask.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [SecTask](sectask.md) object. You can compare this value to the [CFTypeID](../corefoundation/cftypeid.md) identifier obtained by calling the [CFGetTypeID(_:)](<../corefoundation/cfgettypeid(__).md>) function on a specific object. These values might change from release to release or platform to platform.
