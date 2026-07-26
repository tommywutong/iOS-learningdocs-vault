---
title: allowsInlineMediaPlayback
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（12.0 起废弃）, iPadOS 4.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/allowsinlinemediaplayback
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/allowsinlinemediaplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/allowsinlinemediaplayback.json'
content_hash: 'sha256:fb8edeadb57055b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# allowsInlineMediaPlayback

<sub>Instance Property</sub>

A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var allowsInlineMediaPlayback: Bool { get set }
```

## Discussion

You must set this property to play inline video. Set this property to `true` to play videos inline. Set this property to `false` to use the native full-screen controller. When adding a video element to a  HTML document on the iPhone, you must also include the `playsinline` attribute.

The default value for iPhone is `false` and the default value for iPad is `true`.

> [!important] Important
> Apps created before iOS 10.0 must use the `webkit-playsinline` attribute.

## See Also

### Managing media playback

- [mediaPlaybackRequiresUserAction](mediaplaybackrequiresuseraction.md) — A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them. _(deprecated)_
- [mediaPlaybackAllowsAirPlay](mediaplaybackallowsairplay.md) — A Boolean value that determines whether Air Play is allowed from this view. _(deprecated)_
- [allowsPictureInPictureMediaPlayback](allowspictureinpicturemediaplayback.md) — A Boolean value that determines whether Picture in Picture playback is allowed from this view. _(deprecated)_
