---
title: minFreeDiskSpaceLimit
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/minfreediskspacelimit
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/minfreediskspacelimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/minfreediskspacelimit.json'
content_hash: 'sha256:40b8c94122b7f01c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# minFreeDiskSpaceLimit

<sub>Instance Property</sub>

The minimum amount of free space, in bytes, required for recording to continue on a given volume.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var minFreeDiskSpaceLimit: Int64 { get set }
```

## Discussion

This property specifies a hard lower limit on the amount of free space that must remain on a target volume for recording to continue. Recording is stopped when the limit is reached and the [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<../avcapturefileoutputrecordingdelegate/fileoutput(__didfinishrecordingto_from_error_).md>) delegate method is invoked with an appropriate error.

## See Also

### Setting file output properties

- [delegate](delegate.md) — The delegate object for the capture file output.
- [maxRecordedDuration](maxrecordedduration.md) — The longest duration allowed for the recording.
- [maxRecordedFileSize](maxrecordedfilesize.md) — The maximum size, in bytes, of the data that should be recorded by the receiver.
- [outputFileURL](outputfileurl.md) — The URL to which output is directed.
- [recordedDuration](recordedduration.md) — Indicates the duration of the media recorded to the current output file.
- [recordedFileSize](recordedfilesize.md) — Indicates the size, in bytes, of the data recorded to the current output file.
- [recording](isrecording.md) — Indicates whether recording is in progress.
- [recordingPaused](isrecordingpaused.md) — Indicates whether recording to the current output file is paused.
