---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/iTunesLinks/iTunesLinks.html
archived_at: '2026-07-18T02:29:23.497402Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Apple URL Scheme Reference](About%20Apple%20URL%20Schemes.md)


[Next](YouTube%20Links.md)[Previous](Map%20Links.md)

# iTunes Links

The iTunes URL scheme is used to link to content on the iTunes Music Store. The iTunes URL format is complicated to construct, so you create it using an online tool called iTunes Link Maker. The tool allows you to select a country destination and media type, and then search by song, album, or artist. After you select the item you want to link to, it generates the corresponding URL.

The following examples show the strings you would use in Safari and in a native iOS app to link to a song on the iTunes Music Store. The HTML example includes the complete link returned by the iTunes Link Maker tool, which includes a link to any appropriate artwork for the target link.

- HTML link:

```
<a href="http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewAlbum?i=156093464&id=156093462&s=143441">
<img height="15" width="61" alt="Randy Newman - Toy Story
- You&#39;ve Got a Friend In Me" src="http://ax.phobos.apple.com.edgesuite.net/images/
badgeitunes61x15dark.gif"></img>
</a>
```
- Native app URL string:

```
http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewAlbum?i=156093464&id=156093462&s=143441
```

For more information on creating iTunes links, see [iTunes Link Maker FAQ](http://www.apple.com/itunes/linkmaker/faq/). That webpage contains a link to the iTunes Link Maker tool.

[Next](YouTube%20Links.md)[Previous](Map%20Links.md)

