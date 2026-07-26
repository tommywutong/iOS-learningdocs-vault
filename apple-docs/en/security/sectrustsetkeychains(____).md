---
title: 'SecTrustSetKeychains(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.3+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustsetkeychains(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetkeychains(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetkeychains%28_%3A_%3A%29.json'
content_hash: 'sha256:c59ebcbe0356240d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetKeychains(_:_:)

<sub>Function</sub>

Sets the keychains searched for intermediate certificates when evaluating a trust management object.

<sub>macOS</sub>

```swift
func SecTrustSetKeychains(_ trust: SecTrust, _ keychainOrArray: CFTypeRef?) -> OSStatus
```

## Parameters

- `trust` — The trust management object containing the certificate you want to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

- `keychainOrArray` — A keychain object for a single keychain to search, an array of keychain objects for a set of keychains to search, or `NULL` to search the user’s default keychain search list. To prevent the [SecTrustEvaluate](<sectrustevaluate(____).md>) function from searching any keychains at all, pass a `CFArrayRef` array with no elements.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

By default, [SecTrustEvaluateWithError](<sectrustevaluatewitherror(____).md>) uses the user’s keychain search list to look for intermediate certificates in the certificate chain. Use the `SecTrustSetKeychains` function to change the set of keychains to be searched. If you want to modify the default set of keychains, first call the `SecKeychainCopySearchList` function (see [Keychain services](keychain-services.md)) to obtain the current keychain search list, modify that set as you wish, and create a new search list. Then you can call `SecTrustSetKeychains` with the modified list.

Use the [SecTrustSetAnchorCertificates](<sectrustsetanchorcertificates(____).md>) function to set the array of anchor certificates searched.

It is safe to call this function concurrently on two or more threads as long as it is not used to change the value of a trust management object that is simultaneously being used by another function. For example, you cannot call this function on one thread at the same time as you are calling the evaluation function for the same trust management object on another thread, but you can call this function and simultaneously evaluate a different trust management object on another thread. Similarly, calls to functions that return information about a trust management object (such as the [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) function) may fail or return an unexpected result if this function is simultaneously changing the same trust management object on another thread.
