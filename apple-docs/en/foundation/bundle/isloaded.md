---
title: isLoaded
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/isloaded
source_url: 'https://developer.apple.com/documentation/foundation/bundle/isloaded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/isloaded.json'
content_hash: 'sha256:9b882dc0a01dfa4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# isLoaded

<sub>Instance Property</sub>

The load status of a bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLoaded: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the bundle’s code is currently loaded, otherwise [false](../../swift/false.md).

## See Also

### Loading code from a bundle

- [executableArchitectures](executablearchitectures.md) — An array of numbers indicating the architecture types supported by the bundle’s executable.
- [- preflightAndReturnError:](<preflight().md>) — Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [- load](<load().md>) — Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [- loadAndReturnError:](<loadandreturnerror().md>) — Loads the bundle’s executable code and returns any errors.
- [- unload](<unload().md>) — Unloads the code associated with the receiver.
- [Mach-O Architecture](../1495005-mach-o-architecture.md) — Constants that describe the CPU types that a bundle’s executable code supports.
