---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CPreferences_h.html
archived_at: '2026-07-18T03:14:26.212084Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CPrefsWindow.cp.md)[Previous](CPreferences.cp.md)

# CPreferences.h

```c
/*
    Implements a preference file and resource io therein. Also handy
    for resource io in any LFile.

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#include <LFile.h>

class CPreferences
{
public:

    CPreferences();
    CPreferences(
        LFile *inFile);
    CPreferences(
        OSType inFileType,
        OSType inFileCreator,
        StringPtr inFileNameP);

    virtual ~CPreferences();

    void FindOrCreatePreferencesFile(
        OSType inFileType,
        OSType inFileCreator,
        StringPtr inFileNameP);

    Handle GetPreferenceResource(
        OSType inResType,
        ResIDT inResID);

    void SavePreferenceResource(
        OSType inResType,
        ResIDT inResID,
        Handle inPrefH);

private:

    LFile *mFile;
    Boolean mOwnsFile;
};
```

[Next](CPrefsWindow.cp.md)[Previous](CPreferences.cp.md)

