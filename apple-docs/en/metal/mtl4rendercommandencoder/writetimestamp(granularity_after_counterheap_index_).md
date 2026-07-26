---
title: 'writeTimestamp(granularity:after:counterHeap:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/writetimestamp(granularity:after:counterheap:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/writetimestamp(granularity:after:counterheap:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/writetimestamp%28granularity%3Aafter%3Acounterheap%3Aindex%3A%29.json'
content_hash: 'sha256:b4156d620fce5965'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# writeTimestamp(granularity:after:counterHeap:index:)

<sub>Instance Method</sub>

Writes a GPU timestamp into the given [MTL4CounterHeap](../mtl4counterheap.md) at `index` after `stage` completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeTimestamp(granularity: MTL4TimestampGranularity, after stage: MTLRenderStages, counterHeap: any MTL4CounterHeap, index: Int)
```

## Parameters

- `granularity` — A [MTL4TimestampGranularity](../mtl4timestampgranularity.md) hint.

- `stage` — [MTLRenderStages](../mtlrenderstages.md) that need to complete before Metal writes the timestamp. This may also include later stages that are related, for example [MTLRenderStageMesh](../mtlrenderstages/mesh.md) may include [MTLRenderStageVertex](../mtlrenderstages/vertex.md).

- `counterHeap` — [MTL4CounterHeap](../mtl4counterheap.md) into which Metal writes timestamps.

- `index` — The index value into which Metal writes this timestamp.

## Discussion

This command only guarantees all draws prior to this command are complete when Metal writes the timestamp into the counter heap you provide in the `counterHeap` parameter. The timestamp may also include subsequent operations.

If you call this method before any draw calls, Metal writes a timestamp before the stage you specify in the `stage` parameter begins.
