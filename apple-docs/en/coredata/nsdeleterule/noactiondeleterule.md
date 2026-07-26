---
title: NSDeleteRule.noActionDeleteRule
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsdeleterule/noactiondeleterule
source_url: 'https://developer.apple.com/documentation/coredata/nsdeleterule/noactiondeleterule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsdeleterule/noactiondeleterule.json'
content_hash: 'sha256:0e185cae678f5b52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSDeleteRule](../nsdeleterule.md)

# NSDeleteRule.noActionDeleteRule

<sub>Case</sub>

A rule that prevents modification of the referenced managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case noActionDeleteRule
```

## Discussion

If you use this delete rule, make sure you delete any referenced managed objects or nullify their inverse relationships. Otherwise, those objects will reference an object that doesn’t exist, and your persistent store will be in an inconsistent state.

## See Also

### Delete Rules

- [NSNullifyDeleteRule](nullifydeleterule.md) — A rule that nullifies the inverse relationship of the referenced managed objects.
- [NSCascadeDeleteRule](cascadedeleterule.md) — A rule that deletes the referenced managed objects.
- [NSDenyDeleteRule](denydeleterule.md) — A rule that prevents the deletion of the owning managed object if the relationship has references to other objects.
