---
title: 'replyWithException:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdistantobjectrequest/replywithexception:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobjectrequest/replywithexception:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobjectrequest/replywithexception%3A.json'
content_hash: 'sha256:ed06363226009c88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObjectRequest](../nsdistantobjectrequest.md)

# replyWithException:

<sub>Instance Method</sub>

Sends a reply back to the remote object making the distant object request.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) replyWithException:(NSException *) exception;
```

## Parameters

- `exception` — The exception to send.

## Discussion

If `exception` is `nil`, the return value of the receiver’s invocation is sent; otherwise, `exception` is sent and is automatically raised when it arrives at its destination.
