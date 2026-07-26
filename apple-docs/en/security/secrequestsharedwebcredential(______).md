---
title: 'SecRequestSharedWebCredential(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（14.0 起废弃）, iPadOS 8.0+（14.0 起废弃）, Mac Catalyst 14.0+（14.0 起废弃）, macOS 11.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secrequestsharedwebcredential(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secrequestsharedwebcredential(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secrequestsharedwebcredential%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9ed4fa9d16d08be5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecRequestSharedWebCredential(_:_:_:)

<sub>Function</sub>

Asynchronously obtains one or more shared passwords for a website.

> [!warning] Deprecated
> Use [ASAuthorizationController](../authenticationservices/asauthorizationcontroller.md) to make an [ASAuthorizationPasswordRequest](../authenticationservices/asauthorizationpasswordrequest.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func SecRequestSharedWebCredential(_ fqdn: CFString?, _ account: CFString?, _ completionHandler: @escaping (CFArray?, CFError?) -> Void)
```

## Parameters

- `fqdn` — (Optional) The fully qualified domain name of the website for which passwords are being requested. If `NULL` is passed in this argument, the domain name(s) listed in the calling app’s [Associated Domains Entitlement](../bundleresources/entitlements/com.apple.developer.associated-domains.md) are searched implicitly.

- `account` — (Optional) The account name for which passwords are being requested. The account may be `NULL` to request all of the shared credentials that are available for the site, allowing the caller to discover an existing account.

- `completionHandler` — A block that is called to deliver the requested credentials. The block takes two arguments: - **`credentials`** — An array containing the requested passwords. If no matching items are found, the credentials array is empty. The credentials reference is automatically released after this handler is called, though you may optionally retain it for as long as needed. - **`error`** — If the shared password was successfully added (or removed), `NULL`; if not successful, a [CFError](../corefoundation/cferror.md) object that encapsulates the reason why the password could not be added (or removed). The error reference is automatically released after this handler is called, though you may optionally retain it for as long as needed.

## Discussion

This function requests one or more shared passwords for a given website, depending on whether the optional account parameter is supplied. To obtain results, the website specified in the `fqdn` parameter must be one that matches an entry in the calling app’s [Associated Domains Entitlement](../bundleresources/entitlements/com.apple.developer.associated-domains.md).

If matching shared password items are found, the credentials provided to the completion handler will be a [CFArray](../corefoundation/cfarray.md) data type containing [CFDictionary](../corefoundation/cfdictionary.md) entries. Each dictionary contains the following pairs:

| Key | Value |
|---|---|
| [kSecAttrServer](ksecattrserver.md) | [CFString](../corefoundation/cfstring.md) (the website) |
| [kSecAttrAccount](ksecattraccount.md) | [CFString](../corefoundation/cfstring.md) (the account) |
| [kSecSharedPassword](ksecsharedpassword.md) | [CFString](../corefoundation/cfstring.md) (the password) |

If the found item specifies a nonstandard port number (other than 443 for `https`), the following key may also be present:

| [kSecAttrPort](ksecattrport.md) | [CFNumber](../corefoundation/cfnumber.md) (the port number) |
|---|---|

> [!note] Note
> Because a request involving shared web credentials may potentially require user interaction or other verification to be approved, this function is dispatched asynchronously; your code provides a completion handler that will be called as soon as the results (if any) are available.
