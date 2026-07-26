---
title: NSDeleteRule.nullifyDeleteRule
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsdeleterule/nullifydeleterule
source_url: 'https://developer.apple.com/documentation/coredata/nsdeleterule/nullifydeleterule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsdeleterule/nullifydeleterule.json'
content_hash: 'sha256:5c64c305ec9d0e96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSDeleteRule](../nsdeleterule.md)

# NSDeleteRule.nullifyDeleteRule

<sub>Case</sub>

A rule that nullifies the inverse relationship of the referenced managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case nullifyDeleteRule
```

## See Also

### Delete Rules

- [NSNoActionDeleteRule](noactiondeleterule.md) — A rule that prevents modification of the referenced managed objects.
- [NSCascadeDeleteRule](cascadedeleterule.md) — A rule that deletes the referenced managed objects.
- [NSDenyDeleteRule](denydeleterule.md) — A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.
