---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemmetadataoutput/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadataoutput/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:b5b0b1dc40ff3aff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataOutput](../avplayeritemmetadataoutput.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the delegate and a dispatch queue on which the delegate is called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDelegate(_ delegate: (any AVPlayerItemMetadataOutputPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — An object conforming to [AVPlayerItemMetadataOutputPushDelegate](../avplayeritemmetadataoutputpushdelegate.md) protocol.

- `delegateQueue` — A dispatch queue on which all delegate methods will be called.

## Discussion

You specify the metadata delegate, and a dispatch queue on which it will be called, to be notified as new metadata is encountered in the source media.

> [!important] Important
> The values set for the `delegate` and `delegateQueue` arguments can be `nil` , but passing `nil` for one requires you to do the same for the other. Passing a `nil` value for only one argument results in an exception being raised at runtime.

## See Also

### Configuring the delegate

- [advanceIntervalForDelegateInvocation](advanceintervalfordelegateinvocation.md) — The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [delegate](delegate.md) — The delegate object.
- [AVPlayerItemMetadataOutputPushDelegate](../avplayeritemmetadataoutputpushdelegate.md) — Methods you can implement to provide additional metadata.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which messages are sent to the delegate.
