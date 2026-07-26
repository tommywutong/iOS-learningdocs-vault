---
title: 'SecACLCreateWithSimpleContents(_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaclcreatewithsimplecontents(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaclcreatewithsimplecontents(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclcreatewithsimplecontents%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:50043c4643a1f0ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLCreateWithSimpleContents(_:_:_:_:_:)

<sub>Function</sub>

Creates a new ACL entry with the given characteristics, and adds it to an access instance.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecACLCreateWithSimpleContents(_ access: SecAccess, _ applicationList: CFArray?, _ description: CFString, _ promptSelector: SecKeychainPromptSelector, _ newAcl: UnsafeMutablePointer<SecACL?>) -> OSStatus
```

## Parameters

- `access` — The access instance to which to add the information.

- `applicationList` — An array of [SecTrustedApplication](sectrustedapplication.md) instances identifying apps that are allowed access to the keychain item without user confirmation. Set this parameter to `nil` to indicate that any app can use this item. Pass an empty array to indicate that there are no trusted apps.

- `description` — The human readable name to be used to refer to this item when the user is prompted.

- `promptSelector` — A set of prompt selector flags. See [SecKeychainPromptSelector](seckeychainpromptselector.md) for possible values.

- `newAcl` — A pointer the method uses to return the new [SecACL](secacl.md) instance.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The ACL entry returned by this method includes a list of trusted apps, the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies. By default, a new ACL entry applies to all operations. Use the [SecACLUpdateAuthorizations](<secaclupdateauthorizations(____).md>) method to set the list of operations for an ACL entry.

> [!note] Note
> Starting in macOS 10.13.1, for added security, the system ignores the `promptSelector` property of an ACL object and always prompts for the keychain password when asking the user whether to add an app to the list of trusted apps.

The system requires exactly one owner ACL entry in each access instance. The [SecACLCreateWithSimpleContents](<secaclcreatewithsimplecontents(__________).md>) method fails if you attempt to add a second owner entry. To change owner access controls, use the [SecAccessCopyMatchingACLList](<secaccesscopymatchingacllist(____).md>) function to find the owner entry (the only one with an authorization tag of [kSecACLAuthorizationChangeACL](ksecaclauthorizationchangeacl.md)) and the [SecACLSetContents](<secaclsetcontents(________).md>) method to change it as needed.
