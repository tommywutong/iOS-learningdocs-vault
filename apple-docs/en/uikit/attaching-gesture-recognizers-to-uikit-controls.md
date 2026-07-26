---
title: Attaching gesture recognizers to UIKit controls
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/attaching-gesture-recognizers-to-uikit-controls
source_url: 'https://developer.apple.com/documentation/uikit/attaching-gesture-recognizers-to-uikit-controls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/attaching-gesture-recognizers-to-uikit-controls.json'
content_hash: 'sha256:f51058f0cd402f27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md) · [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md)

# Attaching gesture recognizers to UIKit controls

<sub>Article</sub>

Learn how gesture recognizers interact with UIKit controls such as buttons, switches, and sliders.

## Overview

Gesture recognizers attached to your views don’t impact the ability of UIKit controls to handle events. Events occurring within the bounds of a control are handled by the control first, giving the control a chance to call its action method. Specifically, UIKit controls call their action method in the following situations:

- A single finger single tap occurs on a [UIButton](uibutton.md), [UISwitch](uiswitch.md), [UIStepper](uistepper.md), [UISegmentedControl](uisegmentedcontrol.md), or [UIPageControl](uipagecontrol.md) object.
- A single finger swipe occurs on the knob of a [UISlider](uislider.md) object, in a direction parallel to the slider.
- A single finger pan occurs on the knob of a [UISwitch](uiswitch.md) object, in a direction parallel to the switch.

To handle any of the preceding gestures before the control calls its action method, install your gesture recognizer on the control itself. Gesture recognizers handle touch events before the views to which they’re attached. As a result, installing a gesture recognizer directly on a control prevents that control from calling its action method.

> [!important] Important
> Always consult the platform-specific human interface guidelines before changing the default behavior of standard controls. For more information, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/platforms/overview).

## See Also

### Simultaneous gestures

- [Preferring one gesture over another](preferring-one-gesture-over-another.md) — Use a gesture recognizer delegate object to determine the order in which gestures are recognized in your views.
- [Allowing the simultaneous recognition of multiple gestures](allowing-the-simultaneous-recognition-of-multiple-gestures.md) — Learn how to use a delegate object to allow detection of more than one gesture at a time.
