---
title: UIStoryboard
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboard
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboard.json'
content_hash: 'sha256:cc8fd606db0523b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStoryboard

<sub>Class</sub>

An encapsulation of the design-time view controller graph represented in an Interface Builder storyboard resource file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIStoryboard
```

## Overview

A [UIStoryboard](uistoryboard.md) object manages archived versions of your app’s view controllers. At design time, you configure the content of your view controllers visually, and Xcode saves the data needed to recreate that interface in a storyboard file in your app’s bundle. When you want to create a new view controller programmatically, first create a [UIStoryboard](uistoryboard.md) object and specify the appropriate name and bundle information. Then use that object to instantiate the specific view controller that you want.

During the instantiation process, [UIStoryboard](uistoryboard.md) creates your view controller programmatically using its [- initWithCoder:](<uiviewcontroller/init(coder_).md>) method. The storyboard passes the view controller’s data archive to that method, which then uses the data to recreate the state of the view controller and its views. If you have a custom initialization method for your view controller, you can ask the storyboard to instantiate your view controller using a block you provide. You can use this block to call your custom initialization method, passing any extra data your view controller needs.

For visionOS apps, you can load existing storyboards, but you can’t add content specific to the platform. Migrate your interface code to SwiftUI as soon as possible.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting a Storyboard Object

- [+ storyboardWithName:bundle:](<uistoryboard/init(name_bundle_).md>) — Creates and returns a storyboard object for the specified resource file.

### Loading the Initial View Controller

- [- instantiateInitialViewController](<uistoryboard/instantiateinitialviewcontroller().md>) — Creates the initial view controller and initializes it with the data from the storyboard.
- [instantiateInitialViewController(creator:)](<uistoryboard/instantiateinitialviewcontroller(creator_).md>) — Creates the initial view controller from the storyboard and initializes it using your custom initialization code.

### Instantiating Storyboard View Controllers

- [- instantiateViewControllerWithIdentifier:](<uistoryboard/instantiateviewcontroller(withidentifier_).md>) — Creates the view controller with the specified identifier and initializes it with the data from the storyboard.
- [instantiateViewController(identifier:creator:)](<uistoryboard/instantiateviewcontroller(identifier_creator_).md>) — Creates the specified view controller from the storyboard and initializes it using your custom initialization code.

## See Also

### Storyboards

- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md) — Pass data between view controllers during a segue, and programmatically control when segues occur.
- [Dismissing a view controller with an unwind segue](dismissing-a-view-controller-with-an-unwind-segue.md) — Configure an unwind segue in your storyboard file that dynamically chooses the most appropriate view controller to display next.
- [UIStoryboardSegue](uistoryboardsegue.md) — An object that prepares for and performs the visual transition between two view controllers.
- [UIStoryboardUnwindSegueSource](uistoryboardunwindseguesource.md) — An encapsulation of information about an unwind segue.
