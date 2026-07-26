---
title: MTLNewComputePipelineStateCompletionHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlnewcomputepipelinestatecompletionhandler
source_url: 'https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatecompletionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlnewcomputepipelinestatecompletionhandler.json'
content_hash: 'sha256:d03a8c6d38085c84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLNewComputePipelineStateCompletionHandler

<sub>Type Alias</sub>

A completion handler signature a method calls when it finishes creating a compute pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLNewComputePipelineStateCompletionHandler = ((any MTLComputePipelineState)?, (any Error)?) -> Void
```

## Parameters

- `computePipelineState` — An [MTLComputePipelineState](mtlcomputepipelinestate.md) instance if the method completes successfully; otherwise `nil`.

- `error` — On return, if an error occurs, a pointer to an error information instance; otherwise `nil`.

## See Also

### Supporting types

- [MTLNewRenderPipelineStateCompletionHandler](mtlnewrenderpipelinestatecompletionhandler.md) — A completion handler signature a method calls when it finishes creating a render pipeline.
- [MTLNewRenderPipelineStateWithReflectionCompletionHandler](mtlnewrenderpipelinestatewithreflectioncompletionhandler.md) — A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [MTLNewComputePipelineStateWithReflectionCompletionHandler](mtlnewcomputepipelinestatewithreflectioncompletionhandler.md) — A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.
