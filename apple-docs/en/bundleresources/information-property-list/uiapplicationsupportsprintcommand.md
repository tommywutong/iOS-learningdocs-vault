---
title: UIApplicationSupportsPrintCommand
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/uiapplicationsupportsprintcommand
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationsupportsprintcommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/uiapplicationsupportsprintcommand.json'
content_hash: 'sha256:e7c0a08b5a84b46a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# UIApplicationSupportsPrintCommand

<sub>Property List Key</sub>

A Boolean value that indicates whether the app supports the Command-P keyboard shortcut.

## Discussion

When the value for this key is `YES`, the system adds the Command-P keyboard shortcut to the app. When someone enters Command-P while using the app, the system calls the [printContent(_:)](<../../uikit/uiresponderstandardeditactions/printcontent(__).md>) method on the first responder that implements the method found in the responder chain.

An iPad app running in iPadOS shows a Print command in the discoverability HUD when the value for the [UIApplicationSupportsPrintCommand](uiapplicationsupportsprintcommand.md) key is `YES`. When the same app runs on a Mac with Apple silicon, the system adds Print and Export to PDF menu commands to the File menu.

When an app built with Mac Catalyst includes the [UIApplicationSupportsPrintCommand](uiapplicationsupportsprintcommand.md) key with a value of `YES`, the system adds the Print and Export to PDF commands to the File menu. However, the app must also include the [com.apple.security.print](../entitlements/com.apple.security.print.md) and [com.apple.security.files.user-selected.read-write](../entitlements/com.apple.security.files.user-selected.read-write.md) App Sandbox entitlements to make printing and exporting content available to the app when running in macOS.

## See Also

### External accessories

- [UISupportedExternalAccessoryProtocols](uisupportedexternalaccessoryprotocols.md) — The protocols that the app uses to communicate with external accessory hardware.
