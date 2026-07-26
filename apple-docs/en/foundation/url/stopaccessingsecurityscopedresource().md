---
title: stopAccessingSecurityScopedResource()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/stopaccessingsecurityscopedresource()
source_url: 'https://developer.apple.com/documentation/foundation/url/stopaccessingsecurityscopedresource()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/stopaccessingsecurityscopedresource%28%29.json'
content_hash: 'sha256:ba9aa7d227db1b25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# stopAccessingSecurityScopedResource()

<sub>Instance Method</sub>

Revokes the access granted to the url by a prior successful call to the complementary start function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stopAccessingSecurityScopedResource()
```

## Discussion

When you no longer need access to a file or directory pointed to by a security-scoped URL, such as one returned by resolving a security-scoped bookmark, call this method on the URL to relinquish access. You can also use its Core Foundation equivalent, the [CFURLStopAccessingSecurityScopedResource(_:)](<../../corefoundation/cfurlstopaccessingsecurityscopedresource(__).md>) function.

You must balance each call to [startAccessingSecurityScopedResource()](<startaccessingsecurityscopedresource().md>) for a given security-scoped URL with a call to [stopAccessingSecurityScopedResource()](<stopaccessingsecurityscopedresource().md>). When you make the last balanced call to [stopAccessingSecurityScopedResource()](<stopaccessingsecurityscopedresource().md>), you immediately lose access to the resource in question.

> [!warning] Warning
> If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources leak, your app loses its ability to add file-system locations to its sandbox, such as with Powerbox or security-scoped bookmarks, until relaunched.

If you call this method on a URL whose referenced resource you don’t have access to, nothing happens.

> [!note] Version note
> Security-scoped bookmarks aren’t available in versions of macOS prior to OS X 10.7.3.

## See Also

### Working with security scoped resources

- [startAccessingSecurityScopedResource()](<startaccessingsecurityscopedresource().md>) — Given a url created by resolving a bookmark data created with security scope, make the resource referenced by the url accessible to the process.
