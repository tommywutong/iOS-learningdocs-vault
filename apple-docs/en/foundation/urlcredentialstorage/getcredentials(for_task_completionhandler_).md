---
title: 'getCredentials(for:task:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/getcredentials(for:task:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/getcredentials(for:task:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/getcredentials%28for%3Atask%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:231accc3cee4c46f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# getCredentials(for:task:completionHandler:)

<sub>Instance Method</sub>

Gets a dictionary containing the credentials for the specified protection space, on behalf of the given task, and passes the dictionary to the provided completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCredentials(for protectionSpace: URLProtectionSpace, task: URLSessionTask, completionHandler: @escaping @Sendable ([String : URLCredential]?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func credentials(for protectionSpace: URLProtectionSpace, task: URLSessionTask) async -> [String : URLCredential]?
```

## Parameters

- `protectionSpace` — The protection space whose credentials you want to retrieve.

- `task` — The task accessing the specified protection space.

- `completionHandler` — A completion handler that receives a single argument with the credentials for the specified protection space and task. The dictionary’s keys are user name strings, and the corresponding value is a [URLCredential](../urlcredential.md). If no credential has been set for this space, the argument to the completion handler is `nil`.

## See Also

### Retrieving credentials

- [allCredentials](allcredentials.md) — The credentials for all available protection spaces.
- [- credentialsForProtectionSpace:](<credentials(for_).md>) — Returns a dictionary containing the credentials for the specified protection space.
