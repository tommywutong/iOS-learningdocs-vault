---
title: Populating SwiftUI menus with adaptive controls
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/populating-swiftui-menus-with-adaptive-controls
source_url: 'https://developer.apple.com/documentation/swiftui/populating-swiftui-menus-with-adaptive-controls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/populating-swiftui-menus-with-adaptive-controls.json'
content_hash: 'sha256:8e57521a99d309a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Menus and commands](menus-and-commands.md)

# Populating SwiftUI menus with adaptive controls

<sub>Article</sub>

Improve your app by populating menus with controls and organizing your content intuitively.

## Overview

Menus are versatile components you can populate adaptively and use to organize commands, actions, or items in your app.

In tight layouts or smaller devices, menus optimize space by displaying options on demand. Use menus to conceal complex interface options when actions can be logically grouped. You have options for configuring your menus, with various controls like [Button](button.md), [Toggle](toggle.md), [Slider](slider.md), [Divider](divider.md), and more. This adaptability ensures that your menus remain flexible and succinct while supporting complex use cases.

> [!note] Note
> While the code for creating a menu in SwiftUI is largely the same across platforms, the system may display the menu differently depending on the device.

### Plan the structure of your menus

Make your menus simple and flexible, able to adapt to various interfaces, such as regular and compact size classes on iOS and iPadOS and across macOS, tvOS, and visionOS.

A menu consists of three components:

- Label: A view that describes the purpose of the menu.
- Content: A closure that uses a [ViewBuilder](viewbuilder.md) to define the items inside the menu.
- Primary action: An optional closure that performs an action when someone clicks or taps the menu, instead of the default primary action of opening the menu. When provided, opening the menu becomes the secondary action, such as opening after a long press gesture instead of a tap.

