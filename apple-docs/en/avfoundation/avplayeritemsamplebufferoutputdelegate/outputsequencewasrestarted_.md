---
title: 'outputSequenceWasRestarted:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemsamplebufferoutputdelegate/outputsequencewasrestarted:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutputdelegate/outputsequencewasrestarted:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutputdelegate/outputsequencewasrestarted%3A.json'
content_hash: 'sha256:936433ea0ba4976c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSampleBufferOutputDelegate](../avplayeritemsamplebufferoutputdelegate.md)

# outputSequenceWasRestarted:

<sub>Instance Method</sub>

Invoked when the output is commencing a new sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) outputSequenceWasRestarted:(AVPlayerItemSampleBufferOutput *) output;
```

## Discussion

This method is invoked after seeks and changes in playback direction. If you are maintaining any queued future samples previously copied, it may be appropriate to discard these upon receiving this message.

Note that delivery of this message may race with calls to `-copyNextSampleBuffer`.

## See Also

### Responding to output events

- [outputMediaDataAvailable:](outputmediadataavailable_.md) — Invoked when the output becomes ready to deliver a sample buffer. _(beta)_
