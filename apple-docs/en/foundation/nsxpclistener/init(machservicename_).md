---
title: 'init(machServiceName:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpclistener/init(machservicename:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener/init(machservicename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener/init%28machservicename%3A%29.json'
content_hash: 'sha256:1e7d8de4ff0060e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCListener](../nsxpclistener.md)

# init(machServiceName:)

<sub>Initializer</sub>

Initializes a listener in a LaunchAgent or LaunchDaemon which has a name advertised in a `launchd.plist` file.

<sub>macOS</sub>

```swift
init(machServiceName name: String)
```

## Discussion

For example, you might use this in an agent launched by launchd with a `launchd.plist` contained in `~/Library/LaunchAgents`, or a daemon launched by launchd with a `launchd.plist` contained in `/Library/LaunchDaemons`.