For design guidance, see Human Interface Guidelines \> [Menus](https://developer.apple.com/design/human-interface-guidelines/menus).

### Populate your menus

A well-declared SwiftUI [Menu](menu.md) resembles its ultimate rendered appearance: the contents of the menu visually adapt to the purpose of each element. For example, inserting a `Button` in the menu’s closure renders an actionable menu item, while inserting a `Menu` creates a submenu item.

To render a menu item that performs a given action closure, use the `Button` control:

```swift
Menu("Actions") {
    Button("Duplicate") {
        // Duplicate action.
    }
    Button("Rename") {
        // Rename action.
    }
    Button("Delete…") {
        // Delete action.
    }
}
```

![A menu that displays the Duplicate, Rename, and Delete actions.](../../../attachments/3bb3a0df88df1ccaac6e7fb064aa1da1/menus-items@2x.png)

> [!note] Note
> SwiftUI controls and views are adaptive, and represent functionality and meaning, as well as visual representation. When you open a menu, the menu items appear in a context-appropriate order depending on the platform. For more information, see [menuOrder(_:)](<view/menuorder(__).md>).

To show a symbol next to the menu item title, use the [init(_:systemImage:action:)](<button/init(__systemimage_action_).md>) initializer:

```swift
Menu("Actions") {
    Button("Duplicate", systemImage: "doc.on.doc") {
        // Duplicate action.
    }
    Button("Rename", systemImage: "pencil") {
        // Rename action.
    }
    Button("Delete…", systemImage: "trash") {
        // Delete action.
    }
}
```

![](../../../attachments/74cbd5d73f9d46ff7693c5a0c9e72feb/menus-items-glyphs@2x.png)

<sub>A menu that displays the Duplicate, Rename, and Delete actions with system images to the left of the labels. The Duplicate menu item is represented by two overlapping documents. The Rename menu item is represented by a pencil. The Delete menu item is represented by a trash can.</sub>

You can also construct menu actions by adding the label closure initializers on `Button`. This method provides more flexibility for your subtitles.

To add a title and subtitle to a menu item, populate the control’s label closure with two [Text](text.md) views, in which the first text represents the title, and the second represents the subtitle. The following example shows this hierarchical style applied to the views:

```swift
Menu("Actions") {
    Button {
        // Duplicate action.
    } label: {
        Text("Duplicate")
        Text("Duplicate the component")
    }
    Button {
        // Rename action.
    } label: {
        Text("Rename")
        Text("Rename the component")
    }
    Button {
        // Delete action.
    } label: {
        Text("Delete…")
        Text("Delete the component")
    }
}
```

![](../../../attachments/1420cebee21ada69b5b4351e8f03ac57/menus-items-subtitles@2x.png)

<sub>A menu that displays the Duplicate, Rename, and Delete actions with text descriptions underneath the labels. The Duplicate menu item has the text description, Duplicate the component. The Rename menu item has the text description, Rename the component. The Delete menu item has the text description, Delete the component.</sub>

You can insert an icon by replacing the first `Text` with a [Label](label.md):

```swift
Menu("Actions") {
    Button {
        // Duplicate action.
    } label: {
        Label("Duplicate", systemImage: "doc.on.doc")
        Text("Duplicate the component")
    }
    Button {
        // Rename action.
    } label: {
        Label("Rename", systemImage: "pencil")
        Text("Rename the component")
    }
    Button {
        // Delete action.
    } label: {
        Label("Delete…", systemImage: "trash")
        Text("Delete the component")
    }
}
```

![](../../../attachments/74c40505f56cf948c1b562c023d33258/menus-items-subtitles-glyphs@2x.png)

<sub>A menu that displays the Duplicate, Rename, and Delete actions with text descriptions underneath the labels and icons to the left of each label and description. The Duplicate menu item is represented by two overlapping document icons, and has the text description, Duplicate the component. The Rename menu item is represented by a pencil icon, and has the text description, Rename the component. The Delete menu item is represented by a trash can icon, and has the text description of, Delete the component.</sub>

Add a visual warning cue to menu items that are destructive by nature. Add a [destructive](buttonrole/destructive.md) role to `Button` to tint the menu item red. Use `destructive` only for actions that require caution.

```swift
Menu("Actions") {
    // ...

    Button("Delete…", systemImage: "trash", role: .destructive) {
        // Delete action.
    }
}
```

![](../../../attachments/2daf68f488cfafde277f605a2626cf70/menus-items-subtitles-glyphs-destructive@2x.png)

<sub>A menu that displays the Duplicate, Rename, and Delete actions with text descriptions underneath the labels and icons to the right of each label and description. The Duplicate menu item is represented by two overlapping document icons, and has the text description, Duplicate the component. The Rename menu item is represented by a pencil icon, and has the text description, Rename the component. The Delete label has a red tint to indicate that it's a destructive action. The Delete menu item is represented by a trash can icon, and does not include a text description.</sub>

On macOS, menu items constructed with a `Label` render without an icon by default. Use the [titleAndIcon](labelstyle/titleandicon.md) style to override the system behavior and explicitly render an icon for the menu items.

```swift
Menu("Actions") {
    // ...
}
.labelStyle(.titleAndIcon)
```

Menus are also great for representing toggled items. To render a toggled menu item, you can add a `Toggle` to the menu’s content.

Because SwiftUI controls adapt to their context, a `Toggle` in a menu automatically appears with a checkmark indicating its on or off state.

```swift
Menu("Actions") {
    // ...

    Toggle(
        "Favorite",
        systemImage: "suit.heart",
        isOn: $isFavorite)
}
```

![](../../../attachments/5b6d821b385df892ec47f6335f3051e5/menus-items-toggle@2x.png)

<sub>A menu that displays the Duplicate, Rename, Delete, and Favorite actions with text descriptions underneath the labels and icons to the left of each label and description. The Duplicate menu item is represented by two overlapping document icons, and has the text description, Duplicate the component. The Rename menu item is represented by a pencil icon, and has the text description, Rename the component. The Delete menu item is represented by a trash can icon, and has the text description of, Delete the component. The Favorite menu item uses a toggle to favorite the item the menu affects. The Favorite menu item is represented by a heart icon, and does not include a text description. The Favorite menu item has a checkmark to the left of its label.</sub>

Just like `Button`, initialize a `Toggle` with a label closure for more flexibility.

```swift
Menu("Actions") {
    // ...

    Toggle(isOn: $isFavorite) {
        Label("Favorite", systemImage: "suit.heart")
        Text("Adds the component to the favorites list")
    }
}
```

![](../../../attachments/3229d99d00d8c29d95684d8b9c1bede8/menus-items-toggle-subtitles@2x.png)

<sub>A menu that displays the Duplicate, Rename, Delete, and Favorite actions with text descriptions underneath the labels and icons to the left of each label and description. The Duplicate menu item is represented by two overlapping document icons, and has the text description, Duplicate the component. The Rename menu item is represented by a pencil icon, and has the text description, Rename the component. The Delete menu item is represented by a trash can icon, and has the text description of, Delete the component. The Favorite menu item uses a toggle to favorite the item the menu affects. The Favorite menu item is represented by a heart icon, and has the text description, Adds the component to the favorites list. The Favorite menu item has a checkmark to the left of its label.</sub>

Use a [Picker](picker.md) within a menu to let people choose from a list of options:

```swift
enum Flavor: String, CaseIterable, Identifiable {
    case chocolate, vanilla, strawberry
    var id: Self { self }
}

@State private var selectedFlavor: Flavor = .chocolate

var body: some View {
    Picker("Flavor", selection: $selectedFlavor) {
        ForEach(Flavor.allCases) { flavor in
            Text(flavor.rawValue.capitalized)
                .tag(flavor)
        }
    }
}
```

![](../../../attachments/e0be6f1ffcfcb8b760d7267c430b80f1/menus-selection@2x.png)

<sub>A menu that displays a picker of ice cream flavors, including Chocolate, Vanilla, and Strawberry, with the Chocolate option checked.</sub>

This example embeds a picker within a menu, displaying multiple selectable items. Although you can select several options, only one item is active at any given time. The selected item, identified with a checkmark, indicates the current selection.

Adding a picker to a menu creates a more convenient and customized layout than several individual toggles. A picker provides a single interface to manage multiple options, ensuring a person can only select one item at a time. Multiple toggles might be more appropriate when your content doesn’t require mutual exclusivity.

```swift
enum Flavor: String, CaseIterable, Identifiable {
    case chocolate, vanilla, strawberry
    var id: Self { self }
}

@State private var selectedFlavor: Flavor = .chocolate
@State private var includesToppings: Bool = false

var body: some View {
    Menu("Ice Cream Order") {
        Button("Special request") {
            // Create a special request.
        }

        Toggle("Include toppings", isOn: $includesToppings)

        Picker("Flavor", selection: $selectedFlavor) {
            ForEach(Flavor.allCases) { flavor in
                Text(flavor.rawValue.capitalized)
                    .tag(flavor)
            }
        }
    }
}
```

![](../../../attachments/e698d5e49f4964093c95136e6d8c4eef/menus-selection-items@2x.png)

<sub>A menu that displays a picker of ice cream flavors and different picker styles. The options include Special request, Include toppings, Chocolate, Vanilla, and Strawberry, with the Chocolate option checked.</sub>

You can choose picker styles such as [inline](pickerstyle/inline.md), [menu](pickerstyle/menu.md), and [palette](pickerstyle/palette.md).

### Apply style to menu pickers

By default, picker options in menus appear inline. SwiftUI implicitly applies the `inline` style, allowing you to select options without navigating away from the current view. The inline style works well for settings or configurations that require immediate context.

When you apply the `menu` style to a picker within a menu, it transforms into a submenu, presenting options in a hierarchical manner. This style helps organize complex menus with categorized options.

```swift
enum Flavor: String, CaseIterable, Identifiable {
    case chocolate, vanilla, strawberry
    var id: Self { self }
}

@State private var selectedFlavor: Flavor = .chocolate
@State private var includesToppings: Bool = false

var body: some View {
    Menu("Ice Cream Order") {
        Button("Special request") {
            // Create a special request.
        }

        Toggle("Include toppings", isOn: $includesToppings)

        Picker("Flavor", selection: $selectedFlavor) {
            ForEach(Flavor.allCases) { flavor in
                Text(flavor.rawValue.capitalized)
                    .tag(flavor)
            }
        }
        .pickerStyle(.menu)
    }
}
```

![](../../../attachments/b5df2d7ccf7db24edf5ca2f78c7ebf71/menus-selection-submenu@2x.png)

<sub>A menu that displays a picker with a palette picker for ice cream flavors. Items in the menu include Special request, Include toppings, and Flavor. The Flavor item is closed, as indicated by a right-facing chevron at the right edge of the menu.</sub>

Palette pickers work best in compact scenarios in which someone chooses from a set of symbols. Palette pickers minimize icons, and turn into a horizontal scroll if there’s limited space.

```swift
enum Flavor: String, CaseIterable, Identifiable {
    case chocolate, vanilla, strawberry
    var id: Self { self }
}

@State private var selectedFlavor: Flavor = .chocolate
@State private var includesToppings: Bool = false

var body: some View {
    Menu("Ice Cream Order 3") {
        Button("Special request") {
            // Create a special request.
        }
        Toggle("Include toppings", isOn: $includesToppings)
        Picker("Flavor", selection: $selectedFlavor) {
            Text("🟤")
                .tag(Flavor.chocolate)
            Text("⚪️")
                .tag(Flavor.vanilla)
            Text("🔴")
                .tag(Flavor.strawberry)
        }
        .pickerStyle(.palette)
    }
}
```

![](../../../attachments/53632c52f56858fe243f5f7338f945b0/menus-picker-palette@2x.png)

<sub>A menu that displays a palette picker using horizontal space for items. Menu items include Special request and Include toppings. Under Flavor is a horizontal row of three colored circles used to represent the ice cream flavors. The left circle is brown, used to represent Chocolate. The brown circle has a gray highlight to indicate that Chocolate has been selected. The center circle is white, used to represent Vanilla. The right circle is red, used to represent Strawberry.</sub>

Menus can also handle numerical values with sliders and steppers.

```swift
@State private var quantity: Int = 1

Menu("Actions") {
    // ...

    Stepper(value: $quantity) {
        Text("Quantity: \(quantity)")
    }
}
```

![](../../../attachments/145fcfdcf81fe47fea508bf013dacff9/menus-picker-palette-stepper@2x.png)

<sub>A menu that displays a picker using a stepper. Menu items include Special request and Include toppings. Under Flavor is a horizontal row of three colored circles used to represent the ice cream flavors. The left circle is brown, used to represent Chocolate. The brown circle has a gray highlight to indicate that Chocolate has been selected. The center circle is white, used to represent Vanilla. The right circle is red, used to represent Strawberry. Beneath the colored circles is a line of gray text that shows the Quantity selected, indicating that three items have been selected. Beneath the Quantity line are a minus button, used to remove an item from the Quantity, and a plus button, used to add an item to the Quantity.</sub>

### Group menu items

SwiftUI provides multiple ways to group items within menus, including submenus, sections, and dividers.

Submenus group items hierarchically, hiding content until needed. A submenu keeps the main menu uncluttered, while providing access to additional options when necessary:

```swift
Menu("General Settings") {
    // The General Settings submenu.
    Button("Wi-Fi") { openWiFiSettings() }
    Button("Bluetooth") { openBluetoothSettings() }
    Button("Notifications") { openNotificationSettings() }
    
    // The Account Settings submenu.
    Menu("Account Settings") {
        Button("Profile") { openProfileSettings() }
        Button("Security") { openSecuritySettings() }
        Button("Privacy") { openPrivacySettings() }
    }
    
    // The Advanced Settings submenu.
    Menu("Advanced Settings") {
        Button("Developer Options") { openDeveloperOptions() }
        Button("System Update") { openSystemUpdate() }
        Button("Backup & Restore") { openBackupRestore() }
    }
}
```

![](../../../attachments/65219a24e08330ffaca4b8cb5731cb0d/menus-submenus-settings@2x.png)

<sub>A menu that displays submenus for various settings options. Menu items include Wi-Fi, Bluetooth, Notifications, Account Settings, and Advanced Settings. The Account Settings and Advanced Settings menu items have submenus, as indicated by a right-facing chevron at the right edge of the menu.</sub>

In the example above, the Settings menu populates with two submenus, grouping related and less-prominent settings actions.

You can also organize items with sections. The [Section](section.md) view groups items while keeping all elements visible, often with section headers for clarity. This style is useful for organizing related items within the root-level menu, providing clear separation and context for each group.

```swift
Menu("Settings") {
    // The General Settings submenu.
    Section("General Settings") {
        Button("Wi-Fi") { openWiFiSettings() }
        Button("Bluetooth") { openBluetoothSettings() }
        Button("Notifications") { openNotificationSettings() }
    }
    
    // The Account Settings submenu.
    Section("Account Settings") {
        Button("Profile") { openProfileSettings() }
        Button("Security") { openSecuritySettings() }
        Button("Privacy") { openPrivacySettings() }
    }
    
    // The Advanced Settings submenu.
    Section("Advanced Settings") {
        Button("Developer Options") { openDeveloperOptions() }
        Button("System Update") { openSystemUpdate() }
        Button("Backup & Restore") { openBackupRestore() }
    }
}
```

![](../../../attachments/7e9cd112271a5924e5a73c47b610c350/menus-submenus-settings-groups@2x.png)

<sub>A menu that displays submenus with dividers. At the top of the menu is a section, labeled General Settings, with the options Wi-Fi, Bluetooth, and Notifications. In the middle of the menu is a section, labeled Account Settings, with the options Profile, Security, and Privacy. At the bottom of the menu is a section, labeled Advanced Settings, with the options Developer Options, System Update, and Backup and Restore.</sub>

### Display compact menu items

When you want to display a few related actions in a single row within a menu, consider using a [ControlGroup](controlgroup.md). This method provides a compact, horizontally-grouped layout of up to four items.

```swift
Menu("Edit") {
    ControlGroup {
        Button {
            // Undo action
        } label: {
            Label("Undo", systemImage: "arrow.uturn.backward")
        }
        
        Button {
            // Redo action
        } label: {
            Label("Redo", systemImage: "arrow.uturn.forward")
        }
        
        Button {
            // Copy action
        } label: {
            Label("Copy", systemImage: "doc.on.doc")
        }
    }
    
    Divider()
    
    // Additional menu items here...
}
```

While submenus and sections are containers that group items, the `Divider` view provides a simple way to visually separate items within a menu. Unlike `Section`, `Divider` isn’t a container, but serves as a visual break that divides groups of items to organize and group like-commands for improved usability and uniformity across apps.

### Modify content behavior

Beyond populating a menu’s content, SwiftUI also offers a set of APIs to modify the default behavior of menu items.

SwiftUI offers a set of APIs to modify the default behavior of menu items. On iOS and iPadOS, the system rearranges menu items by default so the first items in a menu appear closest to the viewer’s point of interaction. To override this behavior and keep items in the order you define, use the [menuOrder(_:)](<view/menuorder(__).md>) modifier:

```swift
Menu("Settings", systemImage: "ellipsis.circle") {
    Button("Select") {
        // Select folders
    }
    Button("New Folder") {
        // Create folder
    }
    Picker("Appearance", selection: $appearance) {
        Label("Icons", systemImage: "square.grid.2x2").tag(Appearance.icons)
        Label("List", systemImage: "list.bullet").tag(Appearance.list)
    }
}
.menuOrder(.fixed)
```

> [!note] Note
> On macOS, menu items typically follow the standard macOS ordering rules, and don’t reorder for proximity.

By default, menus dismiss as soon as someone clicks or taps an item. If you want the person to make multiple selections, or repeat an action without reopening the menu, override this behavior with the [menuActionDismissBehavior(_:)](<view/menuactiondismissbehavior(__).md>) modifier on specific items.

The following code demonstrates:

- Increase and decrease actions that disable menu dismissal, letting someone click or tap them repeatedly to adjust the font size without re-opening the menu each time.
- A reset action that reverts the font to a default size. Because the action doesn’t disable the dismissal, the menu closes after resetting.

```swift
Menu("Font size") {
    Button(action: increase) {
        Label("Increase", systemImage: "plus.magnifyingglass")
    }
    .menuActionDismissBehavior(.disabled)
    Button("Reset", action: reset)
    Button(action: decrease) {
        Label("Decrease", systemImage: "minus.magnifyingglass")
    }
    .menuActionDismissBehavior(.disabled)
}
```

## See Also

### Creating a menu

- [Menu](menu.md) — A control for presenting a menu of actions.
- [menuStyle(_:)](<view/menustyle(__).md>) — Sets the style for menus within this view.
