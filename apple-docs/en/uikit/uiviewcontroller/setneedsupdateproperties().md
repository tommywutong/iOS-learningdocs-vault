---
title: setNeedsUpdateProperties()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/setneedsupdateproperties()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateproperties()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setneedsupdateproperties%28%29.json'
content_hash: 'sha256:b698be0fba6626a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setNeedsUpdateProperties()

<sub>Instance Method</sub>

Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsUpdateProperties()
```

## See Also

### Managing the view’s properties

- [ViewLoading](viewloading.md) — A property wrapper that loads the view controller’s view before accessing the property.
- [- updateProperties](<updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- updatePropertiesIfNeeded](<updatepropertiesifneeded().md>) — Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
