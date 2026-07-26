---
title: allCredentials
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcredentialstorage/allcredentials
source_url: 'https://developer.apple.com/documentation/foundation/urlcredentialstorage/allcredentials'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcredentialstorage/allcredentials.json'
content_hash: 'sha256:1103265a681930d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCredentialStorage](../urlcredentialstorage.md)

# allCredentials

<sub>Instance Property</sub>

The credentials for all available protection spaces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allCredentials: [URLProtectionSpace : [String : URLCredential]] { get }
```

## Discussion

The dictionary has keys corresponding to the [URLProtectionSpace](../urlprotectionspace.md) instances. The values are dictionaries where the keys are user name strings, and each value is the corresponding [URLCredential](../urlcredential.md) instances.

## See Also

### Retrieving credentials

- [- credentialsForProtectionSpace:](<credentials(for_).md>) — Returns a dictionary containing the credentials for the specified protection space.
- [- getCredentialsForProtectionSpace:task:completionHandler:](<getcredentials(for_task_completionhandler_).md>) — Gets a dictionary containing the credentials for the specified protection space, on behalf of the given task, and passes the dictionary to the provided completion handler.
