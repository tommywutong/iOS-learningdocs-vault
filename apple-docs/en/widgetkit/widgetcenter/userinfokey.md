---
title: WidgetCenter.UserInfoKey
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetcenter/userinfokey
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetcenter/userinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetcenter/userinfokey.json'
content_hash: 'sha256:9e248db7bd4c902c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetCenter](../widgetcenter.md)

# WidgetCenter.UserInfoKey

<sub>Structure</sub>

An object that defines keys for accessing information in a user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct UserInfoKey
```

## Overview

> [!note] Note
> In Objective-C, use [WGWidgetUserInfoKeyFamily](../wgwidgetuserinfokeyfamily.md) and [WGWidgetUserInfoKeyKind](../wgwidgetuserinfokeykind.md) instead.

## Topics

### Describing a widget

- [family](userinfokey/family.md) — A key you use to access the widget’s family.
- [kind](userinfokey/kind.md) — A key you use to access the widget’s kind. The value matches the `kind` property specified in the widget’s configuration.

### Describing a Live Activity

- [activityID](userinfokey/activityid.md) — A key you use to access the activity ID if the widget represents a Live Activity.

## See Also

### Getting Widget Information

- [shared](shared.md) — The shared widget center.
- [getCurrentConfigurations(_:)](<getcurrentconfigurations(__).md>) — Retrieves information about user-configured widgets.
