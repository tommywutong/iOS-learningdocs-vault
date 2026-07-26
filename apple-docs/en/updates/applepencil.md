---
title: Apple Pencil updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/applepencil
source_url: 'https://developer.apple.com/documentation/updates/applepencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/applepencil.json'
content_hash: 'sha256:85fe6bbd547ea5ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# Apple Pencil updates

<sub>Article</sub>

Learn about important changes to Apple Pencil.

## Overview

Browse notable changes in [Apple Pencil](../applepencil.md).

## June 2024

### UIKit

- Implement custom low-latency drawing if your app doesn’t use PencilKit. Participate in UI updates and influence UI update behavior using [UIUpdateLink](../uikit/uiupdatelink.md).

### PencilKit

- Offer a wider variety of marking tools by creating a configurable tool picker. Create a [PKToolPicker](../pencilkit/pktoolpicker.md), add standard system tools or define your own custom tools with [PKToolPickerCustomItem](../pencilkit/pktoolpickercustomitem.md), and specify which order the tools appear in. Include an optional [accessoryItem](../pencilkit/pktoolpicker/accessoryitem.md) in the tool picker to provide quick access to additional features directly from the picker.

## May 2024

### SwiftUI and UIKit

- Perform actions in your app in response to squeeze interactions on Apple Pencil Pro. People can choose their preferred squeeze action in Settings \> Apple Pencil \> Actions \> Squeeze, such as switching drawing tools, showing a contextual palette, or performing an App Shortcut. You can also implement a custom action for squeeze and give people the choice to use your app’s custom behavior instead. In SwiftUI, use [onPencilSqueeze(perform:)](<../swiftui/view/onpencilsqueeze(perform_).md>). In UIKit, use [pencilInteraction(_:didReceiveSqueeze:)](<../uikit/uipencilinteractiondelegate/pencilinteraction(__didreceivesqueeze_).md>).
- Perform actions in your app in response to double-tap interactions on Apple Pencil. People can choose their preferred double-tap action in Settings \> Apple Pencil \> Actions \> Double Tap. In SwiftUI, use [onPencilDoubleTap(perform:)](<../swiftui/view/onpencildoubletap(perform_).md>). In UIKit, update your implementation to use [pencilInteraction(_:didReceiveTap:)](<../uikit/uipencilinteractiondelegate/pencilinteraction(__didreceivetap_).md>), which replaces the deprecated [pencilInteractionDidTap(_:)](<../uikit/uipencilinteractiondelegate/pencilinteractiondidtap(__).md>).
- Leverage the hover pose of Apple Pencil to support more complex interactions in response to a double tap or squeeze. Information about the hover pose — such as azimuth, altitude, and hover distance — is available when a person holds a supported model of Apple Pencil close to the screen during a double tap or squeeze. In SwiftUI, use [PencilHoverPose](../swiftui/pencilhoverpose.md). In UIKit, use [UIPencilHoverPose](../uikit/uipencilhoverpose.md).
- Provide tactile feedback on Apple Pencil Pro by playing haptics in response to certain actions, such as snapping objects to a grid. In SwiftUI, use [SensoryFeedback](../swiftui/sensoryfeedback.md). In UIKit, use [UIFeedbackGenerator](../uikit/uifeedbackgenerator.md).
- Track the barrel-roll angle of Apple Pencil Pro to create more expressive drawing experiences and hover previews using [rollAngle](../uikit/uitouch/rollangle.md).

- Check the value of the hover tool preview preference from the Apple Pencil section of the Settings app using [prefersHoverToolPreview](../uikit/uipencilinteraction/prefershovertoolpreview.md).

### PencilKit

- Take advantage of barrel-roll tracking for Apple Pencil Pro when a person makes marker and fountain pen strokes. Support [PKContentVersion.version3](../pencilkit/pkcontentversion/version3.md), which includes the version of the inks that incorporate barrel-roll data.

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
- [Background Tasks updates](backgroundtasks.md) — Learn about important changes in Background Tasks.
