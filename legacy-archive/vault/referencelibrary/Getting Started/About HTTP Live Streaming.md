---
title: About HTTP Live Streaming
apple_id: TP40013978
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/AboutHTTPLiveStreaming/about/about.html
archived_at: '2026-07-18T02:39:18.080987Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)


[Next](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/AboutHTTPLiveStreaming/RevisionHistory.html)

# About HTTP Live Streaming

HTTP Live Streaming (HLS) is Apple's technology for streaming live and on-demand audio/video content to iPhone, iPad, iPod touch, Apple TV, and Mac. Central to HLS is the delivery of content using the HTTP protocol—the same protocol that powers the web. HTTP lets you easily deploy media content in streams using commonplace web servers rather than specialized streaming servers. HLS streams behave like regular web traffic. They work with preexisting caching infrastructure, such as Content Delivery Networks (CDNs), and reliably pass through typical firewalls and routers. HLS adapts to variable network conditions, dynamically adjusting playback to match the available speed of wired and wireless connections.

In addition to reliability and ease of deployment, HLS supports important features for the delivery of commercial content: closed captions, fast forward and reverse playback, alternate audio and video, fallback alternatives, timed metadata, ad insertion, and content protection.

This document describes key aspects of HLS including the features mentioned above. The full HTTP Live Streaming specification is available as an IETF Internet-Draft at [http://tools.ietf.org/html/draft-pantos-http-live-streaming](http://tools.ietf.org/html/draft-pantos-http-live-streaming).

In a typical HLS workflow, a video encoder solution that supports HLS receives a live video feed or distribution-ready media file. The encoder creates multiple versions (known as _variants_) of the audio/video at different bit rates, resolutions, and quality levels. The encoder then segments the variants into a series of small files, called _media segments_. At the same time, the encoder creates a _media playlist_ file for each variant containing a list of URLs pointing to the variant’s media segments. The encoder also creates a _master playlist_ file, containing a list of the URLs to variant media playlists, and descriptive tags to control the playback behavior of the stream. While producing playlists and segments, the encoder or automated scripts upload the files to a web server or CDN.

You provide access to the content by embedding a link to the master playlist file in a web page, or by creating your own custom application that downloads the master playlist file.

An encoder creates media segments by dividing the event data into short MPEG-2 transport stream files (`.ts`). Typically, the files contain H.264 video or AAC audio with a duration of 5 to 10 seconds each. The encoder lets you set the encoding and duration of the media segments.

The encoder creates the media playlists as text files saved in the M3U format (`.m3u8`). The media playlists contain URLs to the media segments and other information needed for playback. The playlist type—live, event, or video on demand (VOD)—determines how the stream can be navigated.

Live playlists let viewers perform fast forward and reverse playback within a limited time range. The range advances along the program until the end of the live presentation. Event playlists let a viewer rewind to the beginning of the stream even as it continues to stream live. VOD playlists represent a previously completed program that can be fully navigated from beginning to end.

Both the live and event types of programs require updates to the media playlists as newly created media segments become available on the server. The encoder adds new media segment references to the end of the playlist and uploads the updated playlist to the server.

In a live playlist, as shown in Listing 1, references to older media segments can be removed from the media playlist and discarded, providing a sliding window into a continuous stream.

__Listing 1__  A simple live media playlist

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:26
#EXTINF:9.901,
http://media.example.com/wifi/segment26.ts
#EXTINF:9.901,
http://media.example.com/wifi/segment27.ts
#EXTINF:9.501,
http://media.example.com/wifi/segment28.ts
```

An event playlist, shown in Listing 2, has the same format as the live media playlist above, with the exception of an extra line: `#EXT-X-PLAYLIST-TYPE:EVENT`. That designation alerts media player that this playlist will behave differently than a live media playlist. Event playlists maintain the references to older media while gaining new references. This process results in an expanding media playlist. This type of playlist allows the players to navigate freely (backward and forward) from the beginning of the program. Because references to all media segments remain in the playlist when the live event ends, event playlists are easily converted to VOD playlists.

__Listing 2__  A simple event media playlist

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PLAYLIST-TYPE:EVENT
#EXTINF:9.9001,
http://media.example.com/wifi/segment0.ts
#EXTINF:9.9001,
http://media.example.com/wifi/segment1.ts
#EXTINF:9.9001,
http://media.example.com/wifi/segment2.ts
```


A VOD playlist, shown in Listing 3, contains references to all available media segments for the complete presentation, beginning to end. This kind of playlist allows the player to navigate the entire program. A VOD `#EXT-X-ENDLIST` tag marks the end of downloadable media segments.

__Listing 3__  A simple VOD media playlist

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PLAYLIST-TYPE:VOD
#EXTINF:9.9001,
http://media.example.com/wifi/segment0.ts
#EXTINF:9.9001,
http://media.example.com/wifi/segment1.ts
#EXTINF:9.9001,
http://media.example.com/wifi/segment2.ts
#EXT-X-ENDLIST
```


The master playlist provides an address for each individual media playlist in the stream. Figure 1 shows this relationship. The master playlist also provides important details such as bandwidth, resolution, and codec. The player uses that information to decide the most appropriate variant for the device and the currently measured, available bandwidth.

__Figure 1__  Playlist relationships

!

The sample master playlist in Listing 4 shows four variants. The order of the media playlists in the master playlists does not matter, except when you start the stream. The player begins downloading the first variant it can play. If conditions warrant, the player switches to another media playlist midstream.

__Listing 4__  A master playlist file with four available variants

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2855600,CODECS="avc1.4d001f,mp4a.40.2",RESOLUTION=960x540
live/medium.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5605600,CODECS="avc1.640028,mp4a.40.2",RESOLUTION=1280x720
live/high.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1755600,CODECS="avc1.42001f,mp4a.40.2",RESOLUTION=640x360
live/low.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=545600,CODECS="avc1.42001e,mp4a.40.2",RESOLUTION=416x234
live/cellular.m3u8
```

A player downloads a master playlist only once. However, the number of media playlist downloads vary with the playlist type. For live and event broadcasts, the player downloads the media playlist files after each segment duration because the the playlist may update with new segments or lose older segments as the stream progresses. For VOD, players download media playlists only once.

You provide access to your streams by adding a link to the master playlist file in a web page, or by creating your own custom application built with the AV Foundation or Media Player frameworks. See _[AVFoundation Programming Guide](../../documentation/Audio%20Video/AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_ or _[Media Player Framework Reference](https://developer.apple.com/documentation/mediaplayer)_.

The HLS technology lets you stream your content through HTTP and enables automatic switching between streams as network conditions change. Those attributes alone make HLS a great solution for media distribution. Additionally, the technology includes features for usability, availability, advertising, and security. You can build the quality with the following extensible solutions.

HLS supports CEA-608 closed captions embedded in the MPEG-2 transport stream as specified in ATSC A/72. Most encoders automatically include the closed captioning in the media segments as the encoder processes the incoming video. Some encoders also insert closed captioning from a separate closed caption file or segmented QuickTime files that contain closed caption tracks (`cclp`).

HLS also supports multiple subtitles in WebVTT format. For more information on implementation of WebVTT, see [WWDC 2012: What's New in HLS](https://developer.apple.com/videos/wwdc/2012/?include=512#512) and [WebVTT: The Web Video Text Tracks Format specification](http://dev.w3.org/html5/webvtt/).

HLS supports fast forward and reverse playback through the use of an I-frame playlist. The I-frame playlist points to a byte range within already existing media segments. Fast forward and reverse playback do not need special media segments.

For in-depth information on I-frame playlists, watch [WWDC 2012: Effective HLS](https://developer.apple.com/videos/wwdc/2012/?include=502#502).

HLS master playlists offer multiple audio renditions, a valuable trait for localization. For example, your master playlist may include multiple language soundtracks such as French, German, Spanish, and English. The audio tracks contain unmuxed (signals have not been combined) audio segments. The master playlist file controls the playback.

HLS also supports multiple video streams; for example, multiple video angles for a sporting event. Again, the master playlist file controls the playback.

For more information on alternate media renditions, watch [WWDC 2012: Effective HLS](https://developer.apple.com/videos/wwdc/2012/?include=502#502).

Not only do alternate media playlists in your master playlist operate as bandwidth or device alternatives, the alternates also serve as failure fallbacks. If the player cannot reload the media playlist file—due to issues such as 404 errors, server crashing, or a content distributor node problem—the player attempts to switch to another compatible media playlist provided on a different server. Offering multiple media playlists with the same bandwidth, the player switches to an identical playlist, providing consistent stream performance.

You can add various kinds of metadata to media stream segments. The data offers applications additional information during playback. For example, add the album art, artist’s name, and song title to an audio stream, or add the current batter’s name and statistics to video of a baseball game.

You insert the additional data, known as timed metadata, into a media stream at a given time offset. (Optionally, insert timed metadata into all segments after a given time.)

For more information on timed metadata, read _[Timed Metadata for HTTP Live Streaming](../../documentation/Audio%20Video/Timed%20Metadata%20for%20HTTP%20Live%20Streaming/1.0%20Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimzv)_.

HLS facilitates ad insertion through discontinuity markers. The markers within playlists smooth transitions between disparate content.

For more on discontinuities, read _[Example Playlist Files for use with HTTP Live Streaming](https://developer.apple.com/library/archive/technotes/tn2288/_index.html#//apple_ref/doc/uid/DTS40012238)_.

Media segments can be individually encrypted using sample-level encryption. References to the corresponding key files appear in the playlist file so that the player can retrieve the keys for decryption.

HLS supports key exchange with the method of your choice. Static keys, encoder generated keys, and frequently updated keys are just a few of the possibilities.

For detail on the sample-level encryption specified for use with HLS, read _[MPEG-2 Stream Encryption Format for HTTP Live Streaming](../../documentation/Audio%20Video/MPEG-2%20Stream%20Encryption%20Format%20for%20HTTP%20Live%20Streaming/1.0%20Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnrs)_.

For details on serving keys, see _[How to securely serve Key files for HTTP Live Streaming with HTTPS](https://developer.apple.com/library/archive/qa/qa1661/_index.html#//apple_ref/doc/uid/DTS40009204)_.

The following requirements apply to iOS apps submitted for distribution in the App Store for use on Apple products. Noncompliant apps may be rejected or removed, at the discretion of Apple.

- If your app delivers video over cellular networks, and the video exceeds either 10 minutes or 5 MB of data in a five-minute period, you must use HLS. You can use progressive download for smaller clips.
- If your app uses HLS over cellular networks, you must provide at least one stream at 192 Kbps or lower bandwidth. The low-bandwidth stream may be audio-only or audio with a still image.

A series of HTTP streams are available for testing on Apple's developer site. These examples show proper formatting of HTML to embed streams, `.m3u8` playlists to index the streams, and `.ts` media segment files. See the [HTTP Live Streaming page](https://developer.apple.com/streaming/).

Apple provides simplified command-line tools, such as the _Media File Segmenter_ and _Media Stream Segmenter_, to divide presentations and produce playlist files. Sign in with your developer ID and visit the [HTTP Live Streaming page](https://developer.apple.com/streaming/), under "Downloads."

Use the Apple-provided media stream validator found in these downloaded tools prior to serving your streams, to ensure that they are fully compliant with HLS.

To get started with your own HLS streams, the _HTTP Live Streaming Content Guide_ provides a simple walkthrough of basic stream creation. The guide also explains complex HLS concepts, how to implement advanced features, and requirements for streaming to iOS devices.

Read the [HTTP Live Streaming specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming) for current and definitive technical information.

| Internet Draft | EXT-X-VERSION | iOS Version | Apple TV version | Notes |
| --- | --- | --- | --- | --- |
| 00, 01 | 1 | 3 |  | Initial version. |
| 02 | 1 | 3.1 |  | Added EXT-X-DISCONTINUITY. Changed Content-Type. Added redundant streams. |
| 03, 04 | 2 | 3.2 |  | Added EXT-X-VERSION. Added IV attribute to EXT-X-KEY. Added RESOLUTION attribute to EXT-X-STREAM-INF.  Corrected CODECS attribute values. |
| 03, 04 | 2 | 4 |  | Added timed metadata APIs.  Added custom protocols for keys. |
| 05 | 3 | 4.2 | 4.1 | Added EXTINF floating point durations; Support CEA-608 Closed captions. |
| 05 | 3 | 4.3 | 4.3 | Added AccessLog & ErrorLog objects to APIs. |
| 06 | 3 | 4.3.2 |  | Added EXT-X-PLAYLIST-TYPE. |
| 07, 08 | 4 | 5 | 4.4 | Added EXT-X-I-FRAMES-ONLY, EXT-X-I-FRAME-STREAM-INF, EXT-X-MEDIA, EXT-X-BYTERANGE.  Added AUDIO and VIDEO attributes to EXT-X-STREAM-INF. |
| 09, 10, 11 | 5 | 6 | 5.1 | Added EXT-X-MAP.  Added KEYFORMAT and KEYFORMATVERSIONS attributes to EXT-X-KEY; FORCED and CHARACTERISTICS attributes to EXT-X-MEDIA; and SUBTITLES attribute to EXT-X-STREAM-INF.  Added SAMPLE-AES value to METHOD attribute of EXT-X-KEY; and SUBTITLES value to TYPE attribute of EXT-X-MEDIA. |

[Next](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/AboutHTTPLiveStreaming/RevisionHistory.html)

