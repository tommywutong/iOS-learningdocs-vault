---
title: 'downloadShouldUseCredentialStorage(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/downloadshouldusecredentialstorage(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/downloadshouldusecredentialstorage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/downloadshouldusecredentialstorage%28_%3A%29.json'
content_hash: 'sha256:47b30273ab769572'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# downloadShouldUseCredentialStorage(_:)

<sub>Instance Method</sub>

Sent to determine whether the URL loader should consult the credential storage to authenticate the download.

<sub>macOS</sub>

```swift
optional func downloadShouldUseCredentialStorage(_ download: NSURLDownload) -> Bool
```

## Parameters

- `download` — The connection sending the message.

## Discussion

This method is called before any attempt to authenticate is made.  By returning [false](../../swift/false.md), the delegate tells the download not to consult the credential storage and makes itself responsible for providing credentials for any authentication challenges.  Not implementing this method is the same as returing [true](../../swift/true.md). The delegate is free to consult the credential storage itself when it receives a [- download:didReceiveAuthenticationChallenge:](<download(__didreceive_)-1pc0v.md>) message.

## See Also

### Download Authentication

- [- download:canAuthenticateAgainstProtectionSpace:](<download(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [- download:didCancelAuthenticationChallenge:](<download(__didcancel_).md>) — Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [- download:didReceiveAuthenticationChallenge:](<download(__didreceive_)-1pc0v.md>) — Sent when the URL download must authenticate a challenge in order to download the request.
