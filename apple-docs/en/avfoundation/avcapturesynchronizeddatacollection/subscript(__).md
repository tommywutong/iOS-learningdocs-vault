---
title: 'subscript(_:)'
framework: AVFoundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesynchronizeddatacollection/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizeddatacollection/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizeddatacollection/subscript%28_%3A%29.json'
content_hash: 'sha256:d2c8b10e2c226307'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedDataCollection](../avcapturesynchronizeddatacollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns data captured by the specified capture output, using subscript syntax.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
subscript(key: AVCaptureOutput) -> AVCaptureSynchronizedData? { get }
```

## Parameters

- `key` — The capture output for which to retrieve data.

## Return Value

A synchronized data object corresponding to the specified capture output.

## Discussion

This call is equivalent to the [- synchronizedDataForCaptureOutput:](<synchronizeddata(for_).md>) method, but allows subscript syntax.

## See Also

### Accessing synchronized data

- [count](count.md) — The number of synchronized data objects in the collection.
- [- synchronizedDataForCaptureOutput:](<synchronizeddata(for_).md>) — Returns synchronized data captured by the specified capture output.
