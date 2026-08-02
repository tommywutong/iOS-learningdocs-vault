---
title: Example Playlist Files for use with HTTP Live Streaming
apple_id: DTS40012238
resource_type: Technical Note
platform: Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: CoreMedia
published: '2012-05-09'
source_url: https://developer.apple.com/library/archive/technotes/tn2288/_index.html
archived_at: '2026-07-26T19:54:10.252269Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2288

# Example Playlist Files for use with HTTP Live Streaming

This technote describes several example playlist files that can be used to stream multimedia data with HTTP Live Streaming.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvke4vcbi4yq)[Basic Video on Demand (VOD) Playlist](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvke4vcbi4za)[Live Playlist (Sliding Window)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvke4vcbi4zq)[Event Playlist](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvcvmrkokrpvatcblfgesu2u)[Basic Variant Playlist](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvbecu2jinpvmqksjfau4vc7kbgecwkmjfjvi)[Ad Playlist (Discontinuities)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvauix2qjravstcjknkf6x2ejfjugt2okreu4vkjkreuku27)[Encryption Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvcu4q2slfifi)[Alternate Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvauyvcfkjhecvcfl5gukrcjie)[Byte-Range Support for Segments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvbfsvcfl5jectshivpvgvkqkbhvevc7izhvex2tivdu2rkokrjq)[I-Frame Playlist](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvev6rssifgukx2qjravstcjknka)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

HTTP Live Streaming sends audio and video as a series of small files, typically of about 10 seconds duration, called media segment files. An index file, or playlist, provides an ordered list of the URLs of the media segment files. Index files for HTTP Live Streaming are saved as `.m3u8` playlists, an extension of the `.m3u` format used for MP3 playlists. The URL of the index file is accessed by clients, which then request the indexed files in sequence.

This technote describes several different types of playlist files that can be used to stream multimedia data with HTTP Live Streaming.

For complete information about the HTTP Live Streaming Protocol and the playlist information presented in this technote, see the [IETF Internet-Draft of the HTTP Live Streaming specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming).

