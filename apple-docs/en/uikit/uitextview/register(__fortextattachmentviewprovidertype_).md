---
title: 'register(_:forTextAttachmentViewProviderType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uitextview/register(_:fortextattachmentviewprovidertype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/register(_:fortextattachmentviewprovidertype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/register%28_%3Afortextattachmentviewprovidertype%3A%29.json'
content_hash: 'sha256:205459313da56178'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# register(_:forTextAttachmentViewProviderType:)

<sub>Instance Method</sub>

Register the UITextAttachmentViewProviderReusePolicy for all instances of a particular subclass of NSTextAttachmentViewProvider.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ policy: UITextAttachmentViewProviderReusePolicy, forTextAttachmentViewProviderType viewProviderType: AnyClass)
```

## See Also

### Managing attachment view reuse

- [UITextAttachmentViewProviderReusePolicy](../uitextattachmentviewproviderreusepolicy.md) — An option set that controls whether a text view reuses attachment view providers when scrolling or editing.
