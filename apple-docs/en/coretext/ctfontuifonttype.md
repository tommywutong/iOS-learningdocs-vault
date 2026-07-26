---
title: CTFontUIFontType
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontuifonttype
source_url: 'https://developer.apple.com/documentation/coretext/ctfontuifonttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontuifonttype.json'
content_hash: 'sha256:ca01c1062c076114'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontUIFontType

<sub>Enumeration</sub>

Constants that represent the specific user-interface purpose to specify for font creation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFontUIFontType
```

## Overview

Use these constants with the [CTFontCreateUIFontForLanguage](<ctfontcreateuifontforlanguage(______).md>) function to indicate the intended user interface use of the font reference to be created.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTFontUIFontNone](ctfontuifonttype/none.md) — The user-interface font type isn’t specified.
- [kCTFontUIFontUser](ctfontuifonttype/user.md) — The default font for documents and other text whose font the user can typically change.
- [kCTFontUIFontUserFixedPitch](ctfontuifonttype/userfixedpitch.md) — The default font for documents and other text under the user’s control when that font is fixed-pitch.
- [kCTFontUIFontSystem](ctfontuifonttype/system.md) — The system font for standard user-interface items, such as button labels and menu items.
- [kCTFontUIFontEmphasizedSystem](ctfontuifonttype/emphasizedsystem.md) — The system font for emphasis in alerts.
- [kCTFontUIFontSmallSystem](ctfontuifonttype/smallsystem.md) — The standard small system font for informative text in alerts, column headings in lists, help tags, and small controls.
- [kCTFontUIFontSmallEmphasizedSystem](ctfontuifonttype/smallemphasizedsystem.md) — The small system font for emphasis.
- [kCTFontUIFontMiniSystem](ctfontuifonttype/minisystem.md) — The standard miniature system font for mini controls and utility window labels and text.
- [kCTFontUIFontMiniEmphasizedSystem](ctfontuifonttype/miniemphasizedsystem.md) — The miniature system font for emphasis.
- [kCTFontUIFontViews](ctfontuifonttype/views.md) — The default view font for text in lists and tables.
- [kCTFontUIFontApplication](ctfontuifonttype/application.md) — The default font for text documents.
- [kCTFontUIFontLabel](ctfontuifonttype/label.md) — The font for labels and tick marks on full-size sliders.
- [kCTFontUIFontMenuTitle](ctfontuifonttype/menutitle.md) — The font for menu titles.
- [kCTFontUIFontMenuItem](ctfontuifonttype/menuitem.md) — The font for menu items.
- [kCTFontUIFontMenuItemMark](ctfontuifonttype/menuitemmark.md) — The font to draw menu-item marks.
- [kCTFontUIFontMenuItemCmdKey](ctfontuifonttype/menuitemcmdkey.md) — The font for menu-item command-key equivalents.
- [kCTFontUIFontWindowTitle](ctfontuifonttype/windowtitle.md) — The font for window titles.
- [kCTFontUIFontPushButton](ctfontuifonttype/pushbutton.md) — The font for a push button, a rounded rectangular button with a text label on it.
- [kCTFontUIFontUtilityWindowTitle](ctfontuifonttype/utilitywindowtitle.md) — The font for utility window titles.
- [kCTFontUIFontAlertHeader](ctfontuifonttype/alertheader.md) — The font for alert headers.
- [kCTFontUIFontSystemDetail](ctfontuifonttype/systemdetail.md) — The standard system font for details.
- [kCTFontUIFontEmphasizedSystemDetail](ctfontuifonttype/emphasizedsystemdetail.md) — The system font for emphasis in details.
- [kCTFontUIFontToolbar](ctfontuifonttype/toolbar.md) — The font used for labels of toolbar items.
- [kCTFontUIFontSmallToolbar](ctfontuifonttype/smalltoolbar.md) — The small font for labels of toolbar items.
- [kCTFontUIFontMessage](ctfontuifonttype/message.md) — The font for standard interface items, such as button labels and menu items.
- [kCTFontUIFontPalette](ctfontuifonttype/palette.md) — The font in tool palettes.
- [kCTFontUIFontToolTip](ctfontuifonttype/tooltip.md) — The font for tool tips.
- [kCTFontUIFontControlContent](ctfontuifonttype/controlcontent.md) — The font for contents of user-interface controls.

### Deprecated

- [kCTFontNoFontType](ctfontuifonttype/kctfontnofonttype.md) — The user-interface font type isn’t specified. _(deprecated)_
- [kCTFontUserFontType](ctfontuifonttype/kctfontuserfonttype.md) — The font used by default for documents and other text under the user’s control. _(deprecated)_
- [kCTFontUserFixedPitchFontType](ctfontuifonttype/kctfontuserfixedpitchfonttype.md) — The font used by default for documents and other text under the user’s control when that font is fixed-pitch. _(deprecated)_
- [kCTFontSystemFontType](ctfontuifonttype/kctfontsystemfonttype.md) — The system font used for standard user-interface items, such as button labels and menu items. _(deprecated)_
- [kCTFontEmphasizedSystemFontType](ctfontuifonttype/kctfontemphasizedsystemfonttype.md) — The system font used for emphasis in alerts. _(deprecated)_
- [kCTFontSmallSystemFontType](ctfontuifonttype/kctfontsmallsystemfonttype.md) — The standard small system font used for informative text in alerts, column headings in lists, help tags, and small controls. _(deprecated)_
- [kCTFontSmallEmphasizedSystemFontType](ctfontuifonttype/kctfontsmallemphasizedsystemfonttype.md) — The small system font used for emphasis. _(deprecated)_
- [kCTFontMiniSystemFontType](ctfontuifonttype/kctfontminisystemfonttype.md) — The standard miniature system font used for mini controls and utility window labels and text. _(deprecated)_
- [kCTFontMiniEmphasizedSystemFontType](ctfontuifonttype/kctfontminiemphasizedsystemfonttype.md) — The miniature system font used for emphasis. _(deprecated)_
- [kCTFontViewsFontType](ctfontuifonttype/kctfontviewsfonttype.md) — The view font used as the default font of text in lists and tables. _(deprecated)_
- [kCTFontApplicationFontType](ctfontuifonttype/kctfontapplicationfonttype.md) — The default font for text documents. _(deprecated)_
- [kCTFontLabelFontType](ctfontuifonttype/kctfontlabelfonttype.md) — The font used for labels and tick marks on full-size sliders. _(deprecated)_
- [kCTFontMenuTitleFontType](ctfontuifonttype/kctfontmenutitlefonttype.md) — The font used for menu titles. _(deprecated)_
- [kCTFontMenuItemFontType](ctfontuifonttype/kctfontmenuitemfonttype.md) — The font used for menu items. _(deprecated)_
- [kCTFontMenuItemMarkFontType](ctfontuifonttype/kctfontmenuitemmarkfonttype.md) — The font used to draw menu-item marks. _(deprecated)_
- [kCTFontMenuItemCmdKeyFontType](ctfontuifonttype/kctfontmenuitemcmdkeyfonttype.md) — The font used for menu-item command-key equivalents. _(deprecated)_
- [kCTFontWindowTitleFontType](ctfontuifonttype/kctfontwindowtitlefonttype.md) — The font used for window titles. _(deprecated)_
- [kCTFontPushButtonFontType](ctfontuifonttype/kctfontpushbuttonfonttype.md) — The font used for a push button, a rounded rectangular button with a text label on it. _(deprecated)_
- [kCTFontUtilityWindowTitleFontType](ctfontuifonttype/kctfontutilitywindowtitlefonttype.md) — The font used for utility window titles. _(deprecated)_
- [kCTFontAlertHeaderFontType](ctfontuifonttype/kctfontalertheaderfonttype.md) — The font used for alert headers. _(deprecated)_
- [kCTFontSystemDetailFontType](ctfontuifonttype/kctfontsystemdetailfonttype.md) — The standard system font used for details. _(deprecated)_
- [kCTFontEmphasizedSystemDetailFontType](ctfontuifonttype/kctfontemphasizedsystemdetailfonttype.md) — The system font used for emphasis in details. _(deprecated)_
- [kCTFontToolbarFontType](ctfontuifonttype/kctfonttoolbarfonttype.md) — The font used for labels of toolbar items. _(deprecated)_
- [kCTFontSmallToolbarFontType](ctfontuifonttype/kctfontsmalltoolbarfonttype.md) — The small font used for labels of toolbar items. _(deprecated)_
- [kCTFontMessageFontType](ctfontuifonttype/kctfontmessagefonttype.md) — The font used for standard interface items, such as button labels and menu items. _(deprecated)_
- [kCTFontPaletteFontType](ctfontuifonttype/kctfontpalettefonttype.md) — The font used in tool palettes. _(deprecated)_
- [kCTFontToolTipFontType](ctfontuifonttype/kctfonttooltipfonttype.md) — The font used for tool tips. _(deprecated)_
- [kCTFontControlContentFontType](ctfontuifonttype/kctfontcontrolcontentfonttype.md) — The font used for contents of user-interface controls. _(deprecated)_

### Initializers

- [init(rawValue:)](<ctfontuifonttype/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontTableTag](ctfonttabletag.md) — Font table tags provide access to font table data.
- [CTFontTableOptions](ctfonttableoptions.md) — Constants that describe font table options.
- [CTFontOptions](ctfontoptions.md) — Options for font creation and descriptor matching.
