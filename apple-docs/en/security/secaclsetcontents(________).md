---
title: 'SecACLSetContents(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaclsetcontents(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaclsetcontents(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclsetcontents%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cd351b4d69425687'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLSetContents(_:_:_:_:)

<sub>Function</sub>

Sets the application list, description, and prompt selector for a given ACL entry.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecACLSetContents(_ acl: SecACL, _ applicationList: CFArray?, _ description: CFString, _ promptSelector: SecKeychainPromptSelector) -> OSStatus
```

## Parameters

- `acl` — The ACL entry to modify.

- `applicationList` — An array of [SecTrustedApplication](sectrustedapplication.md) instances identifying apps that are allowed access to the keychain item without user confirmation. Use the [SecTrustedApplicationCreateFromPath](<sectrustedapplicationcreatefrompath(____).md>) method to create trusted app objects. If you set this parameter to `nil`, then any app can use this item. If you pass an empty array, then no apps are trusted.

- `description` — The name of the keychain item that appears in the dialog box when the user is prompted for permission to use the item. Note that this name is not necessarily the same as the one displayed for the item by the Keychain Access app.

- `promptSelector` — The prompt selector flags for the given access control list entry. See [SecKeychainPromptSelector](seckeychainpromptselector.md) for details.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Because an ACL entry is always associated with an access instance, when you modify the entry, you are modifying the access instance as well.

Use the [SecACLCopyAuthorizations](<secaclcopyauthorizations(__).md>) method to get the list of operations for an ACL entry.

> [!note] Note
> Starting in macOS 10.13.1, for added security, the system ignores the `promptSelector` property of an ACL entry and always prompts for the keychain password when asking the user whether to add an app to the list of trusted apps.
