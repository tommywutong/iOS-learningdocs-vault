---
title: 'NWBrowser.Result.Change.removed(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwbrowser/result/change/removed(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/result/change/removed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/result/change/removed%28_%3A%29.json'
content_hash: 'sha256:f4eece44123e30a7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWBrowser](../../../nwbrowser.md) · [Result](../../result.md) · [Change](../change.md)

# NWBrowser.Result.Change.removed(_:)

<sub>Case</sub>

A previously discovered result was removed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case removed(NWBrowser.Result)
```

## See Also

### Inspecting Change Types

- [NWBrowser.Result.Change.identical](identical.md) — No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](<added(__).md>) — A new result was discovered.
- [NWBrowser.Result.Change.changed(old:new:flags:)](<changed(old_new_flags_).md>) — A result changed properties but was not removed.
- [Flags](flags.md) — Flags providing details about a change in a discovered service.
