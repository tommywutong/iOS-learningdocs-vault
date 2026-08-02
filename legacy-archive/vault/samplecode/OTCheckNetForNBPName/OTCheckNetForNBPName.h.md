---
title: OTCheckNetForNBPName
apple_id: DTS10000707
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/OTCheckNetForNBPName/Listings/OTCheckNetForNBPName_h.html
archived_at: '2026-07-18T03:17:10.781263Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTCheckNetForNBPName](OTCheckNetForNBPName.md)


[Next](Document%20Revision%20History.md)[Previous](OTCheckNetForNBPName.c.md)

# OTCheckNetForNBPName.h

```
/*
 *  OTCheckNetForNBPName.h
 *  
 */

#ifndef __OTCHECKNETFORNBPNAME__
#define __OTCHECKNETFORNBPNAME__


#endif  // __OTCHECKNETFORNBPNAME__

#define zoneNameSize        33
#define numZonesIncrement   50
#define kNumZonesToCheckFor 20
#define kMaxActiveLookups   30  // maximum number of active lookups at a time.
#define kMaxToMatch         1   
#define kDefaultTimeout     5000    // lookup timeout value - 8 seconds


typedef struct {
        UInt32      flagbits;
        UInt8       zoneName[zoneNameSize];
} ZoneBuffer;

typedef ZoneBuffer *ZoneBufPtr;

typedef struct {
        TLookupReply    lkReply;
        UInt32          index;
        UInt32          lindex;
} MyLookupReply;

typedef MyLookupReply *MyLookupReplyPtr;
```

[Next](Document%20Revision%20History.md)[Previous](OTCheckNetForNBPName.c.md)

