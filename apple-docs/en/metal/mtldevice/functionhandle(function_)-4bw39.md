---
title: 'functionHandle(function:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/functionhandle(function:)-4bw39'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/functionhandle(function:)-4bw39'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/functionhandle%28function%3A%29-4bw39.json'
content_hash: 'sha256:0784041bbc4a638e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# functionHandle(function:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func functionHandle(function: any MTLFunction) -> (any MTLFunctionHandle)?
```

## Discussion

Returns the function handle for a function that was compiled with MTLFunctionOptionPipelineIndependent and MTLFunctionOptionCompileToBinary.
