---
title: 'makeScratchBuffer(minimumSize:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlioscratchbufferallocator/makescratchbuffer(minimumsize:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlioscratchbufferallocator/makescratchbuffer(minimumsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlioscratchbufferallocator/makescratchbuffer%28minimumsize%3A%29.json'
content_hash: 'sha256:baa7c815c349a8f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOScratchBufferAllocator](../mtlioscratchbufferallocator.md)

# makeScratchBuffer(minimumSize:)

<sub>Instance Method</sub>

Creates a scratch memory buffer for an input/output command queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeScratchBuffer(minimumSize: Int) -> (any MTLIOScratchBuffer)?
```

## Parameters

- `minimumSize` — The number of bytes the input/output command buffer needs to successfully run a command buffer.

## Return Value

An [MTLIOScratchBuffer](../mtlioscratchbuffer.md) instance that your app implements or `nil`.

## Discussion

Your app can reduce additional callbacks from the framework by providing additional memory above `minimumSize`. If your implementation returns `nil`, the input/output command queue cancels the [MTLIOCommandBuffer](../mtliocommandbuffer.md) instance that needs the scratch buffer memory.
