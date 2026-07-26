---
title: 'finalSummary(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progressmanager/property/finalsummary(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/property/finalsummary(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/property/finalsummary%28_%3A_%3A%29.json'
content_hash: 'sha256:c58c1a218bc77d9e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProgressManager](../../progressmanager.md) · [Property](../property.md)

# finalSummary(_:_:)

<sub>Type Method</sub>

Determines how to handle summary data when a progress manager is deinitialized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func finalSummary(_ parentSummary: Self.Summary, _ selfSummary: Self.Summary) -> Self.Summary
```

## Parameters

- `parentSummary` — The current summary value of the parent progress manager.

- `selfSummary` — The final summary value from the progress manager being deinitialized.

## Return Value

The updated summary that replaces the parent’s current summary.

## Discussion

This method is used when a progress manager in the hierarchy is being deinitialized and its accumulated summary needs to be processed in relation to its parent’s summary. The behavior can vary depending on the property type:

- For additive properties (like file counts, byte counts): The self summary is typically added to the parent summary to preserve the accumulated progress.
- For max-based properties (like estimated time remaining): The parent summary is typically preserved as it represents an existing estimate.
- For collection-based properties (like file URLs): The self summary may be discarded to avoid accumulating stale references.
