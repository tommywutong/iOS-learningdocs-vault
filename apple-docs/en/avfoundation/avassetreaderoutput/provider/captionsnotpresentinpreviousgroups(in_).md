---
title: 'captionsNotPresentInPreviousGroups(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreaderoutput/provider/captionsnotpresentinpreviousgroups(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider/captionsnotpresentinpreviousgroups(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutput/provider/captionsnotpresentinpreviousgroups%28in%3A%29.json'
content_hash: 'sha256:99547b89309283d8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetReaderOutput](../../avassetreaderoutput.md) · [Provider](../provider.md)

# captionsNotPresentInPreviousGroups(in:)

<sub>Instance Method</sub>

Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func captionsNotPresentInPreviousGroups(in captionGroup: AVCaptionGroup) -> [AVCaption]
```

## Parameters

- `captionGroup` — The group containing the captions of interest.

## Return Value

An array of AVCaption objects.

## See Also

### Reading media data

- [next()](<next().md>) — Returns the next piece of media data.
