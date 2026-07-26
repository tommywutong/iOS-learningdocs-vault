---
title: allowsPictureInPictureMediaPlayback
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（12.0 起废弃）, iPadOS 9.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/allowspictureinpicturemediaplayback
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/allowspictureinpicturemediaplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/allowspictureinpicturemediaplayback.json'
content_hash: 'sha256:79c0c07327066f6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# allowsPictureInPictureMediaPlayback

<sub>Instance Property</sub>

A Boolean value that determines whether Picture in Picture playback is allowed from this view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var allowsPictureInPictureMediaPlayback: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md) on devices that support Picture in Picture (PiP) mode and [false](../../swift/false.md) on all other devices.

## See Also

### Managing media playback

- [allowsInlineMediaPlayback](allowsinlinemediaplayback.md) — A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller. _(deprecated)_
- [mediaPlaybackRequiresUserAction](mediaplaybackrequiresuseraction.md) — A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them. _(deprecated)_
- [mediaPlaybackAllowsAirPlay](mediaplaybackallowsairplay.md) — A Boolean value that determines whether Air Play is allowed from this view. _(deprecated)_
