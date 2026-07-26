---
title: 'recordsVideoOrientationAndMirroringChangesAsMetadataTrack(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemoviefileoutput/recordsvideoorientationandmirroringchangesasmetadatatrack(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/recordsvideoorientationandmirroringchangesasmetadatatrack(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/recordsvideoorientationandmirroringchangesasmetadatatrack%28for%3A%29.json'
content_hash: 'sha256:8d0088a21f20fef5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# recordsVideoOrientationAndMirroringChangesAsMetadataTrack(for:)

<sub>Instance Method</sub>

A Boolean value that indicates whether the movie file output records video orientation and mirroring information as a metadata track.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func recordsVideoOrientationAndMirroringChangesAsMetadataTrack(for connection: AVCaptureConnection) -> Bool
```

## Parameters

- `connection` — A connection delivering video media to the movie file output. This method throws an invalid argument exception if the value isn’t a video connection or if the connection doesn’t terminate at the movie file output.

## See Also

### Setting orientation

- [- setRecordsVideoOrientationAndMirroringChanges:asMetadataTrackForConnection:](<setrecordsvideoorientationandmirroringchangesasmetadatatrack(__for_).md>) — Sets whether the movie file output creates a timed metadata track to capture changes to the connection’s video orientation and mirroring.
