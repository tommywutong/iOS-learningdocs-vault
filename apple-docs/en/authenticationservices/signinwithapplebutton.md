---
title: SignInWithAppleButton
framework: AuthenticationServices
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/authenticationservices/signinwithapplebutton
source_url: 'https://developer.apple.com/documentation/authenticationservices/signinwithapplebutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/authenticationservices/signinwithapplebutton.json'
content_hash: 'sha256:ffc1cafb5b471fc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Authentication Services](../authenticationservices.md)

# SignInWithAppleButton

<sub>Structure</sub>

A SwiftUI view that creates the Sign in with Apple button for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SignInWithAppleButton
```

## Discussion

For more information about which Sign in with Apple buttons are available on different Apple platforms, see [Displaying Sign in with Apple buttons in your app](../signinwithapple/displaying-sign-in-with-apple-buttons-in-your-app.md).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a button

- [init(_:onRequest:onCompletion:)](<signinwithapplebutton/init(__onrequest_oncompletion_).md>) — Creates a Sign in with Apple button.
- [Label](signinwithapplebutton/label.md) — The label that appears on the button.
- [Style](signinwithapplebutton/style.md) — The structure that defines styles that you use to control the button’s appearance.

## See Also

### Sign In with Apple

- [Implementing User Authentication with Sign in with Apple](implementing-user-authentication-with-sign-in-with-apple.md) — Provide a way for users of your app to set up an account and start using your services.
- [Simplifying User Authentication in a tvOS App](simplifying-user-authentication-in-a-tvos-app.md) — Build a fluid sign-in experience for your tvOS apps using AuthenticationServices.
- [Sign in with Apple Entitlement](../bundleresources/entitlements/com.apple.developer.applesignin.md) — An entitlement that lets your app use Sign in with Apple.
- [ASAuthorizationAppleIDProvider](asauthorizationappleidprovider.md) — A mechanism for generating requests to authenticate users based on their Apple ID.
- [ASAuthorizationAppleIDCredential](asauthorizationappleidcredential.md) — A credential that results from a successful Apple ID authentication.
