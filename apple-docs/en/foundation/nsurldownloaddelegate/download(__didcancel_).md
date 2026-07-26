---
title: 'download(_:didCancel:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:didcancel:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didcancel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Adidcancel%3A%29.json'
content_hash: 'sha256:9424a3c1f5885bf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:didCancel:)

<sub>Instance Method</sub>

Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, didCancel challenge: URLAuthenticationChallenge)
```

## Parameters

- `download` — The URL download object sending the message.

- `challenge` — The authentication challenge that caused the download object to cancel the download.

## Discussion

If the delegate receives this message the download will fail and the delegate will receive a [- download:didFailWithError:](<download(__didfailwitherror_).md>) message.

## See Also

### Download Authentication

- [- download:canAuthenticateAgainstProtectionSpace:](<download(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [- download:didReceiveAuthenticationChallenge:](<download(__didreceive_)-1pc0v.md>) — Sent when the URL download must authenticate a challenge in order to download the request.
- [- downloadShouldUseCredentialStorage:](<downloadshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should consult the credential storage to authenticate the download.
