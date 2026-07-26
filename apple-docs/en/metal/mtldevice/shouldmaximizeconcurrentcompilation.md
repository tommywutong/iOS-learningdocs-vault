---
title: shouldMaximizeConcurrentCompilation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/shouldmaximizeconcurrentcompilation
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/shouldmaximizeconcurrentcompilation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/shouldmaximizeconcurrentcompilation.json'
content_hash: 'sha256:636bf7e4f3435df4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# shouldMaximizeConcurrentCompilation

<sub>Instance Property</sub>

A Boolean value that indicates whether the device uses additional CPU threads for compilation tasks.

<sub>macOS</sub>

```swift
var shouldMaximizeConcurrentCompilation: Bool { get set }
```

## Discussion

The property’s default value is [false](../../swift/false.md). You can retrieve the number of concurrent CPU threads the device is currently using by checking the [maximumConcurrentCompilationTaskCount](maximumconcurrentcompilationtaskcount.md) property.

> [!note] Note
> The number of additional CPU threads automatically scales with the system’s hardware capabilities.
