---
title: 'SecACLCopyAuthorizations(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaclcopyauthorizations(_:)'
source_url: 'https://developer.apple.com/documentation/security/secaclcopyauthorizations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclcopyauthorizations%28_%3A%29.json'
content_hash: 'sha256:47fc138c8e2f325e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLCopyAuthorizations(_:)

<sub>Function</sub>

Retrieves the authorization tags of a given ACL entry.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecACLCopyAuthorizations(_ acl: SecACL) -> CFArray
```

## Parameters

- `acl` — The ACL entry from which you wish to retrieve the authorization tags.

## Return Value

An array containing the authorizations for this entry. In Objective-C, free this object with a call to the [CFRelease](../corefoundation/cfrelease.md) method when you are done with it.

## Discussion

An ACL instance includes a list of trusted apps, the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies. Use this method to retrieve the list of operations for an ACL entry. Use the [SecACLCopyContents](<secaclcopycontents(________).md>) method to retrieve the other information.

The [SecACLCopyAuthorizations](<secaclcopyauthorizations(__).md>) method returns an error if there are more tags to return than the number of elements you allocated in the `tags` array. A 20-element array should suffice for most purposes; however, you can test for the [errSecBufferTooSmall](errsecbuffertoosmall.md) error and increase the size of the array before calling the method again if necessary. Alternatively, you can call the method with a tag count of `0`, read the value returned in the `tagCount` parameter, and then call the method again using that value.
