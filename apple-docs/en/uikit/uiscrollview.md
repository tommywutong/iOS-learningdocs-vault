---
title: UIScrollView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview.json'
content_hash: 'sha256:b079e52e90cdcbb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScrollView

<sub>Class</sub>

A view that allows the scrolling and zooming of its contained views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIScrollView
```

## Overview

[UIScrollView](uiscrollview.md) is the superclass of several UIKit classes, including [UITableView](uitableview.md) and [UITextView](uitextview.md).

A scroll view is a view with an origin that’s adjustable over the content view. It clips the content to its frame, which generally (but not necessarily) coincides with that of the app’s main window. A scroll view tracks the movements of fingers, and adjusts the origin accordingly. The view that shows its content through the scroll view draws that portion of itself according to the new origin, which is pinned to an offset in the content view. The scroll view itself does no drawing except for displaying vertical and horizontal scroll indicators. The scroll view must know the size of the content view so it knows when to stop scrolling. By default, it _bounces_ back when scrolling exceeds the bounds of the content.

The object that manages the drawing of content that displays in a scroll view needs to tile the content’s subviews so that no view exceeds the size of the screen. As users scroll in the scroll view, this object adds and removes subviews as necessary.

Because a scroll view has no scroll bars, it must know whether a touch signals an intent to scroll versus an intent to track a subview in the content. To make this determination, it temporarily intercepts a touch-down event by starting a timer and, before the timer fires, seeing if the touching finger makes any movement. If the timer fires without a significant change in position, the scroll view sends tracking events to the touched subview of the content view. If the user then drags their finger far enough before the timer elapses, the scroll view cancels any tracking in the subview and performs the scrolling itself. Subclasses can override the [- touchesShouldBegin:withEvent:inContentView:](<uiscrollview/touchesshouldbegin(__with_in_).md>), [pagingEnabled](uiscrollview/ispagingenabled.md), and [- touchesShouldCancelInContentView:](<uiscrollview/touchesshouldcancel(in_).md>) methods (which the scroll view calls) to affect how the scroll view handles scrolling gestures.

A scroll view also handles zooming and panning of content. As the user makes a pinch-in or pinch-out gesture, the scroll view adjusts the offset and the scale of the content. When the gesture ends, the object managing the content view updates subviews of the content as necessary. (Note that the gesture can end and a finger might still be down.) While the gesture is in progress, the scroll view doesn’t send any tracking calls to the subview.

The [UIScrollView](uiscrollview.md) class can have a delegate that must adopt the [UIScrollViewDelegate](uiscrollviewdelegate.md) protocol. For zooming and panning to work, the delegate must implement both [- viewForZoomingInScrollView:](<uiscrollviewdelegate/viewforzooming(in_).md>) and [- scrollViewDidEndZooming:withView:atScale:](<uiscrollviewdelegate/scrollviewdidendzooming(__with_atscale_).md>). In addition, the [maximumZoomScale](uiscrollview/maximumzoomscale.md) and [minimumZoomScale](uiscrollview/minimumzoomscale.md) zoom scales must be different.

### State preservation

If you assign a value to this view’s [restorationIdentifier](uiviewcontroller/restorationidentifier.md) property, it attempts to preserve its scrolling-related information between app launches. Specifically, the values of the [zoomScale](uiscrollview/zoomscale.md), [contentInset](uiscrollview/contentinset.md), and [contentOffset](uiscrollview/contentoffset.md) properties are preserved. During restoration, the scroll view restores these values so that the content appears scrolled to the same position as before. For more information about how state preservation and restoration works, see [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Inherited By**: [UICollectionView](uicollectionview.md), [UITableView](uitableview.md), [UITextView](uitextview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Responding to scroll view interactions

- [delegate](uiscrollview/delegate.md) — The delegate of the scroll view.
- [UIScrollViewDelegate](uiscrollviewdelegate.md) — The interface for the delegate of a scroll view.

### Managing the content size and offset

- [contentSize](uiscrollview/contentsize.md) — The size of the content view.
- [contentOffset](uiscrollview/contentoffset.md) — The point at which the origin of the content view is offset from the origin of the scroll view.
- [- setContentOffset:animated:](<uiscrollview/setcontentoffset(__animated_).md>) — Sets the offset from the content view’s origin that corresponds to the scroll view’s origin.

### Managing the content inset behavior

- [adjustedContentInset](uiscrollview/adjustedcontentinset.md) — The insets derived from the content insets and the safe area of the scroll view.
- [contentInset](uiscrollview/contentinset.md) — The custom distance that the content view is inset from the safe area or scroll view edges.
- [contentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.property.md) — The behavior for determining the adjusted content offsets.
- [ContentInsetAdjustmentBehavior](uiscrollview/contentinsetadjustmentbehavior-swift.enum.md) — Constants indicating how safe area insets are added to the adjusted content inset.
- [- adjustedContentInsetDidChange](<uiscrollview/adjustedcontentinsetdidchange().md>) — Notifies the scroll view when the adjusted content insets of the scroll view change.

### Getting the layout guides

- [frameLayoutGuide](uiscrollview/framelayoutguide.md) — The layout guide based on the untransformed frame rectangle of the scroll view.
- [contentLayoutGuide](uiscrollview/contentlayoutguide.md) — The layout guide based on the untranslated content rectangle of the scroll view.

### Configuring the scroll view

- [scrollEnabled](uiscrollview/isscrollenabled.md) — A Boolean value that determines whether scrolling is enabled.
- [directionalLockEnabled](uiscrollview/isdirectionallockenabled.md) — A Boolean value that determines whether scrolling is disabled in a particular direction.
- [pagingEnabled](uiscrollview/ispagingenabled.md) — A Boolean value that determines whether paging is enabled for the scroll view.
- [scrollsToTop](uiscrollview/scrollstotop.md) — A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [bounces](uiscrollview/bounces.md) — A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [bouncesHorizontally](uiscrollview/bounceshorizontally.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [bouncesVertically](uiscrollview/bouncesvertically.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [alwaysBounceVertical](uiscrollview/alwaysbouncevertical.md) — A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [alwaysBounceHorizontal](uiscrollview/alwaysbouncehorizontal.md) — A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.

### Managing the scrolling state

- [tracking](uiscrollview/istracking.md) — A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [dragging](uiscrollview/isdragging.md) — A Boolean value that indicates whether the user has begun scrolling the content.
- [decelerating](uiscrollview/isdecelerating.md) — A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [scrollAnimating](uiscrollview/isscrollanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [- stopScrollingAndZooming](<uiscrollview/stopscrollingandzooming().md>) — Stops active scroll and zoom animations.
- [decelerationRate](uiscrollview/decelerationrate-swift.property.md) — A floating-point value that determines the rate of deceleration after the user lifts their finger.
- [DecelerationRate](uiscrollview/decelerationrate-swift.struct.md) — Deceleration rates for the scroll view.

### Applying edge effects

- [bottomEdgeEffect](uiscrollview/bottomedgeeffect.md) — The effect for the bottom edge of the scroll view.
- [leftEdgeEffect](uiscrollview/leftedgeeffect.md) — The effect for the left edge of the scroll view.
- [rightEdgeEffect](uiscrollview/rightedgeeffect.md) — The effect for the right edge of the scroll view.
- [topEdgeEffect](uiscrollview/topedgeeffect.md) — The effect for the top edge of the scroll view.
- [UIScrollEdgeEffect](uiscrolledgeeffect.md) — Properties of the effect on a particular edge of the scroll view.
- [Style](uiscrolledgeeffect/style-swift.class.md) — Styles for a scroll view’s edge effect.

### Managing the scroll indicator and refresh control

- [indicatorStyle](uiscrollview/indicatorstyle-swift.property.md) — The style of the scroll indicators.
- [IndicatorStyle](uiscrollview/indicatorstyle-swift.enum.md) — Defines constants that represent the styles of the scroll indicators.
- [showsHorizontalScrollIndicator](uiscrollview/showshorizontalscrollindicator.md) — A Boolean value that controls whether the horizontal scroll indicator is visible.
- [showsVerticalScrollIndicator](uiscrollview/showsverticalscrollindicator.md) — A Boolean value that controls whether the vertical scroll indicator is visible.
- [horizontalScrollIndicatorInsets](uiscrollview/horizontalscrollindicatorinsets.md) — The horizontal distance the scroll indicators are inset from the edge of the scroll view.
- [verticalScrollIndicatorInsets](uiscrollview/verticalscrollindicatorinsets.md) — The vertical distance the scroll indicators are inset from the edge of the scroll view.
- [automaticallyAdjustsScrollIndicatorInsets](uiscrollview/automaticallyadjustsscrollindicatorinsets.md) — A Boolean value that indicates whether the system automatically adjusts the scroll indicator insets.
- [- flashScrollIndicators](<uiscrollview/flashscrollindicators().md>) — Displays the scroll indicators momentarily.
- [- withScrollIndicatorsShownForContentOffsetChanges:](<uiscrollview/withscrollindicatorsshown(forcontentoffsetchanges_).md>) — Displays the scroll indicators during updates to the scroll view’s content offset.
- [refreshControl](uiscrollview/refreshcontrol.md) — The refresh control associated with the scroll view.
- [UIRefreshControl](uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.

### Scrolling to a specific location

- [- scrollRectToVisible:animated:](<uiscrollview/scrollrecttovisible(__animated_).md>) — Scrolls a specific area of the content so that it’s visible in the scroll view.

### Managing touches

- [- touchesShouldBegin:withEvent:inContentView:](<uiscrollview/touchesshouldbegin(__with_in_).md>) — Overridden by subclasses to customize the default behavior when a finger touches down in displayed content.
- [- touchesShouldCancelInContentView:](<uiscrollview/touchesshouldcancel(in_).md>) — Returns whether to cancel touches related to the content subview and start dragging.
- [canCancelContentTouches](uiscrollview/cancancelcontenttouches.md) — A Boolean value that controls whether touches in the content view always lead to tracking.
- [delaysContentTouches](uiscrollview/delayscontenttouches.md) — A Boolean value that determines whether the scroll view delays the handling of touch-down gestures.
- [directionalPressGestureRecognizer](uiscrollview/directionalpressgesturerecognizer.md) — The underlying gesture recognizer for directional button presses.

### Zooming and panning

- [panGestureRecognizer](uiscrollview/pangesturerecognizer.md) — The underlying gesture recognizer for pan gestures.
- [pinchGestureRecognizer](uiscrollview/pinchgesturerecognizer.md) — The underlying gesture recognizer for pinch gestures.
- [- zoomToRect:animated:](<uiscrollview/zoom(to_animated_).md>) — Zooms to a specific area of the content so that it’s visible in the scroll view.
- [zoomScale](uiscrollview/zoomscale.md) — A floating-point value that specifies the current scale factor applied to the scroll view’s content.
- [- setZoomScale:animated:](<uiscrollview/setzoomscale(__animated_).md>) — A floating-point value that specifies the current zoom scale.
- [maximumZoomScale](uiscrollview/maximumzoomscale.md) — A floating-point value that specifies the maximum scale factor that can apply to the scroll view’s content.
- [minimumZoomScale](uiscrollview/minimumzoomscale.md) — A floating-point value that specifies the minimum scale factor that can apply to the scroll view’s content.
- [zoomBouncing](uiscrollview/iszoombouncing.md) — A Boolean value that indicates that zooming has exceeded the scaling limits specified for the scroll view.
- [zooming](uiscrollview/iszooming.md) — A Boolean value that indicates whether the content view is currently zooming in or out.
- [zoomAnimating](uiscrollview/iszoomanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a zoom update.
- [bouncesZoom](uiscrollview/bounceszoom.md) — A Boolean value that determines whether the scroll view animates the content scaling when the scaling exceeds the maximum or minimum limits.

### Dismissing the keyboard

- [keyboardDismissMode](uiscrollview/keyboarddismissmode-swift.property.md) — The manner in which the system dismisses the keyboard when a drag begins in the scroll view.
- [KeyboardDismissMode](uiscrollview/keyboarddismissmode-swift.enum.md) — Constants that determine how the system dismisses the keyboard when a drag begins in the scroll view.

### Managing the index

- [indexDisplayMode](uiscrollview/indexdisplaymode-swift.property.md) — The manner in which the index appears while the user is scrolling.
- [IndexDisplayMode](uiscrollview/indexdisplaymode-swift.enum.md) — Defines constants that represent how the index appears while the user is scrolling.

### Controlling content alignment

- [contentAlignmentPoint](uiscrollview/contentalignmentpoint.md) — A point where the scroll view anchors content that’s smaller than the scroll view’s frame.

### Nesting scroll views

- [transfersHorizontalScrollingToParent](uiscrollview/transfershorizontalscrollingtoparent.md) — A Boolean value that determines whether the scroll view passes horizontal scroll events to a superview.
- [transfersVerticalScrollingToParent](uiscrollview/transfersverticalscrollingtoparent.md) — A Boolean value that determines whether the scroll view passes vertical scroll events to a superview.

### Deprecated

- [scrollIndicatorInsets](uiscrollview/scrollindicatorinsets.md) — The distance the scroll indicators are inset from the edge of the scroll view. _(deprecated)_

### Instance Properties

- [allowsKeyboardScrolling](uiscrollview/allowskeyboardscrolling.md) — A Boolean value that determines whether the scroll view allows scrolling its content with hardware keyboard input.
- [lookToScrollAxes](uiscrollview/looktoscrollaxes.md) — Setting lookToScrollAxes turns on Look to Scroll for the scroll view in directions of the defined axis

## See Also

### Container views

- [Autosizing views for localization in iOS](../xcode/autosizing-views-for-localization-in-ios.md) — Add auto layout constraints to your app to achieve localizable views.
- [Collection views](collection-views.md) — Display nested views using a configurable and highly customizable layout.
- [Table views](table-views.md) — Display data in a single column of customizable rows.
- [UIStackView](uistackview.md) — A streamlined interface for laying out a collection of views in either a column or a row.
- [UILookToScrollInteraction](uilooktoscrollinteraction.md) _(beta)_
