---
title: coreSpotlightExporter
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/corespotlightexporter
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/corespotlightexporter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/corespotlightexporter.json'
content_hash: 'sha256:8cf1d878add09d45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# coreSpotlightExporter

<sub>Instance Property</sub>

The spotlight exporter associated with this persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var coreSpotlightExporter: NSCoreDataCoreSpotlightDelegate { get }
```

## Discussion

Spotlight support isn’t available in a compatible iPad or iPhone app running in visionOS.
