---
title: Setting Up Your Carbon Application to Use the Services Menu
apple_id: TP30000993
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-12-10'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/appservices/appendixa/servicesappendixa.html
archived_at: '2026-07-15T05:24:48.423514Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Setting Up Your Carbon Application to Use the Services Menu](Introduction%20to%20Setting%20Up%20Your%20Carbon%20Application%20to%20Use%20the%20Services%20Menu.md)


[Next](Document%20Revision%20History.md)[Previous](Application%20Services%20Tasks.md)

# Carbon Events for Services

This chapter outlines the Carbon event classes, kinds, and parameters your application needs to install Carbon event handlers for services events. For more information on Carbon events, see the documentation for the Carbon Event Manager on the Carbon Developer Documentation website.

There are four event kinds associated with the Carbon event class `kEventClassService`.

__Table A-1__  Event classes and kinds used by application services

| Event Class | Event Kind | Means |
| `kEventClassService` | `kEventServiceCopy` | Copy event |
|  | `kEventServicePaste` | Paste event |
|  | `kEventServiceGetTypes` | Get data types handled by the calling application |
|  | `kEventServicePerform` | An application is requesting a service |

The Carbon event parameters that are available for a services event vary depending on the kind of the services event.

__Table A-2__  Carbon event parameters for service events

| Event Kind | Event Parameter | Type |
| `kEventServiceGetTypes` | `kEventParamServiceCopyTypes` | `typeCFMutableArrayRef` |
|  | `kEventParamServicePasteTypes` | `typeCFMutableArrayRef` |
| `kEventServiceCopy` | `kEventParamScrapRef` | `typeScrapRef` |
| `kEventServicePaste` | `kEventParamScrapRef` | `typeScrapRef` |
| `kEventServicePerform` | `kEventParamScrapRef` | `typeScrapRef` |
|  | `kEventParamServiceMessageName` | `typeCFStringRef` |
|  | `kEventParamServiceUserData` | `typeCFStringRef` |

[Next](Document%20Revision%20History.md)[Previous](Application%20Services%20Tasks.md)

