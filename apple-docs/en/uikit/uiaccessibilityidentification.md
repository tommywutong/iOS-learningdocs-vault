---
title: UIAccessibilityIdentification
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityidentification
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityidentification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityidentification.json'
content_hash: 'sha256:a38d59355b00ac04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityIdentification

<sub>Protocol</sub>

Methods that associate a unique identifier with elements in your user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIAccessibilityIdentification : NSObjectProtocol
```

## Overview

You can use the identifiers you define in UI Automation scripts because the value of [accessibilityIdentifier](../appkit/nsaccessibility-c.protocol/accessibilityidentifier.md) corresponds to the return value of the name method of `UIAElement`.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIAccessibilityElement](uiaccessibilityelement.md), [UIAction](uiaction.md), [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIAlertAction](uialertaction.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIBarButtonItem](uibarbuttonitem.md), [UIBarItem](uibaritem.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorWell](uicolorwell.md), [UICommand](uicommand.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIDeferredMenuElement](uideferredmenuelement.md), [UIEventAttributionView](uieventattributionview.md), [UIImage](uiimage.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UIKeyCommand](uikeycommand.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UIMenu](uimenu.md), [UIMenuElement](uimenuelement.md), [UINavigationBar](uinavigationbar.md), [UIPageControl](uipagecontrol.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIRefreshControl](uirefreshcontrol.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchTab](uisearchtab.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITab](uitab.md), [UITabBar](uitabbar.md), [UITabBarItem](uitabbaritem.md), [UITabGroup](uitabgroup.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIView](uiview.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md), [ActivationAction](uiwindowscene/activationaction.md)

## Topics

### Accessing an element identifier

- [accessibilityIdentifier](uiaccessibilityidentification/accessibilityidentifier.md) — A string that identifies the element.

## See Also

### Behaviors

- [UIAccessibilityFocus](../objectivec/uiaccessibilityfocus.md) — An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityReadingContent](uiaccessibilityreadingcontent.md) — Methods to implement for an object that represents content that users read, such as a book or an article.
- [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md) — Methods to determine when to adjust images for different content size categories.
- [UIAccessibilityTextualContext](uiaccessibilitytextualcontext.md) — Constants that describe a named context that helps identify and classify the type of text inside an element.
