---
title: UIActivityIndicatorView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityindicatorview
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityindicatorview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityindicatorview.json'
content_hash: 'sha256:d4c5a53a74aba532'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityIndicatorView

<sub>Class</sub>

A view that shows that a task is in progress.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIActivityIndicatorView
```

## Overview

You control when an activity indicator animates by calling the [- startAnimating](<uiactivityindicatorview/startanimating().md>) and [- stopAnimating](<uiactivityindicatorview/stopanimating().md>) methods. To automatically hide the activity indicator when animation stops, set the [hidesWhenStopped](uiactivityindicatorview/hideswhenstopped.md) property to [true](../swift/true.md).

You can set the color of the activity indicator by using the [color](uiactivityindicatorview/color.md) property.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating an activity indicator

- [- initWithActivityIndicatorStyle:](<uiactivityindicatorview/init(style_).md>) — Creates an activity indicator.
- [- initWithFrame:](<uiactivityindicatorview/init(frame_).md>) — Creates an activity indicator with the specified frame rectangle.
- [- initWithCoder:](<uiactivityindicatorview/init(coder_).md>) — Creates an activity indicator from data in an unarchiver.

### Managing an activity indicator

- [- startAnimating](<uiactivityindicatorview/startanimating().md>) — Starts the animation of the progress indicator.
- [- stopAnimating](<uiactivityindicatorview/stopanimating().md>) — Stops the animation of the progress indicator.
- [animating](uiactivityindicatorview/isanimating.md) — A Boolean value indicating whether the activity indicator is currently running its animation.
- [hidesWhenStopped](uiactivityindicatorview/hideswhenstopped.md) — A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.

### Configuring the activity indicator appearance

- [activityIndicatorViewStyle](uiactivityindicatorview/style-swift.property.md) — The basic appearance of the activity indicator.
- [color](uiactivityindicatorview/color.md) — The color of the activity indicator.

### Constants

- [Style](uiactivityindicatorview/style-swift.enum.md) — The visual style of the progress indicator.

### Initializers

- [init(activityIndicatorStyle:)](<uiactivityindicatorview/init(activityindicatorstyle_).md>)

## See Also

### Content views

- [UICalendarView](uicalendarview.md) — A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [UIContentUnavailableView](uicontentunavailableview.md) — A view that indicates there’s no content to display.
- [UIImageView](uiimageview.md) — A view that displays a single image or a sequence of animated images in your interface.
- [UIPickerView](uipickerview.md) — A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
- [UIProgressView](uiprogressview.md) — A view that depicts the progress of a task over time.
