---
title: recordedFileSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/recordedfilesize
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/recordedfilesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/recordedfilesize.json'
content_hash: 'sha256:b4da86e4a3d32ddb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# recordedFileSize

<sub>Instance Property</sub>

Indicates the size, in bytes, of the data recorded to the current output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var recordedFileSize: Int64 { get }
```

## Discussion

If a recording is in progress, this property returns the size in bytes of the data recorded so far.

## See Also

### Setting file output properties

- [delegate](delegate.md) — The delegate object for the capture file output.
- [maxRecordedDuration](maxrecordedduration.md) — The longest duration allowed for the recording.
- [maxRecordedFileSize](maxrecordedfilesize.md) — The maximum size, in bytes, of the data that should be recorded by the receiver.
- [minFreeDiskSpaceLimit](minfreediskspacelimit.md) — The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [outputFileURL](outputfileurl.md) — The URL to which output is directed.
- [recordedDuration](recordedduration.md) — Indicates the duration of the media recorded to the current output file.
- [recording](isrecording.md) — Indicates whether recording is in progress.
- [recordingPaused](isrecordingpaused.md) — Indicates whether recording to the current output file is paused.
