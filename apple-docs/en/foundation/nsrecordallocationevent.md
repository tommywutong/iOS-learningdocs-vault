---
title: NSRecordAllocationEvent
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrecordallocationevent
source_url: 'https://developer.apple.com/documentation/foundation/nsrecordallocationevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrecordallocationevent.json'
content_hash: 'sha256:fc3cb411df419924'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSRecordAllocationEvent

<sub>Function</sub>

Notes an object or zone allocation event and various other statistics, such as the time and current thread.

<sub>Mac Catalyst, macOS</sub>

```objc
extern void NSRecordAllocationEvent(int eventType, id object);
```

## See Also

### Debugging

- [NSCountFrames](nscountframes.md) — Returns the number of call frames on the stack.
- [NSFrameAddress](nsframeaddress.md) — Returns the value of the frame pointer of the specified frame.
- [NSIsFreedObject](nsisfreedobject.md) — Returns a Boolean indicating whether the specified object has been freed.
- [NSReturnAddress](nsreturnaddress.md) — Returns the value of the return address of the specified frame.
