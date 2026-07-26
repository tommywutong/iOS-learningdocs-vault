---
title: 'resolveCounterHeap(_:range:buffer:fenceToWait:fenceToUpdate:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/resolvecounterheap(_:range:buffer:fencetowait:fencetoupdate:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/resolvecounterheap(_:range:buffer:fencetowait:fencetoupdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/resolvecounterheap%28_%3Arange%3Abuffer%3Afencetowait%3Afencetoupdate%3A%29.json'
content_hash: 'sha256:28199cf3be1c67d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# resolveCounterHeap(_:range:buffer:fenceToWait:fenceToUpdate:)

<sub>Instance Method</sub>

Encodes a command that resolves an opaque counter heap into a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resolveCounterHeap(_ counterHeap: any MTL4CounterHeap, range: Range<Int>, buffer: MTL4BufferRange, fenceToWait: (any MTLFence)? = nil, fenceToUpdate: (any MTLFence)? = nil)
```

## Parameters

- `counterHeap` — A heap the command resolves.

- `range` — A range of index values within the heap the command resolves.

- `buffer` — A buffer the command saves the data it resolves into.

- `fenceToWait` — A fence the GPU waits for before starting, if applicable; otherwise `nil`.

- `fenceToUpdate` — A fence the system updates after the command finishes resolving the data; otherwise `nil`.

## Discussion

The command this method encodes converts the data within a counter heap into a common format and stores it into the `buffer` parameter.

The command places each entry in the counter heap within `range` sequentially, starting at `offset`. Each entry needs to be a fixed size that you can query by calling the [- sizeOfCounterHeapEntry:](<../mtldevice/size(ofcounterheapentry_).md>) method.

This command runs during the `MTLStageBlit` stage of the GPU timeline. Barrier against this stage to ensure the data is present in the resolve buffer parameter before you access it.

> [!note] Note
> Your app needs ensure the GPU places data in the heap before you resolve it by synchronizing this stage with other GPU operations.

Similarly, your app needs to synchronize any GPU accesses to `buffer` after the command completes with barrier.

If your app needs to access `buffer` from the CPU, signal an [MTLSharedEvent](../mtlsharedevent.md) to notify the CPU when it’s ready. Alternatively, you can resolve the heap’s data from the CPU by calling the heap’s [resolveCounterRange:](../mtl4counterheap/resolvecounterrange_.md) method.
