---
title: NSLog
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslog
source_url: 'https://developer.apple.com/documentation/foundation/nslog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslog.json'
content_hash: 'sha256:bfe2b6171994a7fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLog

<sub>Function</sub>

Logs an error message to the Apple System Log facility.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void NSLog(NSString *format, ...);
```

## Discussion

Simply calls [NSLogv](<nslogv(____).md>), passing it a variable number of arguments.

## See Also

### Diagnostics and Debugging

- [NSLogv](<nslogv(____).md>) — Logs an error message to the Apple System Log facility.
- [NSDeallocateZombies](nsdeallocatezombies.md) — A global variable that determines whether or not the memory of zombie objects is deallocated.
- [NSDebugEnabled](nsdebugenabled.md) — A global variable that can be used to enable debug behavior in your app, such as extra logging.
- [NSZombieEnabled](nszombieenabled.md) — A global variable related to zombie objects that in practice has no effect.
- [NSKeepAllocationStatistics](nskeepallocationstatistics.md) — A no-longer-used global variable related to keeping statistics.
