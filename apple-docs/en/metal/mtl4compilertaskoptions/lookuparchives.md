---
title: lookupArchives
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4compilertaskoptions/lookuparchives
source_url: 'https://developer.apple.com/documentation/metal/mtl4compilertaskoptions/lookuparchives'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4compilertaskoptions/lookuparchives.json'
content_hash: 'sha256:553f8e05ba301b25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CompilerTaskOptions](../mtl4compilertaskoptions.md)

# lookupArchives

<sub>Instance Property</sub>

An array of archive instances that can potentially accelerate a compilation task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lookupArchives: [any MTL4Archive]? { get set }
```

## Discussion

The compiler can reduce the runtime of a compilation task if it finds an entry that matches a function description within any of the archives in this array. The compiler searches the archives in the order of the array’s element.

Consider adding archives to the array in scenarios that can benefit from the runtime savings, such as repeat builds or when your app can share compilation results across multiple contexts.

> [!important] Important
> Only add [MTL4Archive](../mtl4archive.md) instances to the array that are compatible with the Metal device.
