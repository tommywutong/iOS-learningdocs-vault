---
title: 'SecTaskCopyValueForEntitlement(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectaskcopyvalueforentitlement(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectaskcopyvalueforentitlement(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectaskcopyvalueforentitlement%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2ecc6ecac094ebe6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTaskCopyValueForEntitlement(_:_:_:)

<sub>Function</sub>

Returns the value of a single entitlement for the represented task.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTaskCopyValueForEntitlement(_ task: SecTask, _ entitlement: CFString, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFTypeRef?
```

## Parameters

- `task` — The task whose entitlement you want.

- `entitlement` — The name of the entitlement to be fetched.

- `error` — A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass `NULL` to ignore the error.

## Return Value

The value of the specified entitlement for the process or `NULL` if the entitlement value could not be retrieved. The type of the returned value depends on the entitlement specified. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.

## Discussion

An empty return value may indicate an error, or it may indicate that the entitlement is simply not present.  In the latter case, no error is returned.
