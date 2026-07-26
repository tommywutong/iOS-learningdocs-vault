---
title: 'NWBrowser.Result.Change.changed(old:new:flags:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwbrowser/result/change/changed(old:new:flags:)'
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/result/change/changed(old:new:flags:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/result/change/changed%28old%3Anew%3Aflags%3A%29.json'
content_hash: 'sha256:abee93875cbc2c49'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWBrowser](../../../nwbrowser.md) · [Result](../../result.md) · [Change](../change.md)

# NWBrowser.Result.Change.changed(old:new:flags:)

<sub>Case</sub>

A result changed properties but was not removed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)
```

## See Also

### Inspecting Change Types

- [NWBrowser.Result.Change.identical](identical.md) — No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](<added(__).md>) — A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](<removed(__).md>) — A previously discovered result was removed.
- [Flags](flags.md) — Flags providing details about a change in a discovered service.
