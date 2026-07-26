---
title: didReceiveMemoryWarning()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/didreceivememorywarning()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/didreceivememorywarning()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/didreceivememorywarning%28%29.json'
content_hash: 'sha256:cd1a81763b6e95eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# didReceiveMemoryWarning()

<sub>Instance Method</sub>

Sent to the view controller when the app receives a memory warning.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didReceiveMemoryWarning()
```

## Discussion

Your app never calls this method directly. Instead, this method is called when the system determines that the amount of available memory is low.

You can override this method to release any additional memory used by your view controller. If you do, your implementation of this method must call the `super` implementation at some point.
