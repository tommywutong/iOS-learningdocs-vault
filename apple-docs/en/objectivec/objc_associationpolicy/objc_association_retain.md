---
title: objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN
framework: Objective-C Runtime
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_associationpolicy/objc_association_retain
source_url: 'https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_associationpolicy/objc_association_retain.json'
content_hash: 'sha256:3ac0baed2ec8765d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [objc_AssociationPolicy](../objc_associationpolicy.md)

# objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN

<sub>Case</sub>

Specifies a strong reference to the associated object, and that the association is made atomically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case OBJC_ASSOCIATION_RETAIN
```

## See Also

### Enumeration Cases

- [OBJC_ASSOCIATION_ASSIGN](objc_association_assign.md) — Specifies an unsafe unretained reference to the associated object.
- [OBJC_ASSOCIATION_COPY](objc_association_copy.md) — Specifies that the associated object is copied, and that the association is made atomically.
- [OBJC_ASSOCIATION_COPY_NONATOMIC](objc_association_copy_nonatomic.md) — Specifies that the associated object is copied, and that the association is not made atomically.
- [OBJC_ASSOCIATION_RETAIN_NONATOMIC](objc_association_retain_nonatomic.md) — Specifies a strong reference to the associated object, and that the association is not made atomically.
