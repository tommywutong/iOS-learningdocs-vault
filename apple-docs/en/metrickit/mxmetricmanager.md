---
title: MXMetricManager
framework: MetricKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/metrickit/mxmetricmanager
source_url: 'https://developer.apple.com/documentation/metrickit/mxmetricmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metrickit/mxmetricmanager.json'
content_hash: 'sha256:342d3d6a81990b11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetricKit](../metrickit.md)

# MXMetricManager

<sub>Class</sub>

The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.

> [!warning] Deprecated
> Use [MetricManager](metricmanager.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MXMetricManager
```

## Overview

The `MXMetricManager` shared object manages your subscription for receiving on-device daily metrics. It receives daily metric reports when the device your app is installed on is running iOS 13 and later or macOS 26 and later.

MetricKit starts accumulating reports for your app after calling [sharedManager](mxmetricmanager/shared.md) for the first time. To receive the reports, call [- addSubscriber:](<mxmetricmanager/add(__).md>) with an object that adopts the [MXMetricManagerSubscriber](mxmetricmanagersubscriber.md) protocol. The system delivers metric reports at most once per day per metric source, and diagnostic reports immediately in iOS 15 and later and macOS 12 and later. Some metrics originate from different system sources and arrive in a separate payload, so your app may receive more than one metric payload per day. The reports contain the metrics from the past 24 hours and any previously undelivered daily reports. To pause receiving reports, call [- removeSubscriber:](<mxmetricmanager/remove(__).md>).

Calls to add a subscriber and to receive reports are safe to use in performance-sensitive code, such as during app launch.

The following example shows a class that subscribes to and receives MetricKit reports.

```swift
class AppMetrics: NSObject, MXMetricManagerSubscriber {
    func receiveReports() {
       let manager = MXMetricManager.shared
       manager.add(self)
    }

    func pauseReports() {
       let manager = MXMetricManager.shared
       manager.remove(self)
    }

    // Receive daily metrics.
    func didReceive(_ payloads: [MXMetricPayload]) {
       // Process metrics.
    }

    // Receive diagnostics immediately when available.
    func didReceive(_ payloads: [MXDiagnosticPayload]) {
       // Process diagnostics.
    }
}

```

> [!note] Note
> To test MetricKit in your app, run your app on a physical device to receive metric reports and `didReceive(_:)` callbacks.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the shared metrics manager

- [sharedManager](mxmetricmanager/shared.md) — An object that returns the shared metrics manager instance. _(deprecated)_

### Subscribing to reports

- [- addSubscriber:](<mxmetricmanager/add(__).md>) — Registers to receive a daily report of app metrics from the metrics manager. _(deprecated)_
- [- removeSubscriber:](<mxmetricmanager/remove(__).md>) — Unsubscribes from daily reports of app metrics. _(deprecated)_

### Retrieving previous reports

- [pastPayloads](mxmetricmanager/pastpayloads.md) — Returns an array of the daily metrics reports generated since the last allocation of the shared manager instance. _(deprecated)_
- [pastDiagnosticPayloads](mxmetricmanager/pastdiagnosticpayloads.md) — The diagnostic reports since the last initialization of the shared manager instance. _(deprecated)_

### Creating custom metric logs

- [+ makeLogHandleWithCategory:](<mxmetricmanager/makeloghandle(category_).md>) — Returns a log handle used for writing custom metric events. _(deprecated)_

### Measuring an extended launch

- [+ extendLaunchMeasurementForTaskID:error:](<mxmetricmanager/extendlaunchmeasurement(fortaskid_).md>) — Starts to measure an extended launch task with the given task identifier. _(deprecated)_
- [+ finishExtendedLaunchMeasurementForTaskID:error:](<mxmetricmanager/finishextendedlaunchmeasurement(fortaskid_).md>) — Signals the end of an extended launch task. _(deprecated)_
- [MXLaunchTaskID](mxlaunchtaskid.md) — The task identifier to track launch measurements. _(deprecated)_

## See Also

### Metric and diagnostic reports

- [MXMetricPayload](mxmetricpayload.md) — An object that encapsulates a daily metrics report. _(deprecated)_
- [MXDiagnosticPayload](mxdiagnosticpayload.md) — An object that encapsulates a diagnostic report. _(deprecated)_
- [MXMetricManagerSubscriber](mxmetricmanagersubscriber.md) — A protocol defining a method for receiving a daily metrics report. _(deprecated)_
