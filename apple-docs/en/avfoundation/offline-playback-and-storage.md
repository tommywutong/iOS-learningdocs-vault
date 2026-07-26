---
title: Offline playback and storage
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/offline-playback-and-storage
source_url: 'https://developer.apple.com/documentation/avfoundation/offline-playback-and-storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/offline-playback-and-storage.json'
content_hash: 'sha256:2371774ebc38d4e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Offline playback and storage

<sub>API Collection</sub>

Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.

## Topics

### Asset downloading

- [Using AVFoundation to play and persist HTTP live streams](using-avfoundation-to-play-and-persist-http-live-streams.md) — Play HTTP Live Streams and persist streams on disk for offline playback using AVFoundation.
- [AVAssetDownloadURLSession](avassetdownloadurlsession.md) — A URL session that creates and manages asset download tasks.
- [AVAssetDownloadTask](avassetdownloadtask.md) — A URL session task that downloads a remote asset to the device for offline playback.
- [AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md) — A task that downloads multiple media selections for an asset. _(deprecated)_

### Offline storage management

- [AVAssetDownloadStorageManager](avassetdownloadstoragemanager.md) — An object that manages policies to automatically purge downloaded assets.
- [AVAssetDownloadStorageManagementPolicy](avassetdownloadstoragemanagementpolicy.md) — An object that defines a policy to automatically manage the storage of downloaded assets.
- [AVMutableAssetDownloadStorageManagementPolicy](avmutableassetdownloadstoragemanagementpolicy.md) — A mutable object that you use to create a new storage management policy.

### Cache monitoring

- [AVAssetCache](avassetcache.md) — An object that you use to inspect locally cached media data.

## See Also

### Playback

- [Media playback](media-playback.md) — Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- [Streaming and AirPlay](streaming-and-airplay.md) — Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.
- [Sample buffer playback](sample-buffer-playback.md) — Create custom controllers to play and synchronize the timing of sample buffer streams.
