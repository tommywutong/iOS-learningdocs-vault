---
title: NSXPCConnectionCodeSigningRequirementFailure
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnectioncodesigningrequirementfailure-c.enum.case
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnectioncodesigningrequirementfailure-c.enum.case'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnectioncodesigningrequirementfailure-c.enum.case.json'
content_hash: 'sha256:34793260840238ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCConnectionCodeSigningRequirementFailure

<sub>Enumeration Case</sub>

A code-signing requirement check failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSXPCConnectionCodeSigningRequirementFailure
```

## Discussion

This error represents a failure to meet the requirement set by a call to [NSXPCConnection](nsxpcconnection.md)‘s [- setCodeSigningRequirement:](<nsxpcconnection/setcodesigningrequirement(__).md>) method, or NSXPCConnectionListener’s [- setConnectionCodeSigningRequirement:](<nsxpclistener/setconnectioncodesigningrequirement(__).md>) method.

## See Also

### Error codes

- [NSXPCConnectionInterrupted](nsxpcconnectioninterrupted-c.enum.case.md) — The XPC connection was interrupted.
- [NSXPCConnectionInvalid](nsxpcconnectioninvalid-c.enum.case.md) — The XPC connection was invalid.
- [NSXPCConnectionReplyInvalid](nsxpcconnectionreplyinvalid-c.enum.case.md) — The XPC connection reply was invalid.
- [NSXPCConnectionErrorMinimum](nsxpcconnectionerrorminimum-c.enum.case.md) — The lower bounds of XPC connection error code values.
- [NSXPCConnectionErrorMaximum](nsxpcconnectionerrormaximum-c.enum.case.md) — The upper bounds of XPC connection error code values.
