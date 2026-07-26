---
title: ProgressManager.Property
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/foundation/progressmanager/property
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property.json'
content_hash: 'sha256:35532bab1c294229'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# ProgressManager.Property

<sub>Protocol</sub>

A type that conveys additional task-specific information on progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Property : SendableMetatype
```

## Overview

The `Property` protocol defines custom properties that can be associated with progress tracking. These properties allow you to store and aggregate additional information alongside the standard progress metrics such as `totalCount` and `completedCount`.

## Relationships

- **Inherits From**: [SendableMetatype](../../swift/sendablemetatype.md)

- **Conforming Types**: [CompletedByteCount](properties/completedbytecount-swift.enum.md), [CompletedFileCount](properties/completedfilecount-swift.enum.md), [EstimatedTimeRemaining](properties/estimatedtimeremaining-swift.enum.md), [Throughput](properties/throughput-swift.enum.md), [TotalByteCount](properties/totalbytecount-swift.enum.md), [TotalFileCount](properties/totalfilecount-swift.enum.md)

## Topics

### Associated Types

- [Summary](property/summary.md) — The type used for aggregated summaries of this property. _(beta)_
- [Value](property/value.md) — The type used for individual values of this property. _(beta)_

### Type Properties

- [defaultSummary](property/defaultsummary.md) — The default summary value for this property type. _(beta)_
- [defaultValue](property/defaultvalue.md) — The default value to return when property is not set to a specific value. _(beta)_
- [key](property/key.md) — A unique identifier for this property type. _(beta)_

### Type Methods

- [finalSummary(_:_:)](<property/finalsummary(____).md>) — Determines how to handle summary data when a progress manager is deinitialized. _(beta)_
- [merge(_:_:)](<property/merge(____).md>) — Merges two summary values into a single combined summary. _(beta)_
- [reduce(into:value:)](<property/reduce(into_value_).md>) — Reduces a property value into an accumulating summary. _(beta)_
