---
title: unusedTrackID()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie/unusedtrackid()
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie/unusedtrackid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie/unusedtrackid%28%29.json'
content_hash: 'sha256:fb3478673b5aba32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovie](../avmutablemovie.md)

# unusedTrackID()

<sub>Instance Method</sub>

Returns an identifier that no other tracks in the asset use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func unusedTrackID() -> CMPersistentTrackID
```

## Return Value

An unused [CMPersistentTrackID](../../coremedia/cmpersistenttrackid.md) value.

## See Also

### Accessing tracks

- [tracks](tracks.md) — The tracks that a movie contains.
- [- trackWithTrackID:](<track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier.
- [- tracksWithMediaType:](<tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type.
- [- tracksWithMediaCharacteristic:](<tracks(withmediacharacteristic_).md>) — Retrieve tracks in the movie that present media of the specified characteristic.
