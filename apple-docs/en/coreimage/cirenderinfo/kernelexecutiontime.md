---
title: kernelExecutionTime
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirenderinfo/kernelexecutiontime
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderinfo/kernelexecutiontime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderinfo/kernelexecutiontime.json'
content_hash: 'sha256:3ff07af958c8410d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderInfo](../cirenderinfo.md)

# kernelExecutionTime

<sub>Instance Property</sub>

The amount of time a render spent executing kernels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var kernelExecutionTime: TimeInterval { get }
```

## See Also

### Instance Properties

- [passCount](passcount.md) — The number of passes the render took.
- [pixelsProcessed](pixelsprocessed.md) — The number of pixels the render produced executing kernels.
- [kernelCompileTime](kernelcompiletime.md)
