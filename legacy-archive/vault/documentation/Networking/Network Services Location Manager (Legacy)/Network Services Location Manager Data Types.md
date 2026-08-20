---
title: Network Services Location Manager (Legacy)
apple_id: TP40000914
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSL/NSL3/NSL34.html
archived_at: '2026-07-15T08:18:17.624050Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Network Services Location Manager (Legacy)](Introduction.md)


[Next](Network%20Services%20Location%20Manager%20Constants.md)[Previous](NSL33.md)

# Network Services Location Manager Data Types

A structure provided when an application creates a search request and looks for neighborhoods and services.

```
struct NSLClientAsyncInfo {
   void*           clientContextPtr;
   void*           mgrContextPtr;
   char*           resultBuffer;
   long            bufferLen;
   long            maxBufferSize;
   UInt32          startTime;
   UInt32          intStartTime;
   UInt32          maxSearchTime;
   UInt32          alertInterval;
   UInt32          totalItems;
   UInt32          alertThreshold;
   NSLSearchState  searchState;
   NSLError        searchResult;
   NSLEventCode    searchDataType
};
typedef struct NSLClientAsyncInfo NSLClientAsyncInfo;
   typedef NSLClientAsyncInfo * NSLClientAsyncInfoPtr;
```

##### Fields

**`clientContextPtr`**
: A value set by the application for its own use.

**`mgrContextPtr`**
: A value set by the Network Services Location Manager for its own use.

**`resultBuffer`**
: A pointer to the buffer that contains search results when your application’s notification routine is called.

**`bufferLen`**
: The number of bytes in `resultBuffer` that contain valid data.

**`maxBufferSize`**
: The length of `resultBuffer`.

**`startTime`**
: Used by the Network Services Location Manager for internal purposes. Your application should not modify this field.

**`intStartTime`**
: Used by the Network Services Location Manager for internal purposes. Your application should not modify this field.

**`maxSearchTime`**
: An application-specified limit in ticks on the total amount of time that is to be expended on the search. The default value is zero, which indicates that the search time is not to be limited. The value of `maxSearchTime` does not override any limit that Mac OS X may impose.

**`alertInterval`**
: An application-specified value that defines in ticks the interval at which the application’s notification routine is to be called. The default value is zero, which indicates that no alert interval is specified.

**`totalItems`**
: The total number of items in `resultBuffer`.

**`alertThreshold`**
: An application-specified value that causes the application’s notification routine to be called whenever the specified number of items have been placed in `resultBuffer`. Typically, applications set `alertThreshold` to 1.

**`searchState`**
: A value that describes the current search state. The value can be one of the following: `kNSLSearchStateBufferFull`, `kNSLSearchStateOnGoing`, `kNSLSearchStateComplete`, or `kNSLSearchStateStalled`.

**`searchResult`**
: An `[NSLError](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngek4tsn5za)` structure containing an error code that may have been returned.

**`searchDataType`**
: An event code that indicates whether the information stored in this `NSLClientAsyncInfo` structure pertains to a neighborhood search (`kNSLNeighborhoodLookupDataEvent`) or a service search (`kNSLServicesLookupDataEvent`).

```
Discussion
This structure contains information about how a neighborhood or a service search is to be conducted and where search results are to be stored. You obtain a pointer to an
NSLClientAsyncInfo
structure by calling
NSLPrepareRequest
, and you pass that pointer as a parameter when you call
NSLStartNeighborhoodLookup
, or
NSLStartServicesLookup
.
Before calling
NSLStartNeighborhoodLookup
or
NSLStartServicesLookup
, you can modify the way in which the search is conducted by changing certain values in the
NSLClientAsyncInfo
structure. However, once you call
NSLStartNeighborhoodLookup
or
NSLStartServicesLookup
, you should not modify the
NSLClientAsyncInfo
structure.
When
NSLStartNeighborhoodLookup
or
NSLStartServicesLookup
returns, or when your application’s notification routine is called, the
NSLClientAsyncInfo
structure contains information about the status of the search and any search results.
```


The structure returned by `NSLGetDefaultDialogOptions` containing information that controls the appearance of the `NSLStandardGetURL` dialog box.

