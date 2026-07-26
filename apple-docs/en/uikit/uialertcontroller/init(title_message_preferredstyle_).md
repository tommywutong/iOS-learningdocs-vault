---
title: 'init(title:message:preferredStyle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uialertcontroller/init(title:message:preferredstyle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/init(title:message:preferredstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/init%28title%3Amessage%3Apreferredstyle%3A%29.json'
content_hash: 'sha256:92295f373346e11c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# init(title:message:preferredStyle:)

<sub>Initializer</sub>

Creates and returns a view controller for displaying an alert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(title: String?, message: String?, preferredStyle: UIAlertController.Style)
```

## Parameters

- `title` — The title of the alert. Use this string to get people’s attention and communicate the reason for the alert.

- `message` — Descriptive text that provides additional details about the reason for the alert.

- `preferredStyle` — The style to use when presenting the alert controller. Use this parameter to configure the alert controller as an action sheet or as a modal alert.

## Return Value

An initialized alert controller object.

## Discussion

After creating the alert controller, configure any actions that you want people to be able to perform by calling the [- addAction:](<addaction(__).md>) method one or more times. When specifying a preferred style of [UIAlertControllerStyleAlert](style/alert.md), you may also configure one or more text fields to display in addition to the actions.
