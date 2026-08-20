---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.016.html
archived_at: '2026-07-15T07:58:29.166750Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.015.md)

## New Methods to Support Multithreading

To support the writing of multithreaded applications, the following methods have been added to the following classes:

|  WOApplication |  |
|  Method |  Description |
|  adaptorsDispatchRequestsConcurrently |  Returns YES or true if at least one adaptor contains multiple threads and will attempt to concurrently invoke the request handlers. |
|  allowsConcurrentRequestHandling |  Specifies whether the application has been written to be able to safely handle concurrent requests. By default, returns NO or false. Subclasses should override to return YES or true if the application is written to be thread-safe. |
|  isConcurrentRequestHandlingEnabled |  Returns YES or true if the application can handle concurrent requests and the adaptor will dispatch requests to the application concurrently. |
|  lockRequestHandling |  Serializes request handler access through the use of an internal lock if concurrent request handling is disabled. Request handlers should invoke this method before calling into application code. |
|  unlockRequestHandling |  Removes the request handling internal lock to allow access to the request handler again. |
|  lock |  Locks access to the WOApplication object. |
|  unlock |  Unlocks access to the WOApplication object. |

```
```

|  WORequestHandler |  |
|  Method |  Description |
|  lock |  Locks access to the WORequestHandler object |
|  unlock |  Unlocks access to the WORequestHandler object |

```
```

|  WOResourceManager |  |
|  Method |  Description |
|  lock |  Locks access to the WOResourceManager object. |
|  unlock |  Unlocks access to the WOResourceManager object. |

```
```

|  WOSessionStore |  |
|  Method |  Description |
|  checkOutSessionWithSessionID:request: (checkOutSessionWithSessionID in Java) |  Checks out a session for exclusive use. When you check a session out, all other access to that session is blocked until the session is checked in again. |
|  checkInSessionForContext: |  Checks in a session. |

```
```

|  WOStatisticsStore |  |
|  Method |  Description |
|  lock |  Locks access to the WOStatisticsStore object. |
|  unlock |  Unlocks access to the WOStatisticsStore object. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Direct%20Actions.md)
