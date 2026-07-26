---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturefileoutput/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutput/delegate.json'
content_hash: 'sha256:b2027a26164c91d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutput](../avcapturefileoutput.md)

# delegate

<sub>Instance Property</sub>

The delegate object for the capture file output.

<sub>macOS</sub>

```swift
unowned(unsafe) var delegate: (any AVCaptureFileOutputDelegate)? { get set }
```

## Discussion

The delegate is an object conforming to the [AVCaptureFileOutputDelegate](../avcapturefileoutputdelegate.md) protocol that will be able to monitor and control recording along exact sample boundaries.

## See Also

### Setting file output properties

- [maxRecordedDuration](maxrecordedduration.md) — The longest duration allowed for the recording.
- [maxRecordedFileSize](maxrecordedfilesize.md) — The maximum size, in bytes, of the data that should be recorded by the receiver.
- [minFreeDiskSpaceLimit](minfreediskspacelimit.md) — The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [outputFileURL](outputfileurl.md) — The URL to which output is directed.
- [recordedDuration](recordedduration.md) — Indicates the duration of the media recorded to the current output file.
- [recordedFileSize](recordedfilesize.md) — Indicates the size, in bytes, of the data recorded to the current output file.
- [recording](isrecording.md) — Indicates whether recording is in progress.
- [recordingPaused](isrecordingpaused.md) — Indicates whether recording to the current output file is paused.
