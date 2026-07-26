---
title: 'setDefaultCredential(_:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/setdefaultcredential%28_%3Afor%3A%29.json'
content_hash: 'sha256:a49f367e793b7289'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# setDefaultCredential(_:for:)

<sub>Instance Method</sub>

Sets the default credential for a specified protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDefaultCredential(_ credential: URLCredential, for space: URLProtectionSpace)
```

## Parameters

- `credential` — The URL credential to set as the default for `space`. If the receiver does not contain `credential` in the specified protection space it will be added.

- `space` — The protection space whose default credential is being set.

## Discussion

If you override this method, also override [- setDefaultCredential:forProtectionSpace:task:](<setdefaultcredential(__for_task_).md>).

## See Also

### Getting and setting default credentials

- [- defaultCredentialForProtectionSpace:](<defaultcredential(for_).md>) — Returns the default credential for the specified protection space.
- [- getDefaultCredentialForProtectionSpace:task:completionHandler:](<getdefaultcredential(for_task_completionhandler_).md>) — Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [- setDefaultCredential:forProtectionSpace:task:](<setdefaultcredential(__for_task_).md>) — Sets the default credential for a given protection space, which is being accessed by the given task.
