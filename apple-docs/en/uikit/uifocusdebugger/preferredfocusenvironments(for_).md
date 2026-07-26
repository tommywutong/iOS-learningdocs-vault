---
title: 'preferredFocusEnvironments(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusdebugger/preferredfocusenvironments(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusdebugger/preferredfocusenvironments(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusdebugger/preferredfocusenvironments%28for%3A%29.json'
content_hash: 'sha256:375e39cc233d85bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusDebugger](../uifocusdebugger.md)

# preferredFocusEnvironments(for:)

<sub>Type Method</sub>

Returns the hierarchy of preferred focus environments for the specified environment object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func preferredFocusEnvironments(for environment: any UIFocusEnvironment) -> any UIFocusDebuggerOutput
```

## Parameters

- `environment` — The object you want to generate a heirarchy of preferred focus environments for. Specify the focus system, view, view controller, or window whose state you want. You can also specify any other object that adopts the [UIFocusEnvironment](../uifocusenvironment.md) protocol.

## Return Value

An object the focus debugger uses to store the results to format for display.

## Discussion

Use this method to better understand how the focus system chooses a default focusable item. You call the method from the `lldb` debugger using the following command. In the example, `obj` corresponds to an object that adopts the [UIFocusEnvironment](../uifocusenvironment.md) protocol.

**Swift**

```swift
po UIFocusDebugger.preferredFocusEnvironments(for: obj)
```

**Objective-C**

```objc
po [UIFocusDebugger preferredFocusEnvironmentsForEnvironment:obj]
```

The method returns the heirarchy of preferred environments for the focus environment object provided.

## See Also

### Getting focus information

- [+ status](<status().md>) — Returns the state of the focus system, including information about the currently focused item.
- [+ checkFocusabilityForItem:](<checkfocusability(for_).md>) — Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [+ focusGroupsForEnvironment:](<focusgroups(for_).md>) — Returns the focus group hierarchy for the specified environment object.
- [+ simulateFocusUpdateRequestFromEnvironment:](<simulatefocusupdaterequest(from_).md>) — Simulates a focus update request from the specified environment.
- [UIFocusDebuggerOutput](../uifocusdebuggeroutput.md) — An interface for specifying output from a focus debugger object.
