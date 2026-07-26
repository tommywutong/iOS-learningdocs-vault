---
title: nextCaptionGroup()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutputcaptionadaptor/nextcaptiongroup()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/nextcaptiongroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputcaptionadaptor/nextcaptiongroup%28%29.json'
content_hash: 'sha256:48c9f90c683f2665'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputCaptionAdaptor](../avassetreaderoutputcaptionadaptor.md)

# nextCaptionGroup()

<sub>Instance Method</sub>

Returns the next caption group.

> [!warning] Deprecated
> Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func nextCaptionGroup() -> AVCaptionGroup?
```

## Return Value

The caption group, or `nil` of there are no more groups.

## See Also

### Reading caption groups

- [- captionsNotPresentInPreviousGroupsInCaptionGroup:](<captionsnotpresentinpreviousgroups(in_).md>) — Returns the set of captions in the caption group that weren’t vended by the adaptor. _(deprecated)_
