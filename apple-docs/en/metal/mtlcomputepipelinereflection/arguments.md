---
title: arguments
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlcomputepipelinereflection/arguments
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection/arguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinereflection/arguments.json'
content_hash: 'sha256:6251fcdda39b75a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineReflection](../mtlcomputepipelinereflection.md)

# arguments

<sub>Instance Property</sub>

An array of instances that describe the arguments of a compute function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var arguments: [MTLArgument] { get }
```

## Discussion

Each element in the array is an [MTLArgument](../mtlargument.md) instance that describes one of the function’s arguments. The elements in the array are in the same order that the arguments appear in the function declaration.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
