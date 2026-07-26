---
title: AVMutableComposition
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablecomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition.json'
content_hash: 'sha256:8d67f4d648250ad8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableComposition

<sub>Class</sub>

An object that you use to create a new composition from existing assets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMutableComposition
```

## Overview

Use this object to add and remove composition tracks, and add, remove, and scale their time ranges. You can make an immutable snapshot of a mutable composition for playback and inspection as follows:

```swift
// Use a mutable composition object you create.
let mutableComposition = AVMutableComposition()
        
guard let composition = mutableComposition.copy() as? AVComposition else { return }
        
// Create a player item to inspect and play the composition.
let playerItem = AVPlayerItem(asset: composition)
```

## Relationships

- **Inherits From**: [AVComposition](avcomposition.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a composition

- [+ compositionWithURLAssetInitializationOptions:](<avmutablecomposition/init(urlassetinitializationoptions_)-rh4y.md>) — Creates a mutable composition that uses the specified initialization options.

### Loading tracks

- [tracks](avpartialasyncproperty/tracks-92p4a.md) — The tracks that a composition contains.
- [- loadTrackWithTrackID:completionHandler:](<avmutablecomposition/loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<avmutablecomposition/loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<avmutablecomposition/loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.

### Accessing tracks

- [tracks](avmutablecomposition/tracks.md) — The tracks that a composition contains.
- [- trackWithTrackID:](<avmutablecomposition/track(withtrackid_).md>) — Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](<avmutablecomposition/tracks(withmediatype_).md>) — Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](<avmutablecomposition/tracks(withmediacharacteristic_).md>) — Returns tracks that contain media of a specified characteristic.

### Managing composition tracks

- [- mutableTrackCompatibleWithTrack:](<avmutablecomposition/mutabletrack(compatiblewith_).md>) — Returns a composition track into which you can insert any time range of the specified asset track.
- [- addMutableTrackWithMediaType:preferredTrackID:](<avmutablecomposition/addmutabletrack(withmediatype_preferredtrackid_).md>) — Adds an empty track to a composition.
- [- removeTrack:](<avmutablecomposition/removetrack(__).md>) — Removes a specified track from the composition.

### Managing Cinematic tracks

- [addTracks(for:preferredStartingTrackID:)](<avmutablecomposition/addtracks(for_preferredstartingtrackid_).md>)

### Managing time ranges

- [- removeTimeRange:](<avmutablecomposition/removetimerange(__).md>) — Removes a specified time range from all tracks of the composition.
- [- scaleTimeRange:toDuration:](<avmutablecomposition/scaletimerange(__toduration_).md>) — Changes the duration of all tracks in a given time range.
- [- insertEmptyTimeRange:](<avmutablecomposition/insertemptytimerange(__).md>) — Adds or extends an empty time range within all tracks of the composition.
- [- insertTimeRange:ofAsset:atTime:completionHandler:](<avmutablecomposition/inserttimerange(__of_at_completionhandler_).md>) — Inserts all tracks of an asset for a time range into a composition. _(deprecated)_
- [- insertTimeRange:ofAsset:atTime:error:](<avmutablecomposition/inserttimerange(__of_at_).md>) — Inserts all the tracks within a given time range of a specified asset into the composition. _(deprecated)_

### Configuring video size

- [naturalSize](avmutablecomposition/naturalsize.md) — The encoded or authored size of the visual portion of the asset.

### Instance methods

- [insertTimeRange(_:of:at:isolation:)](<avmutablecomposition/inserttimerange(__of_at_isolation_).md>)

### Initializers

- [init(URLAssetInitializationOptions:)](<avmutablecomposition/init(urlassetinitializationoptions_)-6codz.md>)

## See Also

### Mutable compositions

- [AVMutableCompositionTrack](avmutablecompositiontrack.md) — A mutable track in a composition that you use to insert, remove, and scale track segments without affecting their low-level representation.
