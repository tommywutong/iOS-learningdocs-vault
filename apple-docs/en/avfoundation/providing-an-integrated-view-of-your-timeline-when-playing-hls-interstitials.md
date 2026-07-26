---
title: Providing an integrated view of your timeline when playing HLS interstitials
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials
source_url: 'https://developer.apple.com/documentation/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials.json'
content_hash: 'sha256:d15090eacec402ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media playback](media-playback.md)

# Providing an integrated view of your timeline when playing HLS interstitials

<sub>Sample Code</sub>

Go beyond simple ad insertion with point and fill occupancy HLS interstitials.

## Overview

> [!note] Note
> This sample code project is associated with WWDC24 session 10114: [Enhance ad experiences with HLS Interstitials](https://developer.apple.com/wwdc24/10114/)

### Configure the sample code project

Using the examples under the Live stream examples section of the app requires running a local test stream. The project includes a Go script that starts a local web server that hosts this example stream. You must have [Go](https://go.dev/doc/install) installed to run this script.

Open a Terminal window, change to the `/Source/LiveStreamExample/` directory, and run the following command to start the stream:

```
go run liveStreamGenerator.go --http :8443 map.mp4 segment0.m4s segment1.m4s segment2.m4s
```

When the stream starts, copy its URL, which is in the following format: `http://<hostname>:8443/media.m3u8`. In the Xcode project, open the `Menu.json` file, and replace the placeholder URLs (http://livestreamserver.url:8443/media.m3u8) with your local stream URL. Relaunch the app to view the live stream examples.

## See Also

### Interstitials

- [AVPlayerInterstitialEvent](avplayerinterstitialevent.md) — An object that provides instructions for how a player presents interstitial content.
- [AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md) — An object that schedules interstitial events for items played by the primary player.
- [AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md) — An object that monitors the scheduling and progress of interstitial events.
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](avplayerinterstitialeventmonitorschedulerequesterrorkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSError. Absent if the request succeeded
- [AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey](avplayerinterstitialeventmonitorschedulerequestidentifierkey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSString.
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](avplayerinterstitialeventmonitorschedulerequestresponsekey.md) — userInfo dictionary key for the AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification. Value is NSData. Absent if the request failed.
- [AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md) — An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.

## Download

- [ProvidingAnIntegratedViewOfYourTimelineWhenPlayingHLSInterstitials.zip](https://docs-assets.developer.apple.com/published/f879c5e639a6/ProvidingAnIntegratedViewOfYourTimelineWhenPlayingHLSInterstitials.zip)
