---
title: 'download(_:canAuthenticateAgainstProtectionSpace:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:canauthenticateagainstprotectionspace:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:canauthenticateagainstprotectionspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Acanauthenticateagainstprotectionspace%3A%29.json'
content_hash: 'sha256:d5cf3215750172e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:canAuthenticateAgainstProtectionSpace:)

<sub>Instance Method</sub>

Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.

<sub>macOS</sub>

```swift
optional func download(_ connection: NSURLDownload, canAuthenticateAgainstProtectionSpace protectionSpace: URLProtectionSpace) -> Bool
```

## Parameters

- `connection` — The download sending the message.

- `protectionSpace` — The protection space that generates an authentication challenge.

## Discussion

This method is called before [- download:didReceiveAuthenticationChallenge:](<download(__didreceive_)-1pc0v.md>), allowing the delegate to inspect a protection space before attempting to authenticate against it. By returning [true](../../swift/true.md), the delegate indicates that it can handle the form of authentication, which it does in the subsequent call to [- download:didReceiveAuthenticationChallenge:](<download(__didreceive_)-1pc0v.md>). Not implementing this method is the same as returning [false](../../swift/false.md), in which case default authentication handling is used.

## See Also

### Download Authentication

- [- download:didCancelAuthenticationChallenge:](<download(__didcancel_).md>) — Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [- download:didReceiveAuthenticationChallenge:](<download(__didreceive_)-1pc0v.md>) — Sent when the URL download must authenticate a challenge in order to download the request.
- [- downloadShouldUseCredentialStorage:](<downloadshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should consult the credential storage to authenticate the download.
