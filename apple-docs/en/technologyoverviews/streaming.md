---
title: Media streaming
framework: Technology Overviews
symbol_kind: article
role: article
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/technologyoverviews/streaming
source_url: 'https://developer.apple.com/documentation/technologyoverviews/streaming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/technologyoverviews/streaming.json'
content_hash: 'sha256:3138e98a55bf30b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Technology Overviews](../technologyoverviews.md) · [Audio and video](audio-and-video.md)

# Media streaming

Stream audio and video content to a device, or to AirPlay-enabled hardware.

Streaming technologies allow people to enjoy their favorite media wherever they are. Whether streaming live events, watching on-demand shows, or sharing content wirelessly between devices, these technologies ensure playback is adaptive, secure, and responsive. With built-in privacy protections and broad compatibility across TVs, speakers, and mobile devices, Apple’s streaming technologies deliver engaging experiences that reach users in more places than ever.

## Stream media to AirPlay-enabled devices

[AirPlay](https://www.apple.com/airplay/) enables people stream audio and video from their Apple devices to Apple TV, AirPlay-enabled [speakers](https://www.apple.com/home-app/accessories/#section-speakers) and [receivers](https://www.apple.com/home-app/accessories/#section-receivers), and [smart TVs](https://www.apple.com/home-app/accessories/#section-tvs), expanding where and how they enjoy their content. Designed with privacy in mind, AirPlay ensures that shared content stays personal and secure, giving people the freedom to enjoy their media anywhere.

Adopting AirPlay in your playback app is simple and requires only [minimal configuration](../avfoundation/configuring-your-app-for-media-playback.md). [AVFoundation](../avfoundation.md) is the framework you use to play audiovisual media and it provides built-in support for AirPlay. You use AVFoundation together with [AVKit](../avkit.md) to provide the interface for people to select which AirPlay-enabled devices, like Apple TV or HomePod speaker, to send their media. By enabling seamless playback on external devices and offering system-standard AirPlay controls, you can deliver a compelling, multi-device experience that aligns with people’s expectations for media across the Apple ecosystem.

## Deliver media with HTTP Live Streaming

[HTTP Live Streaming](https://developer.apple.com/streaming/) (HLS) is Apple’s adaptive streaming technology designed to deliver high-quality audio and video content over standard HTTP connections. Whether you’re broadcasting a live sports event or delivering a on-demand content, HLS enables scalable, reliable playback across all Apple platforms. It dynamically adjusts the stream quality based on the user’s network conditions, which helps to provide smooth playback with minimal buffering and reduced interruptions wherever they are.

It supports segmented delivery, encryption, digital rights management through [FairPlay Streaming](https://developer.apple.com/streaming/fps/), closed captions, multiple audio tracks, and alternative media variants. Apple’s media frameworks, including [AVFoundation](../avfoundation.md) and [AVKit](../avkit.md), provide first-class support for HLS, making it simple to use in your apps. You can also leverage [Low-Latency HLS](../http-live-streaming/enabling-low-latency-http-live-streaming-hls.md) to deliver near real-time streaming experiences for time-sensitive content like gaming, auctions, and live events.

By adopting HTTP Live Streaming, you can ensure your content is compatible with a wide range of devices while meeting people’s expectations for quality, security, and responsiveness. It’s the foundation of Apple’s media streaming ecosystem and the preferred choice for delivering adaptive, standards-compliant media at scale.
