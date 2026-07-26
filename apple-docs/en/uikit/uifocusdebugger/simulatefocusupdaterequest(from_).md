---
title: 'simulateFocusUpdateRequest(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusdebugger/simulatefocusupdaterequest(from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusdebugger/simulatefocusupdaterequest(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusdebugger/simulatefocusupdaterequest%28from%3A%29.json'
content_hash: 'sha256:10e9ada1a5593348'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusDebugger](../uifocusdebugger.md)

# simulateFocusUpdateRequest(from:)

<sub>Type Method</sub>

Simulates a focus update request from the specified environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func simulateFocusUpdateRequest(from environment: any UIFocusEnvironment) -> any UIFocusDebuggerOutput
```

## Parameters

- `environment` — The object you want to generate a request for. Specify the focus system, view, view controller, or window whose state you want. You can also specify any other object that adopts the [UIFocusEnvironment](../uifocusenvironment.md) protocol.

## Return Value

The [UIFocusDebuggerOutput](../uifocusdebuggeroutput.md) object the focus debugger uses to output the diagnostic information to the debugger console.

## Discussion

Call this method from the `lldb` debugger using the following command. In the example, `obj` corresponds to an object that adopts the [UIFocusEnvironment](../uifocusenvironment.md) protocol.

**Swift**

```swift
po UIFocusDebugger.simulateFocusUpdateRequest(from: obj)
```

**Objective-C**

```objc
po [UIFocusDebugger simulateFocusUpdateRequestFromEnvironment: obj]
```

The method simulates a focus update request, outlining each step of the process for determining the next focused item.

## See Also

### Getting focus information

- [+ status](<status().md>) — Returns the state of the focus system, including information about the currently focused item.
- [+ checkFocusabilityForItem:](<checkfocusability(for_).md>) — Returns information about whether the item can become focused, including any known issues that would prevent the item from becoming focused.
- [+ focusGroupsForEnvironment:](<focusgroups(for_).md>) — Returns the focus group hierarchy for the specified environment object.
- [+ preferredFocusEnvironmentsForEnvironment:](<preferredfocusenvironments(for_).md>) — Returns the hierarchy of preferred focus environments for the specified environment object.
- [UIFocusDebuggerOutput](../uifocusdebuggeroutput.md) — An interface for specifying output from a focus debugger object.
