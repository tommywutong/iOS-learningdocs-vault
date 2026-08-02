---
title: MovieShell
apple_id: DTS10000326
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieShell/Listings/Mac_Framework_MWPrefix_h.html
archived_at: '2026-07-18T03:16:08.381417Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieShell](MovieShell.md)


[Next](TestFunctions.c.md)[Previous](Mac%20Framework-MacMain.c.md)

# Mac Framework/MWPrefix.h

```c
// MW Prefix file


// Precompiled headers:
#ifdef powerc
#include <MacHeadersPPC>
#else
#include <MacHeaders68k>
#endif

// Definitions for the project
#define DEBUG true

// If you want to signal that you are using SIOUX, enable the following flag:
#define USESIOUX true

// If you want to restrict the framework to handle just one movie at a time, set this flag:
// #define ONEMOVIELIMIT true
```

[Next](TestFunctions.c.md)[Previous](Mac%20Framework-MacMain.c.md)

