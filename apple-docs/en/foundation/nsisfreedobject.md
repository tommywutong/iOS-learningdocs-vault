---
title: NSIsFreedObject
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsisfreedobject
source_url: 'https://developer.apple.com/documentation/foundation/nsisfreedobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsisfreedobject.json'
content_hash: 'sha256:69e4859e5adcc440'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIsFreedObject

<sub>Function</sub>

Returns a Boolean indicating whether the specified object has been freed.

<sub>Mac Catalyst, macOS</sub>

```objc
extern BOOL NSIsFreedObject(id anObject);
```

## See Also

### Debugging

- [NSCountFrames](nscountframes.md) — Returns the number of call frames on the stack.
- [NSFrameAddress](nsframeaddress.md) — Returns the value of the frame pointer of the specified frame.
- [NSRecordAllocationEvent](nsrecordallocationevent.md) — Notes an object or zone allocation event and various other statistics, such as the time and current thread.
- [NSReturnAddress](nsreturnaddress.md) — Returns the value of the return address of the specified frame.
