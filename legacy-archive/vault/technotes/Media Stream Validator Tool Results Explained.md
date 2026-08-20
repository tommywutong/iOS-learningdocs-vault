---
title: Media Stream Validator Tool Results Explained
apple_id: DTS40010221
resource_type: Technical Note
platform: iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2015-05-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2235/_index.html
archived_at: '2026-07-26T19:54:09.926485Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2235

# Media Stream Validator Tool Results Explained

Describes the warnings and errors returned by the Media Stream Validator tool.

[HTTP Live Streaming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamrsgewugsbrfvke4vcbi4yq)[Media Stream Validator Tool](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamrsgewugsbrfvlectcjiravit2skrhu6ta)[Errors and Warnings Explained](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamrsgewugsbrfvcveuspkjjv6qkoirpvoqksjzeu4r2tl5cvqucmifeu4rke)[Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamrsgewugsbrfvcveuspkjjv6qkoirpvoqksjzeu4r2tl5cvqucmifeu4rkefvcveuspkjjq)[Warnings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamrsgewugsbrfvcveuspkjjv6qkoirpvoqksjzeu4r2tl5cvqucmifeu4rkefvlucusojfheouy)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamrsgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## HTTP Live Streaming

HTTP Live Streaming allows you to send live or prerecorded audio and video to iPhone, iPad, and other devices including desktop computers, using an ordinary Web server. Playback requires iOS 3.0 or later on devices running iOS; QuickTime X or later is required on the desktop. See the [HTTP Live Streaming Overview](https://developer.apple.com/iphone/library/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html) for more information.

[Back to Top](#)

## Media Stream Validator Tool

The Media Stream Validator (`mediastreamvalidator`) is a command-line tool to validate HTTP Live Streaming streams and servers.

This tool simulates an HTTP Live Streaming session and verifies that the index file and media segments conform to the HTTP Live Streaming specification. It performs several checks to ensure reliable streaming. If any errors or problems are found, a detailed diagnostic report is displayed. This technote provides an explanation of many of the common errors and warnings reported by the tool.

__Important:__ You should always run the mediastreamvalidator tool on your stream to verify that it conforms to the HTTP Live Streaming specification.

The Media Stream Validator is part of the HTTP Live Streaming Tools package, which contains several prerelease command-line tools that are used for deployment and validation of HTTP Live Streaming solutions.

iOS Developer Program members and Mac Developer Program members can download the tools as part of the HTTP Live Streaming Tools package.

__Important:__ The tools are frequently updated. If you are an iOS Developer Program member or a Mac Developer Program member, you can download the latest versions from the Apple Developer website. To download, go to [Downloads for Apple Developers](https://developer.apple.com/downloads/index.action?=http%20live%20streaming%20tools), download and install the 'HTTP Live Streaming Tools'.

[Back to Top](#)

## Errors and Warnings Explained

Listed below is a description of many of the common errors and warnings that are returned by the Media Stream Validator tool.

### Errors

These are many of the common errors that can be returned by the Media Stream Validator tool.

These errors indicate a serious problem with the stream that must be corrected in order for the stream to play correctly.

- __ERROR: Invalid response from the validator helper: a track is missing the 'type' property__

  You have defined an audio or video track in your transport stream program map table (PMT), but there are no frames of that type in the actual stream.
- __ERROR: Media segment is incorrectly encrypted.__

  Check to make sure you have properly encrypted your media.

  Both the `mediastreamsegmenter` and `mediafilesegmenter` command-line tools allow you to encrypt the media and produce encryption keys. For details, type `man` `mediastreamsegmenter` and `man` `mediafilesegmenter` from the terminal window.

If the Media Stream Validator tool returns any of the following errors (or any other errors not listed here) when validating your stream please file a bug report against the tool using the [Apple Bug Reporter](https://developer.apple.com/bugreporter/) and include a link to your stream in your report.

- __ERROR: Invalid media segment: The validator helper exited due to a fatal error: failed to create format reader: [errno: -12847] format reader file not recognized__
- __ERROR: Invalid media segment: The validator helper exited due to a SIGABRT signal.__
- __ERROR: Invalid media segment: The validator helper exited due to a fatal error: segment duration is not finite__

### Warnings

These are many of the common warnings that can be returned by the Media Stream Validator tool.

Warnings indicate problems that you should correct in order for your stream to play correctly.

- __WARNING: Media segment duration outside of expected duration by 25.926 % (7.41 vs. 10.00 seconds, limit is 20 %)__

  The playback duration of the segment exceeded the value advertised in the `duration` parameter of the `#EXTINF` tag in the playlist file. See the [HTTP Live Streaming specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming) (currently an IETF Internet-Draft) for more information about the `#EXTINF` tag.

  We suggest you use the latest `mediastreamsegmenter` tool to create your media segments, and use the `optimize` option. MPEG-2 transport streams can include substantial overhead. They utilize fixed packet sizes that are padded when the packet contents are smaller than the default packet size. Encoder and multiplexer implementations vary in their efficiency at packing media data into these fixed packet sizes. The amount of padding can vary with frame rate, sample rate, and resolution.

  See [Technical Note TN2224 Best Practices for Creating and Deploying HTTP Live Streaming Media for the iPhone and iPad](https://developer.apple.com/iphone/library/technotes/tn2010/tn2224.html) for media encoding recommendations.
- __WARNING: Media segment contains a video track but does not contain any IDR access unit with a SPS and a PPS__

  The encoder is not putting any Instantaneous Decoder Refresh (IDR) frames in the media segments except at the very beginning; IDR frames must be included in each segment to allow clients to seek to different points in the stream.

  IDR frames define synchronization points in H.264/MPEG-4 AVC video; IDR frames can be decoded without reference to previous frames. You can seek to these points and play the video (these are the H.264 equivalent of I-frames).
- __WARNING: Media segment bitrate outside of target playlist bitrate by 29.942 % (364530 vs. 520324 bps, limit is 10 %).__

  The actual measured bitrate of the stream is not what is advertised in the `BANDWIDTH` attribute in the `EXT-X-STREAM-INF` tag in the playlist.

  You can reduce the overhead by using a more efficient encoder, and by fine-tuning the encoder settings. The `-optimize` argument can be passed to the Apple segmenter tools to significantly reduce the overhead, particularly for low-bandwidth streams.

  In the case where you are creating a low-bitrate 192 kbps stream, we recommend you create an audio-only stream with a poster frame. The Apple `mediastreamsegmenter` tool can produce an audio-only stream if you specify the following argument:

  `-a | -audio-only`

  This strips the audio elementary stream (AAC/ADTS or MP3) and writes it into the media file. You could, for example, run the `mediastreamsegmenter` on an existing audio/video stream to get an audio-only stream.

  Use the `-meta-file` argument when invoking the stream or file segmenter with `-meta-type=picture` to add an image to every segment. For example, this would add an image named `poster.jpg` to every segment of an audio stream created from the file `track01.mp3`:

  `mediafilesegmenter -f /Dir/outputFile -a --meta-file=poster.jpg --meta-type=picture track01.mp3`

  Remember that the image is resent in every segment. This is typically every ten seconds, so it’s best to keep the file size small.

  You can also get this error if you are using audio inserted in a transport stream; use an audio elementary stream instead.
- __WARNING: 6 samples (2.007 %) do not have timestamps in track 257 (avc1)__

  The encoder is not properly placing timestamps. In AVC video, you should have both a Decoding Time Stamp (DTS) and Presentation Time Stamp (PTS) in each Packetized Elementary Stream (PES) header. These indicate the exact moment where a video frame or an audio frame has to be decoded or presented to the user.
- __WARNING: The playlist should use relative URIs to reduce its size__

  Individual playlist entries that specify full path names require more text than entries with relative path names. In the case of very long video on demand (VOD) playlists or very long duration live playlists this can create a significant file size difference in the playlist file itself, increasing the download time of the playlist files.

  Using relative URIs means less characters, which will reduce the number of bytes going across the network.
- __WARNING: Playlist Content-Type is 'text/plain', but should be one of 'application/vnd.apple.mpegurl', 'audio/x-mpegurl' or 'audio/mpegurl'__

  This is a problem with the MIME-type setting in your webserver. With an Apache webserver the recommended configuration is typically limited to specifying MIME-type associations for .M3U8 files and .ts files as shown in X Table 1:

  __Table 1__  WebServer MIME-type asssociations for .M3U8 files

  | File extension | MIME type |
  | .M3U8 | application/x-mpegURL or vnd.apple.mpegURL |
  | .ts | video/MP2T |
- __WARNING: INF tag with duration 2 seconds or more above the playlist's target duration (10.000 seconds)__

  The `EXTINF` `duration` parameter of each media file in the Playlist file MUST be less than or equal to the target duration.

  The playlist target duration tag MUST appear once in the Playlist file.  Its format is:

  `#EXT-X-TARGETDURATION:<s>`

  where s is an integer indicating the target duration in seconds.

  See the [IETF Internet Draft of the HTTP Live Streaming Protocol Specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming) for more information.
- __WARNING: stream discontinuity detected__

  You must use the `EXT-X-DISCONTINUITY` tag where an encoding discontinuity exists between the media file that follows it and the one that preceded it. See the [IETF Internet Draft of the HTTP Live Streaming Protocol Specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming) for more information.

  If you intend to play a new stream at a given point in your presentation, you must use the `EXT-X-DISCONTINUITY` tag.
- __WARNING: Media segment took longer to download than its duration (10.30 vs. 9.54 seconds).__

  This may be due to a slow server or poor network connection (for example, it required more than 10 seconds to download a 9.54 second segment).
- __WARNING: Timestamps are too spread out across the variant playlists, with a maximum spread of 125.13 seconds and a maximum target duration of 10 seconds (threshold is twice that number).__

  The timestamps aren't equivalent across the variant streams, for example:

  - Stream 1 starts with time 100 and continues

  - Stream 2 starts with time 400 and continues

  For video on demand (VOD), these should be dead-on.
- __WARNING: Cached time for presentation http://yourserver.com/index.m3u8 (21 seconds) exceeds 2 x the target duration (10 seconds)__

  For a live stream index file, the difference between the last modified time and the current time as reported by the server exceeds twice the target duration. This can mean the index file is out of date (it was cached too long).
[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-05-04 | Updated to reflect current App Store Review Guidelines. Fixed broken link for tools download. |
| 2010-08-03 | New document that describes the warnings and errors returned by the Media Stream Validator tool. |

