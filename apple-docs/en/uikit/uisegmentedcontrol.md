---
title: UISegmentedControl
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisegmentedcontrol
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol.json'
content_hash: 'sha256:55add7d72e490a44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISegmentedControl

<sub>Class</sub>

A horizontal control that consists of multiple segments, each segment functioning as a discrete button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISegmentedControl
```

## Overview

A segmented control can display a title (an [NSString](../foundation/nsstring.md) object) or an image ([UIImage](uiimage.md) object). The [UISegmentedControl](uisegmentedcontrol.md) object automatically resizes segments to fit proportionally within their superview unless they have a specific width set. When you add and remove segments, you can request that the action be animated with sliding and fading effects.

You register the target-action methods for a segmented control using the [UIControlEventValueChanged](uicontrol/event/valuechanged.md) constant as shown below.

**Swift**

```swift
segmentedControl.addTarget(self, action: "action:", forControlEvents: .valueChanged)
```

**Objective-C**

```objc
[segmentedControl addTarget:self
                     action:@selector(action:)
           forControlEvents:UIControlEventValueChanged];
```

How you configure a segmented control can affect its display behavior:

- If you set a segmented control to have a momentary style, a segment doesn’t show itself as selected (blue background) when the user touches it. The disclosure button is always momentary and doesn’t affect the actual selection.
- In versions of iOS prior to 3.0, if a segmented control has only two segments, then it behaves like a switch — tapping the currently-selected segment causes the other segment to be selected. In iOS 3.0 and later, tapping the currently-selected segment doesn’t cause the other segment to be selected.

### Customize appearance

You can customize the appearance of segmented controls using the methods listed in [Customizing appearance](uisegmentedcontrol.md#Customizing-appearance). You can customize the appearance of all segmented controls using the appearance proxy (for example, `[UISegmentedControl appearance]`), or just of a single control.

When customizing appearance, in general, you should specify a value for the normal state of a property to be used by other states which don’t have a custom value set. Similarly, when a property is dependent on the bar metrics (on the iPhone in landscape orientation, bars have a different height from standard), you should make sure you specify a value for [UIBarMetricsDefault](uibarmetrics/default.md).

In the case of the segmented control, appearance properties for [UIBarMetricsLandscapePhone](uibarmetrics/landscapephone.md) are only respected for segmented controls in the smaller navigation and toolbars that are used in landscape orientation on the iPhone.

To provide complete customization, you need to provide divider images for different state combinations, using [- setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:](<uisegmentedcontrol/setdividerimage(__forleftsegmentstate_rightsegmentstate_barmetrics_).md>):

**Swift**

```swift
// Image between two unselected segments.
mySegmentedControl.setDividerImage(myImage, forLeftSegmentState: UIControlState.Normal,
                                   rightSegmentState: UIControlState.Normal, barMetrics: UIBarMetrics.Default)
 
// Image between segment selected on the left and unselected on the right.
mySegmentedControl.setDividerImage(myImage, forLeftSegmentState: UIControlState.Selected,
                                   rightSegmentState: UIControlState.Normal, barMetrics: UIBarMetrics.Default)
 
// Image between segment selected on the right and unselected on the left.
mySegmentedControl.setDividerImage(myImage, forLeftSegmentState: UIControlState.Normal,
                                   rightSegmentState: UIControlState.Selected, barMetrics: UIBarMetrics.Default)
```

**Objective-C**

```objc
// Image between two unselected segments.
[mySegmentedControl setDividerImage:image1 forLeftSegmentState:UIControlStateNormal
                  rightSegmentState:UIControlStateNormal barMetrics:barMetrics];
// Image between segment selected on the left and unselected on the right.
[mySegmentedControl setDividerImage:image1 forLeftSegmentState:UIControlStateSelected
                  rightSegmentState:UIControlStateNormal barMetrics:barMetrics];
// Image between segment selected on the right and unselected on the right.
[mySegmentedControl setDividerImage:image1 forLeftSegmentState:UIControlStateNormal
                  rightSegmentState:UIControlStateSelected barMetrics:barMetrics];
