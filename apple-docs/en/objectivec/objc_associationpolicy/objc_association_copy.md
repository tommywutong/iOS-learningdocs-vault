---
title: objc_AssociationPolicy.OBJC_ASSOCIATION_COPY
framework: Objective-C Runtime
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_associationpolicy/objc_association_copy
source_url: 'https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_copy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_associationpolicy/objc_association_copy.json'
content_hash: 'sha256:fd94f3d886274838'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [objc_AssociationPolicy](../objc_associationpolicy.md)

# objc_AssociationPolicy.OBJC_ASSOCIATION_COPY

<sub>Case</sub>

Specifies that the associated object is copied, and that the association is made atomically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case OBJC_ASSOCIATION_COPY
```

## See Also

### Enumeration Cases

- [OBJC_ASSOCIATION_ASSIGN](objc_association_assign.md) — Specifies an unsafe unretained reference to the associated object.
- [OBJC_ASSOCIATION_COPY_NONATOMIC](objc_association_copy_nonatomic.md) — Specifies that the associated object is copied, and that the association is not made atomically.
- [OBJC_ASSOCIATION_RETAIN](objc_association_retain.md) — Specifies a strong reference to the associated object, and that the association is made atomically.
- [OBJC_ASSOCIATION_RETAIN_NONATOMIC](objc_association_retain_nonatomic.md) — Specifies a strong reference to the associated object, and that the association is not made atomically.
