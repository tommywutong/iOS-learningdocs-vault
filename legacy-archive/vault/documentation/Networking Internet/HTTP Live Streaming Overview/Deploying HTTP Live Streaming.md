---
title: HTTP Live Streaming Overview
apple_id: TP40008332
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/DeployingHTTPLiveStreaming/DeployingHTTPLiveStreaming.html
archived_at: '2026-07-15T08:19:13.337798Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HTTP Live Streaming Overview](Introduction.md)


[Next](Frequently%20Asked%20Questions.md)[Previous](Using%20HTTP%20Live%20Streaming.md)

# Deploying HTTP Live Streaming

To actually deploy HTTP Live Streaming, you need to create either an HTML page for browsers or a client app to act as a receiver. You also need the use of a web server and a way to either encode live streams as MPEG-2 transport streams or to create MP3 or MPEG-4 media files with H.264 and AAC encoding from your source material.

You can use the Apple-provided tools to segment the streams or media files, and to produce the index files and variant playlists (see [Download the Tools](Using%20HTTP%20Live%20Streaming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzt)).

You should use the Apple-provided media stream validator prior to serving your streams, to ensure that they are fully compliant with HTTP Live Streaming.

You may want to encrypt your streams, in which case you probably also want to serve the encryption key files securely over HTTPS, so that only your intended clients can decrypt them.

The easiest way to distribute HTTP Live Streaming media is to create a webpage that includes the HTML5 `<video>` tag, using an `.M3U8` playlist file as the video source. An example is shown in Listing 3-1.

__Listing 3-1__  Serving HTTP Live Streaming in a webpage

```
<html>
<head>
    <title>HTTP Live Streaming Example</title>
</head>
<body>
    <video
        src="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8"
        height="300" width="400"
    >
    </video>
</body>
</html>
```

For browsers that don’t support the HTML5 `video` element, or browsers that don’t support HTTP Live Streaming, you can include fallback code between the `<video>` and `</video>` tags. For example, you could fall back to a progressive download movie or an RTSP stream using the QuickTime plug-in. See _[Safari HTML5 Audio and Video Guide](../../Audio%20Video/Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_ for examples.

HTTP Live Streaming can be served from an ordinary web server; no special configuration is necessary, apart from associating the MIME types of the files being served with their file extensions.

Configure the following MIME types for HTTP Live Streaming:

|  |  |
| --- | --- |
| __File Extension__ | __MIME Type__ |
| `.M3U8` | `application/x-mpegURL` or  `vnd.apple.mpegURL` |
| `.ts` | `video/MP2T` |

If your web server is constrained with respect to MIME types, you can serve files ending in `.m3u` with MIME type `audio/mpegURL` for compatibility.

Index files can be long and may be frequently redownloaded, but they are text files and can be compressed very efficiently. You can reduce server overhead by enabling on-the-fly `.gzip` compression of `.M3U8` index files; the HTTP Live Streaming client automatically unzips compressed index files.

Shortening time-to-live (TTL) values for `.M3U8` files may also be needed to achieve proper caching behavior for downstream web caches, as these files are frequently overwritten during live broadcasts, and the latest version should be downloaded for each request. Check with your content delivery service provider for specific recommendations. For VOD, the index file is static and downloaded only once, so caching is not a factor.

The `mediastreamvalidator` tool is a command-line utility for validating HTTP Live Streaming streams and servers (see [Download the Tools](Using%20HTTP%20Live%20Streaming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmzsfvbuqmjqgiwvgvzt) for details on obtaining the tool).

The media stream validator simulates an HTTP Live Streaming session and verifies that the index file and media segments conform to the HTTP Live Streaming specification. It performs several checks to ensure reliable streaming. If any errors or problems are found, a detailed diagnostic report is displayed.

You should always run the validator prior to serving a new stream or alternate stream set.

The media stream validator shows a listing of the streams you provide, followed by the timing results for each of those streams. (It may take a few minutes to calculate the actual timing.) An example of validator output follows.

```
$ mediastreamvalidator -d iphone http://devimages.apple.com/iphone/samples/bipbop/gear3/prog_index.m3u8
mediastreamvalidator: Beta Version 1.1(130423)

Validating http://devimages.apple.com/iphone/samples/bipbop/gear3/prog_index.m3u8

--------------------------------------------------------------------------------
http://devimages.apple.com/iphone/samples/bipbop/gear3/prog_index.m3u8
--------------------------------------------------------------------------------

Playlist Syntax:     OK

Segments:    OK

Average segment duration: 9.91 seconds
Segment bitrate: Average: 509.56 kbits/sec, Max: 840.74 kbits/sec
Average segment structural overhead: 97.49 kbits/sec (19.13 %)
```

For more information, read _[Media Stream Validator Tool Results Explained](https://developer.apple.com/library/archive/technotes/tn2235/_index.html#//apple_ref/doc/uid/DTS40010221)_.

You can protect your media by encrypting it. The file segmenter and stream segmenter both have encryption options, and you can tell them to change the encryption key periodically. Who you share the keys with is up to you.

Key files require an initialization vector (IV) to decode encrypted media. The IVs can be changed periodically, just as the keys can. Current recommendations for encrypting media while minimizing overhead is to change the key every 3-4 hours and change the IV after every 50 Mb of data.

Even with restricted access to keys, however, it is possible for an eavesdropper to obtain copies of the key files if they are sent over HTTP. One solution to this problem is to send the keys securely over HTTPS.

Before you attempt to serve key files over HTTPS, you should do a test serving the keys from an internal web server over HTTP. This allows you to debug your setup before adding HTTPS to the mix. Once you have a known working system, you are ready to make the switch to HTTPS.

There are three conditions you must meet in order to use HTTPS to serve keys for HTTP Live Streaming:

- You need to install an SSL certificate signed by a trusted authority on your HTTPS server.
- The authentication domain for the key files must be the same as the authentication domain for the first playlist file. The simplest way to accomplish this is to serve the variant playlist file from the HTTPS server—the variant playlist file is downloaded only once, so this shouldn’t cause an excessive burden. Other playlist files can be served using HTTP.
- You must either initiate your own dialog for the user to authenticate, or you must store the credentials on the client device—HTTP Live Streaming does not provide user dialogs for authentication. If you are writing your own client app, you can store credentials, whether cookie-based or HTTP digest based, and supply the credentials in the `didReceiveAuthenticationChallenge` callback (see Using NSURLConnection and Authentication Challenges and TLS Chain Validation for details). The credentials you supply are cached and reused by the media player.

If your HTTPS server does not have an SSL certificate signed by a trusted authority, you can still test your setup by creating a self-signed SSL Certificate Authority and a leaf certificate for your server. Attach the certificate for the certificate authority to an email, send it to a device you want to use as a Live Streaming client, and tap on the attachment in Mail to make the device trust the server.

A sample-level encryption format is documented in _[MPEG-2 Stream Encryption Format for HTTP Live Streaming](../../Audio%20Video/MPEG-2%20Stream%20Encryption%20Format%20for%20HTTP%20Live%20Streaming/1.0%20Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnrs)_.

[Next](Frequently%20Asked%20Questions.md)[Previous](Using%20HTTP%20Live%20Streaming.md)

