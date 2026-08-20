---
title: HTTP Live Streaming Overview
apple_id: TP40008332
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/HTTPStreamingArchitecture/HTTPStreamingArchitecture.html
archived_at: '2026-07-15T08:19:13.359504Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HTTP Live Streaming Overview](Introduction.md)


[Next](Using%20HTTP%20Live%20Streaming.md)[Previous](Introduction.md)

# HTTP Streaming Architecture

HTTP Live Streaming allows you to send live or prerecorded audio and video, with support for encryption and authentication, from an ordinary web server to any device running iOS 3.0 or later (including iPad and Apple TV), or any computer with Safari 4.0 or later installed.

Conceptually, HTTP Live Streaming consists of three parts: the server component, the distribution component, and the client software.

The __server component__ is responsible for taking input streams of media and encoding them digitally, encapsulating them in a format suitable for delivery, and preparing the encapsulated media for distribution.

The __distribution component__ consists of standard web servers. They are responsible for accepting client requests and delivering prepared media and associated resources to the client. For large-scale distribution, edge networks or other content delivery networks can also be used.

The __client software__ is responsible for determining the appropriate media to request, downloading those resources, and then reassembling them so that the media can be presented to the user in a continuous stream. Client software is included on iOS 3.0 and later and computers with Safari 4.0 or later installed.

In a typical configuration, a hardware encoder takes audio-video input, encodes it as H.264 video and AAC audio, and outputs it in an MPEG-2 Transport Stream, which is then broken into a series of short media files by a software stream segmenter. These files are placed on a web server. The segmenter also creates and maintains an index file containing a list of the media files. The URL of the index file is published on the web server. Client software reads the index, then requests the listed media files in order and displays them without any pauses or gaps between segments.

An example of a simple HTTP streaming configuration is shown in Figure 1-1.

__Figure 1-1__  A basic configuration

!!

Input can be live or from a prerecorded source. It is typically encoded as MPEG-4 (H.264 video and AAC audio) and packaged in an MPEG-2 Transport Stream by off-the-shelf hardware. The MPEG-2 transport stream is then broken into segments and saved as a series of one or more `.ts` media files. This is typically accomplished using a software tool such as the Apple stream segmenter.

Audio-only streams can be a series of MPEG elementary audio files formatted as AAC with ADTS headers, as MP3, or as AC-3.

The segmenter also creates an index file. The index file contains a list of media files. The index file also contains metadata. The index file is an `.M3U8` playlist. The URL of the index file is accessed by clients, which then request the indexed files in sequence.

The server requires a media encoder, which can be off-the-shelf hardware, and a way to break the encoded media into segments and save them as files, which can either be software such as the media stream segmenter provided by Apple or part of an integrated third-party solution.

The media encoder takes a real-time signal from an audio-video device, encodes the media, and encapsulates it for transport. Encoding should be set to a format supported by the client device, such as H.264 video and HE-AAC audio. Currently, the supported delivery format is MPEG-2 Transport Streams for audio-video, or MPEG elementary streams for audio-only.

The encoder delivers the encoded media in an MPEG-2 Transport Stream over the local network to the stream segmenter. MPEG-2 transport streams should not be confused with MPEG-2 video compression. The transport stream is a packaging format that can be used with a number of different compression formats. The Audio Technologies and Video Technologies list supported compression formats.

The stream segmenter is a process—typically software—that reads the Transport Stream from the local network and divides it into a series of small media files of equal duration. Even though each segment is in a separate file, video files are made from a continuous stream which can be reconstructed seamlessly.

The segmenter also creates an index file containing references to the individual media files. Each time the segmenter completes a new media file, the index file is updated. The index is used to track the availability and location of the media files. The segmenter may also encrypt each media segment and create a key file as part of the process.

Media segments are saved as `.ts` files (MPEG-2 transport stream files). Index files are saved as `.M3U8` playlists.

If you already have a media file encoded using supported codecs, you can use a file segmenter to encapsulate it in an MPEG-2 transport stream and break it into segments of equal length. The file segmenter allows you to use a library of existing audio and video files for sending video on demand via HTTP Live Streaming. The file segmenter performs the same tasks as the stream segmenter, but it takes files as input instead of streams.

The media segment files are normally produced by the stream segmenter, based on input from the encoder, and consist of a series of `.ts` files containing segments of an MPEG-2 Transport Stream carrying H.264 video and AAC, MP3, or AC-3 audio. For an audio-only broadcast, the segmenter can produce MPEG elementary audio streams containing either AAC audio with ADTS headers, MP3 audio, or AC-3 audio.

Index files are normally produced by the stream segmenter or file segmenter, and saved as `.M3U8` playlists, an extension of the `.m3u` format used for MP3 playlists.

Here is a very simple example of an index file, in the form of an `.M3U8` playlist, that a segmenter might produce if the entire stream were contained in three unencrypted 10-second media files:

```
#EXT-X-VERSION:3
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:1

# Old-style integer duration; avoid for newer clients.
#EXTINF:10,
http://media.example.com/segment0.ts

# New-style floating-point duration; use for modern clients.
#EXTINF:10.0,
http://media.example.com/segment1.ts
#EXTINF:9.5,
http://media.example.com/segment2.ts
#EXT-X-ENDLIST
```

For maximum accuracy, you should specify all durations as floating-point values when sending playlists to clients that support version 3 of the protocol or later. (Older clients support only integer values.) You must specify a protocol version when using floating-point lengths; if the version is omitted, the playlist must conform to version 1 of the protocol.

The index file may also contain URLs for encryption key files and alternate index files for different bandwidths. For details of the index file format, see the IETF Internet-Draft of the [HTTP Live Streaming specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming).

Index files are normally created by the same segmenter that creates the media segment files. Alternatively, it is possible to create the `.M3U8` file and the media segment files independently, provided they conform the published specification. For audio-only broadcasts, for example, you could create an `.M3U8` file using a text editor, listing a series of existing `.MP3` files.

The distribution system is a web server or a web caching system that delivers the media files and index files to the client over HTTP. No custom server modules are required to deliver the content, and typically very little configuration is needed on the web server.

Recommended configuration is typically limited to specifying MIME-type associations for `.M3U8` files and `.ts` files.

For details, see [Deploying HTTP Live Streaming](Deploying%20HTTP%20Live%20Streaming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmrnknltg).

The client software begins by fetching the index file, based on a URL identifying the stream. The index file in turn specifies the location of the available media files, decryption keys, and any alternate streams available. For the selected stream, the client downloads each available media file in sequence. Each file contains a consecutive segment of the stream. Once it has a sufficient amount of data downloaded, the client begins presenting the reassembled stream to the user.

The client is responsible for fetching any decryption keys, authenticating or presenting a user interface to allow authentication, and decrypting media files as needed.

This process continues until the client encounters the `#EXT-X-ENDLIST` tag in the index file. If no `#EXT-X-ENDLIST` tag is present, the index file is part of an ongoing broadcast. During ongoing broadcasts, the client loads a new version of the index file periodically. The client looks for new media files and encryption keys in the updated index and adds these URLs to its queue.

[Next](Using%20HTTP%20Live%20Streaming.md)[Previous](Introduction.md)

