---
title: 'textAttachmentViewProviderClass(forFileType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachment/textattachmentviewproviderclass(forfiletype:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/textattachmentviewproviderclass(forfiletype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/textattachmentviewproviderclass%28forfiletype%3A%29.json'
content_hash: 'sha256:4f361c86364016d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# textAttachmentViewProviderClass(forFileType:)

<sub>Type Method</sub>

Returns the text attachment view provider class, if any, for the file type you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func textAttachmentViewProviderClass(forFileType fileType: String) -> AnyClass?
```

## Parameters

- `fileType` — A [String](../../swift/string.md) that represents the file type.

## Return Value

The text attachment view provider class, or `nil` if the there is no class for the specified file type.

## See Also

### Convenience methods

- [+ registerTextAttachmentViewProviderClass:forFileType:](<registerviewproviderclass(__forfiletype_).md>) — Registers a specific file type with the attachment view provider.
