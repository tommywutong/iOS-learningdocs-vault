---
title: 'hash(into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/optional/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/hash%28into%3A%29.json'
content_hash: 'sha256:f35808d76c664fb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of this value by feeding them into the given hasher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hasher to use when combining the components of this instance.

## See Also

### Inspecting an Optional

- [unsafelyUnwrapped](unsafelyunwrapped.md) — The wrapped value of this instance, unwrapped without checking whether the instance is `nil`.
- [debugDescription](debugdescription.md) — A textual representation of this instance, suitable for debugging.
- [customMirror](custommirror.md) — The custom mirror for this instance.
