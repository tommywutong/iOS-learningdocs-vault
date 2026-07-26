---
title: functions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstitchedlibrarydescriptor/functions
source_url: 'https://developer.apple.com/documentation/metal/mtlstitchedlibrarydescriptor/functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstitchedlibrarydescriptor/functions.json'
content_hash: 'sha256:ca10e1021b661d7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStitchedLibraryDescriptor](../mtlstitchedlibrarydescriptor.md)

# functions

<sub>Instance Property</sub>

The list of functions for creating the stitched library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var functions: [any MTLFunction] { get set }
```

## Discussion

The function objects need to all be created by the same Metal device object that you’ll use to create the library. The MSL functions referenced by these function objects need to be declared with the `stitchable` attribute, as in the example below:

```metal
[[stitchable]]
 float add(float a, float b)
{
    return a + b;
}
```

## See Also

### Configuring a stitched library

- [functionGraphs](functiongraphs.md) — The function graphs that define the new stitched library’s functions.
