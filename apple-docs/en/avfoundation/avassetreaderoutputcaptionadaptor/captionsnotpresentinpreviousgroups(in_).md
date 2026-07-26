---
title: 'captionsNotPresentInPreviousGroups(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups%28in%3A%29.json'
content_hash: 'sha256:4349582b680f659e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputCaptionAdaptor](../avassetreaderoutputcaptionadaptor.md)

# captionsNotPresentInPreviousGroups(in:)

<sub>Instance Method</sub>

Returns the set of captions in the caption group that weren’t vended by the adaptor.

> [!warning] Deprecated
> Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func captionsNotPresentInPreviousGroups(in captionGroup: AVCaptionGroup) -> [AVCaption]
```

## Parameters

- `captionGroup` — The caption group to query.

## Return Value

An array of captions not previously vended by the adaptor, or an empty array if there are none.

## See Also

### Reading caption groups

- [- nextCaptionGroup](<nextcaptiongroup().md>) — Returns the next caption group. _(deprecated)_
