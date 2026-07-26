---
title: 'contactAccessPicker(isPresented:completionHandler:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/contactaccesspicker(ispresented:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/contactaccesspicker(ispresented:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/contactaccesspicker%28ispresented%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:14ef30dccf1704f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# contactAccessPicker(isPresented:completionHandler:)

<sub>Instance Method</sub>

Modally present UI which allows the user to select which contacts your app has access to.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func contactAccessPicker(isPresented: Binding<Bool>, completionHandler: @escaping ([String]) -> Void = { _ in }) -> some View

```

## Discussion

This API should only be used when your app has “Limited” authorization.  See `CNAuthorizationStatus` and `CNContactStore/authorizationStatus(for:)`.  The completion handler will be invoked with an empty result if your app doesn’t have the correct authorization status.

Your completion handler will receive an array of contact identifiers that were newly granted to your app.  Contacts which your app lost access to are not listed.  The newly-available contacts can be accessed using `CNContactStore`.

Parameters:

- isPresented: The binding to whether the contact picker should be shown.
- completionHandler: A function to invoke when the management UI is dismissed.  Receives an array containing contact identifiers of newly-available contacts.

## See Also

### Managing contact access

- [contactAccessButtonCaption(_:)](<contactaccessbuttoncaption(__).md>)
- [contactAccessButtonStyle(_:)](<contactaccessbuttonstyle(__).md>)
