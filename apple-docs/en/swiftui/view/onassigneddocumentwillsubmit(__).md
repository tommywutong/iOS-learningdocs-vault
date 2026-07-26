---
title: 'onAssignedDocumentWillSubmit(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onassigneddocumentwillsubmit(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onassigneddocumentwillsubmit(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onassigneddocumentwillsubmit%28_%3A%29.json'
content_hash: 'sha256:eece4afb6831ac8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onAssignedDocumentWillSubmit(_:)

<sub>Instance Method</sub>

Adds an action to perform before submitting an assigned document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func onAssignedDocumentWillSubmit(_ action: @escaping @Sendable (URL) async -> Bool) -> some View

```

## Parameters

- `action` — An asynchronous closure that receives the document URL and returns a Boolean value indicating whether to proceed with submission. Return `true` to continue, or `false` to cancel.

## Return Value

A view that executes the specified action before assigned document submission.

## Discussion

Return `true` to allow the submission to proceed, or `false` to cancel the submission. This is useful for validating document content, confirming user intent, or performing prerequisite operations.

```swift
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentWillSubmit { url in
        // Validate the assigned document before submission
        guard await isDocumentComplete(url) else {
            await showAlert("Please complete all sections before submitting")
            return false // Prevents submission
        }
        return true // Allows submission to continue
    }
```

## See Also

### Submission

- [onAssignedDocumentDidSubmit(_:)](<onassigneddocumentdidsubmit(__).md>) — Adds an action to perform after submitting an assigned document.
- [onAssignedDocumentDidWithdraw(_:)](<onassigneddocumentdidwithdraw(__).md>) — Adds an action to perform after an assigned document submission has been withdrawn.
- [onAssignedDocumentWillWithdraw(_:)](<onassigneddocumentwillwithdraw(__).md>) — Adds an action to perform before withdrawing an assigned document submission.
- [onSubmit(of:_:)](<onsubmit(of___).md>) — Adds an action to perform when the user submits a value to this view.
- [submitScope(_:)](<submitscope(__).md>) — Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [submitLabel(_:)](<submitlabel(__).md>) — Sets the submit label for this view.
