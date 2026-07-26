---
title: 'SecTransformSetDataAction(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformsetdataaction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformsetdataaction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformsetdataaction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ea38ea7a5e83931f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformSetDataAction(_:_:_:)

<sub>Function</sub>

Changes the way a custom transform processes data.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformSetDataAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: @escaping SecTransformDataBlock) -> CFError?
```

## Parameters

- `ref` — A [SecTransformImplementationRef](sectransformimplementationref.md) that is bound to an instance of a custom transform.

- `action` — The action being overridden. Use  [kSecTransformActionProcessData](ksectransformactionprocessdata.md) to change the way that input data is processed into the output data. The default behavior is to simply copy the input data to the output attribute. Changing this behavior is really a special case of a [SecTransformSetAttributeAction](<sectransformsetattributeaction(________).md>) action. Using [kSecTransformActionProcessData](ksectransformactionprocessdata.md) as the `action` overwrites any previously set [kSecTransformActionAttributeNotification](ksectransformactionattributenotification.md) action. Use [kSecTransformActionInternalizeExtraData](ksectransformactioninternalizeextradata.md) to change the way that custom externalized data is imported into the transform. The default behavior is to do nothing.

- `newAction` — A [SecTransformDataBlock](sectransformdatablock.md) which implements the behavior. If the `action` parameter is [kSecTransformActionProcessData](ksectransformactionprocessdata.md) then this block is called to process the input data into the output data. If the action parameter is [kSecTransformActionInternalizeExtraData](ksectransformactioninternalizeextradata.md) then this block is called to input custom data into the transform.

## Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the error’s memory when you are done with it.

## Discussion

When the `action` parameter is [kSecTransformActionProcessData](ksectransformactionprocessdata.md), the `newAction` block changes the way that input data is processed to become the output data. When the `action` parameter is [kSecTransformActionInternalizeExtraData](ksectransformactioninternalizeextradata.md) it changes the way a custom transform reads in data to be imported into the transform.

You may call this function multiple times. The last call takes precedence.
