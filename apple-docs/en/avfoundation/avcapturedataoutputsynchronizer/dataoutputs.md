---
title: dataOutputs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedataoutputsynchronizer/dataoutputs
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/dataoutputs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedataoutputsynchronizer/dataoutputs.json'
content_hash: 'sha256:e1153ea41d364491'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDataOutputSynchronizer](../avcapturedataoutputsynchronizer.md)

# dataOutputs

<sub>Instance Property</sub>

The list of data outputs governed by this data output synchronizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var dataOutputs: [AVCaptureOutput] { get }
```

## Discussion

This array is read-only. You configure the list of data outputs to synchronize only when you create an [AVCaptureDataOutputSynchronizer](../avcapturedataoutputsynchronizer.md) object.

> [!note] Note
> The [AVCaptureDataOutputSynchronizer](../avcapturedataoutputsynchronizer.md) class overrides the delegate (and delegate dispatch queue) settings of all of its data outputs, but video and depth data outputs still honor their [alwaysDiscardsLateVideoFrames](../avcapturevideodataoutput/alwaysdiscardslatevideoframes.md) and [alwaysDiscardsLateDepthData](../avcapturedepthdataoutput/alwaysdiscardslatedepthdata.md) properties.

## See Also

### Configuring synchronized capture

- [- initWithDataOutputs:](<init(dataoutputs_).md>) — Creates a capture output synchronizer for the specified capture outputs.
