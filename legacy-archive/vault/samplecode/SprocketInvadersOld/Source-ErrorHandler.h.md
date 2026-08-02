---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_ErrorHandler_h.html
archived_at: '2026-07-18T03:25:26.135670Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-EventHandler.c.md)[Previous](Source-ErrorHandler.c.md)

# Source/ErrorHandler.h

```
//¥ ------------------------------------------------------------------------------------------  ¥
//¥
//¥ Copyright © 1996 Apple Computer, Inc., All Rights Reserved
//¥
//¥
//¥     You may incorporate this sample code into your applications without
//¥     restriction, though the sample code has been provided "AS IS" and the
//¥     responsibility for its operation is 100% yours.  However, what you are
//¥     not permitted to do is to redistribute the source as "DSC Sample Code"
//¥     after having made changes. If you're going to re-distribute the source,
//¥     we require that you make it clear in the source that the code was
//¥     descended from Apple Sample Code, but that you've made changes.
//¥
//¥     Authors:
//¥         Chris De Salvo
//¥
//¥ ------------------------------------------------------------------------------------------  ¥

#ifndef __ERRORHANDLER__
#define __ERRORHANDLER__

//¥ ------------------------------  Includes
//¥ ------------------------------  Public Definitions
//¥ ------------------------------  Public Constants
//¥ ------------------------------  Public Types
//¥ ------------------------------  Public Structs
//¥ ------------------------------  Public Globals

//¥ ------------------------------  Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern void FatalError(char *error);
extern void NonFatalError(char *error);
extern short MessageError(char *string1, char *string2);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-EventHandler.c.md)[Previous](Source-ErrorHandler.c.md)

