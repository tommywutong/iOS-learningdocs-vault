---
title: effectiveGroupIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/effectivegroupidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/effectivegroupidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/effectivegroupidentifier.json'
content_hash: 'sha256:9c55c8453a7d7fd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# effectiveGroupIdentifier

<sub>Instance Property</sub>

The effective group ID (EGID) of the connecting process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var effectiveGroupIdentifier: gid_t { get }
```

## Discussion

This attribute may be used by the listener delegate to accept or reject connections.

## See Also

### Working with security attributes

- [auditSessionIdentifier](auditsessionidentifier.md) — The BSM audit session identifier for the connecting process.
- [processIdentifier](processidentifier.md) — The process ID (PID) of the connecting process.
- [effectiveUserIdentifier](effectiveuseridentifier.md) — The effective user ID (EUID) of the connecting process.
