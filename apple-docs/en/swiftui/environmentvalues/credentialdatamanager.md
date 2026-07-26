---
title: credentialDataManager
framework: AuthenticationServices
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.2+, iPadOS 26.2+, macOS 26.2+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/credentialdatamanager
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/credentialdatamanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/credentialdatamanager.json'
content_hash: 'sha256:3e18d40a1b0bfbb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# credentialDataManager

<sub>Instance Property</sub>

This environment variable is for SwiftUI clients of the ASCredentialDataManager API. An example usage might look like:

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var credentialDataManager: CredentialDataManager { get }
```

## Discussion

```swift
struct CredentialDataManagerExample: View {
    @Environment(\.credentialDataManager) private var credentialDataManager

    var body: some View {
        Button("Save Credentials") {
            Task {
                do {
                    let credential = getCredential() // defined elsewhere
                    let scope = getScope()
                    try await credentialDataManager.save(credential: credential, for: scope)
                } catch {
                    // code to handle the save error
                }
            }
        }
    }
}
```
