---
title: QT Internals
apple_id: DTS10000848
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_Internals/Listings/Mac_Framework_MWPrefix_h.html
archived_at: '2026-07-18T03:21:22.346593Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT Internals](QT%20Internals.md)


[Next](QTInternals.c.md)[Previous](Mac%20Framework-MacMain.c.md)

# Mac Framework/MWPrefix.h

```c
// MW Prefix file


// Precompiled headers:
#ifdef powerc
#include <MacHeadersPPC>
#else
#include <MacHeaders68K>
#endif

// Definitions for the project
#define DEBUG true

// If you want to signal that you are using SIOUX, enable the following flag:
#define USESIOUX true
```

[Next](QTInternals.c.md)[Previous](Mac%20Framework-MacMain.c.md)

