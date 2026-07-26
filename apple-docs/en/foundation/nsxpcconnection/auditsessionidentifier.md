---
title: auditSessionIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/auditsessionidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/auditsessionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/auditsessionidentifier.json'
content_hash: 'sha256:c6bb08486eddab12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# auditSessionIdentifier

<sub>Instance Property</sub>

The BSM audit session identifier for the connecting process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var auditSessionIdentifier: au_asid_t { get }
```

## Discussion

This attribute may be used by the listener delegate to accept or reject connections.

## See Also

### Working with security attributes

- [processIdentifier](processidentifier.md) — The process ID (PID) of the connecting process.
- [effectiveGroupIdentifier](effectivegroupidentifier.md) — The effective group ID (EGID) of the connecting process.
- [effectiveUserIdentifier](effectiveuseridentifier.md) — The effective user ID (EUID) of the connecting process.
