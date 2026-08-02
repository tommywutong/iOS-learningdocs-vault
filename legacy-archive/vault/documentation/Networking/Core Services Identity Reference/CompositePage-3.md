---
title: Core Services Identity Reference
apple_id: TP40004673
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2008-06-06'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/CSIdentityQuery/CompositePage.html
archived_at: '2026-07-18T01:32:58.492929Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Services Identity Reference](Core%20Services%20Identity%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Networking](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000429) __>__ Core Foundation __>__ [Core Services Identity Reference](Core%20Services%20Identity%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5uwizlooruxi6i) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQuery | CSIdentityQuery | CSIdentityQuery | CSIdentityQuery | CSIdentityQuery |

|  |  |
| --- | --- |
| __Framework:__ | /System/Library/Frameworks/CoreServices.framework/Frameworks/OSServices.framework |
| __See Also:__ | **[Identity Services Programming Guide](../Identity%20Services%20Programming%20Guide/Introduction%20to%20Identity%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojq)** :   **** : |
| __Includes:__ | [<CSIdentity.i>](https://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/CSIdentity/index.html#//apple_ref/doc/header/CSIdentity.i) |

## Overview

A CSIdentityQuery object provides synchronous or asynchronous access to
a collection of identities managed by an identity authority. Clients call
one of the CSIdentityQueryCreate\* functions to define the query criteria. A
query can be executed exactly once, in either synchronous or asynchronous mode.

For synchronous execution, the client calls CSIdentityQueryExecute. This function
will return when all identies matching the criteria have been found. The results
are accessed as an array via CSIdentityQueryCopyResults(). No live updates
to the results array are provided in synchronous mode.

To execute in asynchronous mode, the client calls CSIdentityQueryExecuteAsynchronously,
specifying a client object to receive callbacks and a runloop/mode on which
callbacks are scheduled.

CSIdentityQueryExecuteAsynchronously returns immediately, and events
will be reported to the callback function as results are added by the
query. The client may request live updates to the query which will track changes
to the results as changes are made to the identity authority by other processes.
Currently, only changes to the local identity authority are monitored.

Asynchronous clients must call CSIdentityQueryStop when done processing
query results to prevent the client callbacks from being called again.

---

## Functions

**[CSIdentityQueryCopyResults](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdn5yhsutfon2wy5dt)**
: Retrieve the results of executing an identity query

**[CSIdentityQueryCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5df)**
: Creates an identity query object for all identities in the specified authority

**[CSIdentityQueryCreateForCurrentUser](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxeq3vojzgk3tukvzwk4q)**
: Creates a query for the current session user's identity

**[CSIdentityQueryCreateForName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxettbnvsq)**
: Creates an identity query object based on a name

**[CSIdentityQueryCreateForPersistentReference](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxeudfojzws43umvxhiutfmzsxezlomnsq)**
: Creates an identity query object based on an identity reference data object

**[CSIdentityQueryCreateForPosixID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxeudponuxqske)**
: Creates an identity query object based on a POSIX ID

**[CSIdentityQueryCreateForUUID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kdojswc5dfizxxevkvjfca)**
: Creates an identity query object based on a UUID

**[CSIdentityQueryExecute](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kfpbswg5lumu)**
: Execute an identity query synchronously

**[CSIdentityQueryExecuteAsynchronously](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6kfpbswg5lumvaxg6lomnuhe33on52xg3dz)**
: Execute an identity query asynchronously

**[CSIdentityQueryGetTypeID](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6khmv2fi6lqmveui)**
: Retrieve the CFTypeID of the CSIdentityQuery class

**[CSIdentityQueryStop](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2dknewizlooruxi6krovsxe6ktorxxa)**
: Invalidate an identity query client

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryCopyResults | CSIdentityQueryCopyResults | CSIdentityQueryCopyResults | CSIdentityQueryCopyResults | CSIdentityQueryCopyResults |

---

Retrieve the results of executing an identity query

```
extern CFArrayRef CSIdentityQueryCopyResults(
    CSIdentityQueryRef query );
```

##### Parameters

**`query`**
: The query object to access

##### Return Value

An array of zero or more CSIdentityRefs

##### Discussion

Returns an immutable array of CSIdentityRefs, reflecting the current results
of the query's execution.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryCreate | CSIdentityQueryCreate | CSIdentityQueryCreate | CSIdentityQueryCreate | CSIdentityQueryCreate |

---

Creates an identity query object for all identities in the specified authority

```
extern CSIdentityQueryRef CSIdentityQueryCreate(
    CFAllocatorRef allocator,
    CSIdentityClass identityClass,
    CSIdentityAuthorityRef authority );
```

##### Parameters

**`allocator`**
: The allocator to use for this instance

**`identityClass`**
: The class of identity to find

**`authority`**
: The identity authority to query

##### Return Value

A new CSIdentityQuery object

##### Discussion

The results of this query include all of the identities in the specified authority's database.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryCreateForCurrentUser | CSIdentityQueryCreateForCurrentUser | CSIdentityQueryCreateForCurrentUser | CSIdentityQueryCreateForCurrentUser | CSIdentityQueryCreateForCurrentUser |

---

Creates a query for the current session user's identity

```
extern CSIdentityQueryRef CSIdentityQueryCreateForCurrentUser(
    CFAllocatorRef allocator );
```

##### Parameters

**`allocator`**
: The allocator to use for this instance

##### Return Value

A new CSIdentityQuery object

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryCreateForName | CSIdentityQueryCreateForName | CSIdentityQueryCreateForName | CSIdentityQueryCreateForName | CSIdentityQueryCreateForName |

---

Creates an identity query object based on a name

```
extern CSIdentityQueryRef CSIdentityQueryCreateForName(
    CFAllocatorRef allocator,
    CFStringRef name,
    CSIdentityQueryStringComparisonMethod comparisonMethod,
    CSIdentityClass identityClass,
    CSIdentityAuthorityRef authority );
```

##### Parameters

**`allocator`**
: The allocator to use for this instance

**`name`**
: The name criteria for the query.

**`comparisonMethod`**
: The comparision function (equal or begins with)

**`identityClass`**
: The class of identity to find

**`authority`**
: The identity authority to query

##### Return Value

A new CSIdentityQuery object

##### Discussion

The query finds identities by name. It searches the full names, posix names and aliases for matches.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryCreateForPersistentReference | CSIdentityQueryCreateForPersistentReference | CSIdentityQueryCreateForPersistentReference | CSIdentityQueryCreateForPersistentReference | CSIdentityQueryCreateForPersistentReference |

---

Creates an identity query object based on an identity reference data object

```
extern CSIdentityQueryRef CSIdentityQueryCreateForPersistentReference(
    CFAllocatorRef allocator,
    CFDataRef referenceData );
```

##### Parameters

**`allocator`**
: The allocator to use for this instance

**`referenceData`**
: The reference data that fully describes an identity

##### Return Value

A new CSIdentityQuery object

##### Discussion

Finds an identity by reference data obtained from CSIdentityCreateReferenceData

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryCreateForPosixID | CSIdentityQueryCreateForPosixID | CSIdentityQueryCreateForPosixID | CSIdentityQueryCreateForPosixID | CSIdentityQueryCreateForPosixID |

---

Creates an identity query object based on a POSIX ID

```
extern CSIdentityQueryRef CSIdentityQueryCreateForPosixID(
    CFAllocatorRef allocator,
    id_t posixID,
    CSIdentityClass identityClass,
    CSIdentityAuthorityRef authority );
```

##### Parameters

**`allocator`**
: The allocator to use for this instance

**`posixID`**
: The UID or GID of the identity to find

**`identityClass`**
: The class of identity to find

**`authority`**
: The identity authority to query

##### Return Value

A new CSIdentityQuery object

##### Discussion

Finds an identity by its UID or GID

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryCreateForUUID | CSIdentityQueryCreateForUUID | CSIdentityQueryCreateForUUID | CSIdentityQueryCreateForUUID | CSIdentityQueryCreateForUUID |

---

Creates an identity query object based on a UUID

```
extern CSIdentityQueryRef CSIdentityQueryCreateForUUID(
    CFAllocatorRef allocator,
    CFUUIDRef uuid,
    CSIdentityAuthorityRef authority );
```

##### Parameters

**`allocator`**
: The allocator to use for this instance

**`uuid`**
: The UUID of the identity to find

**`authority`**
: The identity authority to query

##### Return Value

A new CSIdentityQuery object

##### Discussion

Finds an identity by its UUID

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryExecute | CSIdentityQueryExecute | CSIdentityQueryExecute | CSIdentityQueryExecute | CSIdentityQueryExecute |

---

Execute an identity query synchronously

```
extern Boolean CSIdentityQueryExecute(
    CSIdentityQueryRef query,
    CSIdentityQueryFlags flags,
    CFErrorRef *error );
```

##### Parameters

**`query`**
: The query object to execute

**`flags`**
: Execution options

**`error`**
: Optional pointer to a CFError object which must be released by the caller if CSIdentityQueryExecute returns false

##### Return Value

Returns true if the query executed successfully, false if an error occurred.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryExecuteAsynchronously | CSIdentityQueryExecuteAsynchronously | CSIdentityQueryExecuteAsynchronously | CSIdentityQueryExecuteAsynchronously | CSIdentityQueryExecuteAsynchronously |

---

Execute an identity query asynchronously

```
extern Boolean CSIdentityQueryExecuteAsynchronously(
    CSIdentityQueryRef query,
    CSIdentityQueryFlags flags,
    const CSIdentityQueryClientContext *clientContext,
    CFRunLoopRef runLoop,
    CFStringRef runLoopMode );
```

##### Parameters

**`query`**
: The query object to execute

**`flags`**
: Execution options

**`clientContext`**
: The client context and callbacks to be used during execution

**`runLoop`**
: The run loop on which to schedule callbacks

**`runLoopMode`**
: The run loop mode in which callbacks may be scheduled

##### Return Value

Returns true if query execution started, false if the query has already been executed.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryGetTypeID | CSIdentityQueryGetTypeID | CSIdentityQueryGetTypeID | CSIdentityQueryGetTypeID | CSIdentityQueryGetTypeID |

---

Retrieve the CFTypeID of the CSIdentityQuery class

```
extern CFTypeID CSIdentityQueryGetTypeID(
    void );
```

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryStop | CSIdentityQueryStop | CSIdentityQueryStop | CSIdentityQueryStop | CSIdentityQueryStop |

---

Invalidate an identity query client

```
extern void CSIdentityQueryStop(
    CSIdentityQueryRef query );
```

##### Parameters

**`query`**
: The query to access

##### Discussion

Invalidate a query client so that its callback will never be called in the future. Clients
should call CSIdentityQueryStop when an query will no longer be used, prior to releasing the final query reference.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryReceiveEventCallback | CSIdentityQueryReceiveEventCallback | CSIdentityQueryReceiveEventCallback | CSIdentityQueryReceiveEventCallback | CSIdentityQueryReceiveEventCallback |

---

The client event callback function for receiving asynchronous query events

```
typedef extern void ( *CSIdentityQueryReceiveEventCallback )(
    CSIdentityQueryRef query,
    CSIdentityQueryEvent event,
    CFArrayRef identities,
    CFErrorRef error,
    void *info );
```

##### Parameters

> **`query`**
> : The identity query object that has completed an event
>
> **`event`**
> : The event the identity query object has completed
>
> **`identities`**
> : a CFArray containing identities resulting from the query
>
> **`error`**
> : A CFError object if there was an error from the query
>
> **`info`**
> : Any other information you want passed to the callback function

## Structs and Unions

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryClientContext | CSIdentityQueryClientContext | CSIdentityQueryClientContext | CSIdentityQueryClientContext | CSIdentityQueryClientContext |

---

Client structure specifying callbacks and private context data

```
struct CSIdentityQueryClientContext {
    CFIndex version;
    void *info;
    CFAllocatorRetainCallBack retainInfo;
    CFAllocatorReleaseCallBack releaseInfo;
    CFAllocatorCopyDescriptionCallBack copyInfoDescription;
    CSIdentityQueryReceiveEventCallback receiveEvent;
};
```

## Enumerations

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryEvent | CSIdentityQueryEvent | CSIdentityQueryEvent | CSIdentityQueryEvent | CSIdentityQueryEvent |

---

Results from executing an asynchronous query

```
enum {
    kCSIdentityQueryEventSearchPhaseFinished = 1,
    kCSIdentityQueryEventResultsAdded = 2,
    kCSIdentityQueryEventResultsChanged = 3,
    kCSIdentityQueryEventResultsRemoved = 4,
    kCSIdentityQueryEventErrorOccurred = 5
};
```

##### Constants

> **`kCSIdentityQueryEventSearchPhaseFinished`**
> : Event generated when the initial lookup of identities has finished.
> Live update events will follow if caller requests the kCSIdentityQueryGenerateUpdateEvents option.
>
> **`kCSIdentityQueryEventResultsAdded`**
> : Event generated when identities are added to the query results
>
> **`kCSIdentityQueryEventResultsChanged`**
> : Event generated when identities already in the query results have been modified
>
> **`kCSIdentityQueryEventResultsRemoved`**
> : Event generated when identities are removed from the query results
>
> **`kCSIdentityQueryEventErrorOccurred`**
> : Used to report an error. Query execution stops (permanently) if this event is sent.

##### Discussion

Events generated during asynchronous query execution

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryFlags | CSIdentityQueryFlags | CSIdentityQueryFlags | CSIdentityQueryFlags | CSIdentityQueryFlags |

---

Execution options for an identity query

```
enum {
    kCSIdentityQueryGenerateUpdateEvents = 0x0001,
    kCSIdentityQueryIncludeHiddenIdentities = 0x0002
};
```

##### Constants

> **`kCSIdentityQueryGenerateUpdateEvents`**
> : After the intial query phase is complete, monitor the result set for live updates
>
> **`kCSIdentityQueryIncludeHiddenIdentities`**
> : Include all matching identities in the result set, including hidden "system" users and groups (root, www, etc.)

##### Discussion

A bit mask for setting execution options on a query

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CSIdentityQueryStringComparisonMethod | CSIdentityQueryStringComparisonMethod | CSIdentityQueryStringComparisonMethod | CSIdentityQueryStringComparisonMethod | CSIdentityQueryStringComparisonMethod |

---

Options for querying the database by name

```
enum {
    kCSIdentityQueryStringEquals = 1,
    kCSIdentityQueryStringBeginsWith = 2
};
```

##### Constants

> **`kCSIdentityQueryStringEquals`**
> : The identity name must equal the search string
>
> **`kCSIdentityQueryStringBeginsWith`**
> : The identity name must begin with the search string

##### Discussion

When searching for identities by name, this value specifies the string comparison function

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Last Updated: 2008-03-11
