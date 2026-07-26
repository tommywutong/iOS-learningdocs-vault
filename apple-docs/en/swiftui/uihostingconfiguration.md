---
title: UIHostingConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingconfiguration.json'
content_hash: 'sha256:355455c4ae1478a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIHostingConfiguration

<sub>Structure</sub>

A content configuration suitable for hosting a hierarchy of SwiftUI views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIHostingConfiguration<Content, Background> where Content : View, Background : View
```

## Overview

Use a value of this type, which conforms to the [UIContentConfiguration](../uikit/uicontentconfiguration-9eib5.md) protocol, with a [UICollectionViewCell](../uikit/uicollectionviewcell.md) or [UITableViewCell](../uikit/uitableviewcell.md) to host a hierarchy of SwiftUI views in a collection or table view, respectively. For example, the following shows a stack with an image and text inside the cell:

```swift
myCell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "star").foregroundStyle(.purple)
        Text("Favorites")
        Spacer()
    }
}
```

You can also customize the background of the containing cell. The following example draws a blue background:

```swift
myCell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "star").foregroundStyle(.purple)
        Text("Favorites")
        Spacer()
    }
}
.background {
    Color.blue
}
```

When used in a list layout, certain APIs are bridged automatically, like swipe actions and separator alignment. The following example shows a trailing yellow star swipe action:

```swift
cell.contentConfiguration = UIHostingConfiguration {
    HStack {
        Image(systemName: "airplane")
        Text("Flight 123")
        Spacer()
    }
    .swipeActions {
        Button { ... } label: {
            Label("Favorite", systemImage: "star")
        }
        .tint(.yellow)
    }
}
```

## Relationships

- **Conforms To**: [UIContentConfiguration](../uikit/uicontentconfiguration-9eib5.md)

## Topics

### Creating and updating a configuration

- [init(content:)](<uihostingconfiguration/init(content_).md>) — Creates a hosting configuration with the given contents.

### Setting the background

- [background(_:)](<uihostingconfiguration/background(__).md>) — Sets the background contents for the hosting configuration’s enclosing cell.
- [background(content:)](<uihostingconfiguration/background(content_).md>) — Sets the background contents for the hosting configuration’s enclosing cell.

### Setting margins

- [margins(_:_:)](<uihostingconfiguration/margins(____).md>) — Sets the margins around the content of the configuration.

### Setting a size

- [minSize(width:height:)](<uihostingconfiguration/minsize(width_height_).md>) — Sets the minimum size for the configuration.
- [minSize()](<uihostingconfiguration/minsize().md>) — Sets the minimum size for the configuration. _(deprecated)_

## See Also

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](../uikit/using-swiftui-with-uikit.md) — Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingController](uihostingcontroller.md) — A UIKit view controller that manages a SwiftUI view hierarchy.
- [UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md) — Options for how a hosting controller tracks its content’s size.
- [UIHostingSceneDelegate](uihostingscenedelegate.md) — Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.
