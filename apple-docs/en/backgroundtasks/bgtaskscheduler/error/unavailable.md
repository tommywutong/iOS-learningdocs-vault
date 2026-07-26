---
title: unavailable
framework: Background Tasks
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgtaskscheduler/error/unavailable
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/unavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgtaskscheduler/error/unavailable.json'
content_hash: 'sha256:ac8767772b099479'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Background Tasks](../../../backgroundtasks.md) · [BGTaskScheduler](../../bgtaskscheduler.md) · [Error](../error.md)

# unavailable

<sub>Type Property</sub>

A task scheduling error that indicates the app or extension can’t schedule background work.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var unavailable: BGTaskScheduler.Error.Code { get }
```

## Discussion

This error usually occurs for one of three reasons:

- A person disabled background refresh in settings.
- The app runs on Simulator which doesn’t support background processing.
- The extension either didn’t set [RequestsOpenAccess](../../../bundleresources/information-property-list/nsextension/nsextensionattributes/requestsopenaccess.md) to `YES` in [The Info.plist File](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22), or a person didn’t grant open access.

## See Also

### Getting the error codes

- [Code](code.md) — An enumeration of the task scheduling errors.
- [notPermitted](notpermitted.md) — A task scheduling error that indicates the app isn’t permitted to launch the task.
- [tooManyPendingTaskRequests](toomanypendingtaskrequests.md) — A task scheduling error that indicates there are too many pending tasks of the type requested.
