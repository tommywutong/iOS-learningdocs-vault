---
title: 'setPersistent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（10.0 起废弃）, iPadOS 3.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipasteboard/setpersistent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/setpersistent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/setpersistent%28_%3A%29.json'
content_hash: 'sha256:a97c35521e99fdcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# setPersistent(_:)

<sub>Instance Method</sub>

A Boolean value that indicates whether the pasteboard is persistent.

> [!warning] Deprecated
> Use shared app group containers instead. For more information about app groups, see [Adding an App to an App Group](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html#//apple_ref/doc/uid/TP40011195-CH4-SW19). For more information about shared containers, see the [containerURL(forSecurityApplicationGroupIdentifier:)](<../../foundation/filemanager/containerurl(forsecurityapplicationgroupidentifier_).md>) method of [FileManager](../../foundation/filemanager.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setPersistent(_ persistent: Bool)
```

## Discussion

Nonpersistent named pasteboards remain available. You can use these to implement such features as Duplicate or Copy Style. A nonpersistent named pasteboard is available only in the process that creates it.

## See Also

### Deprecated

- [persistent](ispersistent.md) — A Boolean value that indicates whether the pasteboard is persistent. _(deprecated)_
- [detectPatterns(for:completionHandler:)](<detectpatterns(for_completionhandler_)-5zlnd.md>) — Determines whether the first pasteboard item matches the specified patterns, without notifying the user. _(deprecated)_
- [detectPatterns(for:inItemSet:completionHandler:)](<detectpatterns(for_initemset_completionhandler_)-29iwn.md>) — Determines whether pasteboard items match the specified patterns, without notifying the user. _(deprecated)_
- [detectValues(for:completionHandler:)](<detectvalues(for_completionhandler_)-9p2ff.md>) — Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match. _(deprecated)_
- [detectValues(for:inItemSet:completionHandler:)](<detectvalues(for_initemset_completionhandler_)-8y0iw.md>) — Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match. _(deprecated)_
