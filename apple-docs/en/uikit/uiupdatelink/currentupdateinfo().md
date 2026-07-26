---
title: currentUpdateInfo()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiupdatelink/currentupdateinfo()
source_url: 'https://developer.apple.com/documentation/uikit/uiupdatelink/currentupdateinfo()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiupdatelink/currentupdateinfo%28%29.json'
content_hash: 'sha256:a3bbad820f4b37b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUpdateLink](../uiupdatelink.md)

# currentUpdateInfo()

<sub>Instance Method</sub>

Returns an object that describes the current UI update state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func currentUpdateInfo() -> UIUpdateInfo?
```

## Return Value

During a UI update, returns a [UIUpdateInfo](../uiupdateinfo.md) object that describes the current UI update state. Outside a UI update, returns `nil`.

## See Also

### Getting the current UI update information

- [UIUpdateInfo](../uiupdateinfo.md) — An object that contains detailed information about the current UI update state.
