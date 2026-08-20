---
title: Resolving App Store Approval Issues for HTTP Live Streaming
apple_id: DTS40012622
resource_type: QA
platform: iOS
topic: Networking, Internet, & Web
technology: CoreMedia
published: '2015-03-25'
source_url: https://developer.apple.com/library/archive/qa/qa1767/_index.html
archived_at: '2026-07-27T06:57:05.093495Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1767

# Resolving App Store Approval Issues for HTTP Live Streaming

## Q:  My Application was rejected with the "HTTP Live Streaming rejection 9.4". What does this mean and where can I find information about correctly authoring my live streams for approval?

A: The Rejection 9.4 - HTTP Live Streaming rejection notice specifically states:

```
"Video streaming content over a cellular network longer than 10 minutes must use HTTP Live Streaming and include a baseline 192 kbps or lower HTTP Live stream."
```

__Note:__ Audio-only streams need only comply with App Store Review Guideline 9.3 which states:

"Audio streaming content over a cellular network may not use more than 5MB over 5 minutes".

When streaming video content over a __cellular__ network with a duration lasting longer than 10 minutes, your application __must__ use HTTP Live Streaming. When authoring your content for HTTP Live Streaming over __cellular__, you __must provide a baseline stream with a maximum measured bitrate of 192 kbps__ in addition to any other higher bitrate streams.

__Note:__ If you cannot provide video of acceptable quality at 192 kbps or lower, you should provide an audio-only stream, or audio with a still image.

Your application will be rejected with the 9.4 notice if:

- You are not using HTTP Live Streaming when streaming video longer than 10 minutes in duration over a cellular network connection.
- HTTP Live Streaming is being used for cellular but you did not provide a up to 192 kbps maximum stream.
- The stream you are providing for cellular exceeds the maximum 192 kbps requirement.

The recommended way to test the validity of your streams is to use the Media Stream Validator tool to validate your HTTP Live Streaming streams and servers. This tool verifies that the index file and media segments conform to the HTTP Live Streaming specification. It performs several checks to ensure reliable streaming. If any errors or problems are found, a detailed diagnostic report is displayed.

If you are an iOS or Mac Developer Program member you can download the latest version of the Media Stream Validator from the Apple Developer Connection website. To download, go to [Apple Developer Downloads](https://developer.apple.com/downloads/index.action?=http%20) (http://developer.apple.com/downloads/), in the search field type 'HTTP Live Streaming Tools', download and install the 'HTTP Live Streaming Tools'.

See [Media Stream Validator Tool Results Explained](https://developer.apple.com/library/ios/#technotes/tn2235/_index.html) for details discussing any error message that may be returned from the Media Stream Validator tool.

__Note:__ As the baseline 192 kbps maximum HTTP Live Streaming requirement is specifically for streaming over a cellular network, if your application is self-restricting to Wi-Fi only HTTP Live Streaming and you choose to not supply a baseline 192 kbps stream, you must provide this information to the App Review team. Developers can include this information in the __Review Notes__ field for your application.

Information about the Review Notes field can be found in the [Adding New Apps](https://developer.apple.com/library/ios/#documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/8_AddingNewApps/AddingNewApps.html#//apple_ref/doc/uid/TP40011225-CH13-SW1) section of the iTunes Connect Developer Guide.

For recommended encoding settings to use when creating HTTP Live Streaming media for iPhone and iPad apps, and for Safari on iOS see [Best Practices for Creating and Deploying HTTP Live Streaming Media for iPhone and iPad](https://developer.apple.com/library/ios/#technotes/tn2224/_index.html). This Techincal Note also provides tips for creating variant playlists, highlights some special considerations for deploying your media content to a web server and discusses how to validate your media streams.

If you are looking for information discussing streaming audio or video to iPhone, iPod touch, iPad, or Apple TV, streaming live events without special server software, sending video on demand with encryption and authentication see the [HTTP Live Streaming Overview](https://developer.apple.com/library/ios/#documentation/networkinginternet/conceptual/streamingmediaguide/Introduction/Introduction.html) for a complete overview of the HTTP Live Streaming technology.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-25 | Updated to reflect current App Store Review Guidelines. |
| 2014-07-08 | Updated to reflect current App Store Review Guidelines. Added information about audio-only streams. |
| 2012-08-07 | New document that discusses how to resolve App Store approval issues when using HTTP Live Streaming. |
