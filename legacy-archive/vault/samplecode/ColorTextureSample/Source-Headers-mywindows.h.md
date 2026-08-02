---
title: ColorTextureSample
apple_id: DTS10000131
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorTextureSample/Listings/Source_Headers_mywindows_h.html
archived_at: '2026-07-18T03:04:02.557253Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorTextureSample](ColorTextureSample.md)


[Next](Source-Headers-objects.h.md)[Previous](Source-Headers-mymenus.h.md)

# Source/Headers/mywindows.h

```
//
// windows.h
//

extern  void DumpGWorld(GWorldPtr thisWorld, WindowPtr thisWindow);
extern  void DumpGWorld2(GWorldPtr thisWorld, WindowPtr thisWindow,Rect *destRect);
extern  void DumpGWorld3(GWorldPtr thisWorld, WindowPtr thisWindow,Rect *srcRect,Rect *destRect);
extern void DumpGWorldToGWorld(GWorldPtr, GWorldPtr, Rect *, Rect *);
extern void DoLockPixels(GWorldPtr);
extern void DoUnlockPixels(GWorldPtr);
extern void UpdateAnimWindow(void);
extern  pascal void DoBold (WindowPtr dlogPtr, short item);
extern  pascal void DoOutline (WindowPtr dlogPtr, short item);
extern  void Home(void);
extern  void DoCR(void);
extern  void InitBreakdownWindow(void);
extern  void WriteString(Str255 s);
extern  void WriteChar(char c);
extern  void ShowWaitingWindow(void);
extern  void KillWaitingWindow(void);
```

[Next](Source-Headers-objects.h.md)[Previous](Source-Headers-mymenus.h.md)

