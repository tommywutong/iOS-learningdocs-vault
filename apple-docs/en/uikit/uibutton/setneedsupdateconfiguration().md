---
title: setNeedsUpdateConfiguration()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/setneedsupdateconfiguration()
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/setneedsupdateconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/setneedsupdateconfiguration%28%29.json'
content_hash: 'sha256:833688cf6e9f3824'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# setNeedsUpdateConfiguration()

<sub>Instance Method</sub>

Requests the system update the button configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsUpdateConfiguration()
```

## Discussion

Call this method to make the system call [- updateConfiguration](<updateconfiguration().md>). The system calls this method automatically when the button’s state changes. If you call this method multiple times before the system calls [- updateConfiguration](<updateconfiguration().md>), the system calls [- updateConfiguration](<updateconfiguration().md>) once.

## See Also

### Managing the appearance with a configuration object

- [configuration](configuration-5rlyb.md) — The configuration for the button’s appearance.
- [automaticallyUpdatesConfiguration](automaticallyupdatesconfiguration.md) — A Boolean value that determines whether the button configuration changes when button’s state changes.
- [- updateConfiguration](<updateconfiguration().md>) — Updates the button configuration in response to a button state change.
- [configurationUpdateHandler](configurationupdatehandler-swift.property.md) — A closure that executes when the button state changes.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — A closure to update the configuration of a button.
