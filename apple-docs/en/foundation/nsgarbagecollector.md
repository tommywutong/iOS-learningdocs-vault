---
title: NSGarbageCollector
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.5+（10.10 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsgarbagecollector
source_url: 'https://developer.apple.com/documentation/foundation/nsgarbagecollector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgarbagecollector.json'
content_hash: 'sha256:af172d209351c815'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSGarbageCollector

<sub>Class</sub>

A convenient interface to the garbage collection system.

<sub>Mac Catalyst, macOS</sub>

```objc
@interface NSGarbageCollector : NSObject
```

## Overview

> [!important] Important
> Garbage collection is deprecated in OS X 10.8. Use ARC instead—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

Cocoa’s garbage collector is a conservative generational garbage collector. It uses “write-barriers” to detect cross generational stores of pointers so that “young” objects can be collected quickly.

You enable garbage collection (GC) by using the `-fobjc-gc compiler` option. This switch causes the generation of the write-barrier assignment primitives. You must use this option on your main application file _and all others used by the application_, including frameworks and bundles. Bundles are ignored if they are not GC-capable.

The collector determines what is garbage by recursively examining all nodes starting with globals, possible nodes referenced from the thread stacks, and all nodes marked as having “external” references. Nodes not reached by this search are deemed garbage. Weak references to garbage nodes are then cleared.

Garbage nodes that are objects are sent (in an arbitrary order) a [finalize()](<../objectivec/nsobject-swift.class/finalize().md>) message, and after all `finalize` messages have been sent their memory is recovered. It is a runtime error (referred to as “resurrection”) to store a object being finalized into one that is not. For more details, see Implementing a finalize Method in Garbage Collection Programming Guide.

You can request collection from any thread (see [collectIfNeeded](nsgarbagecollector/collectifneeded.md) and [collectExhaustively](nsgarbagecollector/collectexhaustively.md)).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Shared Instance

- [defaultCollector](nsgarbagecollector/defaultcollector.md) — Returns the default garbage collector. _(deprecated)_

### Collection State

- [disable](nsgarbagecollector/disable.md) — Temporarily disables collections. _(deprecated)_
- [enable](nsgarbagecollector/enable.md) — Enables collection after collection has been disabled. _(deprecated)_
- [isEnabled](nsgarbagecollector/isenabled.md) — Returns a Boolean value that indicates whether garbage collection is currently enabled for the current process. _(deprecated)_
- [isCollecting](nsgarbagecollector/iscollecting.md) — Returns a Boolean value that indicates whether a collection is currently in progress. _(deprecated)_

### Triggering Collection

- [collectExhaustively](nsgarbagecollector/collectexhaustively.md) — Tells the receiver to collect iteratively. _(deprecated)_
- [collectIfNeeded](nsgarbagecollector/collectifneeded.md) — Tells the receiver to collect if memory consumption thresholds have been exceeded. _(deprecated)_

### Manipulating External References

- [disableCollectorForPointer:](nsgarbagecollector/disablecollectorforpointer_.md) — Specifies that a given pointer will not be collected. _(deprecated)_
- [enableCollectorForPointer:](nsgarbagecollector/enablecollectorforpointer_.md) — Specifies that a given pointer may be collected. _(deprecated)_

### Accessing an Unscanned Memory Zone

- [zone](nsgarbagecollector/zone.md) — Returns a zone of unscanned memory. _(deprecated)_

## See Also

### Legacy

- [NSAllocateCollectable](nsallocatecollectable.md) — Allocates collectable memory. _(deprecated)_
- [NSReallocateCollectable](nsreallocatecollectable.md) — Reallocates collectable memory. _(deprecated)_
- [NSMakeCollectable](nsmakecollectable.md) — Makes a newly allocated Core Foundation object eligible for collection. _(deprecated)_
- [Memory Allocation Options](1539826-memory-allocation-options.md) — Constants used to control behavior when allocating or reallocating collectible memory.
