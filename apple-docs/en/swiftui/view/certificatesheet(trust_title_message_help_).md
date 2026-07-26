---
title: 'certificateSheet(trust:title:message:help:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/certificatesheet(trust:title:message:help:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/certificatesheet(trust:title:message:help:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/certificatesheet%28trust%3Atitle%3Amessage%3Ahelp%3A%29.json'
content_hash: 'sha256:7f5361fc5e14339d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# certificateSheet(trust:title:message:help:)

<sub>Instance Method</sub>

Displays a certificate sheet using the provided certificate trust.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func certificateSheet(trust: Binding<SecTrust?>, title: String? = nil, message: String? = nil, help: URL? = nil) -> some View

```

## Parameters

- `trust` — A binding to a SecTrust reference created with SecTrustCreateWithCertificates (see \<Security/SecTrust.h\>) that determines whether to present the certificate sheet.

- `title` — The title to display. Uses a default title if nil.

- `message` — The message to display. Uses a default message if nil.

- `help` — URL for the “Learn More” button. Uses a default URL if nil.
