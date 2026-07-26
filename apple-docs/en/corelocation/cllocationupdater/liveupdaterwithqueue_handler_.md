---
title: 'liveUpdaterWithQueue:handler:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationupdater/liveupdaterwithqueue:handler:'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdater/liveupdaterwithqueue:handler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdater/liveupdaterwithqueue%3Ahandler%3A.json'
content_hash: 'sha256:31f6402495a7fc94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationUpdater](../cllocationupdater.md)

# liveUpdaterWithQueue:handler:

<sub>Type Method</sub>

Creates a location updater on the queue you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) liveUpdaterWithQueue:(dispatch_queue_t) queue handler:(void (^)(CLUpdate *update)) handler;
```

## Parameters

- `queue` — Specifies the queue to which the framework submits the handler with each available update

- `handler` — The block that the framework invokes with each update.

## Return Value

Returns a location updater instance with the specified queue and update handler.

## See Also

### Creating a location updater

- [liveUpdaterWithConfiguration:queue:handler:](liveupdaterwithconfiguration_queue_handler_.md) — Creates a location updater with the configuration and queue that you specify.
- [CLLiveUpdateConfiguration](../clliveupdateconfiguration.md) — Specifies the types of locations that a location updater generates.
