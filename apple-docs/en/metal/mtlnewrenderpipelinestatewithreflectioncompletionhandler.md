---
title: MTLNewRenderPipelineStateWithReflectionCompletionHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlnewrenderpipelinestatewithreflectioncompletionhandler
source_url: 'https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatewithreflectioncompletionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlnewrenderpipelinestatewithreflectioncompletionhandler.json'
content_hash: 'sha256:eddf869788281a4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLNewRenderPipelineStateWithReflectionCompletionHandler

<sub>Type Alias</sub>

A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler = ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void
```

## Parameters

- `renderPipelineState` — An [MTLRenderPipelineState](mtlrenderpipelinestate.md) instance if the method successfully compiles the library without any errors; otherwise `nil`.

- `reflection` — An [MTLRenderPipelineReflection](mtlrenderpipelinereflection.md) instance if the method completes successfully; otherwise `nil`.

- `error` — If an error occurs, an error information instance; otherwise `nil`.

## See Also

### Supporting types

- [MTLNewRenderPipelineStateCompletionHandler](mtlnewrenderpipelinestatecompletionhandler.md) — A completion handler signature a method calls when it finishes creating a render pipeline.
- [MTLNewComputePipelineStateCompletionHandler](mtlnewcomputepipelinestatecompletionhandler.md) — A completion handler signature a method calls when it finishes creating a compute pipeline.
- [MTLNewComputePipelineStateWithReflectionCompletionHandler](mtlnewcomputepipelinestatewithreflectioncompletionhandler.md) — A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.
