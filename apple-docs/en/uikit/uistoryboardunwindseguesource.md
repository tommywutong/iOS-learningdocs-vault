---
title: UIStoryboardUnwindSegueSource
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistoryboardunwindseguesource
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardunwindseguesource.json'
content_hash: 'sha256:7962292c21b04743'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStoryboardUnwindSegueSource

<sub>Class</sub>

An encapsulation of information about an unwind segue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIStoryboardUnwindSegueSource
```

## Overview

You don’t create instances of this class yourself. UIKit creates an unwind segue source object in response to the triggering of an unwind segue. It passes the source object to other view controller methods that determine the destination of the unwind segue. The information in an unwind segue source object includes the view controller being dismissed by the segue and the action method responsible for the dismissal.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the unwind segue attributes

- [sourceViewController](uistoryboardunwindseguesource/source.md) — The view controller being dismissed by the unwind segue.
- [unwindAction](uistoryboardunwindseguesource/unwindaction.md) — The action method associated with the unwind segue.
- [sender](uistoryboardunwindseguesource/sender.md) — The object that performed the unwind action.

## See Also

### Storyboards

- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md) — Pass data between view controllers during a segue, and programmatically control when segues occur.
- [Dismissing a view controller with an unwind segue](dismissing-a-view-controller-with-an-unwind-segue.md) — Configure an unwind segue in your storyboard file that dynamically chooses the most appropriate view controller to display next.
- [UIStoryboard](uistoryboard.md) — An encapsulation of the design-time view controller graph represented in an Interface Builder storyboard resource file.
- [UIStoryboardSegue](uistoryboardsegue.md) — An object that prepares for and performs the visual transition between two view controllers.
