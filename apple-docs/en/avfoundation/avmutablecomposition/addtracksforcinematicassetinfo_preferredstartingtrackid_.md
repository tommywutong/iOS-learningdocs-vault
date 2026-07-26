---
title: 'addTracksForCinematicAssetInfo:preferredStartingTrackID:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/addtracksforcinematicassetinfo:preferredstartingtrackid:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/addtracksforcinematicassetinfo:preferredstartingtrackid:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/addtracksforcinematicassetinfo%3Apreferredstartingtrackid%3A.json'
content_hash: 'sha256:ff18606fb31cd04b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# addTracksForCinematicAssetInfo:preferredStartingTrackID:

<sub>Instance Method</sub>

Adds a group of empty tracks associated with a cinematic asset to a mutable composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```objc
- (CNCompositionInfo *) addTracksForCinematicAssetInfo:(CNAssetInfo *) assetInfo preferredStartingTrackID:(CMPersistentTrackID) preferredStartingTrackID;
```

## Return Value

Information about the composition tracks added to the mutable composition. Be sure to call insertTimeRange on the result to specify at least one time range of cinematic asset you’d like in the composition.
