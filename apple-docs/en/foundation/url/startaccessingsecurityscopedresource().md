---
title: startAccessingSecurityScopedResource()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/startaccessingsecurityscopedresource()
source_url: 'https://developer.apple.com/documentation/foundation/url/startaccessingsecurityscopedresource()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/startaccessingsecurityscopedresource%28%29.json'
content_hash: 'sha256:721fee2a84c52c4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# startAccessingSecurityScopedResource()

<sub>Instance Method</sub>

Given a url created by resolving a bookmark data created with security scope, make the resource referenced by the url accessible to the process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startAccessingSecurityScopedResource() -> Bool
```

## Return Value

`true` if the request to access the resource succeeded; otherwise, `false`.

## Discussion

When you obtain a security-scoped URL, such as by resolving a security-scoped bookmark, you can’t immediately use the resource it points to. To make the resource available to your app, by way of adding its location to your app’s sandbox, call this method on the security-scoped URL. You can also use Core Foundation equivalent, the [CFURLStartAccessingSecurityScopedResource(_:)](<../../corefoundation/cfurlstartaccessingsecurityscopedresource(__).md>) function.

If this method returns [true](../../swift/true.md), then you must relinquish access as soon as you finish using the resource. Call the [stopAccessingSecurityScopedResource()](<stopaccessingsecurityscopedresource().md>) method to relinquish access. You must balance each call to [startAccessingSecurityScopedResource()](<startaccessingsecurityscopedresource().md>) for a given security-scoped URL with a call to [stopAccessingSecurityScopedResource()](<stopaccessingsecurityscopedresource().md>). When you make the last balanced call to [stopAccessingSecurityScopedResource()](<stopaccessingsecurityscopedresource().md>), you immediately lose access to the resource in question.

> [!warning] Warning
> If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources leak, your app loses its ability to add file-system locations to its sandbox, such as with Powerbox or security-scoped bookmarks, until relaunched.

> [!note] Version note
> Security-scoped bookmarks aren’t available in versions of macOS prior to OS X 10.7.3.

## See Also

### Working with security scoped resources

- [stopAccessingSecurityScopedResource()](<stopaccessingsecurityscopedresource().md>) — Revokes the access granted to the url by a prior successful call to the complementary start function.
