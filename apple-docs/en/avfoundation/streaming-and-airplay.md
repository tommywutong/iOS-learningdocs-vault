---
title: Streaming and AirPlay
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/streaming-and-airplay
source_url: 'https://developer.apple.com/documentation/avfoundation/streaming-and-airplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/streaming-and-airplay.json'
content_hash: 'sha256:6b95a419b0f03ffb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Streaming and AirPlay

<sub>API Collection</sub>

Stream content wirelessly to other devices using AirPlay, and handle requests involving FairPlay-protected assets.

## Topics

### Essentials

- [Supporting AirPlay in your app](supporting-airplay-in-your-app.md) — Set up your app to use AirPlay to send content wirelessly.

### Route selection

- [AVRouteDetector](avroutedetector.md) — An object that detects available media playback routes.

### Buffered playback

- [Implementing simple enhanced buffering for your content](implementing-simple-enhanced-buffering-for-your-content.md) — Configure your app for simple enhanced buffering to stream content faster to AirPlay-enabled devices and supported CarPlay vehicles.
- [Implementing flexible enhanced buffering for your content](implementing-flexible-enhanced-buffering-for-your-content.md) — Configure your app for flexible enhanced buffering to stream content faster to AirPlay-enabled devices and supported CarPlay vehicles.
- [Integrating AirPlay for long-form video apps](integrating-airplay-for-long-form-video-apps.md) — Integrate AirPlay features and implement a dedicated external playback experience by preparing the routing system for long-form video playback.

### Resource loading

- [AVAssetResourceLoader](avassetresourceloader.md) — An object that mediates resource requests from a URL asset.
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — An object that encapsulates information about a resource request from a resource loader object.
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — An object that contains information about the originator of a resource-loading request.
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — An object for requesting data from a resource that an asset resource-loading request references.
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — A query for retrieving essential information about a resource that an asset resource-loading request references.

### FairPlay streaming

- [AVContentKeySession](avcontentkeysession.md) — An object that creates and tracks decryption keys for media data.
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKey](avcontentkey.md) — An object that represents the content key decryptor.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVContentKeyRequest](avcontentkeyrequest.md) — An object that encapsulates information about a content decryption key request issued from a content key session object.
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [AVContentKeyResponse](avcontentkeyresponse.md) — An object that encapsulates information about a response to a content decryption key request.
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — Constants that specify whether sufficient protection exists to display the content.
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — Attaches a content key to a sample buffer for the purpose of content decryption. _(deprecated)_

## See Also

### Playback

- [Media playback](media-playback.md) — Manage the playback of media assets and interstitial content, independent of how you present that content in your interface.
- [Offline playback and storage](offline-playback-and-storage.md) — Download streamed content to disk to allow offline playback, and define policies to automatically remove downloaded assets.
- [Sample buffer playback](sample-buffer-playback.md) — Create custom controllers to play and synchronize the timing of sample buffer streams.
