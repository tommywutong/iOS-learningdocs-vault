---
title: binaryArchives
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctiondescriptor/binaryarchives
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctiondescriptor/binaryarchives'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctiondescriptor/binaryarchives.json'
content_hash: 'sha256:ea9a23aefcf09faf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionDescriptor](../mtlfunctiondescriptor.md)

# binaryArchives

<sub>Instance Property</sub>

The binary archives to search for a previously-compiled version of this function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var binaryArchives: [any MTLBinaryArchive]? { get set }
```

## Discussion

If you specify an archive that includes a fully compiled version of this function, Metal uses the compiled version rather than creating a new one.

## See Also

### Specifying the function configuration

- [name](name.md) — The name of the function to fetch from the library.
- [specializedName](specializedname.md) — A new name for the created function object.
- [constantValues](constantvalues.md) — The set of constant values assigned to the function constants.
- [options](options.md) — Flags specifying how Metal should create the new function object.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
- [MTLLinkedFunctions](../mtllinkedfunctions.md) — A set of related functions that Metal links to when necessary to create the function instance.
