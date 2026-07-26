---
title: 'setRecordsVideoOrientationAndMirroringChangesAsMetadataTrack(_:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemoviefileoutput/setrecordsvideoorientationandmirroringchangesasmetadatatrack(_:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/setrecordsvideoorientationandmirroringchangesasmetadatatrack(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/setrecordsvideoorientationandmirroringchangesasmetadatatrack%28_%3Afor%3A%29.json'
content_hash: 'sha256:77b1e8b352d561a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# setRecordsVideoOrientationAndMirroringChangesAsMetadataTrack(_:for:)

<sub>Instance Method</sub>

Sets whether the movie file output creates a timed metadata track to capture changes to the connection’s video orientation and mirroring.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setRecordsVideoOrientationAndMirroringChangesAsMetadataTrack(_ doRecordChanges: Bool, for connection: AVCaptureConnection)
```

## Parameters

- `doRecordChanges` — A Boolean value that indicates whether to capture orientation and mirroring information. The system observes this value only at the start of recording. Setting a different value has no effect until you start a new recording.

- `connection` — A connection that delivers video media to the movie file output. This method throws an invalid argument exception if the value isn’t a video connection or if the connection doesn’t terminate at the movie file output.

## See Also

### Setting orientation

- [- recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection:](<recordsvideoorientationandmirroringchangesasmetadatatrack(for_).md>) — A Boolean value that indicates whether the movie file output records video orientation and mirroring information as a metadata track.
