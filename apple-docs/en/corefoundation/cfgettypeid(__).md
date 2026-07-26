---
title: 'CFGetTypeID(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfgettypeid(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfgettypeid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfgettypeid%28_%3A%29.json'
content_hash: 'sha256:7a4dc22b00290114'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFGetTypeID(_:)

<sub>Function</sub>

Returns the unique identifier of an opaque type to which a Core Foundation object belongs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFGetTypeID(_ cf: CFTypeRef!) -> CFTypeID
```

## Parameters

- `cf` — The CFType object to examine.

## Return Value

A value of type [CFTypeID](cftypeid.md) that identifies the opaque type of `cf`.

## Discussion

This function returns a value that uniquely identifies the opaque type of any Core Foundation object. You can compare this value with the known [CFTypeID](cftypeid.md) identifier obtained with a “GetTypeID” function specific to a type, for example [CFDateGetTypeID](<cfdategettypeid().md>). These values might change from release to release or platform to platform.

## See Also

### Miscellaneous Functions

- [CFCopyDescription](<cfcopydescription(__).md>) — Returns a textual description of a Core Foundation object.
- [CFCopyTypeIDDescription](<cfcopytypeiddescription(__).md>) — Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [CFShow](<cfshow(__).md>) — Prints a description of a Core Foundation object to stderr.
