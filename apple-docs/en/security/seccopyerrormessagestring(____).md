---
title: 'SecCopyErrorMessageString(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 11.3+, visionOS 1.0+, watchOS 4.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccopyerrormessagestring(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccopyerrormessagestring(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccopyerrormessagestring%28_%3A_%3A%29.json'
content_hash: 'sha256:3f1a1f1b5e1f1ab9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCopyErrorMessageString(_:_:)

<sub>Function</sub>

Returns a string explaining the meaning of a security result code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafeMutableRawPointer?) -> CFString?
```

## Parameters

- `status` — A result code of type `OSStatus` returned by a security function. See [Security Framework Result Codes](security-framework-result-codes.md) for a list of codes.

- `reserved` — Reserved for future use. Pass `nil` for this parameter.

## Return Value

A human-readable string describing the result, or `nil` if no string is available for the specified result code. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished using it.
