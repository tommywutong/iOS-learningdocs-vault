---
title: functionNames
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibrary/functionnames
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/functionnames'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/functionnames.json'
content_hash: 'sha256:1642fb59c5f982ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# functionNames

<sub>Instance Property</sub>

The names of all public functions in the library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var functionNames: [String] { get }
```

## Discussion

Inside a Metal library, functions with the `vertex`, `fragment`, or `kernel` function attributes are entry points into the library. Functions without these attributes are private.
