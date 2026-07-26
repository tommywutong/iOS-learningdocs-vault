---
title: 'credentials(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/credentials(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/credentials(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/credentials%28for%3A%29.json'
content_hash: 'sha256:18bbaed42523a6b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# credentials(for:)

<sub>Instance Method</sub>

Returns a dictionary containing the credentials for the specified protection space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func credentials(for space: URLProtectionSpace) -> [String : URLCredential]?
```

## Parameters

- `space` — The protection space whose credentials you want to retrieve.

## Return Value

A dictionary containing the credentials for the specified protection space. The dictionary’s keys are user name strings, and each value is the corresponding [URLCredential](../urlcredential.md).

## Discussion

If you override this method, also override [- getCredentialsForProtectionSpace:task:completionHandler:](<getcredentials(for_task_completionhandler_).md>).

## See Also

### Retrieving credentials

- [allCredentials](allcredentials.md) — The credentials for all available protection spaces.
- [- getCredentialsForProtectionSpace:task:completionHandler:](<getcredentials(for_task_completionhandler_).md>) — Gets a dictionary containing the credentials for the specified protection space, on behalf of the given task, and passes the dictionary to the provided completion handler.
