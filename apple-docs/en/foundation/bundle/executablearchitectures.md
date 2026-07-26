---
title: executableArchitectures
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/executablearchitectures
source_url: 'https://developer.apple.com/documentation/foundation/bundle/executablearchitectures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/executablearchitectures.json'
content_hash: 'sha256:071c9f878d3d2e6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# executableArchitectures

<sub>Instance Property</sub>

An array of numbers indicating the architecture types supported by the bundle’s executable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var executableArchitectures: [NSNumber]? { get }
```

## Discussion

An array of `NSNumber` objects, each of which contains an integer value corresponding to a supported processor architecture. For a list of common architecture types, see the constants in [Mach-O Architecture](../1495005-mach-o-architecture.md). If the bundle does not contain a Mach-O executable, this is `nil`.

The bundle scans its Mach-O executable and returns all of the architecture types it finds. Because they are taken directly from the executable, the values may not always correspond to one of the well-known CPU types defined in [Mach-O Architecture](../1495005-mach-o-architecture.md).

## See Also

### Loading code from a bundle

- [- preflightAndReturnError:](<preflight().md>) — Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [- load](<load().md>) — Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [- loadAndReturnError:](<loadandreturnerror().md>) — Loads the bundle’s executable code and returns any errors.
- [- unload](<unload().md>) — Unloads the code associated with the receiver.
- [loaded](isloaded.md) — The load status of a bundle.
- [Mach-O Architecture](../1495005-mach-o-architecture.md) — Constants that describe the CPU types that a bundle’s executable code supports.
