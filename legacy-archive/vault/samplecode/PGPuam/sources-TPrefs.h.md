---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_TPrefs_h.html
archived_at: '2026-07-18T03:18:34.312296Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-TSetupPane.cp.md)[Previous](sources-TPrefs.cp.md)

# sources/TPrefs.h

```
//  TPrefs.h - Preference Object  
// 
// Apple Macintosh Developer Technical Support
// Written by:  Vinnie Moscaritolo
//
//  Copyright (work in progress)  Apple Computer, Inc All rights reserved.
//
// You may incorporate this sample code into your applications without
// restriction, though the sample code has been provided "AS IS" and the
// responsibility for its operation is 100% yours.  However, what you are
// not permitted to do is to redistribute the source as "DSC Sample Code"
// after having made changes. If you're going to re-distribute the source,
// we require that you make it clear in the source that the code was
// descended from Apple Sample Code, but that you've made changes.
// 

#pragma once

#ifndef __COLLECTIONS__
#   include <Collections.h>
#endif

#define kPrefsFileType      'pref'

// ---------------------------------------------------------------------------
//   TPrefs - Preference Object  
// 
// ---------------------------------------------------------------------------
// 
class TPrefs
{
public:

//  CONSTRUCTORS AND DESTRUCTORS
              TPrefs();

    virtual  ~TPrefs();         

// MAIN INTERFACE
    virtual OSErr   Read();         // read them in
    virtual void    Write();        


    virtual OSErr   Set( FourCharCode   tag, 
                         SInt32         id,
                         SInt32         itemSize,
                         void *         itemData);

    virtual OSErr   Get( FourCharCode   tag, 
                         SInt32         id,
                         SInt32*        itemSize,
                         void *         itemData);

protected:  
    virtual OSErr   GetPrefSpec (FSSpec *fss );
    virtual OSErr   CreatePrefFile(FSSpec *fss);        


// PRIVATE FIELDS
protected:
    Collection  fCollection;

  };
```

[Next](sources-TSetupPane.cp.md)[Previous](sources-TPrefs.cp.md)

