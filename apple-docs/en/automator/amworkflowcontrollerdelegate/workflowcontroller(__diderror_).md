---
title: 'workflowController(_:didError:)'
framework: Automator
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:diderror:)'
source_url: 'https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller(_:diderror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automator/amworkflowcontrollerdelegate/workflowcontroller%28_%3Adiderror%3A%29.json'
content_hash: 'sha256:f59f945073da7810'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Automator](../../automator.md) · [AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)

# workflowController(_:didError:)

<sub>Instance Method</sub>

Notifies the delegate when the workflow encounters an error.

<sub>macOS</sub>

```swift
optional func workflowController(_ controller: AMWorkflowController, didError error: any Error)
```

## Parameters

- `controller` — The controller object sending the message.

- `error` — If a workflow error occurs, upon return contains an instance of [NSError](../../foundation/nserror.md) that describes the problem.