See also the [HTTP Live Streaming Overview](https://developer.apple.com/library/ios/#documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html) for more information about HTTP Live Streaming.

You can use the Apple HTTP Live Streaming tools to generate playlists. These tools are frequently updated, so you should make sure and download the current version. You can access them if you are a member of the iPhone Developer Program. Simply log onto the [Apple Developer website](http://www.apple.com), then search the Downloads area.

[Back to Top](#)

## Basic Video on Demand (VOD) Playlist

For Video on Demand (VOD) sessions, media files are available representing the entire duration of the presentation. The index file is static and contains a complete list of URLs to all media files created since the beginning of the presentation. This kind of session allows the client full access to the entire program. See the example VOD playlist in Listing 1.

__Listing 1__  Video on Demand (VOD) Playlist.

```
#EXTM3U
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
http://example.com/movie1/fileSequenceA.ts
#EXTINF:10.0,
http://example.com/movie1/fileSequenceB.ts
#EXTINF:10.0,
http://example.com/movie1/fileSequenceC.ts
#EXTINF:9.0,
http://example.com/movie1/fileSequenceD.ts
#EXT-X-ENDLIST
```

Here's a description of the tags used in the example Video on Demand playlist:

The Extended M3U file format defines two tags: `EXTM3U` and `EXTINF`. An Extended M3U file is distinguished from a basic M3U file by its first line, which must be `EXTM3U`.

`EXTINF` is a record marker that describes the media file identified by the URL that follows it. Each media file URL must be preceded by an `EXTINF` tag. The `EXTINF` tag contains a "duration" attribute that is an integer or floating-point number in decimal positional notation that specifies the duration of the media segment in seconds.

The EXT-X-PLAYLIST-TYPE tag provides mutability information about the playlist file. It applies to the entire playlist file. This tag may contain a value of either EVENT or VOD. If the tag is present and has a value of EVENT, the server __must not__ change or delete any part of the playlist file (although it __may__ append lines to it). If the tag is present and has a value of VOD, the playlist file __must not__ change.

__Important:__ Always use floating point `EXTINF` durations (supported in protocol version 3). This will allow the client to minimize round-off errors when seeking within the stream. Use the `EXT-X-VERSION` tag to indicate the compatibility version of your playlist file when specifying floating point `EXTINF` durations (older clients that don't recognize the `EXT-X-VERSION` tag will just treat it as a comment, and treat the playlist as version 1).

Each media file URL in a playlist has a unique integer sequence number. The sequence number of a URL is equal to the sequence number of the URL that preceded it plus one. The `EXT-X-MEDIA-SEQUENCE` tag indicates the sequence number of the first URL that appears in a playlist file.

The `EXT-X-TARGETDURATION` tag specifies the maximum media file duration.

The `EXT-X-VERSION` tag indicates the compatibility version of the playlist file. The playlist media, and its server __must__ comply with all provisions of the most-recent version of the [IETF Internet-Draft of the HTTP Live Streaming specification](http://tools.ietf.org/html/draft-pantos-http-live-streaming) that defines that protocol version.

The `EXT-X-ENDLIST` tag indicates that no more media files will be added to the playlist file.

__Important:__ Notice the VOD playlist in Listing 1 uses full path names for the media file playlist entries. While this is allowed, it is recommend that relative paths are used instead. Relative path names are more portable than absolute path names. Using full path names for the individual playlist entries most often uses more text than using a relative path name. In the case of a very long VOD playlist, or a very long duration Live playlist, this can create a significant file size difference in the playlist file itself, increasing the download time of the playlist files.

Here's the same playlist with relative path names.

__Listing 2__  Video on Demand Playlist with Relative Path Names.

```
#EXTM3U
#EXT-X-PLAYLIST-TYPE:VOD
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
fileSequenceA.ts
#EXTINF:10.0,
fileSequenceB.ts
#EXTINF:10.0,
fileSequenceC.ts
#EXTINF:9.0,
fileSequenceD.ts
#EXT-X-ENDLIST
```

[Back to Top](#)

## Live Playlist (Sliding Window)

For live sessions, the index file is updated by removing media URIs from the file as new media files are created and made available.

__Important:__ The `EXT-X-ENDLIST` tag is __not__ present in the Live playlist, indicating that new media files will be added to the index file as they become available.

See Listing 3 for an example live playlist as it would appear at the beginning of a session.

__Listing 3__  Live Playlist at the beginning of a session.

```
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:1
#EXTINF:10,
fileSequence1.ts
#EXTINF:10,
fileSequence2.ts
#EXTINF:10,
fileSequence3.ts
#EXTINF:10,
fileSequence4.ts
#EXTINF:10,
fileSequence5.ts
```

The `EXT-X-MEDIA-SEQUENCE` tag value MUST be incremented by 1 for every media `URI` that is removed from the playlist file. Media URIs __must__ be removed from the playlist file in the order that they appear in the playlist. The updated index file presents a moving window into a continuous stream. This type of session is suitable for continuous broadcasts.

Here's the same playlist after it has been updated with new media URIs:

__Listing 4__  Live Playlist after updating the media URIs.

```
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:2
#EXTINF:10,
fileSequence2.ts
#EXTINF:10,
fileSequence3.ts
#EXTINF:10,
fileSequence4.ts
#EXTINF:10,
fileSequence5.ts
#EXTINF:10,
fileSequence6.ts
```

[Back to Top](#)

## Event Playlist

An event playlist is specified by the EXT-X-PLAYLIST-TYPE tag with a value of `EVENT`. An event playlist looks just like a live playlist to start out with. It doesn't initially have an `EXT-X-ENDLIST` tag, indicating that new media files will be added to the playlist as they become available.

__Listing 5__  Event Playlist (start).

```
#EXTM3U
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10,
fileSequence0.ts
#EXTINF:10,
fileSequence1.ts
#EXTINF:10,
fileSequence2.ts
#EXTINF:10,
fileSequence3.ts
#EXTINF:10,
fileSequence4.ts
```

However, with the `EVENT` tag, you cannot change the playlist at all; you may only append new segments to the end of the file. They cannot be added at the front. New segments are added until the event has concluded, at which time the `EXT-X-ENDLIST` tag is appended.

__Listing 6__  Event Playlist (finish).

```
#EXTM3U
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10,
fileSequence0.ts
#EXTINF:10,
fileSequence1.ts
#EXTINF:10,
fileSequence2.ts
#EXTINF:10,
fileSequence3.ts
#EXTINF:10,
fileSequence4.ts
...
#EXTINF:10,
fileSequence120.ts
#EXTINF:10,
fileSequence121.ts
#EXT-X-ENDLIST
```

As the name implies, event playlists are typically used for events such as concerts or sports games where you want to allow the user to seek anywhere in the event from the beginning.

If you are delivering an event like this, you will probably want to protect your content. See [Encryption Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvcu4q2slfifi) to learn about using encryption with your media files.

[Back to Top](#)

## Basic Variant Playlist

You may offer multiple playlist files to provide different encodings of the same presentation. See Listing 7.

A variant is a version of the stream at a particular bit rate. Each variant is a separate playlist. The variant playlist describes all of the available variants. The client will switch to most appropriate variant based on the measured network bit rate. The client’s player is tuned to minimize stalling of playback in order to give the user the best experience possible when streaming.

__Note:__ A variant playlist is not re-read. Once the client has read the variant playlist, it assumes the set of variations isn't changing. As soon as the client sees the endlist tag on one of the individual variant, that ends the stream.

The `EXT-X-STREAM-INF` tag indicates that the next URL in the playlist file identifies another playlist file.

The following attributes are defined:

`BANDWIDTH`

The value is a decimal-integer of bits per second. It must be an upper bound of the overall bitrate of each media file, calculated to include container overhead, that appears or will appear in the playlist.

__Important:__ Every `EXT-X-STREAM-INF` tag __must__ include the `BANDWIDTH` attribute.

`PROGRAM-ID`

The value is a decimal-integer that uniquely identifies a particular presentation within the scope of the playlist file.

A playlist file may contain multiple `EXT-X-STREAM-INF` tags with the same `PROGRAM-ID` to identify different encodings of the same presentation. These variant playlists may contain additional EXT-X- `STREAM-INF` tags.

`CODECS`

The value is a quoted-string containing a comma-separated list of formats, where each format specifies a media sample type that is present in a media segment in the Playlist file. Valid format identifiers are those in the ISO File Format Name Space defined by [RFC 6381 [RFC6381]](http://tools.ietf.org/html/rfc6381).

__Important:__ Every `EXT-X-STREAM-INF` tag __should__ include a `CODECS` attribute. This attribute provides a complete list of codecs that are necessary to decode a particular stream. It allows the client to distinguish between variants that are audio only, and those that have both audio and video. The client can then make use of this information to provide a better user experience when switching streams.

__Note:__ In this and the following examples, a '\' is used to indicate that the tag continues on the following line with whitespace removed:

__Listing 7__  Basic Variant Playlist.

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=150000,RESOLUTION=416x234, \
CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/low/index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=240000,RESOLUTION=416x234, \
CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/lo_mid/index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=440000,RESOLUTION=416x234, \
CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/hi_mid/index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=640000,RESOLUTION=640x360, \
CODECS="avc1.42e00a,mp4a.40.2"
http://example.com/high/index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=64000,CODECS="mp4a.40.5"
http://example.com/audio/index.m3u8
```

[Back to Top](#)

## Ad Playlist (Discontinuities)

Often you'll want to deliver a whole series of movies with some sort of branding (advertisement) displayed in front of each one to let the user know these are originating from your particular site. One way to do this is to simply merge the ad with each movie. But if you have hundreds of movies that's a lot of re-encoding to do, plus you'll be duplicating the ad with each movie.

You could just deliver the ad as one movie, and then play the next movie. The problem is you will get drops in quality when transitioning from the ad to the movie. For example, the ad will start playing with a low data rate to ensure the client is able to read it, then gradually ramp up to provide the best possible playback experience. When the ad finishes playing, the movie will start at a low data rate (just as the ad did) and ramp up, and you will experience a break in quality. Furthermore, if you display the ad in the middle of the movie you will get drops in quality as you go along.

The solution is to let the client know there is a change coming. This is accomplished with the `EXT-X-DISCONTINUITY` tag. The `EXT-X-DISCONTINUITY` tag indicates an encoding discontinuity between the media file that follows it and the one that preceded it.

Here is an example of a stream that uses a `EXT-X-DISCONTINUITY` tag to play some movies that are preceded by an 18s ad (segments `ad0.ts` and `ad1.ts`):

__Listing 8__  Ad example Playlist.

```
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
ad0.ts
#EXTINF:8.0,
ad1.ts
#EXT-X-DISCONTINUITY
#EXTINF:10.0,
movieA.ts
#EXTINF:10.0,
movieB.ts
```

[Back to Top](#)

## Encryption Keys

Media files may be encrypted to control who has access to them. To do so, first encrypt your media, then tag the encrypted media segments in the playlist with a `EXT-X-KEY` tag. The `EXT-X-KEY` tag provides information necessary to decrypt media files that follow it. It supports two different encryption methods, `NONE` and `AES-128`.

The `EXT-X-KEY` tag may contain an Initialization Vector (`IV`) attribute. The Initialization Vector attribute, if present, specifies the Initialization Vector to be used with the key. Its value is a hexadecimal-integer. Varying this Initialization Vector increases the strength of the cipher.

The default Initialization Vector for media encryption (if none is specified) is the sequence number of the media file. You should specify an Initialization Vector value, and not rely on sequence numbers. The main reason for this is portability. For example, if you change where the segment appears in the playlist (e.g. inserting an ad), that changes its sequence number, requiring a re-encrypt.

__Note:__ The Initialization Vector attribute first appeared in protocol version 2, and is not compatible with previous versions of the protocol. Use the `EXT-X-VERSION` tag to indicate the compatibility version of your playlist file when specifying an Initialization Vector.

Here's the same Ad playlist example from Listing 8 but with encryption and an Initialization Vector added for the media using the `EXT-X-KEY` tag.

__Listing 9__  Ad example Playlist with Encryption Keys and Initialization Vector.

```
#EXTM3U
#EXT-X-TARGETDURATION:10
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=52",  \
IV=0x9c7db8778570d05c3177c349fd9236aa
#EXTINF:10.0,
bumper0.ts
#EXTINF:8.0,
bumper1.ts
#EXT-X-DISCONTINUITY
#EXT-X-KEY:METHOD=AES-128,URI="https://priv.example.com/key.php?r=53",  \
IV=0xc055ee9f6c1eb7aa50bfab02b0814972
#EXTINF:10.0,
movieA.ts
#EXTINF:10.0,
movieB.ts
```

[Back to Top](#)

## Alternate Media

New in iOS 5 is support for alternate media. This feature allows a provider to specify one of a set of variant playlists as an "override" of the main presentation. The client will only play the override media (audio or video), and suppress any media of the same type from the main presentation, if present. This allows a presentation to offer multiple versions of the media without requiring the provider to store duplicate media, or requiring the client download all variants when it only needs one. It also allows additional media to be offered subsequently without remastering the original content.

A new `EXT-X-MEDIA` tag has been defined for the variant playlist that identifies a media selection group. In addition, two new attributes have been defined for the `EXT-X-STREAM-INF` tag: `AUDIO` specifies the audio media group and `VIDEO` specifies the video media group. These define the media options available while playing the stream.

Each element in an media group must have similar characteristics (same `CODECS`, same max bandwidth).

A `STREAM-INF` variant can indicate that it offers a choice of audio (or video) with an `AUDIO` (or `VIDEO`) attribute. This value is a group-id shared by every `MEDIA` tag that can be chosen. If a `STREAM-INF` tag has an `AUDIO` (or `VIDEO`) attribute, it must also have a `CODECS` attribute.

The `EXT-X-MEDIA` tag can indicate that the media described is included in the `URI` of the `STREAM-INF` tag by omitting its `URI` attribute.

__Note:__ If one media alternate is carried in the `STREAM-INF` `URI` and the chosen alternate is not, both alternates may be downloaded.

If the `EXT-X-MEDIA` `AUTOSELECT` attribute tag value is YES, then the client __may__ choose to play this alternate in the absence of explicit user preference because it matches the current playback environment, such as chosen system language. Its absence indicates an implicit value of NO. This attribute is optional. If the `EXT-X-MEDIA` `DEFAULT` attribute tag value is YES, then the client __should__ play this alternate in the absence of information from the user indicating a different choice. This attribute is optional. Its absence indicates an implicit value of NO.

Here is an example of a variant playlist with three audio options:

__Listing 10__  Variant playlist with three audio options.

```
#EXTM3U
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="eng",NAME="English",AUTOSELECT=YES, \
DEFAULT=YES,URI="eng/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="fre",NAME="Français",AUTOSELECT=YES, \
DEFAULT=NO,URI="fre/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",LANGUAGE="sp",NAME="Espanol",AUTOSELECT=YES, \
DEFAULT=NO,URI="sp/prog_index.m3u8"

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=195023,CODECS="avc1.42e00a,mp4a.40.2",AUDIO="audio"
lo/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=591680,CODECS="avc1.42e01e,mp4a.40.2",AUDIO="audio"
hi/prog_index.m3u8
```

The `NAME` attribute of the `MEDIA` tag should be unique.

If desired, there could be multiple audio groups, to allow changes in codecs or bit rate. However, each audio group in a variant must have the exact same number of alternates in it.

For example, to provide a higher bit rate audio in the above example, the variant playlist would look like this:

__Listing 11__  Variant playlist with three audio options and multiple audio groups.

```
#EXTM3U
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-lo",LANGUAGE="eng",NAME="English",AUTOSELECT=YES, \
DEFAULT=YES,URI="englo/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-lo",LANGUAGE="fre",NAME="Français",AUTOSELECT=YES, \
DEFAULT=NO,URI="frelo/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-lo",LANGUAGE="sp",NAME="Espanol",AUTOSELECT=YES, \
DEFAULT=NO,URI="splo/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-hi",LANGUAGE="eng",NAME="English",AUTOSELECT=YES, \
DEFAULT=YES,URI="eng/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-hi",LANGUAGE="fre",NAME="Français",AUTOSELECT=YES, \
DEFAULT=NO,URI="fre/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio-hi",LANGUAGE="sp",NAME="Espanol",AUTOSELECT=YES, \
DEFAULT=NO,URI="sp/prog_index.m3u8"

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=195023,CODECS="mp4a.40.5", \
AUDIO="audio-lo"
lo/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=260000,CODECS="avc1.42e01e,mp4a.40.2", \
AUDIO="audio-lo"
hi/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=591680,CODECS="mp4a.40.2, avc1.64001e", \
AUDIO="audio-hi"
lo/prog_index.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=650000,CODECS="avc1.42e01e,mp4a.40.2", \
AUDIO="audio-hi"
hi/prog_index.m3u8
```

Note that each member of the media group must be replicated in each media group for that media type. For example, you could not leave out "`Espanol`" in the "`audio-hi`" group.

Alternate video can also be presented, for alternative angles. For example, this variant playlist describes a single bit rate with 3 different camera angles and a single audio stream:

__Listing 12__  Variant playlist with 3 different camera angles and a single audio stream.

```
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle1",AUTOSELECT=YES,DEFAULT=YES
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle2",AUTOSELECT=YES,DEFAULT=NO, \
URI="Angle2/500kbs/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle3",AUTOSELECT=YES,DEFAULT=NO, \
URI="Angle3/500kbs/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="eng",NAME="English",AUTOSELECT=YES, \
DEFAULT=YES,URI="eng/prog_index.m3u8"
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=754857,CODECS="mp4a.40.2,avc1.4d401e", \
VIDEO="500kbs",AUDIO="aac"
Angle1/500kbs/prog_index.m3u8
```

To produce a different bit rate, a different video group id would be needed for each bit rate.

__Listing 13__  Variant playlist with 3 different camera angles and different bit rates.

```
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="200kbs",NAME="Angle1",AUTOSELECT=YES,DEFAULT=YES
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="200kbs",NAME="Angle2",AUTOSELECT=YES,DEFAULT=NO, \
URI="Angle2/200kbs/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="200kbs",NAME="Angle3",AUTOSELECT=YES,DEFAULT=NO, \
URI="Angle3/200kbs/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle1",AUTOSELECT=YES,DEFAULT=YES
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle2",AUTOSELECT=YES,DEFAULT=NO, \
URI="Angle2/500kbs/prog_index.m3u8"
#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="500kbs",NAME="Angle3",AUTOSELECT=YES,DEFAULT=NO, \
URI="Angle3/500kbs/prog_index.m3u8"

#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="aac",LANGUAGE="eng",NAME="English",AUTOSELECT=YES, \
DEFAULT=YES,URI="eng/prog_index.m3u8"

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=300000,CODECS="mp4a.40.2,avc1.4d401e", \
VIDEO="200kbs",AUDIO="aac"
Angle1/200kbs/prog_index.m3u

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=754857,CODECS="mp4a.40.2,avc1.4d401e", \
VIDEO="500kbs",AUDIO="aac"
Angle1/500kbs/prog_index.m3u8
```

[Back to Top](#)

## Byte-Range Support for Segments

As discussed in the [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytemrthawugsbrfvke4vcbi4yq) section above, a playlist provides the clients with the URLs of the media segment files. Each media URL refers to a media file which is a segment of a single contiguous stream. This means if you have 700 media segments in your movie, you actually have 700 files on your webserver.

New in iOS 5, you can now specify a media segment as a byte range (subrange) of a larger URL. This allows you to consolidate your media segments into larger files or a single large file. The primary benefit of this is when a client is playing your media, rather than downloading each successive segment file from a different location, it is actually walking through a larger file in sequence.

This also allows proxy caching servers to get a much better idea of what needs to be prefetched in order to ensure that the segment you will need is in the cache at the time you want it. An additional benefit is there are far fewer files to manage. If you have many video variants in a long movie, you can have thousands of individual segment files. With byte range support, you only have a few.

__Important:__ Making byte range requests against non-static resources is unreliable over the public Internet. Even if your web server can handle it, your intermediary caching servers may not. For that reason, we recommend your media files for live content be static (of course they will always be static for video on demand content). It doesn't matter if they are very small or very large, just as long as you don't append to them after you start playing.

There is a new tag `EXT-X-BYTERANGE` to specify byte range media segments :

`#EXT-X-BYTERANGE: length[@offset]`

It specifies the length of the range. It must also specify the offset, unless the byte range also follows immediately from the previous byterange.

Here's an example of a playlist file. First, an old style playlist is shown with 3 segments, each with its own URL (a relative URL):

__Listing 14__  Old style playlist with 3 segments.

```
#EXTM3U
#EXT-X-VERSION:3
#EXTINF:10.0,
segment0.ts
#EXTINF:10.0,
segment1.ts
#EXTINF:10.0,
segment2.ts
```

Here's the same playlist rewritten to use byte range media segments. The playlist still has 3 segments, but these now range into a single media segment `media.ts`, and the byte range tag specifies the byte ranges that the segments are actually occupying.

__Important:__ Playlists that specify byte range media segments require protocol version 4. In addition, they __must__ include `EXT-X-TARGETDURATION` and `EXT-X-MEDIA-SEQUENCE` tags, and the media `URI` must reside on a separate line. Even if all segments come from a single resource, they must still be encrypted independently.

__Listing 15__  Playlist using byte range media segments.

```
#EXTM3U
#EXT-X-TARGETDURATION:11
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-VERSION:4
 #EXTINF:10.0,
#EXT-X-BYTERANGE:75232@0
media.ts
 #EXTINF:10.0,
#EXT-X-BYTERANGE:82112@752321
media.ts
 #EXTINF:10.0,
#EXT-X-BYTERANGE:69864
media.ts
```

[Back to Top](#)

## I-Frame Playlist

iOS 5 now supports Fast Forward and Reverse Playback. However, you don't need to produce special purpose content to support Fast Forward and Reverse Playback. All you need to do is specify where the I-Frames are. I-Frames, or Intra frames, are encoded video frames whose encoding does not depend on any other frame. To specify where the I-Frames are, iOS 5 introduces a new I-Frame only playlist.

The new `EXT-X-I-FRAMES-ONLY` tag indicates that each media segment in the playlist describes a single I-Frame.

An I-Frame only playlist is almost identical to a regular playlist. The only difference is that I-Frame playlists do not have an intrinsic duration. They instead represent an instant in time. In an I-Frame only playlist with the `EXT-X-I-FRAMES-ONLY` tag, the `EXTINF` tag duration actually refers to the "span" of the I-Frame. This is the time between the presentation time of the I-Frame in the media segment and the presentation time of the next I-Frame in the playlist (or the end of the presentation if it is the last I-frame in the playlist).

The `EXT-X-BYTERANGE` tag __must__ be used to identify the sub-range of the media resource containing the I-frame.

Here's an example of an I-Frame only playlist that specifies I-Frames in `segment1.ts` and `segment2.ts`:

__Note:__ I-Frame playlists require protocol version 4.

__Listing 16__  I-Frame Playlist.

```
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-I-FRAMES-ONLY
 ...
 #EXTINF:4.12,
#EXT-X-BYTERANGE:9400@376
segment1.ts
#EXTINF:3.56,
#EXT-X-BYTERANGE:7144@47000
segment1.ts
 #EXTINF:3.82,
#EXT-X-BYTERANGE:10340@1880
segment2.ts
```

A new `EXT-X-I-FRAME-STREAM-INF` tag has also been defined to identify a playlist file containing the I-frames of a multimedia presentation.

Its format is:

#`EXT-X-I-FRAME-STREAM-INF`:<attribute-list>

The `EXT-X-I-FRAME-STREAM-INF` tag does not apply to a particular `URI` in the playlist, it stands alone.

All attributes defined for the `EXT-X-STREAM-INF` tag are also defined for the `EXT-X-I-FRAME-STREAM-INF` tag, except for the AUDIO attribute. In addition, the following attribute is defined:

`URI`

The value is a quoted-string containing a `URI` that identifies the I-frame Playlist file.

Here is an example I-Frame playlist file that uses the `EXT-X-I-FRAME-STREAM-INF` tag.

__Listing 17__  I-Frame playlist that uses the EXT-X-I-FRAME-`STREAM-INF` tag.

```
#EXTM3U
#EXT-X-VERSION:4
#EXT-X-I-FRAME-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=80000,CODECS="avc1.42e00a,mp4a.40.2", \
URI="lo/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=200000,CODECS="avc1.42e00a,mp4a.40.2", \
URI="mid/iframes.m3u8"
#EXT-X-I-FRAME-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=380000,CODECS="avc1.42e00a,mp4a.40.2", \
URI="hi/iframes.m3u8"
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-05-09 | New document that provides examples of the different playlist files for use with HTTP Live Streaming. |

