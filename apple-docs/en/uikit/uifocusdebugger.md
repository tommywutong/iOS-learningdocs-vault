---
title: UIFocusDebugger
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusdebugger
source_url: 'https://developer.apple.com/documentation/uikit/uifocusdebugger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusdebugger.json'
content_hash: 'sha256:ac9f3beba13c5416'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusDebugger

<sub>Class</sub>

A runtime object for debugging focus-related interactions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIFocusDebugger
```

## Overview

You do not use this class or its methods directly from your code. During a debugging session, you can call the methods of this class from the `lldb` debugger command line to obtain information about the current state of the focus system.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting help

- [+ help](<uifocusdebugger/help().md>) — Returns information about how to use the commands of the debugger object.

### Getting focus information

- [+ status](<uifocusdebugger/status().md>) — Returns the state of the focus system, including information about the currently focused item.
- [+ checkFocusabilityForItem:](<uifocusdebugger/checkfocusability(for_).md>) — Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [+ focusGroupsForEnvironment:](<uifocusdebugger/focusgroups(for_).md>) — Returns the focus group hierarchy for the specified environment object.
- [+ preferredFocusEnvironmentsForEnvironment:](<uifocusdebugger/preferredfocusenvironments(for_).md>) — Returns the hierarchy of preferred focus environments for the specified environment object.
- [+ simulateFocusUpdateRequestFromEnvironment:](<uifocusdebugger/simulatefocusupdaterequest(from_).md>) — Simulates a focus update request from the specified environment.
- [UIFocusDebuggerOutput](uifocusdebuggeroutput.md) — An interface for specifying output from a focus debugger object.

## See Also

### Focus debugging

- [Debugging focus issues in your app](debugging-focus-issues-in-your-app.md) — Find errors and determine why the next focused item isn’t what you expected.
