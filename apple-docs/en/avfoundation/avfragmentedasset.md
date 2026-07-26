---
title: AVFragmentedAsset
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avfragmentedasset
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedasset.json'
content_hash: 'sha256:241673bb7eeb2b77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVFragmentedAsset

<sub>Class</sub>

An asset with a duration that the system can extend without modifying its existing media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVFragmentedAsset
```

## Overview

By using an `mvex` box in their `moov` box, QuickTime movie files and MPEG-4 files can indicate that they accommodate additional fragments. To determine whether a fragmented asset can monitor the addition of fragments, check the value of its [canContainFragments](avasset/cancontainfragments.md) property.

Associate a fragmented asset with an instance of [AVFragmentedAssetMinder](avfragmentedassetminder.md) to know when the system appends new fragments. When it has an associated asset minder, [AVFragmentedAssetTrack](avfragmentedassettrack.md) posts [AVAssetDurationDidChangeNotification](avassetdurationdidchangenotification.md) notifications whenever it detects new fragments. It may also post [AVAssetContainsFragmentsDidChangeNotification](avassetcontainsfragmentsdidchangenotification.md) and [AVAssetWasDefragmentedNotification](avassetwasdefragmentednotification.md), as the documentation of those notifications explains.

## Relationships

- **Inherits From**: [AVURLAsset](avurlasset.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [AVContentKeyRecipient](avcontentkeyrecipient.md), [AVFragmentMinding](avfragmentminding.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSItemProviderReading](../foundation/nsitemproviderreading.md), [NSItemProviderWriting](../foundation/nsitemproviderwriting.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Loading tracks

- [tracks](avpartialasyncproperty/tracks-9z3j9.md) — The tracks an asset contains.
- [- loadTrackWithTrackID:completionHandler:](<avfragmentedasset/loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<avfragmentedasset/loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<avfragmentedasset/loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.

### Accessing tracks

- [tracks](avfragmentedasset/tracks.md) — The tracks an asset contains. _(deprecated)_
- [- trackWithTrackID:](<avfragmentedasset/track(withtrackid_).md>) — Returns a track that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaType:](<avfragmentedasset/tracks(withmediatype_).md>) — Returns tracks that present media of a specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<avfragmentedasset/tracks(withmediacharacteristic_).md>) — Returns tracks that present media of a specified characteristic. _(deprecated)_

### Initializers

- [init(URL:options:)](<avfragmentedasset/init(url_options_).md>)

## See Also

### Fragmented assets

- [AVFragmentedAssetTrack](avfragmentedassettrack.md) — An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [AVFragmentedAssetMinder](avfragmentedassetminder.md) — An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [AVFragmentMinding](avfragmentminding.md) — A protocol that defines whether an asset supports fragment minding.
