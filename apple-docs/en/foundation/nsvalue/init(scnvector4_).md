---
title: 'init(SCNVector4:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(scnvector4:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(scnvector4:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28scnvector4%3A%29.json'
content_hash: 'sha256:dfded9eed6fe5d3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(SCNVector4:)

<sub>Initializer</sub>

Creates a value object that contains the specified four-element SceneKit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(SCNVector4 v: SCNVector4)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(scnVector4 v: SCNVector4)
```

## Parameters

- `v` — The value for the new object.

## Return Value

A new value object that contains the vector information.

## See Also

### Related Documentation

- [SCNVector4](../../scenekit/scnvector4.md) — A representation of a four-component vector. _(deprecated)_

### Working with SceneKit Vector and Matrix Values

- [+ valueWithSCNVector3:](<init(scnvector3_).md>) — Creates a value object that contains the specified three-element SceneKit vector.
- [+ valueWithSCNMatrix4:](<init(scnmatrix4_).md>) — Creates a value object that contains the specified SceneKit 4 x 4 matrix.
- [SCNVector3Value](scnvector3value.md) — The three-element Scene Kit vector representation of the value.
- [SCNVector4Value](scnvector4value.md) — The four-element Scene Kit vector representation of the value.
- [SCNMatrix4Value](scnmatrix4value.md) — The Scene Kit 4 x 4 matrix representation of the value.
