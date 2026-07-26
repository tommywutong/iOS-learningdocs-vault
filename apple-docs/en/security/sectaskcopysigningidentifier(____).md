---
title: 'SecTaskCopySigningIdentifier(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectaskcopysigningidentifier(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectaskcopysigningidentifier(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectaskcopysigningidentifier%28_%3A_%3A%29.json'
content_hash: 'sha256:629785e934e900bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTaskCopySigningIdentifier(_:_:)

<sub>Function</sub>

Returns the value of the code signing identifier.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTaskCopySigningIdentifier(_ task: SecTask, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?
```

## Parameters

- `task` — The task whose code signing identifier you want.

- `error` — A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass `NULL` to ignore the error.

## Return Value

A string representing the code signing identifier for the task, or `NULL` on error. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this string’s memory when you are done with it.
