---
title: NSDeallocateZombies
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdeallocatezombies
source_url: 'https://developer.apple.com/documentation/foundation/nsdeallocatezombies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdeallocatezombies.json'
content_hash: 'sha256:18d0fbb6dd5c63ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDeallocateZombies

<sub>Global Variable</sub>

A global variable that determines whether or not the memory of zombie objects is deallocated.

<sub>Mac Catalyst, macOS</sub>

```objc
extern BOOL NSDeallocateZombies;
```

## See Also

### Diagnostics and Debugging

- [NSLog](nslog.md) — Logs an error message to the Apple System Log facility.
- [NSLogv](<nslogv(____).md>) — Logs an error message to the Apple System Log facility.
- [NSDebugEnabled](nsdebugenabled.md) — A global variable that can be used to enable debug behavior in your app, such as extra logging.
- [NSZombieEnabled](nszombieenabled.md) — A global variable related to zombie objects that in practice has no effect.
- [NSKeepAllocationStatistics](nskeepallocationstatistics.md) — A no-longer-used global variable related to keeping statistics.
