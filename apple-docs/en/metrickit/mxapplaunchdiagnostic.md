---
title: MXAppLaunchDiagnostic
framework: MetricKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/metrickit/mxapplaunchdiagnostic
source_url: 'https://developer.apple.com/documentation/metrickit/mxapplaunchdiagnostic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metrickit/mxapplaunchdiagnostic.json'
content_hash: 'sha256:c8431405b6ed44ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MetricKit](../metrickit.md)

# MXAppLaunchDiagnostic

<sub>Class</sub>

A diagnostic subclass that encapsulates app launch diagnostic reports.

> [!warning] Deprecated
> Use [AppLaunchDiagnostic](applaunchdiagnostic.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class MXAppLaunchDiagnostic
```

## Relationships

- **Inherits From**: [MXDiagnostic](mxdiagnostic.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Reading app launch metrics

- [callStackTree](mxapplaunchdiagnostic/callstacktree.md) — The call stack tree associated with the app launch. _(deprecated)_
- [launchDuration](mxapplaunchdiagnostic/launchduration.md) — The total app launch duration. _(deprecated)_

## See Also

### Performance diagnostics

- [MXCPUExceptionDiagnostic](mxcpuexceptiondiagnostic.md) — An object representing a diagnostic report for a fatal or nonfatal CPU exception. _(deprecated)_
- [MXCrashDiagnostic](mxcrashdiagnostic.md) — An object representing a diagnostic report for an app crash. _(deprecated)_
- [MXHangDiagnostic](mxhangdiagnostic.md) — An object representing a diagnostic report for an app that is too busy to handle user input responsively. _(deprecated)_
- [MXDiskWriteExceptionDiagnostic](mxdiskwriteexceptiondiagnostic.md) — An object representing a diagnostic report for a disk write exception. _(deprecated)_
