---
title: 'signInWithAppleButtonStyle(_:)'
framework: AuthenticationServices
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, macOS 11.0+, tvOS 14.0+, watchOS 7.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/signinwithapplebuttonstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/signinwithapplebuttonstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/signinwithapplebuttonstyle%28_%3A%29.json'
content_hash: 'sha256:5c2bf798d58a1b7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# signInWithAppleButtonStyle(_:)

<sub>Instance Method</sub>

Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func signInWithAppleButtonStyle(_ style: SignInWithAppleButton.Style) -> some View

```

## Parameters

- `style` — The sign in style to apply to this button.

## See Also

### Authorizing and authenticating

- [LocalAuthenticationView](../../localauthentication/localauthenticationview.md) — A SwiftUI view that displays an authentication interface.
- [SignInWithAppleButton](../../authenticationservices/signinwithapplebutton.md) — A SwiftUI view that creates the Sign in with Apple button for display.
- [authorizationController](../environmentvalues/authorizationcontroller.md) — A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [webAuthenticationSession](../environmentvalues/webauthenticationsession.md) — A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.
