---
title: 'SecAccessControlCreateWithFlags(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secaccesscontrolcreatewithflags(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreatewithflags(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreatewithflags%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:44f5d6570ed55e49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAccessControlCreateWithFlags(_:_:_:_:)

<sub>Function</sub>

Creates a new access control object with the specified protection type and flags.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecAccessControlCreateWithFlags(_ allocator: CFAllocator?, _ protection: CFTypeRef, _ flags: SecAccessControlCreateFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecAccessControl?
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new [SecAccessControl](secaccesscontrol.md) object. Pass `NULL` or [kCFAllocatorDefault](../corefoundation/kcfallocatordefault.md) to allocate memory for the new allocator using the default allocator.

- `protection` — Protection class to be used for the item. Use one of the values that go with the [kSecAttrAccessible](ksecattraccessible.md) attribute key, namely those listed in [Accessibility Values](item-attribute-keys-and-values.md#Accessibility-Values).

- `flags` — Flags specifying the allowed operations for the item. See [SecAccessControlCreateFlags](secaccesscontrolcreateflags.md).

- `error` — On return, if an error occurred, the reference pointed at by this parameter refers to an error object that indicates the reason for failure. The caller is responsible for releasing the error object. Pass `NULL` for this parameter to ignore the error.

## Return Value

The newly created access control object. In Objective-C, free this item with [CFRelease](../corefoundation/cfrelease.md) when you are done with it.

## Discussion

You use the result of this function as a value for the [kSecAttrAccessControl](ksecattraccesscontrol.md) attribute in the [SecItemAdd](<secitemadd(____).md>), [SecItemUpdate](<secitemupdate(____).md>), or [SecKeyGeneratePair](<seckeygeneratepair(______).md>) functions.

Accessing keychain items or performing operations on keys that are protected by access control objects may block execution on the main thread. Perform these actions in the background, or use them in combination with the [kSecUseAuthenticationContext](ksecuseauthenticationcontext.md) and [kSecUseAuthenticationUI](ksecuseauthenticationui.md) attributes to manage user interactions.
