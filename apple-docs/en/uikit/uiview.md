---
title: UIView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview
source_url: 'https://developer.apple.com/documentation/uikit/uiview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview.json'
content_hash: 'sha256:5f2d776db20d6745'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIView

<sub>Class</sub>

An object that manages the content for a rectangular area on the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIView
```

## Overview

Views are the fundamental building blocks of your app’s user interface, and the [UIView](uiview.md) class defines the behaviors that are common to all views. A view object renders content within its bounds rectangle, and handles any interactions with that content. The [UIView](uiview.md) class is a concrete class that you can instantiate and use to display a fixed background color. You can also subclass it to draw more sophisticated content. To display labels, images, buttons, and other interface elements commonly found in apps, use the view subclasses that the UIKit framework provides rather than trying to define your own.

Because view objects are the main way your application interacts with the user, they have a number of responsibilities. Here are just a few:

- Drawing and animation

    - Views draw content in their rectangular area using UIKit or Core Graphics.
    - You can animate some view properties to new values.
- Layout and subview management

    - Views may contain zero or more subviews.
    - Views can adjust the size and position of their subviews.
    - Use Auto Layout to define the rules for resizing and repositioning your views in response to changes in the view hierarchy.
- Event handling

    - A view is a subclass of [UIResponder](uiresponder.md) and can respond to touches and other types of events.
    - Views can install gesture recognizers to handle common gestures.

Views can nest inside other views to create view hierarchies, which offer a convenient way to organize related content. Nesting a view creates a parent-child relationship between the nested child view (known as the _subview_) and the parent (known as the _superview_). A parent view may contain any number of subviews, but each subview has only one superview. By default, when a subview’s visible area extends outside of the bounds of its superview, no clipping of the subview’s content occurs. Use the [clipsToBounds](uiview/clipstobounds.md) property to change that behavior.

The [frame](uiview/frame.md) and [bounds](uiview/bounds.md) properties define the geometry of each view. The [frame](uiview/frame.md) property defines the origin and dimensions of the view in the coordinate system of its superview. The [bounds](uiview/bounds.md) property defines the internal dimensions of the view as it sees them, and its use is almost exclusive to custom drawing code. The center property provides a convenient way to reposition a view without changing its [frame](uiview/frame.md) or [bounds](uiview/bounds.md) properties directly.

### Create a view

Normally, you create views in your storyboards by dragging them from the library to your canvas. You can also create views programmatically. When creating a view, you typically specify its initial size and position relative to its future superview. For example, the following example creates a view and places its top-left corner at the point (10, 10) in the superview’s coordinate system (once it is added to that superview).

**Swift**

```swift
let rect = CGRect(x: 10, y: 10, width: 100, height: 100)
let myView = UIView(frame: rect)
```

**Objective-C**

```objc
CGRect  viewRect = CGRectMake(10, 10, 100, 100);
UIView* myView = [[UIView alloc] initWithFrame:viewRect];
```

To add a subview to another view, call the [- addSubview:](<uiview/addsubview(__).md>) method on the superview. You may add any number of subviews to a view, and sibling views may overlap each other without any issues in iOS. Each call to the [- addSubview:](<uiview/addsubview(__).md>) method places the new view on top of all other siblings. You can specify the relative z-order of subview by adding it using the [- insertSubview:aboveSubview:](<uiview/insertsubview(__abovesubview_).md>) and [- insertSubview:belowSubview:](<uiview/insertsubview(__belowsubview_).md>) methods. You can also exchange the position of already added subviews using the [- exchangeSubviewAtIndex:withSubviewAtIndex:](<uiview/exchangesubview(at_withsubviewat_).md>) method.

After creating a view, create Auto Layout rules to govern how the size and position of the view change in response to changes in the rest of the view hierarchy.

### Draw views

View drawing occurs on an as-needed basis. When a view is first shown, or when all or part of it becomes visible due to layout changes, the system asks the view to draw its contents. For views that contain custom content using UIKit or Core Graphics, the system calls the view’s [- drawRect:](<uiview/draw(__).md>) method. Your implementation of this method is responsible for drawing the view’s content into the current graphics context, which is set up by the system automatically prior to calling this method. This creates a static visual representation of your view’s content that can then be displayed on the screen.

When the actual content of your view changes, it’s your responsibility to notify the system that your view needs to be redrawn. You do this by calling your view’s [- setNeedsDisplay](<uiview/setneedsdisplay().md>) or [- setNeedsDisplayInRect:](<uiview/setneedsdisplay(__).md>) method of the view. These methods let the system know that it should update the view during the next drawing cycle. Because it waits until the next drawing cycle to update the view, you can call these methods on multiple views to update them at the same time.

### Animate views

Changes to several view properties can be animated — that is, changing the property creates an animation starting at the current value and ending at the new value that you specify. The following properties of the [UIView](uiview.md) class are animatable:

- [frame](uiview/frame.md)
- [bounds](uiview/bounds.md)
- [center](uiview/center.md)
- [transform](uiview/transform.md)
- [alpha](uiview/alpha.md)
- [backgroundColor](uiview/backgroundcolor.md)

To animate your changes, create a [UIViewPropertyAnimator](uiviewpropertyanimator.md) object and use its handler block to change the values of your view’s properties. The [UIViewPropertyAnimator](uiviewpropertyanimator.md) class lets you specify the duration and timing of your animations, but it performs the actual animations. You can pause a property-based animator that’s currently running to interrupt the animation and drive it interactively. For more information, see [UIViewPropertyAnimator](uiviewpropertyanimator.md).

### Threading considerations

Manipulations to your app’s user interface must occur on the main thread. Thus, you should always call the methods of the [UIView](uiview.md) class from code running in the main thread of your app. The only time this may not be strictly necessary is when creating the view object itself, but all other manipulations should occur on the main thread.

### Subclassing notes

The [UIView](uiview.md) class is a key subclassing point for visual content that also requires user interactions. Although there are many good reasons to subclass [UIView](uiview.md), it is recommended that you do so only when the basic [UIView](uiview.md) class or the standard system views do not provide the capabilities that you need. Subclassing requires more work on your part to implement the view and to tune its performance.

For information about ways to avoid subclassing, see [Alternatives to subclassing](uiview.md#Alternatives-to-subclassing).

#### Methods to override

When subclassing [UIView](uiview.md), there are only a handful of methods you should override and many methods that you might override depending on your needs. Because [UIView](uiview.md) is a highly configurable class, there are also many ways to implement sophisticated view behaviors without overriding custom methods, which are discussed in the Alternatives to Subclassing section. In the meantime, the following list includes the methods you might consider overriding in your [UIView](uiview.md) subclasses:

- Initialization:

    - [- initWithFrame:](<uiview/init(frame_).md>) - It is recommended that you implement this method. You can also implement custom initialization methods in addition to, or instead of, this method.
    - [- initWithCoder:](<uiview/init(coder_).md>) - Implement this method if you load your view from storyboards or nib files and your view requires custom initialization.
    - [layerClass](uiview/layerclass.md) Use this property only if you want your view to use a different Core Animation layer for its backing store. For example, if your view uses tiling to display a large scrollable area, you might want to set the property to the [CATiledLayer](../quartzcore/catiledlayer.md) class.
- Drawing and printing:

    - [- drawRect:](<uiview/draw(__).md>) - Implement this method if your view draws custom content. If your view does not do any custom drawing, avoid overriding this method.
    - [- drawRect:forViewPrintFormatter:](<uiview/draw(__for_).md>) - Implement this method only if you want to draw your view’s content differently during printing.
- Layout and Constraints:

    - [requiresConstraintBasedLayout](uiview/requiresconstraintbasedlayout.md) Use this property if your view class requires constraints to work properly.
    - [- updateConstraints](<uiview/updateconstraints().md>) - Implement this method if your view needs to create custom constraints between your subviews.
    - [- alignmentRectForFrame:](<uiview/alignmentrect(forframe_).md>), [- frameForAlignmentRect:](<uiview/frame(foralignmentrect_).md>) - Implement these methods to override how your views are aligned to other views.
    - [- didAddSubview:](<uiview/didaddsubview(__).md>), [- willRemoveSubview:](<uiview/willremovesubview(__).md>) - Implement these methods as needed to track the additions and removals of subviews.
    - [- willMoveToSuperview:](<uiview/willmove(tosuperview_).md>), [- didMoveToSuperview](<uiview/didmovetosuperview().md>) - Implement these methods as needed to track the movement of the current view in your view hierarchy.
- Event Handling:

    - [- gestureRecognizerShouldBegin:](<uiview/gesturerecognizershouldbegin(__).md>) - Implement this method if your view handles touch events directly and might want to prevent attached gesture recognizers from triggering additional actions.
    - [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>), [- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>), [- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>), [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) - Implement these methods if you need to handle touch events directly. (For gesture-based input, use gesture recognizers.)

#### Alternatives to subclassing

Many view behaviors can be configured without the need for subclassing. Before you start overriding methods, consider whether modifying the following properties or behaviors would provide the behavior you need.

- [- addConstraint:](<uiview/addconstraint(__).md>) - Define automatic layout behavior for the view and its subviews.
- [autoresizingMask](uiview/autoresizingmask-swift.property.md) - Provides automatic layout behavior when the superview’s frame changes. These behaviors can be combined with constraints.
- [contentMode](uiview/contentmode-swift.property.md) - Provides layout behavior for the view’s content, as opposed to the [frame](uiview/frame.md) of the view. This property also affects how the content is scaled to fit the view and whether it is cached or redrawn.
- [hidden](uiview/ishidden.md) or [alpha](uiview/alpha.md) - Change the transparency of the view as a whole rather than hiding or applying alpha to your view’s rendered content.
- [backgroundColor](uiview/backgroundcolor.md) - Set the view’s color rather than drawing that color yourself.
- Subviews - Rather than draw your content using a [- drawRect:](<uiview/draw(__).md>) method, embed image and label subviews with the content you want to present.
- Gesture recognizers - Rather than subclass to intercept and handle touch events yourself, you can use gesture recognizers to send an action to a target object.
- Animations - Use the built-in animation support rather than trying to animate changes yourself. The animation support provided by Core Animation is fast and easy to use.
- Image-based backgrounds - For views that display relatively static content, consider using a [UIImageView](uiimageview.md) object with gesture recognizers instead of subclassing and drawing the image yourself. Alternatively, you can also use a generic [UIView](uiview.md) object and assign your image as the content of the view’s [CALayer](../quartzcore/calayer.md) object.

Animations are another way to make visible changes to a view without requiring you to subclass and implement complex drawing code. Many properties of the [UIView](uiview.md) class are animatable, which means changes to those properties can trigger system-generated animations. Starting animations requires as little as one line of code to indicate that any changes that follow should be animated. For more information about animation support for views, see [Animate views](uiview.md#Animate-views).

### Sensor coordinate orientation

`UIView` conforms to [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md) and [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), informing Core Location and Core Motion how the app’s UI and this view are situated with respect to reference physical orientations. They use this information to transform the sensor values they provide, such as compass headings and device motion data, so those values align with your UI’s actual orientation. Without this association, Core Location and Core Motion report sensor values relative to the device’s physical orientation, which can produce unexpected results, such as a navigation map that appears rotated.

To use this approach, set any view as the body on a `CLLocationManager` or `CMMotionManager` instance. The system tracks orientation changes through the view and applies the correct transformation automatically.

```swift
let motionManager = CMMotionManager()

