---
title: SectionedFetchRequest.Configuration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchrequest/configuration
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/configuration.json'
content_hash: 'sha256:b2c1301239b7dc2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchRequest](../sectionedfetchrequest.md)

# SectionedFetchRequest.Configuration

<sub>Structure</sub>

The request’s configurable properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Configuration
```

## Overview

You initialize a [SectionedFetchRequest](../sectionedfetchrequest.md) with a section identifier, an optional predicate, and sort descriptors, either explicitly or with a configured [NSFetchRequest](../../coredata/nsfetchrequest.md). Later, you can dynamically update the identifier, predicate, and sort parameters using the request’s configuration structure.

You access or bind to a request’s configuration components through properties on the associated [SectionedFetchResults](../sectionedfetchresults.md) instance, just like you do for a [FetchRequest](../fetchrequest.md) using [Configuration](../fetchrequest/configuration.md).

When configuring a sectioned fetch request, ensure that the combination of the section identifier and the primary sort descriptor doesn’t create discontiguous sections.

## Topics

### Setting the section identifier

- [sectionIdentifier](configuration/sectionidentifier.md) — The request’s section identifier key path.

### Setting a predicate

- [nsPredicate](configuration/nspredicate.md) — The request’s predicate.

### Setting sort descriptors

- [sortDescriptors](configuration/sortdescriptors.md) — The request’s sort descriptors, accessed as value types.
- [nsSortDescriptors](configuration/nssortdescriptors.md) — The request’s sort descriptors, accessed as reference types.

## See Also

### Configuring a request dynamically

- [projectedValue](projectedvalue.md) — A binding to the request’s mutable configuration properties.
