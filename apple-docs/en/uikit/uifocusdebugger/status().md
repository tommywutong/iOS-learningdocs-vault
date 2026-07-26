---
title: status()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusdebugger/status()
source_url: 'https://developer.apple.com/documentation/uikit/uifocusdebugger/status()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusdebugger/status%28%29.json'
content_hash: 'sha256:143f8f9b907238cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusDebugger](../uifocusdebugger.md)

# status()

<sub>Type Method</sub>

Returns the state of the focus system, including information about the currently focused item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func status() -> any UIFocusDebuggerOutput
```

## Return Value

An object the focus debugger uses to output information to the debugger console.

## Discussion

Call this method from the `lldb` debugger using the following command:

**Swift**

```swift
po UIFocusDebugger.status()
```

**Objective-C**

```objc
po [UIFocusDebugger status]
```

The method returns information about the focus system and the currently focused item.

## See Also

### Getting focus information

- [+ checkFocusabilityForItem:](<checkfocusability(for_).md>) — Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [+ focusGroupsForEnvironment:](<focusgroups(for_).md>) — Returns the focus group hierarchy for the specified environment object.
- [+ preferredFocusEnvironmentsForEnvironment:](<preferredfocusenvironments(for_).md>) — Returns the hierarchy of preferred focus environments for the specified environment object.
- [+ simulateFocusUpdateRequestFromEnvironment:](<simulatefocusupdaterequest(from_).md>) — Simulates a focus update request from the specified environment.
- [UIFocusDebuggerOutput](../uifocusdebuggeroutput.md) — An interface for specifying output from a focus debugger object.
