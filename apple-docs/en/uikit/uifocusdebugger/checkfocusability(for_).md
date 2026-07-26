---
title: 'checkFocusability(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusdebugger/checkfocusability(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusdebugger/checkfocusability(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusdebugger/checkfocusability%28for%3A%29.json'
content_hash: 'sha256:ddb6b8bcbadf22ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusDebugger](../uifocusdebugger.md)

# checkFocusability(for:)

<sub>Type Method</sub>

Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func checkFocusability(for item: any UIFocusItem) -> any UIFocusDebuggerOutput
```

## Parameters

- `item` — The focus item to evaluate.

## Return Value

An object the focus debugger uses to store the results that it will format for display.

## Discussion

Call this method from the `lldb` debugger using the following command. In the example, `item` corresponds to an object that adopts the [UIFocusItem](../uifocusitem.md) protocol.

**Swift**

```swift
po UIFocusDebugger.checkFocusability(for: item)
```

**Objective-C**

```objc
po [UIFocusDebugger checkFocusabilityForItem: item]
```

The method returns the focus-related information, including known issues.

## See Also

### Getting focus information

- [+ status](<status().md>) — Returns the state of the focus system, including information about the currently focused item.
- [+ focusGroupsForEnvironment:](<focusgroups(for_).md>) — Returns the focus group hierarchy for the specified environment object.
- [+ preferredFocusEnvironmentsForEnvironment:](<preferredfocusenvironments(for_).md>) — Returns the hierarchy of preferred focus environments for the specified environment object.
- [+ simulateFocusUpdateRequestFromEnvironment:](<simulatefocusupdaterequest(from_).md>) — Simulates a focus update request from the specified environment.
- [UIFocusDebuggerOutput](../uifocusdebuggeroutput.md) — An interface for specifying output from a focus debugger object.
