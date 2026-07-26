---
title: SWAttributionView
framework: Shared with You
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/sharedwithyou/swattributionview
source_url: 'https://developer.apple.com/documentation/sharedwithyou/swattributionview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sharedwithyou/swattributionview.json'
content_hash: 'sha256:7af70fdaafd069dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Shared with You](../sharedwithyou.md)

# SWAttributionView

<sub>Class</sub>

A view that displays the sender who shares a highlight and provides related actions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class SWAttributionView
```

## Overview

The `SWAttributionView` also allows users to get back to the conversation about the [SWHighlight](swhighlight.md) content, and other related actions using a [highlightMenu](swattributionview/highlightmenu.md).

Place an `SWAttributionView` next to the content represented by its `SWHighlight`. The `SWAttributionView` displays the names and avatars within the provided horizontal space.

You can constrain this view’s width anchor or set its frame width to control the maximum width of its contents after which truncation may occur. Don’t constrain the view’s height, as the height is dependent on the [preferredContentSizeCategory](../uikit/uiapplication/preferredcontentsizecategory.md), and the resulting font size. To provide enough vertical space around this view, reference its [heightAnchor](../uikit/uiview/heightanchor.md) when using Auto Layout, or its [intrinsicContentSize](../uikit/uiview/intrinsiccontentsize.md) when using manual layout.

## Relationships

- **Inherits From**: [NSView](../appkit/nsview.md), [UIView](../uikit/uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearance](../uikit/uiappearance.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UICoordinateSpace](../uikit/uicoordinatespace.md), [UIDynamicItem](../uikit/uidynamicitem.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIFocusItem](../uikit/uifocusitem.md), [UIFocusItemContainer](../uikit/uifocusitemcontainer.md), [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Customizing highlights

- [backgroundStyle](swattributionview/backgroundstyle-swift.property.md) — The background style of the child view that contains names and avatars.
- [displayContext](swattributionview/displaycontext-swift.property.md) — The context for the content the system displays with this view.
- [highlight](swattributionview/highlight.md) — The highlight you use to display this attribution.
- [highlightMenu](swattributionview/highlightmenu.md) — A menu with a list of system actions specific to this hightlight.
- [horizontalAlignment](swattributionview/horizontalalignment-swift.property.md) — The horizontal alignment of the view.
- [menuTitleForHideAction](swattributionview/menutitleforhideaction.md) — A localized string the system uses as a custom title for the hide menu item.
- [preferredMaxLayoutWidth](swattributionview/preferredmaxlayoutwidth.md) — A width the system uses to constrain the view contents.
- [supplementalMenu](swattributionview/supplementalmenu.md) — A supplemental menu to augment the attribution view’s existing menu.

### Customizing the view

- [BackgroundStyle](swattributionview/backgroundstyle-swift.enum.md) — The background styling of the attribution view’s contents.
- [DisplayContext](swattributionview/displaycontext-swift.enum.md) — The context for the content that influences the ranking of this view’s highlight.
- [HorizontalAlignment](swattributionview/horizontalalignment-swift.enum.md) — The horizontal alignment of attribution view’s contents.
