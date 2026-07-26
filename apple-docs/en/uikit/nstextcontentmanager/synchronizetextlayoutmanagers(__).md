---
title: 'synchronizeTextLayoutManagers(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentmanager/synchronizetextlayoutmanagers(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/synchronizetextlayoutmanagers(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/synchronizetextlayoutmanagers%28_%3A%29.json'
content_hash: 'sha256:e19c79099c9bb80c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# synchronizeTextLayoutManagers(_:)

<sub>Instance Method</sub>

Synchronizes changes to all nonprimary text layout managers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func synchronizeTextLayoutManagers(_ completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func synchronizeTextLayoutManagers() async throws
```

## Parameters

- `completionHandler` — A completion handler that runs on success, or to handle error conditions.

## Discussion

If `completionHandler` is `nil`, this method performs the operation synchronously. The framework passes any error to the `completionHandler`. The method blocks (or fails, if synchronous) when there’s an active transaction.

## See Also

### Working with layout managers

- [primaryTextLayoutManager](primarytextlayoutmanager.md) — The primary text layout manager for this content.
- [textLayoutManagers](textlayoutmanagers.md) — The array of text layout managers associated with this text content manager.
- [automaticallySynchronizesTextLayoutManagers](automaticallysynchronizestextlayoutmanagers.md) — Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [- addTextLayoutManager:](<addtextlayoutmanager(__).md>) — Adds the layout manager you provide to the list of layout managers.
- [- removeTextLayoutManager:](<removetextlayoutmanager(__).md>) — Removes the layout manager you specifiy from the list of layout managers.
