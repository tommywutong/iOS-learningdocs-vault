---
title: 'addMutableTrack(withMediaType:preferredTrackID:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/addmutabletrack(withmediatype:preferredtrackid:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/addmutabletrack(withmediatype:preferredtrackid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/addmutabletrack%28withmediatype%3Apreferredtrackid%3A%29.json'
content_hash: 'sha256:488beafd51fdc293'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# addMutableTrack(withMediaType:preferredTrackID:)

<sub>Instance Method</sub>

Adds an empty track to a composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addMutableTrack(withMediaType mediaType: AVMediaType, preferredTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?
```

## Parameters

- `mediaType` — The media type of the new track.

- `preferredTrackID` — The preferred track ID for the new track. The system generates a unique ID if the value you specify isn’t available. If you don’t need to specify a preferred track ID, pass [kCMPersistentTrackID_Invalid](../../coremedia/kcmpersistenttrackid_invalid.md), and the system generates an appropriate identifier.

## Return Value

A new mutable composition track.

## See Also

### Managing composition tracks

- [- mutableTrackCompatibleWithTrack:](<mutabletrack(compatiblewith_).md>) — Returns a composition track into which you can insert any time range of the specified asset track.
- [- removeTrack:](<removetrack(__).md>) — Removes a specified track from the composition.
