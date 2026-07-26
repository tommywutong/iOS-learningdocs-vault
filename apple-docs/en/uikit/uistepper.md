---
title: UIStepper
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistepper
source_url: 'https://developer.apple.com/documentation/uikit/uistepper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper.json'
content_hash: 'sha256:03137a1e07e588ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStepper

<sub>Class</sub>

A control for incrementing or decrementing a value.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIStepper
```

## Overview

By default, pressing and holding a stepper’s button increments or decrements the stepper’s value repeatedly. The rate of change depends on how long the user continues pressing the control. To turn off this behavior, set the [autorepeat](uistepper/autorepeat.md) property to [false](../swift/false.md).

The maximum value must be greater than or equal to the minimum value. If you set a maximum or minimum value that would break this invariant, both values are set to the new value. For example, if the minimum value is 200 and you set a maximum value of 100, then both the minimum and maximum become 200.

## Relationships

- **Inherits From**: [UIControl](uicontrol.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Configuring the stepper

- [continuous](uistepper/iscontinuous.md) — A Boolean value that determines whether to send value changes during user interaction or after user interaction ends.
- [autorepeat](uistepper/autorepeat.md) — A Boolean value that determines whether to repeatedly change the stepper’s value as the user presses and holds a stepper button.
- [wraps](uistepper/wraps.md) — A Boolean value that determines whether the stepper can wrap its value to the minimum or maximum value when incrementing and decrementing the value.
- [minimumValue](uistepper/minimumvalue.md) — The lowest possible numeric value for the stepper.
- [maximumValue](uistepper/maximumvalue.md) — The highest possible numeric value for the stepper.
- [stepValue](uistepper/stepvalue.md) — The step, or increment, value for the stepper.

### Accessing the stepper’s value

- [value](uistepper/value.md) — The numeric value of the stepper.

### Customizing appearance

- [- backgroundImageForState:](<uistepper/backgroundimage(for_).md>) — Returns the background image associated with the specified control state.
- [- setBackgroundImage:forState:](<uistepper/setbackgroundimage(__for_).md>) — Sets the background image for the control when it’s in the specified state.
- [- decrementImageForState:](<uistepper/decrementimage(for_).md>) — Returns the image used for the decrement glyph of the control.
- [- setDecrementImage:forState:](<uistepper/setdecrementimage(__for_).md>) — Sets the image to use for the decrement glyph of the control.
- [- dividerImageForLeftSegmentState:rightSegmentState:](<uistepper/dividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image for the given combination of left and right states.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:](<uistepper/setdividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the image to use for the given combination of left and right states.
- [- incrementImageForState:](<uistepper/incrementimage(for_).md>) — Returns the image used for the increment glyph of the control.
- [- setIncrementImage:forState:](<uistepper/setincrementimage(__for_).md>) — Sets the image to use for the increment glyph of the control.

## See Also

### Controls

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md) — Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [UIControl](uicontrol.md) — The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
- [UIButton](uibutton.md) — A control that executes your custom code in response to user interactions.
- [UIColorWell](uicolorwell.md) — A control that displays a color picker.
- [UIDatePicker](uidatepicker.md) — A control for inputting date and time values.
- [UIPageControl](uipagecontrol.md) — A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.
- [UISegmentedControl](uisegmentedcontrol.md) — A horizontal control that consists of multiple segments, each segment functioning as a discrete button.
- [UISlider](uislider.md) — A control for selecting a single value from a continuous range of values.
- [UISwitch](uiswitch.md) — A control that offers a binary choice, such as on/off.
