---
title: AuntieDialog
apple_id: DTS10000556
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/AuntieDialog/Listings/AppearanceHelpers_h.html
archived_at: '2026-07-18T03:01:33.555587Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AuntieDialog](AuntieDialog.md)


[Next](Assertions.h.md)[Previous](AppearanceHelpers.c.md)

# AppearanceHelpers.h

```c
#ifndef _APPEARANCEHELPERS_
#define _APPEARANCEHELPERS_

#ifdef __MWERKS__

// includes for MetroWerks CodeWarrior

#include <Controls.h>
#include <Lists.h>

#else

#ifdef __APPLE_CC__

// includes for ProjectBuilder

#include <Carbon/Carbon.h>

#else

// includes for MPW

#include <Carbon.h>

#endif
#endif

extern pascal OSStatus SetPushButtonDefaultState    ( ControlHandle control, Boolean isDefault );
extern pascal OSStatus SetProgressIndicatorState    ( ControlHandle control, Boolean isDeterminate );
extern pascal OSStatus GetListBoxListHandle         ( ControlHandle control, ListHandle* list );

#endif // _APPEARANCEHELPERS_
```

[Next](Assertions.h.md)[Previous](AppearanceHelpers.c.md)

