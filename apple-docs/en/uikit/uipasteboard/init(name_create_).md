---
title: 'init(name:create:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/init(name:create:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/init(name:create:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/init%28name%3Acreate%3A%29.json'
content_hash: 'sha256:800b0ea080c0b512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# init(name:create:)

<sub>Initializer</sub>

Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init?(name pasteboardName: UIPasteboard.Name, create: Bool)
```

## Parameters

- `pasteboardName` — A string or string constant that identifies (or should identify) the pasteboard. To create a pasteboard with a `nil` name, specify a `nil` value for this parameter.

- `create` — A Boolean value that specifies whether to create the pasteboard if it doesn’t already exist. Specify [false](../../swift/false.md) for system pasteboards or if you want to use an existing app pasteboard.

## Return Value

A pasteboard object you can use to transfer data within an app or between apps that have the same team ID.

## Discussion

Call this method to create custom app pasteboards. (You can also use it to obtain the general pasteboard, but the [generalPasteboard](general.md) class method exists for that purpose.) App pasteboards this method returns aren’t persistent, existing only until the app quits. Starting in iOS 10, persistent, named pasteboards are deprecated. Instead, use a shared container, as described in the overview for the [UIPasteboard](../uipasteboard.md) class.

## See Also

### Getting and removing pasteboards

- [generalPasteboard](general.md) — The systemwide general pasteboard, which you use for general copy-paste operations.
- [+ pasteboardWithUniqueName](<withuniquename().md>) — Returns an app pasteboard that you identify by a unique system-generated name.
- [+ removePasteboardWithName:](<remove(withname_).md>) — Invalidates the designated app pasteboard.
