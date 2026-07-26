---
title: 'registerViewProviderClass(_:forFileType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachment/registerviewproviderclass(_:forfiletype:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/registerviewproviderclass(_:forfiletype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/registerviewproviderclass%28_%3Aforfiletype%3A%29.json'
content_hash: 'sha256:fef64b7a518ffeee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# registerViewProviderClass(_:forFileType:)

<sub>Type Method</sub>

Registers a specific file type with the attachment view provider.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func registerViewProviderClass(_ textAttachmentViewProviderClass: AnyClass, forFileType fileType: String)
```

## Parameters

- `textAttachmentViewProviderClass` — The text attachment view provider class.

- `fileType` — A [String](../../swift/string.md) that represents the file type.

## See Also

### Convenience methods

- [+ textAttachmentViewProviderClassForFileType:](<textattachmentviewproviderclass(forfiletype_).md>) — Returns the text attachment view provider class, if any, for the file type you specify.
