---
title: 'SecTransformCreate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformcreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformcreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcreate%28_%3A_%3A%29.json'
content_hash: 'sha256:36877b37edb82aac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCreate(_:_:)

<sub>Function</sub>

Creates a transform computation object.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformCreate(_ name: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecTransform?
```

## Parameters

- `name` — The type of transform to create. Use one of the pre-defined transform types or a custom type that you previously registered using [SecTransformRegister](<sectransformregister(______).md>).

- `error` — A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass `NULL` to ignore the error.

## Return Value

A pointer to a new transform or `NULL` on failure. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.
