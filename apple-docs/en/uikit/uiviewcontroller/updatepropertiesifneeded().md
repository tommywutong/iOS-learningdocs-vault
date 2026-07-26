---
title: updatePropertiesIfNeeded()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/updatepropertiesifneeded()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/updatepropertiesifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/updatepropertiesifneeded%28%29.json'
content_hash: 'sha256:31886345ef19c536'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# updatePropertiesIfNeeded()

<sub>Instance Method</sub>

Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updatePropertiesIfNeeded()
```

## See Also

### Managing the view’s properties

- [ViewLoading](viewloading.md) — A property wrapper that loads the view controller’s view before accessing the property.
- [- updateProperties](<updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- setNeedsUpdateProperties](<setneedsupdateproperties().md>) — Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.
