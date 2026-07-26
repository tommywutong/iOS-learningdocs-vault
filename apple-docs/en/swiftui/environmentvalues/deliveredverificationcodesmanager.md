---
title: deliveredVerificationCodesManager
framework: AuthenticationServices
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/deliveredverificationcodesmanager
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/deliveredverificationcodesmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/deliveredverificationcodesmanager.json'
content_hash: 'sha256:c0b767c880058545'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# deliveredVerificationCodesManager

<sub>Instance Property</sub>

This environment variable is for SwiftUI clients of the ASDeliveredVerificationCodesManager API. An example usage might look like:

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var deliveredVerificationCodesManager: DeliveredVerificationCodesManager { get }
```

## Discussion

```swift
struct DeliveredVerificationCodesManagerExample: View {
    @Environment(\.deliveredVerificationCodesManager) private var deliveredVerificationCodesManager

    var body: some View {
        Button("Listen for Codes") {
            Task {
                do {
                    let codes = try deliveredVerificationCodesManager.oneTimeCodes()
                    for try await code in codes {
                        handle(code: code)
                    }
                } catch DeliveredVerificationCodesManager.VerificationError.userPermissionDenied {
                    // Explaining why OTCs are needed or try without codes
                } catch DeliveredVerificationCodesManager.VerificationError.appIsNotEnabledCredentialProvider {
                    // Show UI explaining how to turn on the app as a Password Manager
                } catch {
                    // code to handle the save error
                }
            }
        }
    }
}
```
