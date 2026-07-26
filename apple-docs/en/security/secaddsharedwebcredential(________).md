---
title: 'SecAddSharedWebCredential(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（26.2 起废弃）, iPadOS 8.0+（26.2 起废弃）, Mac Catalyst 14.0+（26.2 起废弃）, macOS 11.0+（26.2 起废弃）, visionOS 1.0+（26.2 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaddsharedwebcredential(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaddsharedwebcredential(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaddsharedwebcredential%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:09d27091d90c8f60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAddSharedWebCredential(_:_:_:_:)

<sub>Function</sub>

Asynchronously stores (or updates) a shared password for a website.

> [!warning] Deprecated
> Use ASCredentialDataManager.save(password:for:title:anchor:)  (AuthenticationServices framework)

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func SecAddSharedWebCredential(_ fqdn: CFString, _ account: CFString, _ password: CFString?, _ completionHandler: @escaping (CFError?) -> Void)
```

## Parameters

- `fqdn` — The fully qualified domain name of the website requiring the password.

- `account` — The account name associated with this password.

- `password` — The password to be stored. Pass `NULL` to remove a shared password if it exists.

- `completionHandler` — A block invoked when the function has completed. The block takes one argument: - **`error`** — If the shared password was successfully added (or removed), `NULL`; if not successful, a [CFError](../corefoundation/cferror.md) object that encapsulates the reason why the password could not be added (or removed). The error reference is automatically released after this handler is called, though you may optionally retain it for as long as needed.

## Discussion

This function adds a shared password item that will be accessible by Safari and apps that have the specified fully qualified domain name in their [Associated Domains Entitlement](../bundleresources/entitlements/com.apple.developer.associated-domains.md). If a shared password item already exists for the specified website and account, it is updated with the provided password. To remove a password, pass `NULL` for the password parameter.

> [!note] Note
> Because a request involving shared web credentials may potentially require user interaction or other verification to be approved, this function is dispatched asynchronously; your code provides a completion handler that is called as soon as the results (if any) are available.

When this function is called, the system tries to get the site association file from the server. If the file is unavailable, the sever returns a 500-599 code.
