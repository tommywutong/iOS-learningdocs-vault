---
title: Garbage Collection Release Notes
apple_id: TP40006603
resource_type: Release Note
platform: macOS
topic: General
technology: Foundation
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Cocoa/GCReleaseNotes/index.html
archived_at: '2026-07-18T02:50:22.577994Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Garbage Collection Release Notes—Mac OS X v10.5.0

> [!IMPORTANT]
> 

#### Contents:

- [Performance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmbtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Framework Adoption](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmmbtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)

### Performance

In general, in the first release garbage collection (GC) should have adequate performance for most Cocoa-level application programming. Some real-time and multi-media applications, however, may suffer performance (and even stability) problems.

The memory allocator for garbage collection is modeled after the underlying `malloc` and is intended to have similar performance characteristics. In the first release, however, the collector will not throttle allocation and so allocation-heavy threads may outrun the collector. Overall, allocation rates are lower than traditional `malloc`.

Since the collector runs on a background thread and obviously has to do work, a GC-enabled application is likely to consume more CPU cycles than it would without GC.

### Framework Adoption

The first release of garbage collection for Mac OS X is not only the first release of the GC architecture itself but also of support for GC within the system frameworks. Adoption within frameworks is also at the 1.0 level, and is expected to improve with subsequent releases of the operating system. The frameworks themselves have been well-tested in most contexts, nevertheless some paths have received less coverage. If you find errors, you should report them using [Apple’s bug reporting system](http://bugreporter.apple.com/).
