---
title: HTTP Live Streaming Overview
apple_id: TP40008332
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/FrequentlyAskedQuestions/FrequentlyAskedQuestions.html
archived_at: '2026-07-15T08:19:13.347346Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HTTP Live Streaming Overview](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Deploying%20HTTP%20Live%20Streaming.md)

# Frequently Asked Questions

1. __What kinds of encoders are supported?__

   The protocol specification does not limit the encoder selection. However, the current Apple implementation should interoperate with encoders that produce MPEG-2 Transport Streams containing H.264 video and AAC audio (HE-AAC or AAC-LC). Encoders that are capable of broadcasting the output stream over UDP should also be compatible with the current implementation of the Apple provided segmenter software.
2. __What are the specifics of the video and audio formats supported?__

   Although the protocol specification does not limit the video and audio formats, the current Apple implementation supports the following formats:

   - Video:

     - H.264 Baseline Level 3.0, Baseline Level 3.1, Main Level 3.1, and High Profile Level 4.1.
   - Audio:

     - HE-AAC or AAC-LC up to 48 kHz, stereo audio
     - MP3 (MPEG-1 Audio Layer 3) 8 kHz to 48 kHz, stereo audio
     - AC-3 (for Apple TV, in pass-through mode only)
3. __What duration should media files be?__

   The main point to consider is that shorter segments result in more frequent refreshes of the index file, which might create unnecessary network overhead for the client. Longer segments will extend the inherent latency of the broadcast and initial startup time. A duration of 10 seconds of media per file seems to strike a reasonable balance for most broadcast content.
4. __How many files should be listed in the index file during a continuous, ongoing session?__

   The normal recommendation is 3, but the optimum number may be larger.

   The important point to consider when choosing the optimum number is that the number of files available during a live session constrains the client's behavior when doing play/pause and seeking operations. The more files in the list, the longer the client can be paused without losing its place in the broadcast, the further back in the broadcast a new client begins when joining the stream, and the wider the time range within which the client can seek. The trade-off is that a longer index file adds to network overhead—during live broadcasts, the clients are all refreshing the index file regularly, so it does add up, even though the index file is typically small.
5. __What data rates are supported?__

   The data rate that a content provider chooses for a stream is most influenced by the target client platform and the expected network topology. The streaming protocol itself places no limitations on the data rates that can be used. The current implementation has been tested using audio-video streams with data rates as low as 64 Kbps and as high as 3 Mbps to iPhone. Audio-only streams at 64 Kbps are recommended as alternates for delivery over slow cellular connections.

   For recommended data rates, see [Preparing Media for Delivery to iOS-Based Devices](Using%20HTTP%20Live%20Streaming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzy).
