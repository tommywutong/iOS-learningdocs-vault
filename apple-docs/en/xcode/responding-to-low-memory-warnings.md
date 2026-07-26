---
title: Responding to low-memory warnings
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/responding-to-low-memory-warnings
source_url: 'https://developer.apple.com/documentation/xcode/responding-to-low-memory-warnings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/responding-to-low-memory-warnings.json'
content_hash: 'sha256:28673d365e4eefa4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s memory use](reducing-your-app-s-memory-use.md)

# Responding to low-memory warnings

<sub>Article</sub>

Detect when your app is using excessive memory, and bring memory use under control.

## Overview

iOS sends your app a warning when its memory use approaches the limit of available device memory. The amount of memory use that triggers a memory warning corresponds to the yellow region in Xcode’s memory gauge. Your app can receive a memory warning in any of these ways:

- UIKit calls the [applicationDidReceiveMemoryWarning(_:)](<../uikit/uiapplicationdelegate/applicationdidreceivememorywarning(__).md>) method of your app delegate.
- UIKit calls the [didReceiveMemoryWarning()](<../uikit/uiviewcontroller/didreceivememorywarning().md>) method of active [UIViewController](../uikit/uiviewcontroller.md) objects.
- iOS posts [didReceiveMemoryWarningNotification](../uikit/uiapplication/didreceivememorywarningnotification.md) to the default notification center.
- Dispatch queues receive an event with source type [DISPATCH_SOURCE_TYPE_MEMORYPRESSURE](../dispatch/dispatch_source_type_memorypressure.md).

The operating system sends low-memory warnings using a best-effort approach, and your app needs to respond to them as quickly as possible. If memory demand on the system increases faster than the warnings relieve memory pressure, the system may not have time to send the low-memory warnings and wait for apps to respond. When this occurs, the system resorts to jettisoning apps to reclaim their memory and recording the reason in a log file, as described in [Identifying high-memory use with jetsam event reports](identifying-high-memory-use-with-jetsam-event-reports.md).

Make sure your app changes its approach for allocating memory when it receives a memory warning—adopting a conservative policy of looking for opportunities to release objects or reduce their size as it uses them. If your app allocates large amounts of memory at once and crashes before it receives the low-memory warning during the large allocation, modify your code to slowly allocate the necessary memory, so the system has adequate time to free memory from across the system.

If your app loads data it can easily recreate, consider using [NSPurgeableData](../foundation/nspurgeabledata.md). When the contents of [NSPurgeableData](../foundation/nspurgeabledata.md) aren’t marked as in-use through [beginContentAccess()](<../foundation/nsdiscardablecontent/begincontentaccess().md>), the system automatically discards the contents in low-memory situations. This automatic discard process helps your app react to a low-memory warnings more quickly, because the kernel handles discarding the data, rather than your app, which is waiting to receive the low-memory notification before discarding the data.

> [!important] Important
> Don’t traverse your app’s whole object graph looking for memory to release when your app receives a memory warning, and avoid using [NSCache](../foundation/nscache.md) in connection with [NSPurgeableData](../foundation/nspurgeabledata.md). iOS compresses memory pages that apps haven’t accessed recently. Searching for memory to purge brings these pages out of the compressor, and increases memory demands on the system.

## See Also

### Related Documentation

- [Identifying high-memory use with jetsam event reports](identifying-high-memory-use-with-jetsam-event-reports.md) — Discover why the operating system terminated your app when available memory was low.

### Tasks

- [Gathering information about memory use](gathering-information-about-memory-use.md) — Identify memory-use inefficiencies by measuring and profiling your app.
- [Making changes to reduce memory use](making-changes-to-reduce-memory-use.md) — Decrease your app’s use of memory by addressing common causes of excessive use.
- [Preventing memory-use regressions](preventing-memory-use-regressions.md) — Measure the memory that your app’s features use, and detect increases by using XCTest performance tests.
