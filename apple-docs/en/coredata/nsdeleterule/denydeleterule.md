---
title: NSDeleteRule.denyDeleteRule
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsdeleterule/denydeleterule
source_url: 'https://developer.apple.com/documentation/coredata/nsdeleterule/denydeleterule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsdeleterule/denydeleterule.json'
content_hash: 'sha256:99aad38a6c3c65fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSDeleteRule](../nsdeleterule.md)

# NSDeleteRule.denyDeleteRule

<sub>Case</sub>

A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case denyDeleteRule
```

## See Also

### Delete Rules

- [NSNoActionDeleteRule](noactiondeleterule.md) — A rule that prevents modification of the referenced managed objects.
- [NSNullifyDeleteRule](nullifydeleterule.md) — A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSCascadeDeleteRule](cascadedeleterule.md) — A rule that deletes the referenced managed objects.
