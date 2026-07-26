---
title: NSXPCConnectionCodeSigningRequirementFailure
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnectioncodesigningrequirementfailure-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnectioncodesigningrequirementfailure-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnectioncodesigningrequirementfailure-swift.var.json'
content_hash: 'sha256:4d10a135ca877763'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCConnectionCodeSigningRequirementFailure

<sub>Global Variable</sub>

A code-signing requirement check failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSXPCConnectionCodeSigningRequirementFailure: Int { get }
```

## Discussion

This error represents a failure to meet the requirement set by a call to [NSXPCConnection](nsxpcconnection.md)‘s [- setCodeSigningRequirement:](<nsxpcconnection/setcodesigningrequirement(__).md>) method, or NSXPCConnectionListener’s [- setConnectionCodeSigningRequirement:](<nsxpclistener/setconnectioncodesigningrequirement(__).md>) method.

## See Also

### Error codes

- [NSXPCConnectionInterrupted](nsxpcconnectioninterrupted-swift.var.md) — The XPC connection was interrupted.
- [NSXPCConnectionInvalid](nsxpcconnectioninvalid-swift.var.md) — The XPC connection was invalid.
- [NSXPCConnectionReplyInvalid](nsxpcconnectionreplyinvalid-swift.var.md) — The XPC connection reply was invalid.
- [NSXPCConnectionErrorMinimum](nsxpcconnectionerrorminimum-swift.var.md) — The lower bounds of XPC connection error code values.
- [NSXPCConnectionErrorMaximum](nsxpcconnectionerrormaximum-swift.var.md) — The upper bounds of XPC connection error code values.
