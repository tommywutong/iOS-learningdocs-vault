---
title: notPermitted
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/error/notpermitted
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/notpermitted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/error/notpermitted.json'
content_hash: 'sha256:5a763b2a444c1b24'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Background Tasks](../../../backgroundtasks.md) · [BGTaskScheduler](../../bgtaskscheduler.md) · [Error](../error.md)

# notPermitted

<sub>Type Property</sub>

A task scheduling error that indicates the app isn’t permitted to launch the task.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var notPermitted: BGTaskScheduler.Error.Code { get }
```

## Discussion

There are two causes for this error:

- The app didn’t set the appropriate mode in the [UIBackgroundModes](../../../bundleresources/information-property-list/uibackgroundmodes.md) array.
- The task identifier of the submitted task wasn’t in the [BGTaskSchedulerPermittedIdentifiers](../../../bundleresources/information-property-list/bgtaskschedulerpermittedidentifiers.md) array in [The Info.plist File](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22).

## See Also

### Getting the error codes

- [Code](code.md) — An enumeration of the task scheduling errors.
- [tooManyPendingTaskRequests](toomanypendingtaskrequests.md) — A task scheduling error that indicates there are too many pending tasks of the type requested.
- [unavailable](unavailable.md) — A task scheduling error that indicates the app or extension can’t schedule background work.
