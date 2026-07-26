---
title: 'SecKeychainSetSearchList(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetsearchlist(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetsearchlist(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetsearchlist%28_%3A%29.json'
content_hash: 'sha256:2ff68ce790a4d15e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetSearchList(_:)

<sub>Function</sub>

Specifies the list of keychains to use in the default keychain search list.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainSetSearchList(_ searchList: CFArray) -> OSStatus
```

## Parameters

- `searchList` — An array of keychain references (of type [SecKeychain](seckeychain.md)) specifying the list of keychains to use in the default keychain search list. Passing an empty array clears the search list.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The default keychain search list is used by several functions; see for example [SecKeychainSearchCreateFromAttributes](seckeychainsearchcreatefromattributes.md), [SecKeychainFindInternetPassword](<seckeychainfindinternetpassword(______________________________).md>), or [SecKeychainFindGenericPassword](<seckeychainfindgenericpassword(________________).md>). To obtain the current default keychain search list, use the [SecKeychainCopySearchList](<seckeychaincopysearchlist(__).md>) function.

The default keychain search list is displayed as the keychain list in the Keychain Access utility. If you use [SecKeychainSetSearchList](<seckeychainsetsearchlist(__).md>) to change the keychain search list, the list displayed in Keychain Access changes accordingly.
