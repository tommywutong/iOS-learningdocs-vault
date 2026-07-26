---
title: 'SecTransformSetAttributeAction(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformsetattributeaction(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformsetattributeaction(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformsetattributeaction%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8cafe861d5e5f705'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformSetAttributeAction(_:_:_:_:)

<sub>Function</sub>

Requests a callback when an attribute is set.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformSetAttributeAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ attribute: SecTransformStringOrAttribute?, _ newAction: @escaping SecTransformAttributeActionBlock) -> CFError?
```

## Parameters

- `ref` — A [SecTransformImplementationRef](sectransformimplementationref.md) that is bound to an instance of a custom transform.

- `action` — The behavior to be set. Use [kSecTransformActionAttributeNotification](ksectransformactionattributenotification.md) to add a block that is called when an attribute is set. If the name is `NULL`, then the supplied block is called for all set attributes except for ones that have a specific block as a handler. Use [kSecTransformActionAttributeValidation](ksectransformactionattributevalidation.md) to add a block that is called to validate the input to an attribute.

- `attribute` — The name of the attribute that will be handled. An attribute reference may also be given here. A `NULL` value indicates that the supplied action is for all attributes.

- `newAction` — A [SecTransformAttributeActionBlock](sectransformattributeactionblock.md) which implements the behavior.

## Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the error’s memory when you are done with it.

## Discussion

The [kSecTransformActionProcessData](ksectransformactionprocessdata.md) action used with the [SecTransformSetDataAction](<sectransformsetdataaction(______).md>) function is a special case of a [SecTransformSetAttributeAction](<sectransformsetattributeaction(________).md>) action. If this is called on the input attribute then it will overwrite any [kSecTransformActionProcessData](ksectransformactionprocessdata.md) action.

You may call this function multiple times for either a named attribute or for all attributes when the attribute parameter is `NULL`. The last call takes precedence.
