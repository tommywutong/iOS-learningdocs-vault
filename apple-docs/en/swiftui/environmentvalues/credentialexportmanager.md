---
title: credentialExportManager
framework: AuthenticationServices
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/credentialexportmanager
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/credentialexportmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/credentialexportmanager.json'
content_hash: 'sha256:8cac91bab71d4a13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# credentialExportManager

<sub>Instance Property</sub>

This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var credentialExportManager: ASCredentialExportManager { get }
```

## Discussion

```swift
struct CredentialExchangeManagerExample: View {
    @Environment(\.credentialExchangeManager) private var credentialExchangeManager

    var body: some View {
        Button("Export Credentials") {
            Task {
                do {
                    let credentialData = getCredentialData() // defined elsewhere
                    try await credentialExchangeManager.exportCredentials(credentialData)
                } catch {
                    // code to handle the export error
                }
            }
        }
    }
}
```
