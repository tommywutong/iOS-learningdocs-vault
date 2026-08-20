---
title: HTTP Live Streaming Overview
apple_id: TP40008332
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/UsingHTTPLiveStreaming/UsingHTTPLiveStreaming.html
archived_at: '2026-07-15T08:19:13.838192Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HTTP Live Streaming Overview](Introduction.md)


[Next](Deploying%20HTTP%20Live%20Streaming.md)[Previous](HTTP%20Streaming%20Architecture.md)

# Using HTTP Live Streaming

There are several tools available that can help you set up an HTTP Live Streaming service. The tools include a media stream segmenter, a media file segmenter, a stream validator, an id3 tag generator, and a variant playlist generator.

The tools are frequently updated, so you should download the current version of the HTTP Live Streaming Tools from the Apple Developer website. You can access them if you are a member of the iOS Developer Program. One way to navigate to the tools is to log onto [developer.apple.com](https://developer.apple.com/), then use the search feature.

The `mediastreamsegmenter` command-line tool takes an MPEG-2 transport stream as an input and produces a series of equal-length files from it, suitable for use in HTTP Live Streaming. It can also generate index files (also known as playlists), encrypt the media, produce encryption keys, optimize the files by reducing overhead, and create the necessary files for automatically generating multiple stream alternates. For details, verify you have installed the tools, and type `man mediastreamsegmenter` from the terminal window.

Usage example: `mediastreamsegmenter -s 3 -D -f /Library/WebServer/Documents/stream 239.4.1.5:20103`

The usage example captures a live stream from the network at address `239.4.1.5:20103` and creates media segment files and index files from it. The index files contain a list of the current three media segment files (`-s 3`). The media segment files are deleted after use (`-D`). The index files and media segment files are stored in the directory `/Library/WebServer/Documents/stream`.

The `mediafilesegmenter` command-line tool takes an encoded media file as an input, wraps it in an MPEG-2 transport stream, and produces a series of equal-length files from it, suitable for use in HTTP Live Streaming. The media file segmenter can also produce index files (playlists) and decryption keys. The file segmenter behaves very much like the stream segmenter, but it works on existing files instead of streams coming from an encoder. For details, type `man mediafilesegmenter` from the terminal window.

The `mediastreamvalidator` command-line tool examines the index files, stream alternates, and media segment files on a server and tests to determine whether they will work with HTTP Live Streaming clients. For details, type `man mediastreamvalidator` from the terminal window.

The `variantplaylistcreator` command-line tool creates a master index file, or playlist, listing the index files for alternate streams at different bit rates, using the output of the `mediafilesegmenter`. The `mediafilesegmenter` must be invoked with the `-generate-variant-playlist` argument to produce the required output for the variant playlist creator. For details, type `man variantplaylistcreator` from the terminal window.

The `id3taggenerator` command-line tool generates ID3 metadata tags. These tags can either be written to a file or inserted into outgoing stream segments. For details, see [Adding Timed Metadata](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzu).

The HTTP Live Streaming protocol supports two types of sessions: events (live broadcasts) and video on demand (VOD).

For VOD sessions, media files are available representing the entire duration of the presentation. The index file is static and contains a complete list of all files created since the beginning of the presentation. This kind of session allows the client full access to the entire program.

VOD can also be used to deliver “canned” media. HTTP Live Streaming offers advantages over progressive download for VOD, such as support for media encryption and dynamic switching between streams of different data rates in response to changing connection speeds. (QuickTime also supports multiple-data-rate movies using progressive download, but QuickTime movies do not support dynamically switching between data rates in mid-movie.)

Live sessions (events) can be presented as a complete record of an event, or as a sliding window with a limited time range the user can seek within.

For live sessions, as new media files are created and made available, the index file is updated. The new index file lists the new media files. Older media files can be removed from the index and discarded, presenting a moving window into a continuous stream—this type of session is suitable for continuous broadcasts. Alternatively, the index can simply add new media files to the existing list—this type of session can be easily converted to VOD after the event completes.

It is possible to create a live broadcast of an event that is instantly available for video on demand. To convert a live broadcast to VOD, do not remove the old media files from the server or delete their URLs from the index file; instead, add an `#EXT-X-ENDLIST` tag to the index when the event ends. This allows clients to join the broadcast late and still see the entire event. It also allows an event to be archived for rebroadcast with no additional time or effort.

If your playlist contains an `EXT-X-PLAYLIST-TYPE` tag, you should also change the value from `EVENT` to `VOD`.

Media files containing stream segments may be individually encrypted. When encryption is employed, references to the corresponding key files appear in the index file so that the client can retrieve the keys for decryption.

When a key file is listed in the index file, the key file contains a cipher key that must be used to decrypt subsequent media files listed in the index file. Currently HTTP Live Streaming supports AES-128 encryption using 16-octet keys. The format of the key file is a packed array of these 16 octets in binary format.

The media stream segmenter available from Apple provides encryption and supports three modes for configuring encryption.

The first mode allows you to specify a path to an existing key file on disk. In this mode the segmenter inserts the URL of the existing key file in the index file. It encrypts all media files using this key.

The second mode instructs the segmenter to generate a random key file, save it in a specified location, and reference it in the index file. All media files are encrypted using this randomly generated key.

The third mode instructs the segmenter to generate a new random key file every _n_ media segments, save it in a specified location, and reference it in the index file. This mode is referred to as key rotation. Each group of _n_ files is encrypted using a different key.

You can serve key files using either HTTP or HTTPS. You may also choose to protect the delivery of the key files using your own session-based authentication scheme. For details, see [Serving Key Files Securely Over HTTPS](Deploying%20HTTP%20Live%20Streaming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmrnknlte).

Key files require an initialization vector (IV) to decode encrypted media. The IVs can be changed periodically, just as the keys can.

HTTPS is commonly used to deliver key files. It may also be used to deliver the media segment files and index files, but this is not recommended when scalability is important, since HTTPS requests often bypass web server caches, causing all content requests to be routed through your server and defeating the purpose of edge network distribution systems.

For this very reason, however, it is important to make sure that any content delivery network you use understands that the `.M3U8` index files are not to be cached for longer than one media segment duration for live broadcasts, where the index file is changing dynamically.

A master index file may reference alternate streams of content. References can be used to support delivery of multiple streams of the same content with varying quality levels for different bandwidths or devices. HTTP Live Streaming supports switching between streams dynamically if the available bandwidth changes. The client software uses heuristics to determine appropriate times to switch between the alternates. Currently, these heuristics are based on recent trends in measured network throughput.

The master index file points to alternate streams of media by including a specially tagged list of other index files, as illustrated in Figure 2-1

__Figure 2-1__  Stream alternates

!

Both the master index file and the alternate index files are in `.M3U8` playlist format. The master index file is downloaded only once, but for live broadcasts the alternate index files are reloaded periodically. The first alternate listed in the master index file is the first stream used—after that, the client chooses among the alternates by available bandwidth.

Note that the client may choose to change to an alternate stream at any time, such as when a mobile device enters or leaves a WiFi hotspot. All alternates should use identical audio to allow smooth transitions among streams.

You can create a set of stream alternates by using the `variantplaylistcreator` tool and specifying the `-generate-variant-playlist` option for either the `mediafilesegmenter` tool or the `mediastreamsegmenter` tool (see [Download the Tools](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzt) for details).

When using stream alternates, it is important to bear the following considerations in mind:

- The first entry in the variant playlist is played when a user joins the stream and is used as part of a test to determine which stream is most appropriate. The order of the other entries is irrelevant.
- Where possible, encode enough variants to provide the best quality stream across a wide range of connection speeds. For example, encode variants at 150 kbps, 350 kbps, 550 kbps, 900 kbps, 1500 kbps.
- When possible, use relative path names in variant playlists and in the individual `.M3U8` playlist files
- The video aspect ratio on alternate streams _must_ be exactly the same, but alternates can have different pixel dimensions, as long as they have the same aspect ratio. For example, two stream alternates with the same 4:3 aspect ratio could have dimensions of 400 x 300 and 800 x 600.
- The `RESOLUTION` field in the `EXT-X-STREAM-INF` should be included to help the client choose an appropriate stream.
- If you are an iOS app developer, you can query the user’s device to determine whether the initial connection is cellular or WiFi and choose an appropriate master index file.

  To ensure the user has a good experience when the stream is first played, regardless of the initial network connection, you should have more than one master index file consisting of the same alternate index files but with a different first stream.

  A 150k stream for the cellular variant playlist is recommended.

  A 240k or 440k stream for the Wi-Fi variant playlist is recommended.
- When you specify the bitrates for stream variants, it is important that the `BANDWIDTH` attribute closely match the actual bandwidth required by a given stream. If the actual bandwidth requirement is substantially different than the `BANDWIDTH` attribute, automatic switching of streams may not operate smoothly or even correctly.

When you send video to a mobile device such as iPhone or iPad, the client’s Internet connection may move to or from a cellular network at any time.

HTTP Live Streaming allows the client to choose among stream alternates dynamically as the network bandwidth changes, providing the best stream as the device moves between cellular and WiFi connections, for example, or between 3G and EDGE connections. This is a significant advantage over progressive download.

It is strongly recommended that you use HTTP Live Streaming to deliver video to all cellular-capable devices, even for video on demand, so that your viewers have the best experience possible under changing conditions.

In addition, you should provide cellular-capable clients an alternate stream at 64 Kbps or less for slower data connections. If you cannot provide video of acceptable quality at 64 Kbps or lower, you should provide an audio-only stream, or audio with a still image.

A good choice for pixel dimensions when targeting cellular network connections is 400 x 224 for 16:9 content and 400 x 300 for 4:3 content (see [Preparing Media for Delivery to iOS-Based Devices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzy)).

If your app delivers video over cellular networks, and the video exceeds either 10 minutes duration or 5 MB of data in a five minute period, you are required to use HTTP Live Streaming. (Progressive download may be used for smaller clips.)

If your app uses HTTP Live Streaming over cellular networks, you are required to provide at least one stream at 64 Kbps or lower bandwidth (the low-bandwidth stream may be audio-only or audio with a still image).

These requirements apply to iOS apps submitted for distribution in the App Store for use on Apple products. Non-compliant apps may be rejected or removed, at the discretion of Apple.

If your playlist contains alternate streams, they can not only operate as bandwidth or device alternates, but as failure fallbacks. Starting with iOS 3.1, if the client is unable to reload the index file for a stream (due to a 404 error, for example), the client attempts to switch to an alternate stream.

In the event of an index load failure on one stream, the client chooses the highest bandwidth alternate stream that the network connection supports. If there are multiple alternates at the same bandwidth, the client chooses among them in the order listed in the playlist.

You can use this feature to provide redundant streams that will allow media to reach clients even in the event of severe local failures, such as a server crashing or a content distributor node going down.

To support redundant streams, create a stream—or multiple alternate bandwidth streams—and generate a playlist file as you normally would. Then create a parallel stream, or set of streams, on a separate server or content distribution service. Add the list of backup streams to the playlist file, so that the backup stream at each bandwidth is listed after the primary stream. For example, if the primary stream comes from server ALPHA, and the backup stream is on server BETA, your playlist file might look something like this:

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=200000, RESOLUTION=720x480
http://ALPHA.mycompany.com/lo/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=200000, RESOLUTION=720x480
http://BETA.mycompany.com/lo/prog_index.m3u8

#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=500000, RESOLUTION=1920x1080
http://ALPHA.mycompany.com/md/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1, BANDWIDTH=500000, RESOLUTION=1920x1080
http://BETA.mycompany.com/md/prog_index.m3u8
```

Note that the backup streams are intermixed with the primary streams in the playlist, with the backup at each bandwidth listed after the primary for that bandwidth.

You are not limited to a single backup stream set. In the example above, ALPHA and BETA could be followed by GAMMA, for instance. Similarly, you need not provide a complete parallel set of streams. You could provide a single low-bandwidth stream on a backup server, for example.

You can add various kinds of metadata to media stream segments. For example, you can add the album art, artist’s name, and song title to an audio stream. As another example, you could add the current batter’s name and statistics to video of a baseball game.

If an audio-only stream includes an image as metadata, the Apple client software automatically displays it. Currently, the only metadata that is automatically displayed by the Apple-supplied client software is a still image accompanying an audio-only stream.

If you are writing your own client software, however, using either `MPMoviePlayerController` or `AVPlayerItem`, you can access streamed metadata using the `timedMetaData` property.

If you are writing your own segmenter, you can read about the stream format for timed metadata information in _[Timed Metadata for HTTP Live Streaming](../../Audio%20Video/Timed%20Metadata%20for%20HTTP%20Live%20Streaming/1.0%20Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimzv)_.

If you are using Apple’s tools, you can add timed metadata by specifying a metadata file in the `-F` command line option to either the stream segmenter or the file segmenter. The specified metadata source can be a file in ID3 format or an image file (JPEG or PNG). Metadata specified this way is automatically inserted into every media segment.

This is called timed metadata because it is inserted into a media stream at a given time offset. Timed metadata can optionally be inserted into all segments after a given time.

To add timed metadata to a live stream, use the `id3taggenerator` tool, with its output set to the stream segmenter. The tool generates ID3 metadata and passes it the stream segmenter for inclusion in the outbound stream.

The tag generator can be run from a shell script, for example, to insert metadata at the desired time, or at desired intervals. New timed metadata automatically replaces any existing metadata.

Once metadata has been inserted into a media segment, it is persistent. If a live broadcast is re-purposed as video on demand, for example, it retains any metadata inserted during the original broadcast.

Adding timed metadata to a stream created using the file segmenter is slightly more complicated.

1. First, generate the metadata samples. You can generate ID3 metadata using the `id3taggenerator` command-line tool, with the output set to file.
2. Next, create a __metadata macro file__—a text file in which each line contains the time to insert the metadata, the type of metadata, and the path and filename of a metadata file.

   For example, the following metadata macro file would insert a picture at 1.2 seconds into the stream, then an ID3 tag at 10 seconds:

   `1.2 picture /meta/images/picture.jpg`

   `10 id3 /meta/id3/title.id3`
3. Finally, specify the metadata macro file by name when you invoke the media file segmenter, using the `-M` command line option.

For additional details, see the `man` pages for `mediastreamsegmenter`, `mediafilesegmenter`, and `id3taggenerator`.

HTTP Live Streaming supports closed captions within streams. If you are using the stream segmenter, you need to add CEA-608 closed captions to the MPEG-2 transport stream (in the main video elementary stream) as specified in ATSC A/72. If you are using the file segmenter, you should encapsulate your media in a QuickTime movie file and add a closed captions track (`'clcp'`). If you are writing an app, the AVFoundation framework supports playback of closed captions.

Live streaming also supports multiple subtitle and closed caption tracks in Web Video Text Tracks (WebVTT) format. The sample in Listing 2-1 shows two closed captions tracks in a master playlist.

__Listing 2-1__  Master playlist with multiple closed captions tracks

```
#EXTM3U

#EXT-X-MEDIA:TYPE=CLOSED-CAPTIONS,GROUP-ID="cc",NAME="CC1",LANGUAGE="en",DEFAULT=YES,AUTOSELECT=YES,INSTREAM-ID="CC1"
#EXT-X-MEDIA:TYPE=CLOSED-CAPTIONS,GROUP-ID="cc",NAME="CC2",LANGUAGE="sp",AUTOSELECT=YES,INSTREAM-ID="CC2"

#EXT-X-STREAM-INF:BANDWIDTH=1000000,SUBTITLES="subs",CLOSED-CAPTIONS="cc"
x.m3u8
```

In the encoding process, the WebVTT files are broken into segments just as audio and video media. The resulting media playlist includes segment durations to sync text with the correct point in the associated video.

Advanced features of live streaming subtitles and closed captions include semantic metadata, CSS styling, and simple animation.

For more information on implementation of WebVTT is available in _WWDC 2012: What's New in HTTP Live Streaming_ and [WebVTT: The Web Video Text Tracks Format specification](http://dev.w3.org/html5/webvtt/).

The recommended encoder settings for streams used with iOS-based devices are shown in the following four tables. For live streams, these settings should be available from your hardware or software encoder. If you are re-encoding from a master file for video on demand, you can use a video editing tool such as Compressor.

File format for the file segmenter can be a QuickTime movie, MPEG-4 video, or MP3 audio, using the specified encoding.

Stream format for the stream segmenter must be MPEG elementary audio and video streams, wrapped in an MPEG-2 transport stream, and using the following encoding. The Audio Technologies and Video Technologies list supported compression formats.

- Encode video using H.264 compression

  - H.264 Baseline 3.0: All devices
  - H.264 Baseline 3.1: iPhone 3G and later, and iPod touch 2nd generation and later.
  - H.264 Main profile 3.1: iPad (all versions), Apple TV 2 and later, and iPhone 4 and later.
  - H.264 Main Profile 4.0: Apple TV 3 and later, iPad 2 and later, and iPhone 4S and later
  - H.264 High Profile 4.0: Apple TV 3 and later, iPad 2 and later, and iPhone 4S and later.
  - H.264 High Profile 4.1: iPad 2 and later and iPhone 4S and later.
- A frame rate of 10 fps is recommended for video streams under 200 kbps. For video streams under 300 kbps, a frame rate of 12 to 15 fps is recommended. For all other streams, a frame rate of 29.97 is recommended.
- Encode audio as either of the following:

  - HE-AAC or AAC-LC, stereo
  - MP3 (MPEG-1 Audio Layer 3), stereo
- Optionally include an AC-3 audio track for Apple TV (or AirPlay to an Apple TV) when used with a surround sound receiver or TV that supports AC-3 input.
- A minimum audio sample rate of 22.05 kHz and audio bit rate of 40 kbps is recommended in all cases, and higher sampling rates and bit rates are strongly encouraged when streaming over Wi-Fi.

__Table 2-1__  Baseline profile encoder settings, 16:9 aspect ratio

| Connection | Dimensions | Total  bit rate | Video  bit rate | Keyframes |
| Cellular | 400 x 224 | 64 kbps | audio only | none |
| Cellular | 400 x 224 | 150 kbps | 110 kbps | 30 |
| Cellular | 400 x 224 | 240 kbps | 200 kbps | 45 |
| Cellular | 400 x 224 | 440 kbps | 400 kbps | 90 |
| WiFi | 640 x 360 | 640 kbps | 600 kbps | 90 |

__Table 2-2__  Baseline profile encoder settings, 4:3 aspect ratio

| Connection | Dimensions | Total  bit rate | Video  bit rate | Keyframes |
| Cellular | 400 x 300 | 64 kbps | audio only | none |
| Cellular | 400 x 300 | 150 kbps | 110 kbps | 30 |
| Cellular | 400 x 300 | 240 kbps | 200 kbps | 45 |
| Cellular | 400 x 300 | 440 kbps | 400 kbps | 90 |
| WiFi | 640 x 480 | 640 kbps | 600 kbps | 90 |

__Table 2-3__  Additional main profile encoder settings, 16:9 aspect ratio

| Connection | Dimensions | Total  bit rate | Video  bit rate | Keyframes |
| WiFi | 640 x 360 | 1240 kbps | 1200 kbps | 90 |
| WiFi | 960 x 540 | 1840 kbps | 1800 kbps | 90 |
| WiFi | 1280 x 720 | 2540 kbps | 1500 kbps | 90 |
| WiFi | 1280 x 720 | 4540 kbps | 4500 kbps | 90 |

__Table 2-4__  Additional main profile encoder settings, 4:3 aspect ratio

| Connection | Dimensions | Total  bit rate | Video  bit rate | Keyframes |
| WiFi | 640 x 480 | 1240 kbps | 1200 kbps | 90 |
| WiFi | 960 x 720 | 1840 kbps | 1800 kbps | 90 |
| WiFi | 960 x 720 | 2540 kbps | 2500 kbps | 90 |
| WiFi | 1280 x 960 | 4540 kbps | 4500 kbps | 90 |

__Table 2-5__  Additional high profile encoder settings, 16:9 aspect ratio

| Connection | Dimensions | Total  bit rate | Video  bit rate | Keyframes |
| WiFi | 1920 x 1080 | 12000 kbps | 11000 kbps | 90 |
| WiFi | 1920 x 1080 | 25000 kbps | 24000 kbps | 90 |
| WiFi | 1920 x 1080 | 40000 kbps | 39000 kbps | 90 |

There are a series of HTTP streams available for testing on Apple’s developer site. These examples show proper formatting of HTML to embed streams, `.M3U8` files to index the streams, and `.ts` media segment files. The streams can be accessed from the [HTTP Live Streaming Resources](https://developer.apple.com/streaming/).

[Next](Deploying%20HTTP%20Live%20Streaming.md)[Previous](HTTP%20Streaming%20Architecture.md)

