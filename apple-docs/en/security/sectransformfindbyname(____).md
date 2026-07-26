---
title: 'SecTransformFindByName(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformfindbyname(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformfindbyname(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformfindbyname%28_%3A_%3A%29.json'
content_hash: 'sha256:0343685e9466b728'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformFindByName(_:_:)

<sub>Function</sub>

Finds a member of a transform group by its name.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformFindByName(_ transform: SecGroupTransform, _ name: CFString) -> SecTransform?
```

## Parameters

- `transform` — The transform group to be searched.

- `name` — The name of the transform to be found.

## Return Value

The transform group member, or `NULL` if the member was not found.

## Discussion

When a transform instance is created you give it a unique name. This name can be used to find that instance in a group. While it is possible to use the [SecTransformSetAttribute](<sectransformsetattribute(________).md>) function to change a transform’s name after creating it, this is not recommended because doing so causes the [SecTransformFindByName](<sectransformfindbyname(____).md>) function to misbehave.
