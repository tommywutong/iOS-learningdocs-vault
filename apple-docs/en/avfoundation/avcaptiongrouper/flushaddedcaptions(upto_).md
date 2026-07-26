---
title: 'flushAddedCaptions(upTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptiongrouper/flushaddedcaptions(upto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptiongrouper/flushaddedcaptions(upto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptiongrouper/flushaddedcaptions%28upto%3A%29.json'
content_hash: 'sha256:deb314b2c4d393a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionGrouper](../avcaptiongrouper.md)

# flushAddedCaptions(upTo:)

<sub>Instance Method</sub>

Creates caption groups for the captions you enqueue up to the time.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func flushAddedCaptions(upTo upToTime: CMTime) -> [AVCaptionGroup]
```

## Parameters

- `upToTime` — The time up to which the system flushes the queue.

## Return Value

An array of zero or more caption groups.
