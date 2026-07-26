---
title: help()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusdebugger/help()
source_url: 'https://developer.apple.com/documentation/uikit/uifocusdebugger/help()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusdebugger/help%28%29.json'
content_hash: 'sha256:2e9d3ea05c0ec547'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusDebugger](../uifocusdebugger.md)

# help()

<sub>Type Method</sub>

Returns information about how to use the commands of the debugger object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func help() -> any UIFocusDebuggerOutput
```

## Discussion

Call this method from the `lldb` debugger using the following commands:

**Swift**

```swift
po UIFocusDebugger.help()
```

**Objective-C**

```objc
po [UIFocusDebugger help]
```

The method returns information about how to use the other methods of this class to get information.
