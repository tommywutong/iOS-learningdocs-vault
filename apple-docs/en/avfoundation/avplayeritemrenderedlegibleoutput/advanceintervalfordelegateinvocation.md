---
title: advanceIntervalForDelegateInvocation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemrenderedlegibleoutput/advanceintervalfordelegateinvocation
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/advanceintervalfordelegateinvocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutput/advanceintervalfordelegateinvocation.json'
content_hash: 'sha256:faa2cadc08319813'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemRenderedLegibleOutput](../avplayeritemrenderedlegibleoutput.md)

# advanceIntervalForDelegateInvocation

<sub>Instance Property</sub>

Permits advance invocation of the associated delegate, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var advanceIntervalForDelegateInvocation: TimeInterval { get set }
```

## Discussion

Use this property specify the number of seconds early to invoke the delegate object. When possible, an AVPlayerItemLegibleOutput uses this value to call its delegate earlier than it would otherwise.

## See Also

### Configuring an output

- [videoDisplaySize](videodisplaysize.md) — Set the video display size to use for rendering of pixel buffers.
