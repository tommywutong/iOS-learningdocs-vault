---
title: Mach-O Architecture
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/1495005-mach-o-architecture
source_url: 'https://developer.apple.com/documentation/foundation/1495005-mach-o-architecture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1495005-mach-o-architecture.json'
content_hash: 'sha256:48ac94e26c66da77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Resources](resources.md) · [Bundle](bundle.md)

# Mach-O Architecture

<sub>API Collection</sub>

Constants that describe the CPU types that a bundle’s executable code supports.

## Topics

### Constants

- [NSBundleExecutableArchitectureARM64](nsbundleexecutablearchitecturearm64.md) — The 64-bit ARM architecture.
- [NSBundleExecutableArchitectureI386](nsbundleexecutablearchitecturei386.md) — The 32-bit Intel architecture.
- [NSBundleExecutableArchitectureX86_64](nsbundleexecutablearchitecturex86_64.md) — The 64-bit Intel architecture.
- [NSBundleExecutableArchitecturePPC](nsbundleexecutablearchitectureppc.md) — The 32-bit PowerPC architecture.
- [NSBundleExecutableArchitecturePPC64](nsbundleexecutablearchitectureppc64.md) — The 64-bit PowerPC architecture.

## See Also

### Loading code from a bundle

- [executableArchitectures](bundle/executablearchitectures.md) — An array of numbers indicating the architecture types supported by the bundle’s executable.
- [- preflightAndReturnError:](<bundle/preflight().md>) — Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [- load](<bundle/load().md>) — Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [- loadAndReturnError:](<bundle/loadandreturnerror().md>) — Loads the bundle’s executable code and returns any errors.
- [- unload](<bundle/unload().md>) — Unloads the code associated with the receiver.
- [loaded](bundle/isloaded.md) — The load status of a bundle.
