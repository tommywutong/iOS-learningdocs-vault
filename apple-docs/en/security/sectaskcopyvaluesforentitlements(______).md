---
title: 'SecTaskCopyValuesForEntitlements(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectaskcopyvaluesforentitlements(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectaskcopyvaluesforentitlements(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectaskcopyvaluesforentitlements%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8fefffff7c2c0c29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTaskCopyValuesForEntitlements(_:_:_:)

<sub>Function</sub>

Returns the values of multiple entitlements for the represented task.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTaskCopyValuesForEntitlements(_ task: SecTask, _ entitlements: CFArray, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?
```

## Parameters

- `task` — The task whose entitlements you want.

- `entitlements` — An array of the names of the entitlement to be fetched.

- `error` — A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass `NULL` to ignore the error.

## Return Value

A dictionary containing the entitlement names as keys with the corresponding entitlements as the dictionary values, or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this dictionary’s memory when you are done with it.
