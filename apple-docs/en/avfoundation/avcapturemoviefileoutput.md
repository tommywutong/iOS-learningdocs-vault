---
title: AVCaptureMovieFileOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput.json'
content_hash: 'sha256:c2e91872dc99faa8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureMovieFileOutput

<sub>Class</sub>

A capture output that records video and audio to a QuickTime movie file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureMovieFileOutput
```

## Overview

A movie file output provides a complete file recording interface for writing media data to QuickTime movie files. It includes the ability to configure QuickTime-specific options, including writing metadata collections to each file, specify media encoding options for each track, and specify the interval at which it writes movie fragments.

## Relationships

- **Inherits From**: [AVCaptureFileOutput](avcapturefileoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a movie file output

- [- init](<avcapturemoviefileoutput/init().md>) — Creates a new of movie file output.

### Configuring movies

- [movieFragmentInterval](avcapturemoviefileoutput/moviefragmentinterval.md) — The number of seconds of output that are written per fragment.
- [metadata](avcapturemoviefileoutput/metadata.md) — The metadata for the output file.

### Managing output settings

- [- supportedOutputSettingsKeysForConnection:](<avcapturemoviefileoutput/supportedoutputsettingskeys(for_).md>) — Returns a list of supported keys to use in the output settings dictionary.
- [- outputSettingsForConnection:](<avcapturemoviefileoutput/outputsettings(for_).md>) — Returns the settings the output uses to encode media from the specified connection.
- [- setOutputSettings:forConnection:](<avcapturemoviefileoutput/setoutputsettings(__for_).md>) — Sets the options the output uses to encode media from the given connection while recording.
- [availableVideoCodecTypes](avcapturemoviefileoutput/availablevideocodectypes.md) — The video codecs types the output supports for recording movie files.

### Enabling spatial capture

- [spatialVideoCaptureSupported](avcapturemoviefileoutput/isspatialvideocapturesupported.md) — A Boolean value that indicates whether a movie file output supports capturing spatial videos.
- [spatialVideoCaptureEnabled](avcapturemoviefileoutput/isspatialvideocaptureenabled.md) — A Boolean value that indicates whether a movie file output captures spatial videos.

### Setting orientation

- [- recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection:](<avcapturemoviefileoutput/recordsvideoorientationandmirroringchangesasmetadatatrack(for_).md>) — A Boolean value that indicates whether the movie file output records video orientation and mirroring information as a metadata track.
- [- setRecordsVideoOrientationAndMirroringChanges:asMetadataTrackForConnection:](<avcapturemoviefileoutput/setrecordsvideoorientationandmirroringchangesasmetadatatrack(__for_).md>) — Sets whether the movie file output creates a timed metadata track to capture changes to the connection’s video orientation and mirroring.

### Restricting camera switching

- [primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled](avcapturemoviefileoutput/isprimaryconstituentdeviceswitchingbehaviorforrecordingenabled.md) — A Boolean value that indicates whether to restrict constituent device switching behavior during recording.
- [- setPrimaryConstituentDeviceSwitchingBehaviorForRecording:restrictedSwitchingBehaviorConditions:](<avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(__restrictedswitchingbehaviorconditions_).md>) — Sets the camera switching behavior to use during recording.
- [primaryConstituentDeviceSwitchingBehaviorForRecording](avcapturemoviefileoutput/primaryconstituentdeviceswitchingbehaviorforrecording.md) — The camera switching behavior to use for recording.
- [primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording](avcapturemoviefileoutput/primaryconstituentdevicerestrictedswitchingbehaviorconditionsforrecording.md) — The conditions during which camera switching may occur while recording.

### Instance Properties

- [proVideoStorageSupported](avcapturemoviefileoutput/isprovideostoragesupported.md) — Whether this movie file output supports writing to Pro Video Storage in its current configuration. _(beta)_
- [usesProVideoStorage](avcapturemoviefileoutput/usesprovideostorage.md) — Whether this movie file output is configured to write to Pro Video Storage. _(beta)_

## See Also

### File capture

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md) — Change the default format for capturing movie files.
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md) — A capture output that records audio and saves the recorded audio to a file.
- [AVCaptureFileOutput](avcapturefileoutput.md) — The abstract superclass for capture outputs that can record captured data to a file.
- [AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md) — Methods for monitoring or controlling the output of a media file capture.
- [AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md) — Methods for responding to events that occur while recording captured media to a file.
