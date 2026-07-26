---
title: 'dataOutputSynchronizer(_:didOutput:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer(_:didoutput:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer(_:didoutput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedataoutputsynchronizerdelegate/dataoutputsynchronizer%28_%3Adidoutput%3A%29.json'
content_hash: 'sha256:15e5a478ef9c2ca8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDataOutputSynchronizerDelegate](../avcapturedataoutputsynchronizerdelegate.md)

# dataOutputSynchronizer(_:didOutput:)

<sub>Instance Method</sub>

Provides a collection of synchronized capture data to the delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func dataOutputSynchronizer(_ synchronizer: AVCaptureDataOutputSynchronizer, didOutput synchronizedDataCollection: AVCaptureSynchronizedDataCollection)
```

## Parameters

- `synchronizer` — The synchronizer object delivering synchronized data.

- `synchronizedDataCollection` — A collection of data samples, one for each capture output governed by the data output synchronizer for which capture data is ready.

## Discussion

Use the data collection’s [- synchronizedDataForCaptureOutput:](<../avcapturesynchronizeddatacollection/synchronizeddata(for_).md>) method (or equivalent [- objectForKeyedSubscript:](<../avcapturesynchronizeddatacollection/subscript(__).md>) operator) to retrieve the captured data corresponding to each capture output.
