---
title: 'onAssignedDocumentWillWithdraw(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onassigneddocumentwillwithdraw(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onassigneddocumentwillwithdraw(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onassigneddocumentwillwithdraw%28_%3A%29.json'
content_hash: 'sha256:ff03da75897fbba4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onAssignedDocumentWillWithdraw(_:)

<sub>Instance Method</sub>

Adds an action to perform before withdrawing an assigned document submission.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func onAssignedDocumentWillWithdraw(_ action: @escaping @Sendable (URL) async -> Bool) -> some View

```

## Parameters

- `action` — An asynchronous closure that receives the document URL and returns a Boolean value indicating whether to proceed. Return `true` to continue, or `false` to cancel.

## Return Value

A view that executes the specified action before withdrawing an assigned document.

## Discussion

Return `true` to allow the withdrawal to proceed or `false` to cancel it. This action confirms whether the person wants to withdraw their work.

```swift
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentWillWithdraw { url in
        // Confirm the person's intent
        let confirmed = await showConfirmation(
            "Are you sure you want to withdraw your document submission?"
        )
        return confirmed
    }
```

## See Also

### Submission

- [onAssignedDocumentDidSubmit(_:)](<onassigneddocumentdidsubmit(__).md>) — Adds an action to perform after submitting an assigned document.
- [onAssignedDocumentDidWithdraw(_:)](<onassigneddocumentdidwithdraw(__).md>) — Adds an action to perform after an assigned document submission has been withdrawn.
- [onAssignedDocumentWillSubmit(_:)](<onassigneddocumentwillsubmit(__).md>) — Adds an action to perform before submitting an assigned document.
- [onSubmit(of:_:)](<onsubmit(of___).md>) — Adds an action to perform when the user submits a value to this view.
- [submitScope(_:)](<submitscope(__).md>) — Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [submitLabel(_:)](<submitlabel(__).md>) — Sets the submit label for this view.
