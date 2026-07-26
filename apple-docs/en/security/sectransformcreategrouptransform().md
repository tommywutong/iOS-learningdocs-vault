---
title: SecTransformCreateGroupTransform()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformcreategrouptransform()
source_url: 'https://developer.apple.com/documentation/security/sectransformcreategrouptransform()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcreategrouptransform%28%29.json'
content_hash: 'sha256:f48030b72f05f831'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCreateGroupTransform()

<sub>Function</sub>

Creates an object that acts as a container for a set of connected transforms.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformCreateGroupTransform() -> SecGroupTransform
```

## Return Value

A transform group object.

## Discussion

A [SecGroupTransform](secgrouptransform.md) is a container for all of the transforms that are in a directed graph. You can use this container as you would a single transform with the [SecTransformExecute](<sectransformexecute(____).md>), [SecTransformExecuteAsync](<sectransformexecuteasync(______).md>) and [SecTransformCopyExternalRepresentation](<sectransformcopyexternalrepresentation(__).md>) functions.On the other hand, unlike a stand alone transform, you can’t use a transform group with the [SecTransformConnectTransforms](<sectransformconnecttransforms(____________).md>), [SecTransformSetAttribute](<sectransformsetattribute(________).md>) or [SecTransformGetAttribute](<sectransformgetattribute(____).md>) functions. Attempting to do so produces undefined behavior.
