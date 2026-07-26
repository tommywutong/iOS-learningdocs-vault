---
title: registryDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsimagerep/registrydidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsimagerep/registrydidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsimagerep/registrydidchangenotification.json'
content_hash: 'sha256:19657968c752c6d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSImageRep](../nsimagerep.md)

# registryDidChangeNotification

<sub>Type Property</sub>

Posted whenever the image representation class registry changes.

<sub>macOS</sub>

```swift
class let registryDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the image class that is registered or unregistered. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [RegistryDidChangeMessage](registrydidchangemessage.md).