```
struct NSLDialogOptions {
   UInt16 version;
   NSLDialogOptionFlags dialogOptionFlags;
   Str255 windowTitle;
   Str255 actionButtonLabel;
   Str255 cancelButtonLabel;
   Str255 message;
};
typedef struct NSLDialogOptions NSLDialogOptions;
```

##### Fields

**`version`**
: A value that specifies the version of the default values.

**`dialogOptionFlags`**
: A bit map. Use the constants defined by the `[NSLDialogOptionsFlags](NSL35.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngei2lbnrxwot3qoruw63sgnrqwo4y)` enumeration to indicate that the default values should be used or to indicate that the Address text field should not be displayed in the `NSLStandardGetURL` dialog box.

**`windowTitle`**
: A string containing the name that is to appear in the title bar of the dialog box displayed by `NSLStandardGetURL`. The default title is “Connect to Server.”

**`actionButtonLabel`**
: A string containing the name that is to be used as the label for the cancel button. If `NULL`, the default name is used. The default name is “Cancel.”

**`message`**
: A string containing instructional text that is displayed at the top of the dialog box. If `message` is `NULL`, no instructional text is displayed. The default message is “Choose a server from the list or enter a server address.”

A structure returned by many Network Services Location Manager functions containing a result code as well as a context value.

```
typedef struct NSLError {
   OSStatus    theErr;
   UInt32  theContext;
};
typedef struct NSLError NSLError;
   typedef NSLError * NSLErrorPtr;
```

##### Fields

**`theErr`**
: The result code.

**`theContext`**
: A value the Network Services Location Manager uses to determine the context of an error so that it can provide an appropriate error message when `[NSLErrorToString](NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngek4tsn5zfi32torzgs3th)` is called.

```
Discussion
To determine if an error occurred, compare the constant
kNSLErrorNoErr
to the value returned by a function that returns an
NSLError
structure.
If you want to display information about the error to the user, your application should call
NSLErrorToString
and pass the
NSLError
structure that your application received. The
NSLErrorToString
function returns two strings — a problem string and a solution string — that your application can display.
```


A reference returned by `NSLOpenNavigationAPI` when you open a Network Services Location Manager session.

```
typedef UInt32 NSLClientRef;
```

```
Discussion
When calling
NSLPrepareRequest
and
NSLCloseNavigationAPI
, pass the client reference that
NSLOpenNavigationAPI
returned.
```


A value that identifies a neighborhood.

```
typedef unsigned char * NSLNeighborhood;
```

```
Discussion
A value of type
NSLNeighborhood
is returned by
NSLMakeNewNeighborhood
that is used when calling
NSLStartNeighborhoodLookup
,
NSLStartServicesLookup
,
NSLStandardRegisterURL
, and
NSLStandardDeregisterURL
. Call
NSLFreeNeighborhood
to deallocate the memory associated with a value of type
NSLNeighborhood
.
```


A value used to specify a URL.

```
typedef char * NSLPath;
```

```
Discussion
A value of type
NSLPath
is used when calling
NSLStandardRegisterURL
, and
NSLStandardDeregisterURL
.
```


A request reference returned by `NSLPrepareRequest`.

```
typedef UInt32 NSLRequestRef;
```

```
Discussion
When calling
NSLStartServicesLookup
or
NSLStartNeighborhoodLookup
, pass the
NSLRequestRef
that
NSLPrepareRequest
returned.
```


A value that identifies a service.

```
typedef char * NSLServiceType;
```

```
Discussion
A value of type
NSLServiceType
is a null-terminated string containing the name of the service, such as
http
or
ftp
.
```


A value that contains a list of services.

```
typedef Handle NSLServicesList;
```

```
Discussion
A value of type
NSLServiceList
contains a list of service names.
```


A value created by `NSLMakeServicesRequestPB`.

```
struct NSLTypedData {
   unsigned long dataType;
   unsigned long lengthOfData;
};
typedef struct NSLTypedData NSLTypedData;
   typedef NSLTypedData *NSLTypedDataPtr;
```

```
Discussion
A value of type
NSLTypedDataPtr
is passed to
NSLStartServicesLookup
. When you no longer need a value of type
NSLTypedDataPtr
, call
NSLFreeTypedDataPtr
.
```

[Next](Network%20Services%20Location%20Manager%20Constants.md)[Previous](NSL33.md)

