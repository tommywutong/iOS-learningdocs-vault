---
title: 'workflowControllerDidStop(_:)'
framework: Automator
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidstop(_:)'
source_url: 'https://developer.apple.com/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidstop(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/automator/amworkflowcontrollerdelegate/workflowcontrollerdidstop%28_%3A%29.json'
content_hash: 'sha256:9eb9c3634d732ec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Automator](../../automator.md) · [AMWorkflowControllerDelegate](../amworkflowcontrollerdelegate.md)

# workflowControllerDidStop(_:)

<sub>Instance Method</sub>

Tells the delegate that the workflow controller object has stopped.

<sub>macOS</sub>

```swift
optional func workflowControllerDidStop(_ controller: AMWorkflowController)
```

## Parameters

- `controller` — The workflow controller object that stopped.

## See Also

### Stopping

- [- workflowControllerWillStop:](<workflowcontrollerwillstop(__).md>) — Tells the delegate that the workflow controller object is about to stop.
