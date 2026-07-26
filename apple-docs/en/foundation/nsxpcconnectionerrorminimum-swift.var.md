---
title: NSXPCConnectionErrorMinimum
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnectionerrorminimum-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnectionerrorminimum-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnectionerrorminimum-swift.var.json'
content_hash: 'sha256:818312be7ee0bb50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCConnectionErrorMinimum

<sub>Global Variable</sub>

The lower bounds of XPC connection error code values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSXPCConnectionErrorMinimum: Int { get }
```

## Discussion

All XPC error codes have values between [NSXPCConnectionErrorMinimum](nsxpcconnectionerrorminimum-swift.var.md) and [NSXPCConnectionErrorMaximum](nsxpcconnectionerrormaximum-swift.var.md), exclusive. This constant does not correspond to any particular error.

## See Also

### Error codes

- [NSXPCConnectionInterrupted](nsxpcconnectioninterrupted-swift.var.md) — The XPC connection was interrupted.
- [NSXPCConnectionInvalid](nsxpcconnectioninvalid-swift.var.md) — The XPC connection was invalid.
- [NSXPCConnectionReplyInvalid](nsxpcconnectionreplyinvalid-swift.var.md) — The XPC connection reply was invalid.
- [NSXPCConnectionErrorMaximum](nsxpcconnectionerrormaximum-swift.var.md) — The upper bounds of XPC connection error code values.
- [NSXPCConnectionCodeSigningRequirementFailure](nsxpcconnectioncodesigningrequirementfailure-swift.var.md) — A code-signing requirement check failed.
