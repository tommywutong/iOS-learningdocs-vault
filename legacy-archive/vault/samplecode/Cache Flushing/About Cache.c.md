---
title: Cache Flushing
apple_id: DTS10000222
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Cache_Flushing/Listings/About_Cache_c.html
archived_at: '2026-07-18T03:02:48.283326Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Cache Flushing](Cache%20Flushing.md)


[Next](Document%20Revision%20History.md)[Previous](Cache%20Flushing.md)

# About Cache.c

```
Cache.c contains code to correctly flush instruction and data caches on all Macintosh CPUs.

Beginning with the Macintosh II, developers were faced with situations where instruction and/or data caches needed to be flushed for code to execute correctly.  Unfortunately, despite recent improvements (i.e. _HWPriv, see Tech Note #261), cache flushing remains highly CPU and system specific and developers have had difficulty doing it in a way the ensures both forward and backward compatibility.   Cache.c contains a single function call that will work across all platforms, yet still provides access to such advanced MC68040 features as selective cache range flushing.

See instructions in Cache.h for details on usage.

Dave Radcliffe
Apple DTS
January, 1992
```

[Next](Document%20Revision%20History.md)[Previous](Cache%20Flushing.md)

