---
title: 'synchronizedData(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesynchronizeddatacollection/synchronizeddata(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection/synchronizeddata(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddatacollection/synchronizeddata%28for%3A%29.json'
content_hash: 'sha256:569112e3d3a87673'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedDataCollection](../avcapturesynchronizeddatacollection.md)

# synchronizedData(for:)

<sub>Instance Method</sub>

Returns synchronized data captured by the specified capture output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func synchronizedData(for captureOutput: AVCaptureOutput) -> AVCaptureSynchronizedData?
```

## Parameters

- `captureOutput` — The capture output for which to retrieve data.

## Return Value

A synchronized data object corresponding to the specified capture output.

## See Also

### Accessing synchronized data

- [count](count.md) — The number of synchronized data objects in the collection.
- [- objectForKeyedSubscript:](<subscript(__).md>) — Returns data captured by the specified capture output, using subscript syntax.
