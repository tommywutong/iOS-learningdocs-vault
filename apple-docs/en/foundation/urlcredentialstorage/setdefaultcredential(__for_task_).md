---
title: 'setDefaultCredential(_:for:task:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:task:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/setdefaultcredential(_:for:task:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/setdefaultcredential%28_%3Afor%3Atask%3A%29.json'
content_hash: 'sha256:88597f749490d133'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# setDefaultCredential(_:for:task:)

<sub>Instance Method</sub>

Sets the default credential for a given protection space, which is being accessed by the given task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDefaultCredential(_ credential: URLCredential, for protectionSpace: URLProtectionSpace, task: URLSessionTask)
```

## Parameters

- `credential` — The URL credential to set as the default for the protection space. If the receiver does not contain `credential` in the specified protection space it will be added.

- `protectionSpace` — The protection space whose default credential is being set.

- `task` — The task accessing the specified protection space. Subclasses of [URLCredentialStorage](../urlcredentialstorage.md) may use the request URL or other properties of this task to affect how the default credential is stored.

## See Also

### Getting and setting default credentials

- [- defaultCredentialForProtectionSpace:](<defaultcredential(for_).md>) — Returns the default credential for the specified protection space.
- [- getDefaultCredentialForProtectionSpace:task:completionHandler:](<getdefaultcredential(for_task_completionhandler_).md>) — Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.
- [- setDefaultCredential:forProtectionSpace:](<setdefaultcredential(__for_).md>) — Sets the default credential for a specified protection space.
