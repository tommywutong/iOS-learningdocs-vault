---
title: 'liveUpdaterWithConfiguration:queue:handler:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationupdater/liveupdaterwithconfiguration:queue:handler:'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdater/liveupdaterwithconfiguration:queue:handler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdater/liveupdaterwithconfiguration%3Aqueue%3Ahandler%3A.json'
content_hash: 'sha256:7d154d49c76fafc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationUpdater](../cllocationupdater.md)

# liveUpdaterWithConfiguration:queue:handler:

<sub>Type Method</sub>

Creates a location updater with the configuration and queue that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) liveUpdaterWithConfiguration:(CLLiveUpdateConfiguration) configuration queue:(dispatch_queue_t) queue handler:(void (^)(CLUpdate *update)) handler;
```

## Parameters

- `configuration` — Specifies the live update configuration that the framework uses.

- `queue` — Specifies the queue to which the framework submits the handler with each available update.

- `handler` — The block that the framework invokes with each update.

## Return Value

Returns a location updater instance with the specified configuration, queue, and update handler.

## See Also

### Creating a location updater

- [liveUpdaterWithQueue:handler:](liveupdaterwithqueue_handler_.md) — Creates a location updater on the queue you specify.
- [CLLiveUpdateConfiguration](../clliveupdateconfiguration.md) — Specifies the types of locations that a location updater generates.
