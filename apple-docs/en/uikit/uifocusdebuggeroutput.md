---
title: UIFocusDebuggerOutput
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusdebuggeroutput
source_url: 'https://developer.apple.com/documentation/uikit/uifocusdebuggeroutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusdebuggeroutput.json'
content_hash: 'sha256:303908912f513f20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusDebuggerOutput

<sub>Protocol</sub>

An interface for specifying output from a focus debugger object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIFocusDebuggerOutput : NSObjectProtocol
```

## Overview

Don’t use this protocol directly in your code. When debugging your app from the `lldb` command line, the methods of [UIFocusDebugger](uifocusdebugger.md) output their results to an object that adopts this protocol. The debugger takes the output and formats it for display.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Getting focus information

- [+ status](<uifocusdebugger/status().md>) — Returns the state of the focus system, including information about the currently focused item.
- [+ checkFocusabilityForItem:](<uifocusdebugger/checkfocusability(for_).md>) — Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [+ focusGroupsForEnvironment:](<uifocusdebugger/focusgroups(for_).md>) — Returns the focus group hierarchy for the specified environment object.
- [+ preferredFocusEnvironmentsForEnvironment:](<uifocusdebugger/preferredfocusenvironments(for_).md>) — Returns the hierarchy of preferred focus environments for the specified environment object.
- [+ simulateFocusUpdateRequestFromEnvironment:](<uifocusdebugger/simulatefocusupdaterequest(from_).md>) — Simulates a focus update request from the specified environment.
