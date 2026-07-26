---
title: NSZone
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nszone
source_url: 'https://developer.apple.com/documentation/foundation/nszone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nszone.json'
content_hash: 'sha256:38a89ede1920f333'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSZone

<sub>Type Alias</sub>

A type used to identify and manage memory zones.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct _NSZone NSZone;
```

## Topics

### Managing Zones

- [NSCreateZone](nscreatezone.md) — Creates a new zone. _(deprecated)_
- [NSRecycleZone](nsrecyclezone.md) — Frees memory in a zone. _(deprecated)_
- [NSSetZoneName](nssetzonename.md) — Sets the name of the specified zone. _(deprecated)_
- [NSZoneCalloc](nszonecalloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSZoneFree](nszonefree.md) — Deallocates a block of memory in the specified zone. _(deprecated)_
- [NSZoneFromPointer](nszonefrompointer.md) — Gets the zone for a given block of memory. _(deprecated)_
- [NSZoneMalloc](nszonemalloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSZoneName](nszonename.md) — Returns the name of the specified zone. _(deprecated)_
- [NSZoneRealloc](nszonerealloc.md) — Allocates memory in a zone. _(deprecated)_
- [NSDefaultMallocZone](nsdefaultmalloczone.md) — Returns the default zone. _(deprecated)_

## See Also

### Legacy

- [Distributed Objects Support](distributed-objects-support.md) — Enable communication among objects in different processes, both locally and on remote systems.
- [Objective-C Garbage Collection](objective-c-garbage-collection.md) — Interface with the legacy garbage collection system.
