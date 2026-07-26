---
title: NSCountFrames
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscountframes
source_url: 'https://developer.apple.com/documentation/foundation/nscountframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountframes.json'
content_hash: 'sha256:60281e973a720bc8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCountFrames

<sub>Function</sub>

Returns the number of call frames on the stack.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSUInteger NSCountFrames();
```

## See Also

### Debugging

- [NSFrameAddress](nsframeaddress.md) — Returns the value of the frame pointer of the specified frame.
- [NSIsFreedObject](nsisfreedobject.md) — Returns a Boolean indicating whether the specified object has been freed.
- [NSRecordAllocationEvent](nsrecordallocationevent.md) — Notes an object or zone allocation event and various other statistics, such as the time and current thread.
- [NSReturnAddress](nsreturnaddress.md) — Returns the value of the return address of the specified frame.
