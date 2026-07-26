---
title: MXAppLaunchMetric
framework: MetricKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/metrickit/mxapplaunchmetric
source_url: 'https://developer.apple.com/documentation/metrickit/mxapplaunchmetric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metrickit/mxapplaunchmetric.json'
content_hash: 'sha256:ee83abe7210e0d11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetricKit](../metrickit.md)

# MXAppLaunchMetric

<sub>Class</sub>

An object representing metrics about app launch time.

> [!warning] Deprecated
> Use [MetricResult](metricresult.md), and read the [TimeToFirstDrawMetric](timetofirstdrawmetric.md), [OptimizedTimeToFirstDrawMetric](optimizedtimetofirstdrawmetric.md), [ApplicationResumeTimeMetric](applicationresumetimemetric.md), or [ExtendedLaunchMetric](extendedlaunchmetric.md) cases instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MXAppLaunchMetric
```

## Relationships

- **Inherits From**: [MXMetric](mxmetric.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Viewing app launch and resume time

- [histogrammedOptimizedTimeToFirstDraw](mxapplaunchmetric/histogrammedoptimizedtimetofirstdraw.md) — A histogram of the different amounts of time associated with prewarmed app launches. _(deprecated)_
- [histogrammedTimeToFirstDraw](mxapplaunchmetric/histogrammedtimetofirstdraw.md) — A histogram of the different amounts of time taken to launch the app. _(deprecated)_
- [histogrammedApplicationResumeTime](mxapplaunchmetric/histogrammedapplicationresumetime.md) — A histogram of the different amounts of time taken to resume the app from the background. _(deprecated)_
- [histogrammedExtendedLaunch](mxapplaunchmetric/histogrammedextendedlaunch.md) — A histogram of the different amounts of time taken to launch the app, including the extended launch tasks. _(deprecated)_

## See Also

### Responsiveness metrics

- [MXAnimationMetric](mxanimationmetric.md) — An object representing metrics about the responsiveness of animation in the app. _(deprecated)_
- [MXAppResponsivenessMetric](mxappresponsivenessmetric.md) — An object representing metrics about the responsiveness of the app to user interaction. _(deprecated)_
- [MXLaunchTaskID](mxlaunchtaskid.md) — The task identifier to track launch measurements. _(deprecated)_
