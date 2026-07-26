---
title: outputFileURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/outputfileurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/outputfileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/outputfileurl.json'
content_hash: 'sha256:f4e5ae8862e0ac4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# outputFileURL

<sub>Instance Property</sub>

The URL to which output is directed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var outputFileURL: URL? { get }
```

## See Also

### Setting file output properties

- [delegate](delegate.md) — The delegate object for the capture file output.
- [maxRecordedDuration](maxrecordedduration.md) — The longest duration allowed for the recording.
- [maxRecordedFileSize](maxrecordedfilesize.md) — The maximum size, in bytes, of the data that should be recorded by the receiver.
- [minFreeDiskSpaceLimit](minfreediskspacelimit.md) — The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [recordedDuration](recordedduration.md) — Indicates the duration of the media recorded to the current output file.
- [recordedFileSize](recordedfilesize.md) — Indicates the size, in bytes, of the data recorded to the current output file.
- [recording](isrecording.md) — Indicates whether recording is in progress.
- [recordingPaused](isrecordingpaused.md) — Indicates whether recording to the current output file is paused.
