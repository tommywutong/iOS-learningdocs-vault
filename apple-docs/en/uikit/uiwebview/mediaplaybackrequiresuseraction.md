---
title: mediaPlaybackRequiresUserAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（12.0 起废弃）, iPadOS 4.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/mediaplaybackrequiresuseraction
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/mediaplaybackrequiresuseraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/mediaplaybackrequiresuseraction.json'
content_hash: 'sha256:3e057abd3f101a5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# mediaPlaybackRequiresUserAction

<sub>Instance Property</sub>

A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var mediaPlaybackRequiresUserAction: Bool { get set }
```

## Discussion

The default value on both iPad and iPhone is [true](../../swift/true.md). To make media play automatically when loaded, set this property to [false](../../swift/false.md) and ensure the `<audio>` or `<video>` element you want to play has the `autoplay` attribute set.

## See Also

### Managing media playback

- [allowsInlineMediaPlayback](allowsinlinemediaplayback.md) — A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller. _(deprecated)_
- [mediaPlaybackAllowsAirPlay](mediaplaybackallowsairplay.md) — A Boolean value that determines whether Air Play is allowed from this view. _(deprecated)_
- [allowsPictureInPictureMediaPlayback](allowspictureinpicturemediaplayback.md) — A Boolean value that determines whether Picture in Picture playback is allowed from this view. _(deprecated)_
