---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/YouTubeLinks/YouTubeLinks.html
archived_at: '2026-07-18T02:29:23.465333Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Apple URL Scheme Reference](About%20Apple%20URL%20Schemes.md)


[Next](Document%20Revision%20History.md)[Previous](iTunes%20Links.md)

# YouTube Links

The YouTube URL scheme is used to connect to the YouTube website to play the specified video. If your app links to YouTube content, you can use this scheme to play videos from your app.

Unlike some schemes, YouTube URLs do not start with a “youtube” scheme identifier. Instead, they are specified as regular `http` links but are targeted at the YouTube server. The following examples show the basic strings you would use in Safari and in an app to show a YouTube video. In each example, you would need to replace the `VIDEO_IDENTIFIER` value with the identifier of the video you wanted to display:

- HTML links:

```
<a href="http://www.youtube.com/watch?v=VIDEO_IDENTIFIER">Play Video</a>
<a href="http://www.youtube.com/v/VIDEO_IDENTIFIER">Play Video</a>
```
- Native app URL strings:

```
http://www.youtube.com/watch?v=VIDEO_IDENTIFIER
http://www.youtube.com/v/VIDEO_IDENTIFIER
```

[Next](Document%20Revision%20History.md)[Previous](iTunes%20Links.md)

