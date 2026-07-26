---
title: 'SecTransformSetTransformAction(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformsettransformaction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformsettransformaction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformsettransformaction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:18400aec5a02e05f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformSetTransformAction(_:_:_:)

<sub>Function</sub>

Changes the way that a transform deals with transform lifecycle behaviors.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: @escaping SecTransformActionBlock) -> CFError?
```

## Parameters

- `ref` — A custom transform.

- `action` — The behavior to change. Valid values are [kSecTransformActionCanExecute](ksectransformactioncanexecute.md), [kSecTransformActionStartingExecution](ksectransformactionstartingexecution.md), [kSecTransformActionFinalize](ksectransformactionfinalize.md), or [kSecTransformActionExternalizeExtraData](ksectransformactionexternalizeextradata.md).

- `newAction` — A [SecTransformActionBlock](sectransformactionblock.md) block that implements the behavior.

## Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the error’s memory when you are done with it.
