---
title: Network Services Location Manager (Legacy)
apple_id: TP40000914
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSL/NSL3/NSL35.html
archived_at: '2026-07-15T08:18:17.635764Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Services Location Manager (Legacy)](Introduction.md)


[Next](Network%20Services%20Location%20Manager%20Result%20Codes.md)[Previous](Network%20Services%20Location%20Manager%20Data%20Types.md)

# Network Services Location Manager Constants

### NSLDialogOptionsFlags

Constants defined for use with the `NSLDialogOptions` structure.

```
enum {
   kNSLDefaultNSLDlogOptions = 0x00000000,
   kNSLNoURLTEField = 0x00000001
};
typedef UInt32 NSLDialogOptionFlags;
```

##### Constants

****

****

```
Discussion
The
NSLDialogOptionFlags
enumeration defines constants that tell the
NSLStandardGetURL
function how to display its dialog box.
```


### NSLEventCode

Constants defined for use in the `searchDataType` field of the `NSLClientAsyncInfo` structure.

```
enum {
   kNSLServicesLookupDataEvent = 6,
   kNSLNeighborhoodLookupDataEvent = 7,
   kNSLSNewDataEvent = 8,
   kNSLContinueLookupEvent = 9
};
typedef UInt16 NSLEventCode;
```

##### Constants

****

****

****
:

****

### NSLSearchState

Constants defined for use in the `searchState` field of the `NSLClientAsyncInfo` structure to describe the state of a search.

```
enum {
   kNSLSearchStateBufferFull = 1,
   kNSLSearchStateOnGoing = 2,
   kNSLSearchStateComplete = 3,
   kNSLSearchStateStalled = 4,
   kNSLWaitingForContinue = 5
};
typedef UInt16 NSLSearchState;
```

##### Constants

****

****

****

****

****

```
Discussion
The
NSLSearchState
enumeration defines constants that describe the state of a search.
```

[Next](Network%20Services%20Location%20Manager%20Result%20Codes.md)[Previous](Network%20Services%20Location%20Manager%20Data%20Types.md)

