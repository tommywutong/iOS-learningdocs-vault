---
title: 'SecTransformRegister(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformregister(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformregister(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformregister%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9030f64c8dbb7229'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformRegister(_:_:_:)

<sub>Function</sub>

Registers a custom transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformRegister(_ uniqueName: CFString, _ createTransformFunction: SecTransformCreateFP, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

## Parameters

- `uniqueName` — A unique name for this custom transform. It is recommended that a reverse DNS name be used for the name of your custom transform

- `createTransformFunction` — A [SecTransformCreateFP](sectransformcreatefp.md) function pointer. The function must return a [SecTransformInstanceBlock](sectransforminstanceblock.md) block. Call block_copy on this block before returning it. Failure to do so results in undefined behavior.

- `error` — A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass `NULL` to ignore the error.

## Return Value

A Boolean that is set to [true](../swift/true.md) if the custom transform was registered and [false](../swift/false.md) otherwise
