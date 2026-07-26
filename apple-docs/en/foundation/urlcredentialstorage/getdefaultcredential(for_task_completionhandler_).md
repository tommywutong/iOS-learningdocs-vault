---
title: 'getDefaultCredential(for:task:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlcredentialstorage/getdefaultcredential(for:task:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/getdefaultcredential(for:task:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/getdefaultcredential%28for%3Atask%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:e649c06a9ead03a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# getDefaultCredential(for:task:completionHandler:)

<sub>Instance Method</sub>

Gets the default credential for the specified protection space, which is being accessed by the given task, and passes it to the provided completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getDefaultCredential(for space: URLProtectionSpace, task: URLSessionTask, completionHandler: @escaping @Sendable (URLCredential?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func defaultCredential(for space: URLProtectionSpace, task: URLSessionTask) async -> URLCredential?
```

## Parameters

- `space` — The protection space of interest.

- `task` — The task seeking to use the protection space

- `completionHandler` — A completion handler that receives the default credential as its argument, or `nil` if there is no default credential for this combination of protection space and task.

## See Also

### Getting and setting default credentials

- [- defaultCredentialForProtectionSpace:](<defaultcredential(for_).md>) — Returns the default credential for the specified protection space.
- [- setDefaultCredential:forProtectionSpace:](<setdefaultcredential(__for_).md>) — Sets the default credential for a specified protection space.
- [- setDefaultCredential:forProtectionSpace:task:](<setdefaultcredential(__for_task_).md>) — Sets the default credential for a given protection space, which is being accessed by the given task.
