---
title: UIAlertController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller.json'
content_hash: 'sha256:2cbdc02463a1030c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAlertController

<sub>Class</sub>

An object that displays an alert message.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAlertController
```

## Overview

Use this class to configure alerts and action sheets with the message that you want to display and the actions from which to choose. After configuring the alert controller with the actions and style you want, present it using the [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) method. UIKit displays alerts and action sheets modally over your app’s content.

In addition to displaying a message to a user, you can associate actions with your alert controller to give people a way to respond. For each action you add using the [- addAction:](<uialertcontroller/addaction(__).md>) method, the alert controller configures a button with the action details. When a person taps that action, the alert controller executes the block you provided when creating the action object. The following code shows how to configure an alert with a single action.

**Swift**

```swift
let alert = UIAlertController(title: "My Alert", message: "This is an alert.", preferredStyle: .alert) 
alert.addAction(UIAlertAction(title: NSLocalizedString("OK", comment: "Default action"), style: .default, handler: { _ in 
NSLog("The \"OK\" alert occured.")
}))
self.present(alert, animated: true, completion: nil)
```

**Objective-C**

```objc
UIAlertController* alert = [UIAlertController alertControllerWithTitle:@"My Alert"
                               message:@"This is an alert."
                               preferredStyle:UIAlertControllerStyleAlert];
 
UIAlertAction* defaultAction = [UIAlertAction actionWithTitle:@"OK" style:UIAlertActionStyleDefault
   handler:^(UIAlertAction * action) {}];
 
[alert addAction:defaultAction];
[self presentViewController:alert animated:YES completion:nil];
```

When configuring an alert with the [UIAlertControllerStyleAlert](uialertcontroller/style/alert.md) style, you can also add text fields to the alert interface. The alert controller lets you provide a block for configuring your text fields prior to display. The alert controller maintains a reference to each text field so that you can access its value later.

> [!important] Important
> The [UIAlertController](uialertcontroller.md) class is intended to be used as-is and doesn’t support subclassing. The view hierarchy for this class is private and must not be modified.

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating an alert controller

- [+ alertControllerWithTitle:message:preferredStyle:](<uialertcontroller/init(title_message_preferredstyle_).md>) — Creates and returns a view controller for displaying an alert.

### Configuring the alert

- [title](uialertcontroller/title.md) — The title of the alert.
- [message](uialertcontroller/message.md) — Descriptive text that provides more details about the reason for the alert.
- [preferredStyle](uialertcontroller/preferredstyle.md) — The style of the alert controller.
- [Style](uialertcontroller/style.md) — Constants indicating the type of alert to display.

### Configuring the user actions

- [- addAction:](<uialertcontroller/addaction(__).md>) — Attaches an action object to the alert or action sheet.
- [actions](uialertcontroller/actions.md) — The actions that the user can take in response to the alert or action sheet.
- [preferredAction](uialertcontroller/preferredaction.md) — The preferred action for the user to take from an alert.

### Configuring text fields

- [- addTextFieldWithConfigurationHandler:](<uialertcontroller/addtextfield(configurationhandler_).md>) — Adds a text field to an alert.
- [textFields](uialertcontroller/textfields.md) — The array of text fields displayed by the alert.

### Configuring alert severity

- [severity](uialertcontroller/severity.md) — Indicates the severity of the alert.
- [UIAlertControllerSeverity](uialertcontrollerseverity.md) — Constants for specifying the severity of an alert in apps built with Mac Catalyst.

## See Also

### Alerts

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md) — Present important information to a person or prompt them about an important choice.
- [UIAlertAction](uialertaction.md) — An action that can be taken when the user taps a button in an alert.
