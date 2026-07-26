---
title: 'SecACLCopyContents(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaclcopycontents(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaclcopycontents(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclcopycontents%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1d227182d39f580e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLCopyContents(_:_:_:_:)

<sub>Function</sub>

Returns the application list, description, and prompt selector for a given ACL entry.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecACLCopyContents(_ acl: SecACL, _ applicationList: UnsafeMutablePointer<CFArray?>, _ description: UnsafeMutablePointer<CFString?>, _ promptSelector: UnsafeMutablePointer<SecKeychainPromptSelector>) -> OSStatus
```

## Parameters

- `acl` — The ACL entry from which you want information.

- `applicationList` — The address of an array into which a copy of the application list should be stored on return. This array is filled with [SecTrustedApplication](sectrustedapplication.md) instances identifying applications that are allowed access to the keychain item without user confirmation. If the array is `nil`, then any app can use this item. If the array is empty, then there are no trusted applications. Call the [CFRelease](../corefoundation/cfrelease.md) method to release this array when you are finished using it.

- `description` — The address of a string into which a copy of the description is stored on return. This description is the name of the keychain item that appears in the dialog box when the user is prompted for permission to use the item. Note that this name is not necessarily the same as the name displayed for the item by the Keychain Access app. Call the [CFRelease](../corefoundation/cfrelease.md) method to release this string when you are finished using it.

- `promptSelector` — The address of a [SecKeychainPromptSelector](seckeychainpromptselector.md) instance into which a copy of the prompt selector is stored on return. If the [kSecKeychainPromptRequirePassphase](seckeychainpromptselector/requirepassphase.md) bit is set, the user is prompted for the keychain password each time a non-trusted application attempts to access this item, even if the keychain is already unlocked.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

An ACL entry applies to a specific use or set of uses for a specific keychain item. The entry includes a list of trusted applications, the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies.

Use the [SecACLCopyAuthorizations](<secaclcopyauthorizations(__).md>) method to get the list of operations for an ACL entry.

> [!note] Note
> Starting in macOS 10.13.1, for added security, the system ignores the `promptSelector` property of an ACL entry and always prompts for the keychain password when asking the user whether to add an app to the list of trusted apps.
