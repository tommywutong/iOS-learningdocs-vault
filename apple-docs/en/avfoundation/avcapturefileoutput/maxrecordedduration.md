---
title: maxRecordedDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/maxrecordedduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/maxrecordedduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/maxrecordedduration.json'
content_hash: 'sha256:be08e07438bdecb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# maxRecordedDuration

<sub>Instance Property</sub>

The longest duration allowed for the recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var maxRecordedDuration: CMTime { get set }
```

## Discussion

This property specifies a hard limit on the duration of recorded files. Recording is stopped when the limit is reached and the [- captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:](<../avcapturefileoutputrecordingdelegate/fileoutput(__didfinishrecordingto_from_error_).md>) delegate method is invoked with an appropriate error. The default value of this property is [invalid](../../coremedia/cmtime/invalid.md), which indicates no limit.

## See Also

### Setting file output properties

- [delegate](delegate.md) — The delegate object for the capture file output.
- [maxRecordedFileSize](maxrecordedfilesize.md) — The maximum size, in bytes, of the data that should be recorded by the receiver.
- [minFreeDiskSpaceLimit](minfreediskspacelimit.md) — The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [outputFileURL](outputfileurl.md) — The URL to which output is directed.
- [recordedDuration](recordedduration.md) — Indicates the duration of the media recorded to the current output file.
- [recordedFileSize](recordedfilesize.md) — Indicates the size, in bytes, of the data recorded to the current output file.
- [recording](isrecording.md) — Indicates whether recording is in progress.
- [recordingPaused](isrecordingpaused.md) — Indicates whether recording to the current output file is paused.