override func viewDidLoad() {
    super.viewDidLoad()
    motionManager.deviceMotionBody = view
}
```

## Relationships

- **Inherits From**: [UIResponder](uiresponder.md)

- **Inherited By**: [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIAlertView](uialertview.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UICalendarView](uicalendarview.md), [UICollectionReusableView](uicollectionreusableview.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIEventAttributionView](uieventattributionview.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UITabBar](uitabbar.md), [UITableViewCell](uitableviewcell.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UIToolbar](uitoolbar.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md)

- **Conforms To**: [AppEntityAnnotatable](../appintents/appentityannotatable.md), [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a view object

- [- initWithFrame:](<uiview/init(frame_).md>) — Creates a view with the specified frame rectangle.
- [- initWithCoder:](<uiview/init(coder_).md>) — Creates a view from data in an unarchiver.

### Configuring a view’s visual appearance

- [backgroundColor](uiview/backgroundcolor.md) — The view’s background color.
- [hidden](uiview/ishidden.md) — A Boolean value that determines whether the view is hidden.
- [alpha](uiview/alpha.md) — The view’s alpha value.
- [opaque](uiview/isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintColor](uiview/tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](uiview/tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](uiview/clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [clearsContextBeforeDrawing](uiview/clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [maskView](uiview/mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](uiview/layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](uiview/layer.md) — The view’s Core Animation layer to use for rendering.

### Configuring a view’s corners

- [cornerConfiguration](uiview/cornerconfiguration-7l0ja.md) — A configuration that defines the corners of the view.
- [UICornerConfiguration](uicornerconfiguration-swift.struct.md) — A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [UICornerRadius](uicornerradius-swift.struct.md) — A type that represents the radius the system uses to round a corner.
- [- effectiveRadiusForCorner:](<uiview/effectiveradius(corner_).md>) — Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.

### Configuring the event-related behavior

- [userInteractionEnabled](uiview/isuserinteractionenabled.md) — A Boolean value that determines whether user events are ignored and removed from the event queue.
- [multipleTouchEnabled](uiview/ismultipletouchenabled.md) — A Boolean value that indicates whether the view receives more than one touch at a time.
- [exclusiveTouch](uiview/isexclusivetouch.md) — A Boolean value that indicates whether the receiver handles touch events exclusively.

### Configuring the bounds and frame rectangles

- [frame](uiview/frame.md) — The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [bounds](uiview/bounds.md) — The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [center](uiview/center.md) — The center point of the view’s frame rectangle.
- [transform](uiview/transform.md) — Specifies the transform applied to the view, relative to the center of its bounds.
- [transform3D](uiview/transform3d.md) — The three-dimensional transform to apply to the view.
- [anchorPoint](uiview/anchorpoint.md) — The anchor point of the view’s bounds rectangle.

### Managing the view hierarchy

- [superview](uiview/superview.md) — The receiver’s superview, or `nil` if it has none.
- [subviews](uiview/subviews.md) — The receiver’s immediate subviews.
- [window](uiview/window.md) — The receiver’s window object, or `nil` if it has none.
- [- addSubview:](<uiview/addsubview(__).md>) — Adds a view to the end of the receiver’s list of subviews.
- [- bringSubviewToFront:](<uiview/bringsubviewtofront(__).md>) — Moves the specified subview so that it appears on top of its siblings.
- [- sendSubviewToBack:](<uiview/sendsubviewtoback(__).md>) — Moves the specified subview so that it appears behind its siblings.
- [- removeFromSuperview](<uiview/removefromsuperview().md>) — Unlinks the view from its superview and its window, and removes it from the responder chain.
- [- insertSubview:atIndex:](<uiview/insertsubview(__at_).md>) — Inserts a subview at the specified index.
- [- insertSubview:aboveSubview:](<uiview/insertsubview(__abovesubview_).md>) — Inserts a view above another view in the view hierarchy.
- [- insertSubview:belowSubview:](<uiview/insertsubview(__belowsubview_).md>) — Inserts a view below another view in the view hierarchy.
- [- exchangeSubviewAtIndex:withSubviewAtIndex:](<uiview/exchangesubview(at_withsubviewat_).md>) — Exchanges the subviews at the specified indices.
- [- isDescendantOfView:](<uiview/isdescendant(of_).md>) — Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.

### Observing view-related changes

- [- didAddSubview:](<uiview/didaddsubview(__).md>) — Tells the view that a subview was added.
- [- willRemoveSubview:](<uiview/willremovesubview(__).md>) — Tells the view that a subview is about to be removed.
- [- willMoveToSuperview:](<uiview/willmove(tosuperview_).md>) — Tells the view that its superview is about to change to the specified superview.
- [- didMoveToSuperview](<uiview/didmovetosuperview().md>) — Tells the view that its superview changed.
- [- willMoveToWindow:](<uiview/willmove(towindow_).md>) — Tells the view that its window object is about to change.
- [- didMoveToWindow](<uiview/didmovetowindow().md>) — Tells the view that its window object changed.

### Observing trait changes

- [UITraitChangeObservable](uitraitchangeobservable-67e94.md) — A type that calls your code in reaction to changes in the trait environment.

### Requesting trait updates

- [- updateTraitsIfNeeded](<uiview/updatetraitsifneeded().md>) — Forces an immediate trait update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree. Any trait change callbacks are sent synchronously.

### Overriding trait values

- [traitOverrides](uiview/traitoverrides-fd9z.md)
- [UITraitOverrides](uitraitoverrides-swift.struct.md) — A mutable container of traits you use to set trait changes for an object and its descendants.

### Configuring content margins

- [Positioning content within layout margins](positioning-content-within-layout-margins.md) — Position views so that they aren’t crowded by other content.
- [directionalLayoutMargins](uiview/directionallayoutmargins.md) — The default spacing to use when laying out content in a view, taking into account the current language direction.
- [layoutMargins](uiview/layoutmargins.md) — The default spacing to use when laying out content in the view.
- [preservesSuperviewLayoutMargins](uiview/preservessuperviewlayoutmargins.md) — A Boolean value indicating whether the current view also respects the margins of its superview.
- [- layoutMarginsDidChange](<uiview/layoutmarginsdidchange().md>) — Notifies the view that the layout margins changed.

### Getting the safe area

- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [safeAreaInsets](uiview/safeareainsets.md) — The insets that you use to determine the safe area for this view.
- [safeAreaLayoutGuide](uiview/safearealayoutguide.md) — The layout guide representing the portion of your view that is unobscured by bars and other content.
- [- safeAreaInsetsDidChange](<uiview/safeareainsetsdidchange().md>) — Called when the safe area of the view changes.
- [insetsLayoutMarginsFromSafeArea](uiview/insetslayoutmarginsfromsafearea.md) — A Boolean value indicating whether the view’s layout margins are updated automatically to reflect the safe area.

### Managing the view’s constraints

- [constraints](uiview/constraints.md) — The constraints held by the view.
- [- addConstraint:](<uiview/addconstraint(__).md>) — Adds a constraint on the layout of the receiving view or its subviews.
- [- addConstraints:](<uiview/addconstraints(__).md>) — Adds multiple constraints on the layout of the receiving view or its subviews.
- [- removeConstraint:](<uiview/removeconstraint(__).md>) — Removes the specified constraint from the view.
- [- removeConstraints:](<uiview/removeconstraints(__).md>) — Removes the specified constraints from the view.

### Creating constraints using layout anchors

- [bottomAnchor](uiview/bottomanchor.md) — A layout anchor representing the bottom edge of the view’s frame.
- [centerXAnchor](uiview/centerxanchor.md) — A layout anchor representing the horizontal center of the view’s frame.
- [centerYAnchor](uiview/centeryanchor.md) — A layout anchor representing the vertical center of the view’s frame.
- [firstBaselineAnchor](uiview/firstbaselineanchor.md) — A layout anchor representing the baseline for the topmost line of text in the view.
- [heightAnchor](uiview/heightanchor.md) — A layout anchor representing the height of the view’s frame.
- [lastBaselineAnchor](uiview/lastbaselineanchor.md) — A layout anchor representing the baseline for the bottommost line of text in the view.
- [leadingAnchor](uiview/leadinganchor.md) — A layout anchor representing the leading edge of the view’s frame.
- [leftAnchor](uiview/leftanchor.md) — A layout anchor representing the left edge of the view’s frame.
- [rightAnchor](uiview/rightanchor.md) — A layout anchor representing the right edge of the view’s frame.
- [topAnchor](uiview/topanchor.md) — A layout anchor representing the top edge of the view’s frame.
- [trailingAnchor](uiview/trailinganchor.md) — A layout anchor representing the trailing edge of the view’s frame.
- [widthAnchor](uiview/widthanchor.md) — A layout anchor representing the width of the view’s frame.

### Working with layout guides

- [- addLayoutGuide:](<uiview/addlayoutguide(__).md>) — Adds the specified layout guide to the view.
- [layoutGuides](uiview/layoutguides.md) — The array of layout guide objects owned by this view.
- [layoutMarginsGuide](uiview/layoutmarginsguide.md) — A layout guide representing the view’s margins.
- [readableContentGuide](uiview/readablecontentguide.md) — A layout guide representing an area with a readable width within the view.
- [- removeLayoutGuide:](<uiview/removelayoutguide(__).md>) — Removes the specified layout guide from the view.

### Measuring in Auto Layout

- [- systemLayoutSizeFittingSize:](<uiview/systemlayoutsizefitting(__).md>) — Returns the optimal size of the view based on its current constraints.
- [- systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:](<uiview/systemlayoutsizefitting(__withhorizontalfittingpriority_verticalfittingpriority_).md>) — Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [intrinsicContentSize](uiview/intrinsiccontentsize.md) — The natural size for the receiving view, considering only properties of the view itself.
- [- invalidateIntrinsicContentSize](<uiview/invalidateintrinsiccontentsize().md>) — Invalidates the view’s intrinsic content size.
- [- contentCompressionResistancePriorityForAxis:](<uiview/contentcompressionresistancepriority(for_).md>) — Returns the priority with which a view resists being made smaller than its intrinsic size.
- [- setContentCompressionResistancePriority:forAxis:](<uiview/setcontentcompressionresistancepriority(__for_).md>) — Sets the priority with which a view resists being made smaller than its intrinsic size.
- [- contentHuggingPriorityForAxis:](<uiview/contenthuggingpriority(for_).md>) — Returns the priority with which a view resists being made larger than its intrinsic size.
- [- setContentHuggingPriority:forAxis:](<uiview/setcontenthuggingpriority(__for_).md>) — Sets the priority with which a view resists being made larger than its intrinsic size.

### Aligning views in Auto Layout

- [- alignmentRectForFrame:](<uiview/alignmentrect(forframe_).md>) — Returns the view’s alignment rectangle for a given frame.
- [- frameForAlignmentRect:](<uiview/frame(foralignmentrect_).md>) — Returns the view’s frame for a given alignment rectangle.
- [alignmentRectInsets](uiview/alignmentrectinsets.md) — The insets from the view’s frame that define its alignment rectangle.
- [viewForFirstBaselineLayout](uiview/forfirstbaselinelayout.md) — Returns a view used to satisfy first baseline constraints.
- [viewForLastBaselineLayout](uiview/forlastbaselinelayout.md) — Returns a view used to satisfy last baseline constraints.

### Triggering Auto Layout

- [- needsUpdateConstraints](<uiview/needsupdateconstraints().md>) — A Boolean value that determines whether the view’s constraints need updating.
- [- setNeedsUpdateConstraints](<uiview/setneedsupdateconstraints().md>) — Controls whether the view’s constraints need updating.
- [- updateConstraints](<uiview/updateconstraints().md>) — Updates constraints for the view.
- [- updateConstraintsIfNeeded](<uiview/updateconstraintsifneeded().md>) — Updates the constraints for the receiving view and its subviews.

### Debugging Auto Layout

- [- constraintsAffectingLayoutForAxis:](<uiview/constraintsaffectinglayout(for_).md>) — Returns the constraints impacting the layout of the view for a given axis.
- [hasAmbiguousLayout](uiview/hasambiguouslayout.md) — A Boolean value that determines whether the constraints impacting the layout of the view incompletely specify the location of the view.
- [- exerciseAmbiguityInLayout](<uiview/exerciseambiguityinlayout().md>) — Randomly changes the frame of a view with an ambiguous layout between the different valid values.

### Configuring the resizing behavior

- [contentMode](uiview/contentmode-swift.property.md) — A flag used to determine how a view lays out its content when its bounds change.
- [ContentMode](uiview/contentmode-swift.enum.md) — Options to specify how a view adjusts its content when its size changes.
- [- sizeThatFits:](<uiview/sizethatfits(__).md>) — Asks the view to calculate and return the size that best fits the specified size.
- [- sizeToFit](<uiview/sizetofit().md>) — Resizes and moves the receiver view so it just encloses its subviews.
- [autoresizesSubviews](uiview/autoresizessubviews.md) — A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [autoresizingMask](uiview/autoresizingmask-swift.property.md) — An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.

### Laying out subviews

- [- layoutSubviews](<uiview/layoutsubviews().md>) — Lays out subviews.
- [- setNeedsLayout](<uiview/setneedslayout().md>) — Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [- layoutIfNeeded](<uiview/layoutifneeded().md>) — Lays out the subviews immediately, if layout updates are pending.
- [requiresConstraintBasedLayout](uiview/requiresconstraintbasedlayout.md) — A Boolean value that indicates whether the receiver depends on the constraint-based layout system.
- [translatesAutoresizingMaskIntoConstraints](uiview/translatesautoresizingmaskintoconstraints.md) — A Boolean value that determines whether the view’s autoresizing mask converts to Auto Layout constraints.

### Accessing insets and layout guides

- [LayoutRegion](uiview/layoutregion.md)
- [directionalEdgeInsets(for:)](<uiview/directionaledgeinsets(for_).md>)
- [edgeInsets(for:)](<uiview/edgeinsets(for_).md>)
- [layoutGuide(for:)](<uiview/layoutguide(for_).md>)

### Adjusting the user interface

- [overrideUserInterfaceStyle](uiview/overrideuserinterfacestyle.md) — The user interface style adopted by the view and all of its subviews.
- [semanticContentAttribute](uiview/semanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [effectiveUserInterfaceLayoutDirection](uiview/effectiveuserinterfacelayoutdirection.md) — The user interface layout direction appropriate for arranging the immediate content of the view.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:](<uiview/userinterfacelayoutdirection(for_).md>) — Returns the user interface direction for the given semantic content attribute.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:relativeToLayoutDirection:](<uiview/userinterfacelayoutdirection(for_relativeto_).md>) — Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.

### Constraining views to the keyboard

- [keyboardLayoutGuide](uiview/keyboardlayoutguide.md) — A layout guide that tracks the keyboard’s position in your app’s layout.

### Adding and removing interactions

- [- addInteraction:](<uiview/addinteraction(__).md>) — Adds an interaction to the view.
- [- removeInteraction:](<uiview/removeinteraction(__).md>) — Removes an interaction from the view.
- [interactions](uiview/interactions.md) — The array of interactions for the view.
- [UIInteraction](uiinteraction.md) — The protocol that an interaction implements to access the view that owns it.

### Drawing and updating the view

- [- drawRect:](<uiview/draw(__).md>) — Draws the view’s image within the passed-in rectangle.
- [- setNeedsDisplay](<uiview/setneedsdisplay().md>) — Marks the receiver’s entire bounds rectangle as needing to be redrawn.
- [- setNeedsDisplayInRect:](<uiview/setneedsdisplay(__).md>) — Marks the specified rectangle of the receiver as needing to be redrawn.
- [contentScaleFactor](uiview/contentscalefactor.md) — The scale factor applied to the view.
- [- tintColorDidChange](<uiview/tintcolordidchange().md>) — Called by the system when the tint color property changes.

### Updating the view when property values change

- [Invalidating](uiview/invalidating.md) — A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.
- [UIViewInvalidating](uiviewinvalidating.md) — Implements a type of invalidation that can occur on a view that requires an update.

### Formatting printed view content

- [- viewPrintFormatter](<uiview/viewprintformatter().md>) — Returns a print formatter for the receiving view.
- [- drawRect:forViewPrintFormatter:](<uiview/draw(__for_).md>) — Implemented to draw the view’s content for printing.

### Managing gesture recognizers

- [- addGestureRecognizer:](<uiview/addgesturerecognizer(__).md>) — Attaches a gesture recognizer to the view.
- [- removeGestureRecognizer:](<uiview/removegesturerecognizer(__).md>) — Detaches a gesture recognizer from the receiving view.
- [gestureRecognizers](uiview/gesturerecognizers.md) — The gesture-recognizer objects currently attached to the view.
- [- gestureRecognizerShouldBegin:](<uiview/gesturerecognizershouldbegin(__).md>) — Asks the view if the gesture recognizer should continue tracking touch events.

### Working with focus

- [canBecomeFocused](uiview/canbecomefocused.md) — A Boolean value that indicates whether the view is currently capable of being focused.
- [inheritedAnimationDuration](uiview/inheritedanimationduration.md) — Returns the inherited duration of the current animation.
- [focused](uiview/isfocused.md) — A Boolean value that indicates whether the item is currently focused.
- [focusGroupIdentifier](uiview/focusgroupidentifier.md) — The identifier of the focus group that this view belongs to.
- [focusEffect](uiview/focuseffect.md) — The visual effect to apply when the view becomes focused.
- [focusGroupPriority](uiview/focusgrouppriority.md) — The importance of the item within a focus group, used by the focus system to determine the group’s primary item.

### Using motion effects

- [- addMotionEffect:](<uiview/addmotioneffect(__).md>) — Begins applying a motion effect to the view.
- [motionEffects](uiview/motioneffects.md) — The array of motion effects for the view.
- [- removeMotionEffect:](<uiview/removemotioneffect(__).md>) — Stops applying a motion effect to the view.

### Managing the hover appearance

- [hoverStyle](uiview/hoverstyle.md) — The hover style for the view.
- [UIHoverStyle](uihoverstyle.md) — The hover style to apply to a view, including an effect and a shape to use for displaying that effect.
- [UIHoverEffectLayer](uihovereffectlayer.md) — A layer type that can be used to apply a hover effect to its sublayers.

### Managing font-sizing preferences

- [minimumContentSizeCategory](uiview/minimumcontentsizecategory.md) — The minimum content size category for the view and its subviews.
- [maximumContentSizeCategory](uiview/maximumcontentsizecategory.md) — The maximum content size category for the view and its subviews.
- [appliedContentSizeCategoryLimitsDescription](uiview/appliedcontentsizecategorylimitsdescription.md) — A string that lists each of the view’s superviews, its content size category, and whether that view has content size category limits.

### Preserving and restoring state

- [restorationIdentifier](uiview/restorationidentifier.md) — The identifier that determines whether the view supports state restoration.
- [- encodeRestorableStateWithCoder:](<uiview/encoderestorablestate(with_).md>) — Encodes state-related information for the view.
- [- decodeRestorableStateWithCoder:](<uiview/decoderestorablestate(with_).md>) — Decodes and restores state-related information for the view.

### Capturing a view snapshot

- [- snapshotViewAfterScreenUpdates:](<uiview/snapshotview(afterscreenupdates_).md>) — Returns a snapshot view based on the contents of the current view.
- [- resizableSnapshotViewFromRect:afterScreenUpdates:withCapInsets:](<uiview/resizablesnapshotview(from_afterscreenupdates_withcapinsets_).md>) — Returns a snapshot view based on the specified contents of the current view, with stretchable insets.
- [- drawViewHierarchyInRect:afterScreenUpdates:](<uiview/drawhierarchy(in_afterscreenupdates_).md>) — Renders a snapshot of the complete view hierarchy as visible onscreen into the current context.

### Identifying the view at runtime

- [tag](uiview/tag.md) — An integer that you can use to identify view objects in your application.
- [- viewWithTag:](<uiview/viewwithtag(__).md>) — Returns the view whose tag matches the specified value.

### Converting between view coordinate systems

- [- convertPoint:toView:](<uiview/convert(__to_)-1xizt.md>) — Converts a point from the receiver’s coordinate system to that of the specified view.
- [- convertPoint:fromView:](<uiview/convert(__from_)-8neo1.md>) — Converts a point from the coordinate system of a given view to that of the receiver.
- [- convertRect:toView:](<uiview/convert(__to_)-2kf3d.md>) — Converts a rectangle from the receiver’s coordinate system to that of another view.
- [- convertRect:fromView:](<uiview/convert(__from_)-7irzk.md>) — Converts a rectangle from the coordinate system of another view to that of the receiver.

### Hit-testing in a view

- [- hitTest:withEvent:](<uiview/hittest(__with_).md>) — Returns the farthest descendant in the view hierarchy of the current view, including itself, that contains the specified point.
- [- pointInside:withEvent:](<uiview/point(inside_with_).md>) — Returns a Boolean value indicating whether the receiver contains the specified point.

### Ending a view-editing session

- [- endEditing:](<uiview/endediting(__).md>) — Causes the view (or one of its embedded text fields) to resign the first responder status.

### Modifying the accessibility behavior

- [accessibilityIgnoresInvertColors](uiview/accessibilityignoresinvertcolors.md) — A Boolean value indicating whether the view ignores an accessibility request to invert its colors.
- [largeContentImage](uiview/largecontentimage.md) — An image that represents the view in the large content viewer.
- [largeContentImageInsets](uiview/largecontentimageinsets.md) — Insets to adjust the position of the view’s image so it appears centered in the large content viewer.
- [largeContentTitle](uiview/largecontenttitle.md) — A string that describes the view in the large content viewer.
- [scalesLargeContentImage](uiview/scaleslargecontentimage.md) — A Boolean value that indicates whether the large content viewer scales the item’s image to a larger size.
- [showsLargeContentViewer](uiview/showslargecontentviewer.md) — A Boolean value that indicates whether to show the view in the large content viewer.

### Animating views

- [animate(_:changes:completion:)](<uiview/animate(__changes_completion_).md>)
- [animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)](<uiview/animate(springduration_bounce_initialspringvelocity_delay_options_animations_completion_).md>) — Animates changes to one or more views using a spring animation with the specified duration, bounce, initial velocity, delay, options, and completion handler.
- [+ animateWithDuration:delay:options:animations:completion:](<uiview/animate(withduration_delay_options_animations_completion_).md>) — Animate changes to one or more views using the specified duration, delay, options, and completion handler.
- [+ animateWithDuration:animations:completion:](<uiview/animate(withduration_animations_completion_).md>) — Animate changes to one or more views using the specified duration and completion handler.
- [+ animateWithDuration:animations:](<uiview/animate(withduration_animations_).md>) — Animate changes to one or more views using the specified duration.
- [+ transitionWithView:duration:options:animations:completion:](<uiview/transition(with_duration_options_animations_completion_).md>) — Creates a transition animation for the specified container view.
- [+ transitionFromView:toView:duration:options:completion:](<uiview/transition(from_to_duration_options_completion_).md>) — Creates a transition animation between the specified views using the given parameters.
- [+ animateKeyframesWithDuration:delay:options:animations:completion:](<uiview/animatekeyframes(withduration_delay_options_animations_completion_).md>) — Creates an animation block object that can be used to set up keyframe-based animations for the current view.
- [+ addKeyframeWithRelativeStartTime:relativeDuration:animations:](<uiview/addkeyframe(withrelativestarttime_relativeduration_animations_).md>) — Specifies the timing and animation values for a single frame of a keyframe animation.
- [+ performSystemAnimation:onViews:options:animations:completion:](<uiview/perform(__on_options_animations_completion_).md>) — Performs a specified system-provided animation on one or more views, along with optional parallel animations that you define.
- [+ animateWithDuration:delay:usingSpringWithDamping:initialSpringVelocity:options:animations:completion:](<uiview/animate(withduration_delay_usingspringwithdamping_initialspringvelocity_options_animations_completion_).md>) — Performs a view animation using a timing curve corresponding to the motion of a physical spring.
- [+ performWithoutAnimation:](<uiview/performwithoutanimation(__).md>) — Disables a view transition animation.
- [+ modifyAnimationsWithRepeatCount:autoreverses:animations:](<uiview/modifyanimations(withrepeatcount_autoreverses_animations_).md>) — Repeats the specified animations a specific number of times, optionally running the animation forward and backward.

### Sensor coordinate orientation

- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md) _(beta)_
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md) _(beta)_

### Constants

- [AnimationCurve](uiview/animationcurve.md) — Specifies the supported animation curves.
- [AnimationOptions](uiview/animationoptions.md) — Options for animating views using block objects.
- [AnimationTransition](uiview/animationtransition.md) — Animation transition options for use in an animation block object.
- [SystemAnimation](uiview/systemanimation.md) — Option to remove the views from the hierarchy when animation is complete.
- [KeyframeAnimationOptions](uiview/keyframeanimationoptions.md) — Options for configuring keyframe-based animations.
- [Axis](nslayoutconstraint/axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [TintAdjustmentMode](uiview/tintadjustmentmode-swift.enum.md) — The tint adjustment mode for the view.
- [UILayoutFittingCompressedSize](uiview/layoutfittingcompressedsize.md) — The option to use the smallest possible size.
- [UILayoutFittingExpandedSize](uiview/layoutfittingexpandedsize.md) — The option to use the largest possible size.
- [UIViewNoIntrinsicMetric](uiview/nointrinsicmetric.md) — The absence of an intrinsic metric for a given numeric view property.
- [AutoresizingMask](uiview/autoresizingmask-swift.struct.md) — Options for automatic view resizing.
- [UISemanticContentAttribute](uisemanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.

### Deprecated

- [Deprecated symbols](uiview-deprecated-symbols.md) — Symbols that views no longer support.

### Initializers

- [- init](<uiview/init().md>)

### Instance Properties

- [appEntityUIElementProvider](uiview/appentityuielementprovider.md) — return AppEntityUIElement( identifier: EntityIdentifier( for: PhotoModel.self, identifier: photo.id ), bounds: photo.frame, state: State(isSelected: photo.isSelected) ) } } } }

### Instance Methods

- [- setNeedsUpdateProperties](<uiview/setneedsupdateproperties().md>) — Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [- updateProperties](<uiview/updateproperties().md>) — Configures the view’s content and styling properties before layout.
- [- updatePropertiesIfNeeded](<uiview/updatepropertiesifneeded().md>) — Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.

### Enumerations

- [Invalidations](uiview/invalidations.md) — Changes that cause an aspect of a view to be invalid and require an update.

### Default Implementations

- [AppEntityAnnotatable Implementations](uiview/appentityannotatable-implementations.md)

## See Also

### View fundamentals

- [UIKit Catalog: Creating and customizing views and controls](uikit-catalog-creating-and-customizing-views-and-controls.md) — Customize your app’s user interface with views and controls.
