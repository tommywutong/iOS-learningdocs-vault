---
title: specializedName
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctiondescriptor/specializedname
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctiondescriptor/specializedname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctiondescriptor/specializedname.json'
content_hash: 'sha256:ad8e696596c11df6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionDescriptor](../mtlfunctiondescriptor.md)

# specializedName

<sub>Instance Property</sub>

A new name for the created function object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var specializedName: String? { get set }
```

## Discussion

The default value is `nil`. If you specify a value for this property, Metal creates the new [MTLFunction](../mtlfunction.md) object with the new name. Use this property if you want to specialize a function with multiple variants and give each a distinct name.

## See Also

### Specifying the function configuration

- [name](name.md) — The name of the function to fetch from the library.
- [constantValues](constantvalues.md) — The set of constant values assigned to the function constants.
- [options](options.md) — Flags specifying how Metal should create the new function object.
- [binaryArchives](binaryarchives.md) — The binary archives to search for a previously-compiled version of this function.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
- [MTLLinkedFunctions](../mtllinkedfunctions.md) — A set of related functions that Metal links to when necessary to create the function instance.
