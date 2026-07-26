---
title: Building rich SwiftUI text experiences
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, Xcode 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/building-rich-swiftui-text-experiences
source_url: 'https://developer.apple.com/documentation/swiftui/building-rich-swiftui-text-experiences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/building-rich-swiftui-text-experiences.json'
content_hash: 'sha256:d824db1162d714c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Text input and output](text-input-and-output.md)

# Building rich SwiftUI text experiences

<sub>Sample Code</sub>

Build an editor for formatted text using SwiftUI text editor views and attributed strings.

## Overview

> [!note] Note
> This sample code project is associated with WWDC25 session 280: [Code-along: Cook up a rich text experience in SwiftUI with AttributedString](https://developer.apple.com/wwdc25/280/).

You can follow along with the code written in the WWDC25 session, learning how to upgrade `TextEditor` to rich text, build custom controls, and constrain the formatting options the editor provides.

After the code-along, you can learn more about how to persist rich text using SwiftData, and how to export rich text documents using the `Transferable` protocol.

### Configure the sample code project

To configure the sample code project, do the following in Xcode:

1. Open the sample with the latest version of Xcode.
2. Set the developer team to let Xcode automatically manage the provisioning profile. For more information, see [Set the bundle ID](../xcode/preparing-your-app-for-distribution.md#Set-the-bundle-ID) and [Assign the project to a team](../xcode/preparing-your-app-for-distribution.md#Assign-the-project-to-a-team).

## See Also

### Getting text input

- [TextField](textfield.md) — A control that displays an editable text interface.
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — Sets the style for text fields within this view.
- [SecureField](securefield.md) — A control into which people securely enter private text.
- [TextEditor](texteditor.md) — A view that can display and edit long-form text.

## Download

- [BuildingRichSwiftUITextExperiences.zip](https://docs-assets.developer.apple.com/published/af5124237a05/BuildingRichSwiftUITextExperiences.zip)
