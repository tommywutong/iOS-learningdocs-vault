---
title: 'finishWithClientState:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplannedsegmentwritingrequest/finishwithclientstate:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/finishwithclientstate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentwritingrequest/finishwithclientstate%3A.json'
content_hash: 'sha256:fb743c35b01051ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedSegmentWritingRequest](../avplannedsegmentwritingrequest.md)

# finishWithClientState:

<sub>Instance Method</sub>

Clients must call this method after all writing activities for the intermediate segment file have successfully completed. If called with nil, this is equivalent to calling finish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) finishWithClientState:(NSData *) segmentEndingClientState;
```

## Discussion

This method throws NSGenericException if finish, finishWithClientState:, finishWithError:, or cancel has already been called on this request.

## See Also

### Managing client state

- [clientStateToRestore](clientstatetorestore.md) — The client state persisted from the previous segment, if any. Specifically, this is the NSData provided to the previous segment’s finishWithClientState: method. The client is responsible to restore its client state before writing the current segment. For example, clients such as compositors with a temporal element may need some processing history of previous samples in order to generate an output sample at time N. This will be nil for algorithms that are stateless. _(beta)_
