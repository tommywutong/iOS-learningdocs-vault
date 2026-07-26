---
title: NWBrowser.Result.Change.Flags
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/result/change/flags
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/result/change/flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/result/change/flags.json'
content_hash: 'sha256:74c171adf2b8f5e0'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWBrowser](../../../nwbrowser.md) · [Result](../../result.md) · [Change](../change.md)

# NWBrowser.Result.Change.Flags

<sub>Structure</sub>

Flags providing details about a change in a discovered service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Flags
```

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [ExpressibleByArrayLiteral](../../../../swift/expressiblebyarrayliteral.md), [Hashable](../../../../swift/hashable.md), [OptionSet](../../../../swift/optionset.md), [RawRepresentable](../../../../swift/rawrepresentable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md), [SetAlgebra](../../../../swift/setalgebra.md)

## Topics

### Change Flags

- [identical](flags/identical.md) — The results are identical.
- [interfaceAdded](flags/interfaceadded.md) — The service was discovered over a new interface.
- [interfaceRemoved](flags/interfaceremoved.md) — The service was no longer discovered over a certain interface.
- [metadataChanged](flags/metadatachanged.md) — The service’s associated metadata changed.

## See Also

### Inspecting Change Types

- [NWBrowser.Result.Change.identical](identical.md) — No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](<added(__).md>) — A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](<removed(__).md>) — A previously discovered result was removed.
- [NWBrowser.Result.Change.changed(old:new:flags:)](<changed(old_new_flags_).md>) — A result changed properties but was not removed.
