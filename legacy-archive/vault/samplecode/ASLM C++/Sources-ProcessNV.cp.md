---
title: ASLM C++
apple_id: DTS10000280
resource_type: Sample Code
platform: Xcode Developer Tools
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ASLM_C++/Listings/Sources_ProcessNV_cp.html
archived_at: '2026-07-18T02:59:42.798749Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ASLM C++](ASLM%20C%2B%2B.md)


[Next](Sources-TestTool.cp.md)[Previous](Sources-Process.r.md)

# Sources/ProcessNV.cp

```c
/* _________________________________________________________________________________________________________ //
  Copyright © 1992 Apple Computer, Inc. All rights reserved.
  Macintosh Developer Technical Support.C++ Macintosh Toolbox Framework.
  Date: Monday, August 10, 1992 1:17:29
  Revision comments are at the end of this file.
  ---
  TProcess is a Process Manager class.
  ProcessNV.cp contains the SLM constructor/destructor and other non-virtual function information.
  _________________________________________________________________________________________________________ */


// Include files
#ifndef _PROCESS_
#include "Process.h"
#endif

#ifndef __LIBRARYMANAGERUTILITIES__
#include <LibraryManagerUtilities.h>
#endif

// Library statements
#pragma library id="slm:dtsl$", version=00.00.01
#pragma class name=TProcess, id=kTProcessID, parent=kTDynamicID, flags=newobject


// _________________________________________________________________________________________________________ //
// TRandom class member function implementations

//  CONSTRUCTORS & DESTRUCTORS

TProcess::TProcess()
// Constructor, we are not doing anything inside this one just now.
{
}


TProcess::~TProcess()
// Destructor, we are not doing anything inside this one just now.
{
}
```

[Next](Sources-TestTool.cp.md)[Previous](Sources-Process.r.md)

