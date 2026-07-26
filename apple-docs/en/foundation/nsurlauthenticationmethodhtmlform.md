---
title: NSURLAuthenticationMethodHTMLForm
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlauthenticationmethodhtmlform
source_url: 'https://developer.apple.com/documentation/foundation/nsurlauthenticationmethodhtmlform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlauthenticationmethodhtmlform.json'
content_hash: 'sha256:94433bb44b8853fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLAuthenticationMethodHTMLForm

<sub>Global Variable</sub>

Use HTML form authentication for this protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLAuthenticationMethodHTMLForm: String
```

## Discussion

The URL loading system never issues authentication challenges based on this authentication method. However, if your app authenticates by submitting a web form (or in some other protocol-neutral way), you can specify this protection space when you persist or look up credentials using the [URLCredentialStorage](urlcredentialstorage.md) class.

## See Also

### Task-specific authentication challenges

- [NSURLAuthenticationMethodDefault](nsurlauthenticationmethoddefault.md) — Use the default authentication method for a protocol.
- [NSURLAuthenticationMethodHTTPBasic](nsurlauthenticationmethodhttpbasic.md) — Use HTTP basic authentication for this protection space.
- [NSURLAuthenticationMethodHTTPDigest](nsurlauthenticationmethodhttpdigest.md) — Use HTTP digest authentication for this protection space.
