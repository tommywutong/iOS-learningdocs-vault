---
title: 'writingToolsCoordinator(_:willChangeTo:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator%28_%3Awillchangeto%3Acompletion%3A%29.json'
content_hash: 'sha256:410edd7662bea6dc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWritingToolsCoordinator](../../uiwritingtoolscoordinator.md) · [Delegate](../delegate-swift.protocol.md)

# writingToolsCoordinator(_:willChangeTo:completion:)

<sub>Instance Method</sub>

Notifies your delegate of relevant state changes when Writing Tools is running in your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, willChangeTo newState: UIWritingToolsCoordinator.State, completion: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, willChangeTo newState: UIWritingToolsCoordinator.State) async
```

## Parameters

- `writingToolsCoordinator` — The coordinator object providing information to your custom view.

- `completion` — A handler to execute when your delegate finishes processing the change of state. The handler has no parameters or return value. You must call this handler at some point during the implementation of your method.

## Discussion

Use state transitions to perform actions related to your view or text storage. When Writing Tools is active, it updates its state to indicate what task it’s currently performing. Writing Tools starts in the [UIWritingToolsCoordinatorStateInactive](../state-swift.enum/inactive.md) state and moves to other states as it presents UI and starts interacting with your view’s content. For example, it moves to the [UIWritingToolsCoordinatorStateInteractiveStreaming](../state-swift.enum/interactivestreaming.md) state when it’s making changes to your view’s text storage.
