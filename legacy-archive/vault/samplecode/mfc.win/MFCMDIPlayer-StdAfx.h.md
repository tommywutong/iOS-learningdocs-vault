---
title: mfc.win
apple_id: DTS10000769
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/mfc.win/Listings/MFCMDIPlayer_StdAfx_h.html
archived_at: '2026-07-18T03:29:51.965478Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [mfc.win](mfc.win.md)


[Next](MFCQTClasses-CQuickTime.cpp.md)[Previous](MFCMDIPlayer-StdAfx.cpp.md)

# MFCMDIPlayer/StdAfx.h

```c
// stdafx.h : include file for standard system include files,
//  or project specific include files that are used frequently, but
//      are changed infrequently
//
// QTML and QuickTime
#include <ConditionalMacros.h>
#include <QTML.h>
#include <Movies.h>
#include <scrap.h>
#define VC_EXTRALEAN        // Exclude rarely-used stuff from Windows headers

#include <afxwin.h>         // MFC core and standard components
#include <afxext.h>         // MFC extensions
#ifndef _AFX_NO_AFXCMN_SUPPORT
#include <afxcmn.h>         // MFC support for Windows Common Controls
#endif // _AFX_NO_AFXCMN_SUPPORT
```

[Next](MFCQTClasses-CQuickTime.cpp.md)[Previous](MFCMDIPlayer-StdAfx.cpp.md)

