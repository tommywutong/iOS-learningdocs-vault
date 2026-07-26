---
title: NSReturnAddress
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsreturnaddress
source_url: 'https://developer.apple.com/documentation/foundation/nsreturnaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsreturnaddress.json'
content_hash: 'sha256:594223e3c5c9c966'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSReturnAddress

<sub>Function</sub>

Returns the value of the return address of the specified frame.

<sub>Mac Catalyst, macOS</sub>

```objc
extern void *NSReturnAddress(NSUInteger frame);
```

## See Also

### Debugging

- [NSCountFrames](nscountframes.md) — Returns the number of call frames on the stack.
- [NSFrameAddress](nsframeaddress.md) — Returns the value of the frame pointer of the specified frame.
- [NSIsFreedObject](nsisfreedobject.md) — Returns a Boolean indicating whether the specified object has been freed.
- [NSRecordAllocationEvent](nsrecordallocationevent.md) — Notes an object or zone allocation event and various other statistics, such as the time and current thread.