```

## Relationships

- **Inherits From**: [UIControl](uicontrol.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a segmented control

- [- initWithItems:](<uisegmentedcontrol/init(items_).md>) — Creates a segmented control with segments having the given titles or images.
- [- initWithFrame:actions:](<uisegmentedcontrol/init(frame_actions_).md>) — Creates a segmented control with the given frame and adds segments for the actions you specify.
- [- initWithFrame:](<uisegmentedcontrol/init(frame_).md>) — Creates an empty segmented control with the frame you specify.
- [- initWithCoder:](<uisegmentedcontrol/init(coder_).md>) — Creates a segmented control with data from an unarchiver.

### Managing segment content

- [- setImage:forSegmentAtIndex:](<uisegmentedcontrol/setimage(__forsegmentat_).md>) — Sets the content of a segment to a given image.
- [- imageForSegmentAtIndex:](<uisegmentedcontrol/imageforsegment(at_).md>) — Returns the image for a specific segment.
- [- setTitle:forSegmentAtIndex:](<uisegmentedcontrol/settitle(__forsegmentat_).md>) — Sets the title of a segment.
- [- titleForSegmentAtIndex:](<uisegmentedcontrol/titleforsegment(at_).md>) — Returns the title of the specified segment.

### Managing segment actions

- [- actionForSegmentAtIndex:](<uisegmentedcontrol/actionforsegment(at_).md>) — Fetches the action of the segment at the index you specify, if one exists.
- [- setAction:forSegmentAtIndex:](<uisegmentedcontrol/setaction(__forsegmentat_).md>) — Sets the action for the segment at the index you specify.

### Managing segments

- [numberOfSegments](uisegmentedcontrol/numberofsegments.md) — Returns the number of segments the segmented control has.
- [- segmentIndexForActionIdentifier:](<uisegmentedcontrol/segmentindex(identifiedby_).md>) — The index of a segment with an action that has an identifier matching the identifier you specify.
- [- insertSegmentWithAction:atIndex:animated:](<uisegmentedcontrol/insertsegment(action_at_animated_).md>) — Insert a segment with the action you specify at the given index.
- [- insertSegmentWithImage:atIndex:animated:](<uisegmentedcontrol/insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- insertSegmentWithTitle:atIndex:animated:](<uisegmentedcontrol/insertsegment(withtitle_at_animated_).md>) — Inserts a segment at the position you specify and gives it a title as content.
- [- removeAllSegments](<uisegmentedcontrol/removeallsegments().md>) — Removes all segments of the segmented control.
- [- removeSegmentAtIndex:animated:](<uisegmentedcontrol/removesegment(at_animated_).md>) — Removes the segment you specify from the segmented control, optionally animating the transition.
- [selectedSegmentIndex](uisegmentedcontrol/selectedsegmentindex.md) — The index number that identifies the selected segment that the user last touched.
- [UISegmentedControlNoSegment](uisegmentedcontrol/nosegment.md) — A segment index value indicating that there’s no selected segment.

### Managing segment behavior and appearance

- [momentary](uisegmentedcontrol/ismomentary.md) — A Boolean value that determines whether segments in the segmented control show selected state.
- [- setEnabled:forSegmentAtIndex:](<uisegmentedcontrol/setenabled(__forsegmentat_).md>) — Enables the segment you specify.
- [- isEnabledForSegmentAtIndex:](<uisegmentedcontrol/isenabledforsegment(at_).md>) — Returns whether the indicated segment is enabled.
- [- setContentOffset:forSegmentAtIndex:](<uisegmentedcontrol/setcontentoffset(__forsegmentat_).md>) — Adjusts the offset for drawing the content (image or text) of the specified segment.
- [- contentOffsetForSegmentAtIndex:](<uisegmentedcontrol/contentoffsetforsegment(at_).md>) — Returns the offset for drawing the content (image or text) of the segment you specify.
- [- setWidth:forSegmentAtIndex:](<uisegmentedcontrol/setwidth(__forsegmentat_).md>) — Sets the width of the segment at the index you specify.
- [- widthForSegmentAtIndex:](<uisegmentedcontrol/widthforsegment(at_).md>) — Returns the width of the segment at the index you specify.
- [apportionsSegmentWidthsByContent](uisegmentedcontrol/apportionssegmentwidthsbycontent.md) — Indicates whether the control attempts to adjust segment widths based on their content widths.

### Customizing appearance

- [selectedSegmentTintColor](uisegmentedcontrol/selectedsegmenttintcolor.md) — The color to use for highlighting the currently selected segment.
- [- backgroundImageForState:barMetrics:](<uisegmentedcontrol/backgroundimage(for_barmetrics_).md>) — Returns the background image for a given state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<uisegmentedcontrol/setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for given state and bar metrics.
- [- contentPositionAdjustmentForSegmentType:barMetrics:](<uisegmentedcontrol/contentpositionadjustment(forsegmenttype_barmetrics_).md>) — Returns the positioning offset for a given segment and bar metrics.
- [- setContentPositionAdjustment:forSegmentType:barMetrics:](<uisegmentedcontrol/setcontentpositionadjustment(__forsegmenttype_barmetrics_).md>) — Sets the content positioning offset for a given segment and bar metrics.
- [Segment](uisegmentedcontrol/segment.md) — Constants for specifying a segment in a control.
- [- dividerImageForLeftSegmentState:rightSegmentState:barMetrics:](<uisegmentedcontrol/dividerimage(forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:](<uisegmentedcontrol/setdividerimage(__forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [- titleTextAttributesForState:](<uisegmentedcontrol/titletextattributes(for_).md>) — Returns the text attributes of the title for a given control state.
- [- setTitleTextAttributes:forState:](<uisegmentedcontrol/settitletextattributes(__for_).md>) — Sets the text attributes of the title for a given control state.

## See Also

### Controls

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md) — Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [UIControl](uicontrol.md) — The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
- [UIButton](uibutton.md) — A control that executes your custom code in response to user interactions.
- [UIColorWell](uicolorwell.md) — A control that displays a color picker.
- [UIDatePicker](uidatepicker.md) — A control for inputting date and time values.
- [UIPageControl](uipagecontrol.md) — A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.
- [UISlider](uislider.md) — A control for selecting a single value from a continuous range of values.
- [UIStepper](uistepper.md) — A control for incrementing or decrementing a value.
- [UISwitch](uiswitch.md) — A control that offers a binary choice, such as on/off.
