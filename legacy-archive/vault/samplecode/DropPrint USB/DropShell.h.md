---
title: DropPrint USB
apple_id: DTS10000288
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/DropPrint_USB/Listings/DropShell_h.html
archived_at: '2026-07-18T03:07:21.375769Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DropPrint USB](DropPrint%20USB.md)


[Next](dropshell.r.md)[Previous](DropShell.c.md)

# DropShell.h

```
#ifndef __DROPSHELL_H__
#define __DROPSHELL_H__

void            Panic(void);
void            InitToolbox(void);
Boolean         InitGlobals(void);
void            SetUpMenus(void);
void            InstallSplashScreen(void); 
void            ShowAbout(void);
void            DoMenu(long retVal);
void            DoMouseDown(EventRecord *curEvent);
void            DoKeyDown(EventRecord *curEvent);

#endif
```

[Next](dropshell.r.md)[Previous](DropShell.c.md)

