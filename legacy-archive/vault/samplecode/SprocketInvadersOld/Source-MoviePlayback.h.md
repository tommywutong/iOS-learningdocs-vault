---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_MoviePlayback_h.html
archived_at: '2026-07-18T03:25:27.154307Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-NetSprocketSupport.c.md)[Previous](Source-MoviePlayback.c.md)

# Source/MoviePlayback.h

```
#ifndef __MOVIEPLAYBACK__
#define __MOVIEPLAYBACK__

//¥ ----------------------------------------    Includes
//¥ ----------------------------------------    Definitions
//¥ ----------------------------------------    Types
//¥ ----------------------------------------    Public Variables

extern FSSpec   gMovieSpec;

//¥ ----------------------------------------    Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern void PlaybackMovie(void);
extern void ServiceMoviePlayback(void);
extern void ShutdownMoviePlayback(void);
extern void SelectBackgroundMovie(void);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-NetSprocketSupport.c.md)[Previous](Source-MoviePlayback.c.md)

