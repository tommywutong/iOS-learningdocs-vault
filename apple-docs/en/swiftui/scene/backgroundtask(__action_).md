---
title: 'backgroundTask(_:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/backgroundtask(_:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/backgroundtask(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/backgroundtask%28_%3Aaction%3A%29.json'
content_hash: 'sha256:8c53ff3e77227b87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# backgroundTask(_:action:)

<sub>Instance Method</sub>

Runs the specified action when the system provides a background task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func backgroundTask<D, R>(_ task: BackgroundTask<D, R>, action: @escaping @Sendable (D) async -> R) -> some Scene where D : Sendable, R : Sendable

```

## Parameters

- `task` — The type of task with which to associate the provided action.

- `action` — An async closure that the system runs for the specified task type.

## Discussion

When the system wakes your app or extension for one or more background tasks, it will call any actions associated with matching tasks. When your async actions return, the system put your app back into a suspended state. The system considers the task completed when the action closure that you provide returns. If the action closure has not returned when the task runs out of time to complete, the system cancels the task. Use [withTaskCancellationHandler(operation:onCancel:isolation:)](<../../swift/withtaskcancellationhandler(operation_oncancel_isolation_).md>) to observe whether the task is low on runtime.

```swift
/// An example of a Weather Application.
struct WeatherApp: App {
    var body: some Scene {
        WindowGroup {
            Text("Responds to App Refresh")
        }
        .backgroundTask(.appRefresh("WEATHER_DATA")) {
            await updateWeatherData()
        }
    }
    func updateWeatherData() async {
        // fetches new weather data and updates app state
    }
}
```

## See Also

### Handling background tasks

- [BackgroundTask](../backgroundtask.md) — The kinds of background tasks that your app or extension can handle.
- [SnapshotData](../snapshotdata.md) — The associated data of a snapshot background task.
- [SnapshotResponse](../snapshotresponse.md) — Your application’s response to a snapshot background task.
