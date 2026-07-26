---
title: NWBrowser.Result.Change
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/result/change
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/result/change'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/result/change.json'
content_hash: 'sha256:0cc7ec4960978e2d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWBrowser](../../nwbrowser.md) · [Result](../result.md)

# NWBrowser.Result.Change

<sub>Enumeration</sub>

Ways in which discovered services can change between specific results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Change
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Inspecting Change Types

- [NWBrowser.Result.Change.identical](change/identical.md) — No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](<change/added(__).md>) — A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](<change/removed(__).md>) — A previously discovered result was removed.
- [NWBrowser.Result.Change.changed(old:new:flags:)](<change/changed(old_new_flags_).md>) — A result changed properties but was not removed.
- [Flags](change/flags.md) — Flags providing details about a change in a discovered service.

### Calculating Result Changes

- [init(between:_:)](<change/init(between___).md>) — Initializes a change between two results.
