---
title: Load PCI Driver
apple_id: DTS10000439
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Load_PCI_Driver/Listings/FullPath_h.html
archived_at: '2026-07-18T03:13:42.599763Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Load PCI Driver](Load%20PCI%20Driver.md)


[Next](Load%20PCI%20Driver.c.md)[Previous](FullPath.c.md)

# FullPath.h

```
/*
    File:       FullPath.h

    Contains:   Routines for dealing with full pathnames... if you really must.

    Written by:     

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/3/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#pragma once
pascal  OSErr   GetFullPath(short vRefNum,
                            long dirID,
                            ConstStr255Param name,
                            short *fullPathLength,
                            Handle *fullPath);

pascal  OSErr   FSpGetFullPath(const FSSpec *spec,
                               short *fullPathLength,
                               Handle *fullPath);


pascal OSErr FSpLocationFromFullPath(short fullPathLength,
                                     const void *fullPath,
                                     FSSpec *spec);

pascal OSErr LocationFromFullPath(short fullPathLength,
                                  const void *fullPath,
                                  short *vRefNum,
                                  long *parID,
                                  Str31 name);
```

[Next](Load%20PCI%20Driver.c.md)[Previous](FullPath.c.md)

