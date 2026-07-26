---
title: authorizationController
framework: AuthenticationServices
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, macOS 13.3+, tvOS 16.4+, watchOS 9.4+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/authorizationcontroller
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/authorizationcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/authorizationcontroller.json'
content_hash: 'sha256:9c3c0a6cd1abee44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# authorizationController

<sub>Instance Property</sub>

A value provided in the SwiftUI environment that views can use to perform authorization requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var authorizationController: AuthorizationController { get }
```

## Discussion

For example, you can perform authorization requests when the user taps a button:

```swift
struct AuthorizationControllerExample: View {
    @Environment(\.authorizationController) private var authorizationController

    var body: some View {
        Button("Sign In") {
            Task {
                do {
                    async let requests = authorizationRequests() // defined elsewhere
                    let result = try await authorizationController
                        .performRequests(requests)

                    switch result {
                    // code to handle the authorization result
                    }
                } catch {
                    // code to handle the authorization error
                }
            }
        }
    }
}
```

## See Also

### Authorizing and authenticating

- [LocalAuthenticationView](../../localauthentication/localauthenticationview.md) — A SwiftUI view that displays an authentication interface.
- [SignInWithAppleButton](../../authenticationservices/signinwithapplebutton.md) — A SwiftUI view that creates the Sign in with Apple button for display.
- [signInWithAppleButtonStyle(_:)](<../view/signinwithapplebuttonstyle(__).md>) — Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [webAuthenticationSession](webauthenticationsession.md) — A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.
