---
title: SKDownloaderExtension
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skdownloaderextension
source_url: 'https://developer.apple.com/documentation/storekit/skdownloaderextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownloaderextension.json'
content_hash: 'sha256:42962036f2e136d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKDownloaderExtension

<sub>Protocol</sub>

An application extension that uses the system implementation to schedule Apple-hosted asset-pack downloads automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
@protocol SKDownloaderExtension <BAManagedDownloaderExtension>
```

## Overview

You can optionally implement the inherited `BAManagedDownloaderExtension` requirements, but don’t implement any of the inherited `BADownloaderExtension` requirements. For more information, see [Background Assets](../backgroundassets.md).

## Relationships

- **Inherits From**: [BAManagedDownloaderExtension](../backgroundassets/bamanageddownloaderextension.md)
