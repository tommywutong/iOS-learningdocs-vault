---
title: 'init(SCNVector3:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(scnvector3:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(scnvector3:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28scnvector3%3A%29.json'
content_hash: 'sha256:cb59f2482050ca65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(SCNVector3:)

<sub>Initializer</sub>

Creates a value object that contains the specified three-element SceneKit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(SCNVector3 v: SCNVector3)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(scnVector3 v: SCNVector3)
```

## Parameters

- `v` — The value for the new object.

## Return Value

A new value object that contains the vector information.

## See Also

### Related Documentation

- [SCNVector3](../../scenekit/scnvector3.md) — A representation of a three-component vector. _(deprecated)_

### Working with SceneKit Vector and Matrix Values

- [+ valueWithSCNVector4:](<init(scnvector4_).md>) — Creates a value object that contains the specified four-element SceneKit vector.
- [+ valueWithSCNMatrix4:](<init(scnmatrix4_).md>) — Creates a value object that contains the specified SceneKit 4 x 4 matrix.
- [SCNVector3Value](scnvector3value.md) — The three-element Scene Kit vector representation of the value.
- [SCNVector4Value](scnvector4value.md) — The four-element Scene Kit vector representation of the value.
- [SCNMatrix4Value](scnmatrix4value.md) — The Scene Kit 4 x 4 matrix representation of the value.
