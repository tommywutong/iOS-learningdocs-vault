---
title: UIMenu.Identifier
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenu/identifier-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/identifier-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/identifier-swift.struct.json'
content_hash: 'sha256:e7aee259d85bd280'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# UIMenu.Identifier

<sub>Structure</sub>

Constants you use to identify an app’s standard menus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Identifier
```

## Overview

Use these constants to identify [UIMenu](../uimenu.md) objects containing standard configurations.

When creating a custom menu identifier, provide a reverse domain name string value, such as `UIMenu.Identifier("com.example.apple-samplecode.MenubarSample.reloadMenu")`.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Top-level menus

- [UIMenuApplication](identifier-swift.struct/application.md) — The standard app menu.
- [UIMenuFile](identifier-swift.struct/file.md) — The standard File menu.
- [UIMenuEdit](identifier-swift.struct/edit.md) — The standard Edit menu.
- [UIMenuView](identifier-swift.struct/view.md) — The standard View menu.
- [UIMenuWindow](identifier-swift.struct/window.md) — The standard Window menu.
- [UIMenuHelp](identifier-swift.struct/help.md) — The standard Help menu.

### App menu commands

- [UIMenuAbout](identifier-swift.struct/about.md) — The About menu.
- [UIMenuPreferences](identifier-swift.struct/preferences.md) — The Preferences menu.
- [UIMenuServices](identifier-swift.struct/services.md) — The Services menu.
- [UIMenuHide](identifier-swift.struct/hide.md) — The Hide menu.
- [UIMenuQuit](identifier-swift.struct/quit.md) — The Quit menu.

### File menus

- [UIMenuNewItem](identifier-swift.struct/newitem.md) — New item menu
- [UIMenuNewScene](identifier-swift.struct/newscene.md) — The New Scene menu. _(deprecated)_
- [UIMenuOpenRecent](identifier-swift.struct/openrecent.md) — The Open Recent menu.
- [UIMenuOpen](identifier-swift.struct/open.md) — The Open menu.
- [UIMenuClose](identifier-swift.struct/close.md) — The Close menu.
- [UIMenuPrint](identifier-swift.struct/print.md) — The Print menu.
- [UIMenuDocument](identifier-swift.struct/document.md) — The Document menu.

### Edit menus

- [UIMenuUndoRedo](identifier-swift.struct/undoredo.md) — The Undo/Redo menu.
- [UIMenuStandardEdit](identifier-swift.struct/standardedit.md) — The standard Edit menu.
- [UIMenuFind](identifier-swift.struct/find.md) — The Find menu.
- [UIMenuFindPanel](identifier-swift.struct/findpanel.md) — Find panel menu (Find, Find and Replace, Find Next, Find Previous)
- [UIMenuReplace](identifier-swift.struct/replace.md) — The Replace menu.
- [UIMenuShare](identifier-swift.struct/share.md) — The Share menu.
- [UIMenuTextStyle](identifier-swift.struct/textstyle.md) — The Text Style menu.
- [UIMenuSpelling](identifier-swift.struct/spelling.md) — The Spelling menu.
- [UIMenuSpellingPanel](identifier-swift.struct/spellingpanel.md) — The Spelling Panel menu.
- [UIMenuSpellingOptions](identifier-swift.struct/spellingoptions.md) — The Spelling Options menu.
- [UIMenuSubstitutions](identifier-swift.struct/substitutions.md) — The Substitutions menu.
- [UIMenuSubstitutionsPanel](identifier-swift.struct/substitutionspanel.md) — The Substitutions Panel menu.
- [UIMenuSubstitutionOptions](identifier-swift.struct/substitutionoptions.md) — The Substitutions Options menu.
- [UIMenuTransformations](identifier-swift.struct/transformations.md) — The Transformations menu.
- [UIMenuSpeech](identifier-swift.struct/speech.md) — The Speech menu.
- [UIMenuLookup](identifier-swift.struct/lookup.md) — The Lookup menu.
- [UIMenuLearn](identifier-swift.struct/learn.md) — The Learn menu.
- [UIMenuFormat](identifier-swift.struct/format.md) — The Format menu.
- [UIMenuFont](identifier-swift.struct/font.md) — The Font menu.
- [UIMenuTextSize](identifier-swift.struct/textsize.md) — The Text Size menu.
- [UIMenuTextColor](identifier-swift.struct/textcolor.md) — The Text Color menu.
- [UIMenuTextStylePasteboard](identifier-swift.struct/textstylepasteboard.md) — The Text Style Pasteboard menu.
- [UIMenuText](identifier-swift.struct/text.md) — The Text menu.
- [UIMenuAutoFill](identifier-swift.struct/autofill.md) — The AutoFill menu.
- [UIMenuWritingDirection](identifier-swift.struct/writingdirection.md) — The Writing Direction menu.
- [UIMenuAlignment](identifier-swift.struct/alignment.md) — The Alignment menu.

### View menus

- [UIMenuToolbar](identifier-swift.struct/toolbar.md) — The Toolbar menu group.
- [UIMenuSidebar](identifier-swift.struct/sidebar.md) — The Sidebar menu group.
- [UIMenuFullscreen](identifier-swift.struct/fullscreen.md) — The Full Screen menu.

### Window menus

- [UIMenuMinimizeAndZoom](identifier-swift.struct/minimizeandzoom.md) — The Minimize and Zoom menu.
- [UIMenuBringAllToFront](identifier-swift.struct/bringalltofront.md) — The Bring All to Front menu.

### Root menu

- [UIMenuRoot](identifier-swift.struct/root.md) — The root menu.

### Initializers

- [init(_:)](<identifier-swift.struct/init(__).md>) — Creates a menu identifier.
- [init(rawValue:)](<identifier-swift.struct/init(rawvalue_).md>) — Creates a menu identifier with the specified raw value.

## See Also

### Creating a menu object

- [init(title:image:identifier:options:children:)](<init(title_image_identifier_options_children_).md>) — Creates a new menu with the specified values.
- [init(title:subtitle:image:identifier:options:children:)](<init(title_subtitle_image_identifier_options_children_).md>) — Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [init(title:subtitle:image:identifier:options:preferredElementSize:children:)](<init(title_subtitle_image_identifier_options_preferredelementsize_children_).md>) — Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [Options](options-swift.struct.md) — Options you use to configure a menu’s appearance.
- [- initWithCoder:](<init(coder_).md>) — Creates a menu from data in an unarchiver.
