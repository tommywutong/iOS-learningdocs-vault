---
title: AVFoundation updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/avfoundation
source_url: 'https://developer.apple.com/documentation/updates/avfoundation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/avfoundation.json'
content_hash: 'sha256:8826afd4ce3b9bad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# AVFoundation updates

<sub>Article</sub>

Learn about important changes to AVFoundation.

## Overview

Browse notable changes in [AVFoundation](../avfoundation.md).

## June 2024

### Assets

- Preserve HDR data when generating images with `AVAssetImageGenerator` by setting the value of its [dynamicRangePolicy](../avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.property.md) property to match the source video.
- Export media asynchronously using the [export(to:as:isolation:)](<../avfoundation/avassetexportsession/export(to_as_isolation_).md>) method of [AVAssetExportSession](../avfoundation/avassetexportsession.md). You can monitor the progress of an export by calling the [states(updateInterval:)](<../avfoundation/avassetexportsession/states(updateinterval_).md>) method and awaiting its results.
- Determine whether an [AVURLAsset](../avfoundation/avurlasset.md) decodes its data using a Media Extension by inspecting its [mediaExtensionProperties](../avfoundation/avurlasset/mediaextensionproperties.md) property.

### Camera

- Show your camera app on the Lock Screen by adopting the  [LockedCameraCapture](../lockedcameracapture.md) framework.
- Capture photos in constant color by configuring a photo output’s [isConstantColorEnabled](../avfoundation/avcapturephotooutput/isconstantcolorenabled.md) property.
- Continue background audio playback while performing audio and video capture by enabling a capture session’s [configuresApplicationAudioSessionToMixWithOthers](../avfoundation/avcapturesession/configuresapplicationaudiosessiontomixwithothers.md) property.
- Pause and resume video recording in iOS when using [AVCaptureFileOutput](../avfoundation/avcapturefileoutput.md).
- Support enhanced video stabilization using [AVCaptureVideoStabilizationMode.cinematicExtendedEnhanced](../avfoundation/avcapturevideostabilizationmode/cinematicextendedenhanced.md).
- Configure a capture device to automatically adjust its frame rate based on lighting conditions by enabling its [isAutoVideoFrameRateEnabled](../avfoundation/avcapturedevice/isautovideoframerateenabled.md) property.
- Configure a capture device to replace background content in macOS by enabling its [isBackgroundReplacementEnabled](../avfoundation/avcapturedevice/isbackgroundreplacementenabled.md) property.

### Playback

- Build playback apps using the latest Swift Concurrency features due to enhanced [Sendable](../swift/sendable.md) adoption throughout the playback APIs.
- Capture performance and playback metrics using [AVMetrics](../avfoundation/avmetrics.md).
- Receive rendered captions for the currently playing media using [AVPlayerItemRenderedLegibleOutput](../avfoundation/avplayeritemrenderedlegibleoutput.md).
- Simplify handling of interstitial content by using [AVPlayerItemIntegratedTimeline](../avfoundation/avplayeritemintegratedtimeline.md).
- Send Common Media Client Data (CMCD) as HTTP headers by enabling the new [sendsCommonMediaClientDataAsHTTPHeaders](../avfoundation/avassetresourceloader/sendscommonmediaclientdataashttpheaders.md) property on [AVAssetResourceLoader](../avfoundation/avassetresourceloader.md).

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [Background Tasks updates](backgroundtasks.md) — Learn about important changes in Background Tasks.
