---
title: inheritPipelineState
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbufferdescriptor/inheritpipelinestate
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/inheritpipelinestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferdescriptor/inheritpipelinestate.json'
content_hash: 'sha256:321ec0455fedff3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBufferDescriptor](../mtlindirectcommandbufferdescriptor.md)

# inheritPipelineState

<sub>Instance Property</sub>

A Boolean value that determines where commands in the indirect command buffer get their pipeline state from when you execute them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inheritPipelineState: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). If the value is [false](../../swift/false.md), set the pipeline state object when you encode the commands into the indirect command buffer. The commands ignore any pipeline state object set on the parent encoder.

If you set the value to [true](../../swift/true.md), don’t set a pipeline state object when you encode commands into the indirect command buffer. The commands use (inherit) the pipeline stage object that you set on the parent encoder.

This property doesn’t exist in iOS 12 and earlier, and tvOS 12 and earlier. If you create an indirect command buffer on those systems, it inherits the pipeline state, exactly as if the property existed, with a value of [true](../../swift/true.md). If you need your app to run on earlier versions of iOS, use an availability attribute to set the property conditionally:

**Swift**

```swift
if #available(iOS 13.0, tvOS 13, *) {
    descriptor.inheritPipelineState = true
}
```

**Objective-C**

```objective-c
if (@available(iOS 13.0, tvOS 13.0, *)) {
    descriptor.inheritPipelineState = YES;
}
```

## See Also

### Declaring command inheritance

- [inheritBuffers](inheritbuffers.md) — A Boolean value that determines where commands in the indirect command buffer get their buffer arguments from when you execute them.
