---
title: Third-party casting support
framework: AVKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/third-party-casting-support
source_url: 'https://developer.apple.com/documentation/avkit/third-party-casting-support'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/third-party-casting-support.json'
content_hash: 'sha256:452cd8c793528810'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# Third-party casting support

<sub>API Collection</sub>

Provide custom playback controls for third-party casting services and other media sources.

## Overview

Use the [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md) protocol suite to build custom transport controls that work with third-party casting services. The [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md) composite protocol combines playback, timeline, media selection, volume, and metadata capabilities into a single interface.

## Topics

### Playback

- [AVPlaybackUserInterfacePlaybackControllable](avplaybackuserinterfaceplaybackcontrollable-9he54.md) — Provides playback control and state management for media content. _(beta)_
- [AVPlaybackUserInterfacePlaybackState](avplaybackuserinterfaceplaybackstate.md) — Describes possible transport states of the playback source. _(beta)_
- [AVPlaybackUserInterfaceSeekCapabilities](avplaybackuserinterfaceseekcapabilities.md) — Describes navigation capabilities of the media source. _(beta)_

### Timeline

- [AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md) — Provides time control and navigation capabilities for media content. _(beta)_
- [AVPlaybackUserInterfacePlaybackPosition](avplaybackuserinterfaceplaybackposition.md) — A snapshot comprising a playback position recorded at a known host time and the rate of position advancement. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimelinesegment.md) — Represents a contiguous segment of timeline content with specific playback characteristics. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentType](avplaybackuserinterfacetimelinesegmenttype.md) — Describes the type of content within a timeline segment. _(beta)_

### Media selection

- [AVPlaybackUserInterfaceMediaSelectionControllable](avplaybackuserinterfacemediaselectioncontrollable-8ee5z.md) — Provides audio and subtitle selection capabilities for media content. _(beta)_
- [AVPlaybackUserInterfaceMediaSelectionOption](avplaybackuserinterfacemediaselectionoption.md) — Represents a media selection option for audio tracks or subtitle tracks. _(beta)_

### Volume

- [AVPlaybackUserInterfaceVolumeControllable](avplaybackuserinterfacevolumecontrollable-4vgi1.md) — Provides volume and audio muting control for media content. _(beta)_

### Metadata

- [AVPlaybackUserInterfaceMetadataProviding](avplaybackuserinterfacemetadataproviding-814y4.md) — Provides metadata information about media content including title, artwork, and content type. _(beta)_
- [AVPlaybackUserInterfaceContentMetadata](avplaybackuserinterfacecontentmetadata-swift.struct.md) — A Swift-friendly structure representing media metadata. _(beta)_
- [AVPlaybackUserInterfaceContentArtwork](avplaybackuserinterfacecontentartwork.md) — Base class representing artwork or cover art for media content. _(beta)_
- [AVPlaybackUserInterfaceContentURLArtwork](avplaybackuserinterfacecontenturlartwork.md) — An artwork subclass that references artwork via a URL and content type. _(beta)_

### Complete interface

- [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md) — A comprehensive protocol that provides complete media control and information for playback, timeline navigation, audio/subtitle selection, volume control, and metadata access. _(beta)_

## See Also

### iOS playback and capture

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md) — Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [AVPlayerViewController](avplayerviewcontroller.md) — A view controller that displays content from a player and presents a native user interface to control playback.
- [AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md) — A protocol that defines the methods to implement to respond to player view controller events.
- [AVCaptureEventInteraction](avcaptureeventinteraction.md) — An object that registers handlers to respond to capture events from system hardware buttons.
- [AVCaptureEvent](avcaptureevent.md) — An object that describes a user interaction with a system hardware button.
- [AVCaptureEventSound](avcaptureeventsound.md) — A sound object for a capture event.
- [AVInputPickerInteraction](avinputpickerinteraction.md) — Use `AVInputPickerInteraction` to present an input picker.
