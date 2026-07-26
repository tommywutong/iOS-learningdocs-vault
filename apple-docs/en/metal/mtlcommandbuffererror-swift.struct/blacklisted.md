---
title: blacklisted
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlcommandbuffererror-swift.struct/blacklisted
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffererror-swift.struct/blacklisted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffererror-swift.struct/blacklisted.json'
content_hash: 'sha256:74493a3da753dfe5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBufferError](../mtlcommandbuffererror-swift.struct.md)

# blacklisted

<sub>Type Property</sub>

A former error code that indicates the system has revoked the Metal device’s access because it’s responsible for too many timeouts or hangs.

> [!warning] Deprecated
> Use [accessRevoked](accessrevoked.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var blacklisted: MTLCommandBufferError.Code { get }
```
