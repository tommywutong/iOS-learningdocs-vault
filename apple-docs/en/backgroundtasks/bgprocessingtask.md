---
title: BGProcessingTask
framework: Background Tasks
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/backgroundtasks/bgprocessingtask
source_url: 'https://developer.apple.com/documentation/backgroundtasks/bgprocessingtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/backgroundtasks/bgprocessingtask.json'
content_hash: 'sha256:bff3cdb4deb55fa1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Background Tasks](../backgroundtasks.md)

# BGProcessingTask

<sub>Class</sub>

A time-consuming processing task that runs while the app is in the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class BGProcessingTask
```

## Overview

Use processing tasks for long data updates, processing data, and app maintenance. Although processing tasks can run for minutes, the system can interrupt the process. Add an expiration handler by setting [expirationHandler](bgtask/expirationhandler.md) for any required cleanup.

Executing processing tasks requires setting the `processing` [UIBackgroundModes](../bundleresources/information-property-list/uibackgroundmodes.md) capability. For information on setting this capability, see [BGTaskScheduler](bgtaskscheduler.md).

Processing tasks run only when the device is idle. The system terminates any background processing tasks running when the user starts using the device. Background refresh tasks aren’t affected.

## Relationships

- **Inherits From**: [BGTask](bgtask.md)

- **Inherited By**: [BGHealthResearchTask](bghealthresearchtask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Background tasks

- [Using background tasks to update your app](../uikit/using-background-tasks-to-update-your-app.md) — Configure your app to perform tasks in the background to make efficient use of processing time and power.
- [Refreshing and Maintaining Your App Using Background Tasks](refreshing-and-maintaining-your-app-using-background-tasks.md) — Use scheduled background tasks for refreshing your app content and for performing maintenance.
- [Choosing Background Strategies for Your App](choosing-background-strategies-for-your-app.md) — Select the best method of scheduling background runtime for your app.
- [BGAppRefreshTask](bgapprefreshtask.md) — An object representing a short task typically used to refresh content that’s run while the app is in the background.
- [BGHealthResearchTask](bghealthresearchtask.md) — A time-consuming, necessary processing task that runs while the app is in the background to prepare data essential to a health research study.
