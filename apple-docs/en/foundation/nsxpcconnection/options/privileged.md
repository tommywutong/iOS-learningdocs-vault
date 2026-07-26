---
title: privileged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/options/privileged
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/options/privileged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/options/privileged.json'
content_hash: 'sha256:4983c36ce6770573'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSXPCConnection](../../nsxpcconnection.md) · [Options](../options.md)

# privileged

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var privileged: NSXPCConnection.Options { get }
```

## Discussion

Use this option if connecting to a service in the privileged Mach bootstrap (for example, a daemon with a `launchd.plist` in `/Library/LaunchDaemons)`.
