---
title: failOnBinaryArchiveMiss
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstitchedlibraryoptions/failonbinaryarchivemiss
source_url: 'https://developer.apple.com/documentation/metal/mtlstitchedlibraryoptions/failonbinaryarchivemiss'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstitchedlibraryoptions/failonbinaryarchivemiss.json'
content_hash: 'sha256:642b608401a48598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStitchedLibraryOptions](../mtlstitchedlibraryoptions.md)

# failOnBinaryArchiveMiss

<sub>Type Property</sub>

An option that instructs the compiler to return an error when a GPU function for a stitched library isn’t in a binary archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var failOnBinaryArchiveMiss: MTLStitchedLibraryOptions { get }
```

## Discussion

By default, Metal compiles the functions for a stitched library if they aren’t in a binary archive. When you set this option, Metal returns an error instead of compiling a missing function.
