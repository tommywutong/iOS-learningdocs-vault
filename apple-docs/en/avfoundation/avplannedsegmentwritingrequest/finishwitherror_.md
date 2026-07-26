---
title: 'finishWithError:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplannedsegmentwritingrequest/finishwitherror:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/finishwitherror:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplannedsegmentwritingrequest/finishwitherror%3A.json'
content_hash: 'sha256:da89600b028a3b3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlannedSegmentWritingRequest](../avplannedsegmentwritingrequest.md)

# finishWithError:

<sub>Instance Method</sub>

Clients must call this method if a non-recoverable error occurs while generating the segment file. The completionHandler of AVAssetWritingPlanner will be called with an error whose code is AVErrorAssetWritingPlannerClientWritingError, and the error provided here will be available in the NSUnderlyingErrorKey of the userInfo dictionary. If called with nil, this is equivalent to calling finish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) finishWithError:(NSError *) error;
```

## Discussion

This method throws NSGenericException if finish, finishWithClientState:, finishWithError:, or cancel has already been called on this request.

## See Also

### Finishing the request

- [finish](finish.md) — Clients must call this method after all writing activities for the intermediate segment file have successfully completed. _(beta)_
- [cancel](cancel.md) — Clients should call this if the current segment is to be cancelled, but the export is still expected to be resumed at a later time. For example, this could happen if the export is running in the background and the expiration handler is called due to changes in system conditions. _(beta)_