6. __What is a .ts file?__

   A `.ts` file contains an MPEG-2 Transport Stream. This is a file format that encapsulates a series of encoded media samples—typically audio and video. The file format supports a variety of compression formats, including MP3 audio, AAC audio, H.264 video, and so on. Not all compression formats are currently supported in the Apple HTTP Live Streaming implementation, however. (For a list of currently supported formats, see [Media Encoder](HTTP%20Streaming%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgewvgvzt).

   MPEG-2 Transport Streams are containers, and should not be confused with MPEG-2 compression.
7. __What is an .M3U8 file?__

   An `.M3U8` file is a extensible playlist file format. It is an m3u playlist containing UTF-8 encoded text. The m3u file format is a de facto standard playlist format suitable for carrying lists of media file URLs. This is the format used as the index file for HTTP Live Streaming. For details, see [IETF Internet-Draft of the HTTP Live Streaming specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming).
8. __How does the client software determine when to switch streams?__

   The current implementation of the client observes the effective bandwidth while playing a stream. If a higher-quality stream is available and the bandwidth appears sufficient to support it, the client switches to a higher quality. If a lower-quality stream is available and the current bandwidth appears insufficient to support the current stream, the client switches to a lower quality.
9. __Where can I find a copy of the media stream segmenter from Apple?__

   The media stream segmenter, file stream segmenter, and other tools are frequently updated, so you should download the current version of the HTTP Live Streaming Tools from the Apple Developer website. See [Download the Tools](Using%20HTTP%20Live%20Streaming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzt) for details.
10. __What settings are recommended for a typical HTTP stream, with alternates, for use with the media segmenter from Apple?__

    See [Preparing Media for Delivery to iOS-Based Devices](Using%20HTTP%20Live%20Streaming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzy).

    These settings are the current recommendations. There are also certain requirements. The current `mediastreamsegmenter` tool works only with MPEG-2 Transport Streams as defined in ISO/IEC 13818. The transport stream must contain H.264 (MPEG-4, part 10) video and AAC or MPEG audio. If AAC audio is used, it must have ADTS headers. H.264 video access units must use Access Unit Delimiter NALs, and must be in unique PES packets.

    The segmenter also has a number of user-configurable settings. You can obtain a list of the command line arguments and their meanings by typing `man mediastreamsegmenter` from the Terminal application. A target duration (length of the media segments) of 10 seconds is recommended, and is the default if no target duration is specified.
11. __How can I specify what codecs or H.264 profile are required to play back my stream?__

    Use the `CODECS` attribute of the `EXT-X-STREAM-INF` tag. When this attribute is present, it must include all codecs and profiles required to play back the stream. The following values are currently recognized:

|  |  |
| --- | --- |
| AAC-LC | `"mp4a.40.2"` |
| HE-AAC | `"mp4a.40.5"` |
| MP3 | `"mp4a.40.34"` |
| H.264 Baseline Profile level 3.0 | `"avc1.42001e"` or `"avc1.66.30"`  Note: Use `"avc1.66.30"` for compatibility with iOS versions 3.0 to 3.1.2. |
| H.264 Baseline Profile level 3.1 | `"avc1.42001f"` |
| H.264 Main Profile level 3.0 | `"avc1.4d001e"` or `"avc1.77.30"`  Note: Use `"avc1.77.30"` for compatibility with iOS versions 3.0 to 3.12. |
| H.264 Main Profile level 3.1 | `"avc1.4d001f"` |
| H.264 Main Profile level 4.0 | `"avc1.4d0028"` |
| H.264 High Profile level 3.1 | `"avc1.64001f"` |
| H.264 High Profile level 4.0 | `"avc1.640028"` |
| H.264 High Profile level 4.1 | `"avc1.640029"` |

    The attribute value must be in quotes. If multiple values are specified, one set of quotes is used to contain all values, and the values are separated by commas. An example follows.

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=500000, RESOLUTION=720x480
mid_video_index.M3U8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=800000, RESOLUTION=1280x720
wifi_video_index.M3U8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=3000000, CODECS="avc1.4d001e,mp4a.40.5", RESOLUTION=1920x1080
h264main_heaac_index.M3U8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=64000, CODECS="mp4a.40.5"
aacaudio_index.M3U8
```
12. __How can I create an audio-only stream from audio/video input?__

    Add the `-audio-only` argument when invoking the stream or files segmenter.
13. __How can I add a still image to an audio-only stream?__

    Use the `-meta-file` argument when invoking the stream or file segmenter with `-meta-type=picture` to add an image to every segment. For example, this would add an image named poster.jpg to every segment of an audio stream created from the file track01.mp3:

    `mediafilesegmenter -f` _/Dir/outputFile_ `-a --meta-file=poster.jpg --meta-type=picture track01.mp3`

    Remember that the image is typically resent every ten seconds, so it’s best to keep the file size small.
14. __How can I specify an audio-only alternate to an audio-video stream?__

    Use the `CODECS` and `BANDWIDTH` attributes of the `EXT-X-STREAM-INF` tag together.

    The `BANDWIDTH` attribute specifies the bandwidth required for each alternate stream. If the available bandwidth is enough for the audio alternate, but not enough for the lowest video alternate, the client switches to the audio stream.

    If the `CODECS` attribute is included, it must list all codecs required to play the stream. If only an audio codec is specified, the stream is identified as audio-only. Currently, it is not required to specify that a stream is audio-only, so use of the `CODECS` attribute is optional.

    The following is an example that specifies video streams at 500 Kbps for fast connections, 150 Kbps for slower connections, and an audio-only stream at 64 Kbps for very slow connections. All the streams should use the same 64 Kbps audio to allow transitions between streams without an audible disturbance.

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=500000, RESOLUTION=1920x1080
mid_video_index.M3U8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=150000, RESOLUTION=720x480
3g_video_index.M3U8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=64000, CODECS="mp4a.40.5"
aacaudio_index.M3U8
```
15. __What are the hardware requirements or recommendations for servers?__

    See question #1 for encoder hardware recommendations.

    The Apple stream segmenter is capable of running on any Intel-based Mac. We recommend using a Mac with two Ethernet network interfaces, such as a Mac Pro or an XServe. One network interface can be used to obtain the encoded stream from the local network, while the second network interface can provide access to a wider network.
16. __Does the Apple implementation of HTTP Live Streaming support DRM?__

    No. However, media can be encrypted, and key access can be limited by requiring authentication when the client retrieves the key from your HTTPS server.
17. __What client platforms are supported?__

    iPhone, iPad, and iPod touch (requires iOS version 3.0 or later), Apple TV (version 2 and later), and Mac OS X computers.
18. __Is the protocol specification available?__

    Yes. The protocol specification is an IETF Internet-Draft, at [http://tools.ietf.org/html/draft-pantos-http-live-streaming](http://tools.ietf.org/html/draft-pantos-http-live-streaming).
19. __Does the client cache content?__

    The index file can contain an instruction to the client that content should not be cached. Otherwise, the client may cache data for performance optimization when seeking within the media.
20. __Is this a real-time delivery system?__

    No. It has inherent latency corresponding to the size and duration of the media files containing stream segments. At least one segment must fully download before it can be viewed by the client, and two may be required to ensure seamless transitions between segments. In addition, the encoder and segmenter must create a file from the input; the duration of this file is the minimum latency before media is available for download. Typical latency with recommended settings is in the neighborhood of 30 seconds.
21. __What is the latency?__

    Approximately 30 seconds, with recommended settings. See question #15.
22. __Do I need to use a hardware encoder?__

    No. Using the protocol specification, it is possible to implement a software encoder.
23. __What advantages does this approach have over RTP/RTSP?__

    HTTP is less likely to be disallowed by routers, NAT, or firewall settings. No ports need to be opened that are commonly closed by default. Content is therefore more likely to get through to the client in more locations and without special settings. HTTP is also supported by more content-distribution networks, which can affect cost in large distribution models. In general, more available hardware and software works unmodified and as intended with HTTP than with RTP/RTSP. Expertise in customizing HTTP content delivery using tools such as PHP is also more widespread.

    Also, HTTP Live Streaming is supported in Safari and the media player framework on iOS. RTSP streaming is not supported.
24. __Why is my stream’s overall bit rate higher than the sum of the audio and video bitrates?__

    MPEG-2 transport streams can include substantial overhead. They utilize fixed packet sizes that are padded when the packet contents are smaller than the default packet size. Encoder and multiplexer implementations vary in their efficiency at packing media data into these fixed packet sizes. The amount of padding can vary with frame rate, sample rate, and resolution.
25. __How can I reduce the overhead and bring the bit rate down?__

    Using a more efficient encoder can reduce the amount of overhead, as can tuning the encoder settings.
26. __Do all media files have to be part of the same MPEG-2 Transport Stream?__

    No. You can mix media files from different transport streams, as long as they are separated by `EXT-X-DISCONTINUITY` tags. See the protocol specification for more detail. For best results, however, all video media files should have the same height and width dimensions in pixels.
27. __Where can I get help or advice on setting up an HTTP audio/video server?__

    You can visit the Apple Developer Forum at [http://devforums.apple.com/](http://devforums.apple.com/).

    Also, check out _[Best Practices for Creating and Deploying HTTP Live Streaming Media for Apple Devices](https://developer.apple.com/library/archive/technotes/tn2224/_index.html#//apple_ref/doc/uid/DTS40009745)_.

[Next](Document%20Revision%20History.md)[Previous](Deploying%20HTTP%20Live%20Streaming.md)

