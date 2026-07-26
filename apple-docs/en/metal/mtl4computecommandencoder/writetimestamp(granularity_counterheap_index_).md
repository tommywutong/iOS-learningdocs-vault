---
title: 'writeTimestamp(granularity:counterHeap:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/writetimestamp(granularity:counterheap:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/writetimestamp(granularity:counterheap:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/writetimestamp%28granularity%3Acounterheap%3Aindex%3A%29.json'
content_hash: 'sha256:2d5b06364a8136b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# writeTimestamp(granularity:counterHeap:index:)

<sub>Instance Method</sub>

Writes a GPU timestamp into a heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeTimestamp(granularity: MTL4TimestampGranularity, counterHeap: any MTL4CounterHeap, index: Int)
```

## Parameters

- `granularity` — [MTL4TimestampGranularity](../mtl4timestampgranularity.md) hint to Metal about acceptable the level of precision.

- `counterHeap` — [MTL4CounterHeap](../mtl4counterheap.md) to write timestamps into.

- `index` — The index value into which Metal writes the timestamp.

## Discussion

The method ensures that any prior work finishes, but doesn’t delay any subsequent work.

You can alter this command’s behavior through the `granularity` parameter.

- Pass [MTL4TimestampGranularityRelaxed](../mtl4timestampgranularity/relaxed.md) to allow Metal to provide timestamps with minimal impact to runtime performance, but with less detail. For example, the command may group all timestamps for a pass together.
- Pass [MTL4TimestampGranularityPrecise](../mtl4timestampgranularity/precise.md) to request that Metal provides timestamps with the most detail. This can affect runtime performance.
