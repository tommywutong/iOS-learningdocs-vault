---
title: UIStoryboardSegue
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboardsegue
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardsegue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardsegue.json'
content_hash: 'sha256:633debe27334bb34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStoryboardSegue

<sub>Class</sub>

An object that prepares for and performs the visual transition between two view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIStoryboardSegue
```

## Overview

The [UIStoryboardSegue](uistoryboardsegue.md) class supports the standard visual transitions available in UIKit. You can also subclass to define custom transitions between the view controllers in your storyboard file.

Segue objects contain information about the view controllers involved in a transition. When a segue is triggered, but before the visual transition occurs, the storyboard runtime calls the current view controller’s [- prepareForSegue:sender:](<uiviewcontroller/prepare(for_sender_).md>) method so that it can pass any needed data to the view controller that’s about to be displayed.

You don’t create segue objects directly. Instead, the storyboard runtime creates them when it must perform a segue between two view controllers. You can still initiate a segue programmatically using the [- performSegueWithIdentifier:sender:](<uiviewcontroller/performsegue(withidentifier_sender_).md>) method of [UIViewController](uiviewcontroller.md) if you want. You might do so to initiate a segue from a source that was added programmatically and therefore not available in Interface Builder.

### Subclassing notes

You can subclass [UIStoryboardSegue](uistoryboardsegue.md) in situations where you want to provide a custom transition between view controllers in your application. To use your custom segue, create a segue line between the appropriate view controllers in Interface Builder and set its type to Custom in the inspector; you must also specify the class name of the segue to use in the inspector.

When the storyboard runtime detects a custom segue, it creates a new instance of your class, configures it with the view controller objects, asks the view controller source to prepare for the segue, and then performs the segue.

#### Methods to override

For custom segues, the main method you need to override is the [- perform](<uistoryboardsegue/perform().md>) method. The storyboard runtime calls this method when it’s time to perform the visual transition from the view controller in [sourceViewController](uistoryboardsegue/source.md) to the view controller in [destinationViewController](uistoryboardsegue/destination.md). If you need to initialize any variables in your custom segue subclass, you can also override the [- initWithIdentifier:source:destination:](<uistoryboardsegue/init(identifier_source_destination_).md>) method and initialize them in your custom implementation.

#### Alternatives to subclassing

If your segue doesn’t need to store additional information or provide anything other than a [- perform](<uistoryboardsegue/perform().md>) method, consider using the [+ segueWithIdentifier:source:destination:performHandler:](<uistoryboardsegue/init(identifier_source_destination_performhandler_).md>) method instead.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a storyboard segue

- [- initWithIdentifier:source:destination:](<uistoryboardsegue/init(identifier_source_destination_).md>) — Initializes and returns a storyboard segue object for use in performing a segue.

### Accessing the segue attributes

- [sourceViewController](uistoryboardsegue/source.md) — The source view controller for the segue.
- [destinationViewController](uistoryboardsegue/destination.md) — The destination view controller for the segue.
- [identifier](uistoryboardsegue/identifier.md) — The identifier for the segue object.

### Performing the segue

- [- perform](<uistoryboardsegue/perform().md>) — Performs the visual transition for the segue.

### Creating a custom segue

- [+ segueWithIdentifier:source:destination:performHandler:](<uistoryboardsegue/init(identifier_source_destination_performhandler_).md>) — Creates a segue that calls a block to perform the segue transition.

## See Also

### Storyboards

- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md) — Pass data between view controllers during a segue, and programmatically control when segues occur.
- [Dismissing a view controller with an unwind segue](dismissing-a-view-controller-with-an-unwind-segue.md) — Configure an unwind segue in your storyboard file that dynamically chooses the most appropriate view controller to display next.
- [UIStoryboard](uistoryboard.md) — An encapsulation of the design-time view controller graph represented in an Interface Builder storyboard resource file.
- [UIStoryboardUnwindSegueSource](uistoryboardunwindseguesource.md) — An encapsulation of information about an unwind segue.
