---
title: options
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctiondescriptor/options
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctiondescriptor/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctiondescriptor/options.json'
content_hash: 'sha256:cb40b4b3646fbd62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionDescriptor](../mtlfunctiondescriptor.md)

# options

<sub>Instance Property</sub>

Flags specifying how Metal should create the new function object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var options: MTLFunctionOptions { get set }
```

## See Also

### Specifying the function configuration

- [name](name.md) — The name of the function to fetch from the library.
- [specializedName](specializedname.md) — A new name for the created function object.
- [constantValues](constantvalues.md) — The set of constant values assigned to the function constants.
- [binaryArchives](binaryarchives.md) — The binary archives to search for a previously-compiled version of this function.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
- [MTLLinkedFunctions](../mtllinkedfunctions.md) — A set of related functions that Metal links to when necessary to create the function instance.
