---
title: MTLNewRenderPipelineStateCompletionHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlnewrenderpipelinestatecompletionhandler
source_url: 'https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatecompletionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlnewrenderpipelinestatecompletionhandler.json'
content_hash: 'sha256:5e4a16ea98f7bad1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLNewRenderPipelineStateCompletionHandler

<sub>Type Alias</sub>

A completion handler signature a method calls when it finishes creating a render pipeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLNewRenderPipelineStateCompletionHandler = ((any MTLRenderPipelineState)?, (any Error)?) -> Void
```

## Parameters

- `renderPipelineState` — An [MTLRenderPipelineState](mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise `nil`.

- `error` — If an error occurs, an error information instance; otherwise `nil`.

## See Also

### Supporting types

- [MTLNewRenderPipelineStateWithReflectionCompletionHandler](mtlnewrenderpipelinestatewithreflectioncompletionhandler.md) — A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [MTLNewComputePipelineStateCompletionHandler](mtlnewcomputepipelinestatecompletionhandler.md) — A completion handler signature a method calls when it finishes creating a compute pipeline.
- [MTLNewComputePipelineStateWithReflectionCompletionHandler](mtlnewcomputepipelinestatewithreflectioncompletionhandler.md) — A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.
