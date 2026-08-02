---
title: AirPlay Overview
apple_id: TP40011045
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AirPlayGuide/PreparingYourMediaforAirPlay/PreparingYourMediaforAirPlay.html
archived_at: '2026-07-15T05:21:02.011049Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AirPlay Overview](About%20AirPlay.md)


[Next](Opting%20Into%20or%20Out%20of%20AirPlay.md)[Previous](About%20AirPlay.md)

# Preparing Your Media and Server for AirPlay

For your media to play over AirPlay, it needs to be playable on an iOS-based device, such as an iPhone, iPod touch, or iPad. For your server to work with AirPlay, it needs to be configured to send audio and video over HTTP.

When preparing your media for AirPlay, you should do the following:

- Encode your audio using mono or stereo AAC or MP3 compression.
- Encode your video using H.264 compression.

  Use Baseline Profile 3.0 if your video is intended for playback on iPhone 3G or earlier.

  For playback on iPhone 4 and later, iPod touch, iPad, and Apple TV, use Baseline Profile 3.1.

  Use Main Profile 3.1 if your video is intended for playback exclusively on iPad, OS X, and Apple TV.

- Use a QuickTime reference movie or an alternate-stream playlist to provide an alternative version of audio/video content with an AC3 surround-sound track and high-definition video to be used when your media is being played through a home theater system.

If you are using HTTP Live Streaming to provide video at multiple bandwidths, see _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_ for recommended bit rates and encoder settings.

You can package your media in `.mp3`, `.aac`, `.m4a`, `.m4v`, `.mp4,` and `.mov` files. Alternatively, you can pass your media directly to the HTTP Live Streaming media segmenter as an MPEG-2 transport stream containing AAC-compressed audio and H.264-compressed video (normally the case for live broadcast).

You can also create `.m3u8` playlists, but these are typically generated automatically by the HTTP Live Streaming server software, which also generates `.ts` files from the media.

The AirPlay-enabled sound system that is playing your audio media might be able to play AC3 surround-sound audio. You can provide an alternate stream playlist that has an AC3 selection to give your app richer sound when the output device supports it. Similarly, the AirPlay output device might be able to display high-definition video; provide a 1280 x 720 video stream alternate to give the user the richest display possible.

Alternate stream playlists are a feature of HTTP Live Streaming. Alternate streams are normally specified by bit rate, but you can also specify streams by screen resolution and required codecs, so that the AC3 audio and high-definition video streams are chosen only when the output device supports them.

You can specify the ability to play AC3 audio as a requirement for a stream alternate by setting the `CODECS` parameter in your master playlist. The string for the AC3 audio codec is `"ac-3"`. Similarly, you can use the `RESOLUTION` parameter to set the minimum video resolution required for a video stream.

As an example, the following variant playlist specifies a low bandwidth stream, a high bandwidth stream, and an AirPlay stream that requires a 1280 x 720 display, AC3 audio capability, and a 1.5 Mbit/s Internet connection.

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=150000
http://example.com/low/index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=640000
http://example.com/high/index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1500000, RESOLUTION=1280x720,CODECS="avc1.42e01e,ac-3"
http://example.com/airplay/index.m3u8
```

For more information on alternate stream playlists, see _[HTTP Live Streaming Overview](../../Networking%20Internet/HTTP%20Live%20Streaming%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzs)_.

Your server needs to be configured for sending audio and video over HTTP. The most important step in configuring your server is to associate the correct MIME type for each supported file extension. Table 1-1 summarizes the MIME types and file extensions.

__Table 1-1__  File extensions and MIME types

| __File extension__ | __MIME type__ |
| `.m3u8` | `application/x-mpegURL` or  `application/vnd.apple.mpegURL` |
| `.ts` | `video/MP2T` |
| `.mov` | `video/quicktime` |
| `.mp3` | `audio/MPEG3` |
| `.aac` | `audio/aac` |
| `.m4a` | `audio/mpeg4` |
| `.m4v`, `.mp4` | `video/mpeg4` |

[Next](Opting%20Into%20or%20Out%20of%20AirPlay.md)[Previous](About%20AirPlay.md)

