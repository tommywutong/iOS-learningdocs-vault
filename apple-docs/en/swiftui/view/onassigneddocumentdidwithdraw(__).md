---
title: 'onAssignedDocumentDidWithdraw(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onassigneddocumentdidwithdraw(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onassigneddocumentdidwithdraw(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onassigneddocumentdidwithdraw%28_%3A%29.json'
content_hash: 'sha256:3d96289b514c8b0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onAssignedDocumentDidWithdraw(_:)

<sub>Instance Method</sub>

Adds an action to perform after an assigned document submission has been withdrawn.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func onAssignedDocumentDidWithdraw(_ action: @escaping (URL) -> Void) -> some View

```

## Parameters

- `action` — An asynchronous closure that receives the document URL and executes after successful submission withdrawal.

## Return Value

A view that executes the specified action after submission withdrawal.

## Discussion

This action runs regardless of whether you provided an [onAssignedDocumentWillWithdraw(_:)](<onassigneddocumentwillwithdraw(__).md>) action, and only runs if the withdrawal completes successfully.

```swift
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentDidWithdraw { url in
        // Handle successful withdrawal
        logEvent("Assigned document withdrawn successfully!")
    }
```

## See Also

### Submission

- [onAssignedDocumentDidSubmit(_:)](<onassigneddocumentdidsubmit(__).md>) — Adds an action to perform after submitting an assigned document.
- [onAssignedDocumentWillSubmit(_:)](<onassigneddocumentwillsubmit(__).md>) — Adds an action to perform before submitting an assigned document.
- [onAssignedDocumentWillWithdraw(_:)](<onassigneddocumentwillwithdraw(__).md>) — Adds an action to perform before withdrawing an assigned document submission.
- [onSubmit(of:_:)](<onsubmit(of___).md>) — Adds an action to perform when the user submits a value to this view.
- [submitScope(_:)](<submitscope(__).md>) — Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [submitLabel(_:)](<submitlabel(__).md>) — Sets the submit label for this view.
