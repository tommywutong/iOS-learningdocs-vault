---
title: Link
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/link
source_url: 'https://developer.apple.com/documentation/swiftui/link'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/link.json'
content_hash: 'sha256:8b0a3416edab6492'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Link

<sub>Structure</sub>

A control for navigating to a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Link<Label> where Label : View
```

## Overview

Create a link by providing a destination URL and a title. The title tells the user the purpose of the link, and can be a string, a title key that produces a localized string, or a view that acts as a label. The example below creates a link to `example.com` and displays the title string as a link-styled view:

```swift
Link("View Our Terms of Service",
      destination: URL(string: "https://www.example.com/TOS.html")!)
```

When a user taps or clicks a `Link`, the default behavior depends on the contents of the URL. For example, SwiftUI opens a Universal Link in the associated app if possible, or in the user’s default web browser if not. Alternatively, you can override the default behavior by setting the [openURL](environmentvalues/openurl.md) environment value with a custom [OpenURLAction](openurlaction.md):

```swift
Link("Visit Our Site", destination: URL(string: "https://www.example.com")!)
    .environment(\.openURL, OpenURLAction { url in
        print("Open \(url)")
        return .handled
    })
```

As with other views, you can style links using standard view modifiers depending on the view type of the link’s label. For example, a [Text](text.md) label could be modified with a custom [font(_:)](<view/font(__).md>) or [foregroundStyle(_:)](<view/foregroundstyle(__).md>) to customize the appearance of the link in your app’s UI.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a link

- [init(_:destination:)](<link/init(__destination_).md>) — Creates a control, consisting of a URL and a title resource, used to navigate to a URL.
- [init(destination:label:)](<link/init(destination_label_).md>) — Creates a control, consisting of a URL and a label, used to navigate to the given URL.

## See Also

### Linking to other content

- [ShareLink](sharelink.md) — A view that controls a sharing presentation.
- [SharePreview](sharepreview.md) — A representation of a type to display in a share preview.
- [TextFieldLink](textfieldlink.md) — A control that requests text input from the user when pressed.
- [HelpLink](helplink.md) — A button with a standard appearance that opens app-specific help documentation.
