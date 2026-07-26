---
title: StoreDownloaderExtension
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/storedownloaderextension
source_url: 'https://developer.apple.com/documentation/storekit/storedownloaderextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storedownloaderextension.json'
content_hash: 'sha256:df24b68ba25bc06c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# StoreDownloaderExtension

<sub>Protocol</sub>

An app extension that uses the system implementation to schedule Apple-hosted asset-pack downloads automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol StoreDownloaderExtension : ManagedDownloaderExtension
```

## Overview

You can optionally implement the inherited `ManagedDownloaderExtension` requirements, but don’t implement any of the inherited `BADownloaderExtension` requirements for which this protocol provides a default implementation. For more information, see [Background Assets](../backgroundassets.md).

## Relationships

- **Inherits From**: [AppExtension](../extensionfoundation/appextension.md), [BADownloaderExtension](../backgroundassets/badownloaderextension-qwaw.md), [ManagedDownloaderExtension](../backgroundassets/manageddownloaderextension.md)
