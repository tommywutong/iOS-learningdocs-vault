---
title: retainedReferences
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/retainedreferences
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/retainedreferences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/retainedreferences.json'
content_hash: 'sha256:dd5bc487ae48d8dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# retainedReferences

<sub>Instance Property</sub>

A Boolean value that indicates whether the command buffer maintains strong references to the resources it uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var retainedReferences: Bool { get }
```

## Discussion

You can configure this property when you create a command buffer by setting [retainedReferences](../mtlcommandbufferdescriptor/retainedreferences.md) of an [MTLCommandBufferDescriptor](../mtlcommandbufferdescriptor.md) instance and calling the [- commandBufferWithDescriptor:](<../mtlcommandqueue/makecommandbuffer(descriptor_).md>) method. The [- commandBuffer](<../mtlcommandqueue/makecommandbuffer().md>) method sets this property to [true](../../swift/true.md), and [- commandBufferWithUnretainedReferences](<../mtlcommandqueue/makecommandbufferwithunretainedreferences().md>) sets it to [false](../../swift/false.md).

If [false](../../swift/false.md), your app is responsible for maintaining strong references to all the resources the command buffer relies on until it completes.

> [!important] Important
> Releasing a resource before a command buffer’s commands complete may cause a runtime error or erratic behavior.
