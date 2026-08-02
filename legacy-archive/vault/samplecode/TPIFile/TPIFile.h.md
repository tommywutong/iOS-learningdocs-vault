---
title: TPIFile
apple_id: DTS10000267
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/TPIFile/Listings/TPIFile_h.html
archived_at: '2026-07-18T03:26:05.994977Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TPIFile](TPIFile.md)


[Next](TPIFileRegister.c.md)[Previous](TPIFile.c.md)

# TPIFile.h

```c
/*
    File:       TPIFile.h

    Contains:   Interface to the TPI Module to access File Manager files.
                Technology demonstration only!

    Written by: Quinn "The Eskimo!"

    Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

    You may incorporate this sample code into your applications without
    restriction, though the sample code has been provided "AS IS" and the
    responsibility for its operation is 100% yours.  However, what you are
    not permitted to do is to redistribute the source as "DSC Sample Code"
    after having made changes. If you're going to re-distribute the source,
    we require that you make it clear in the source that the code was
    descended from Apple Sample Code, but that you've made changes.
*/

#include <Files.h>
#include <OpenTransport.h>

enum {
    AF_FILESPEC = 666           // FSSpec
};

struct FileSpecAddress {
    OTAddressType   fAddressType;       // Use AF_FILESPEC to denote this format.
    FSSpec          fss;
};
typedef struct FileSpecAddress FileSpecAddress, *FileSpecAddressPtr;

struct TPIFilePortInfoRecord {
    OSType      magic1;
    OTPortRef   portRef;
    OSType      magic2;
};
typedef struct TPIFilePortInfoRecord TPIFilePortInfoRecord, *TPIFilePortInfoRecordPtr;

enum {
    kTPIFilePerStreamDataMagic = 'ESK0',
    kTPIFilePortInfoMagic1 = 'ESK1',
    kTPIFilePortInfoMagic2 = 'ESK2'
};

#define kTPIFilePortName "TPIFile"
```

[Next](TPIFileRegister.c.md)[Previous](TPIFile.c.md)

