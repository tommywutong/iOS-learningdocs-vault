---
title: UIProgressView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprogressview
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview.json'
content_hash: 'sha256:e12def7be406bc55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIProgressView

<sub>Class</sub>

A view that depicts the progress of a task over time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIProgressView
```

## Overview

The [UIProgressView](uiprogressview.md) class provides properties for managing the style of the progress bar and for getting and setting values that are pinned to the progress of a task.

For an indeterminate progress indicator — or a “spinner” — use an instance of the [UIActivityIndicatorView](uiactivityindicatorview.md) class.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a progress view

- [- initWithProgressViewStyle:](<uiprogressview/init(progressviewstyle_).md>) — Creates a progress view with the specified style.
- [- initWithFrame:](<uiprogressview/init(frame_).md>) — Creates a progress view with the specified frame rectangle.
- [- initWithCoder:](<uiprogressview/init(coder_).md>) — Creates a progress view from data in an unarchiver.

### Managing the progress bar

- [progress](uiprogressview/progress.md) — The current progress of the progress view.
- [- setProgress:animated:](<uiprogressview/setprogress(__animated_).md>) — Adjusts the current progress of the progress view, optionally animating the change.
- [observedProgress](uiprogressview/observedprogress.md) — The progress object to use for updating the progress view.

### Configuring the progress bar

- [progressViewStyle](uiprogressview/progressviewstyle.md) — The current graphical style of the progress view.
- [progressTintColor](uiprogressview/progresstintcolor.md) — The color shown for the portion of the progress bar that’s filled.
- [progressImage](uiprogressview/progressimage.md) — An image to use for the portion of the progress bar that’s filled.
- [trackTintColor](uiprogressview/tracktintcolor.md) — The color shown for the portion of the progress bar that isn’t filled.
- [trackImage](uiprogressview/trackimage.md) — An image to use for the portion of the track that isn’t filled.

### Constants

- [Style](uiprogressview/style.md) — The styles permitted for the progress bar.

## See Also

### Content views

- [UIActivityIndicatorView](uiactivityindicatorview.md) — A view that shows that a task is in progress.
- [UICalendarView](uicalendarview.md) — A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [UIContentUnavailableView](uicontentunavailableview.md) — A view that indicates there’s no content to display.
- [UIImageView](uiimageview.md) — A view that displays a single image or a sequence of animated images in your interface.
- [UIPickerView](uipickerview.md) — A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.
