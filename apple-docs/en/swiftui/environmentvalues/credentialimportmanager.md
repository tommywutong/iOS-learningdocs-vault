---
title: credentialImportManager
framework: AuthenticationServices
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/credentialimportmanager
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/credentialimportmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/credentialimportmanager.json'
content_hash: 'sha256:d200790bd529959d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# credentialImportManager

<sub>Instance Property</sub>

This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var credentialImportManager: ASCredentialImportManager { get }
```

## Discussion

```swift
struct CredentialImportManagerExample: View {
    @Environment(\.credentialImportManager) private var credentialImportManager

    var body: some View {
        content // defined elsewhere
            .onContinueUserActivity(ASCredentialExchangeActivity) { activity in
                Task {
                    do {
                        guard let token = activity.userInfo?[ASCredentialImportToken] as? UUID else { return }
                        let credentialData = try await credentialImportManager.importCredentials(token: token)
                        // do something with the data
                    } catch {
                        // code to handle the import error
                    }
                }
            }
    }
}
```
