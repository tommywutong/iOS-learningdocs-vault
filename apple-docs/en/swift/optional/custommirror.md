---
title: customMirror
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/optional/custommirror
source_url: 'https://developer.apple.com/documentation/swift/optional/custommirror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/custommirror.json'
content_hash: 'sha256:45cc0ecdf45e7892'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# customMirror

<sub>Instance Property</sub>

The custom mirror for this instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var customMirror: Mirror { get }
```

## Discussion

If this type has value semantics, the mirror should be unaffected by subsequent mutations of the instance.

## See Also

### Inspecting an Optional

- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [unsafelyUnwrapped](unsafelyunwrapped.md) — The wrapped value of this instance, unwrapped without checking whether the instance is `nil`.
- [debugDescription](debugdescription.md) — A textual representation of this instance, suitable for debugging.
