---
title: BackgroundTask
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/backgroundtask
source_url: 'https://developer.apple.com/documentation/swiftui/backgroundtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/backgroundtask.json'
content_hash: 'sha256:95b2d78d4e9562a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BackgroundTask

<sub>Structure</sub>

The kinds of background tasks that your app or extension can handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BackgroundTask<Request, Response>
```

## Overview

Use a value of this type with the [backgroundTask(_:action:)](<scene/backgroundtask(__action_).md>) scene modifier to create a handler for background tasks that the system sends to your app or extension. For example, you can use [urlSession](backgroundtask/urlsession.md) to define an asynchronous closure that the system calls when it launches your app or extension to handle a response from a background [URLSession](../foundation/urlsession.md).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Refreshing the app

- [appRefresh(_:)](<backgroundtask/apprefresh(__).md>) — A task that updates your app’s state in the background for a matching identifier.

### Receiving connectivity updates

- [bluetoothAlert](backgroundtask/bluetoothalert.md) — A background task used to receive critical alerts from paired bluetooth accessories.
- [watchConnectivity](backgroundtask/watchconnectivity.md) — A background task used to receive background updates from the Watch Connectivity framework.

### Responding to URL sessions

- [urlSession](backgroundtask/urlsession.md) — A task that responds to background URL sessions.
- [urlSession(_:)](<backgroundtask/urlsession(__).md>) — A task that responds to background URL sessions matching the given identifier.
- [urlSession(matching:)](<backgroundtask/urlsession(matching_).md>) — A task that responds to background URL sessions matching the given predicate.

### Updating intents and shortcuts

- [intentDidRun](backgroundtask/intentdidrun.md) — A background task used to update your app after a SiriKit intent runs.
- [relevantShortcut](backgroundtask/relevantshortcut.md) — A background task used to periodically donate relevant Siri shortcuts.

### Processing tasks

- [processingTask(_:)](<backgroundtask/processingtask(__).md>) — A task that processes tasks in the background. _(beta)_

### Deprecated symbols

- [appRefresh](backgroundtask/apprefresh.md) — A task that updates your app’s state in the background. _(deprecated)_
- [snapshot](backgroundtask/snapshot.md) — A background task used to update your app’s user interface in preparation for a snapshot.

## See Also

### Handling background tasks

- [backgroundTask(_:action:)](<scene/backgroundtask(__action_).md>) — Runs the specified action when the system provides a background task.
- [SnapshotData](snapshotdata.md) — The associated data of a snapshot background task.
- [SnapshotResponse](snapshotresponse.md) — Your application’s response to a snapshot background task.
