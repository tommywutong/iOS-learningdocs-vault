---
title: GXSetDefaultDTP
apple_id: DTS10000291
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/GXSetDefaultDTP/Listings/FSSetPrinter_h.html
archived_at: '2026-07-18T03:10:37.865127Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GXSetDefaultDTP](GXSetDefaultDTP.md)


[Next](SetDefaultDTP.c.md)[Previous](FSSetPrinter.c.md)

# FSSetPrinter.h

```
#pragma once


// defines for Finder extensions
#define kFinderExtension            'fext'
#define kPrintingExtension          'pxtn'
#define kFinderSignature            'MACS'
#define kSetDefaultPrinterType      'pfpr'


typedef struct {
    OSType      pfeCreator;
    OSType      extensionType;
    Str31       dtpName;
} SetDTPEvent;

OSErr SASendAEToFinder(Ptr dataPtr,Size dataSize);
OSErr SendTestAE(StringPtr dtpName);
```

[Next](SetDefaultDTP.c.md)[Previous](FSSetPrinter.c.md)

