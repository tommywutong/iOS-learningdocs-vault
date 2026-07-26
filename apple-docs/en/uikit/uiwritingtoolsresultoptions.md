---
title: UIWritingToolsResultOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolsresultoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolsresultoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolsresultoptions.json'
content_hash: 'sha256:2901ff342d4b8f3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWritingToolsResultOptions

<sub>Structure</sub>

Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIWritingToolsResultOptions
```

## Overview

When configuring a text view, specify what type of text input you want Writing Tools to deliver to your view. You can ask it to return plain text without any attributes, or you can ask it to apply relevant formatting attributes to the text. You can even encourage it to return items in a list or format them in a table.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting the output options

- [UIWritingToolsResultPlainText](uiwritingtoolsresultoptions/plaintext.md) — An option to allow only plain text without any attributes in the returned text.
- [UIWritingToolsResultRichText](uiwritingtoolsresultoptions/richtext.md) — An option to include style attributes consistent with the RTF format in the returned text.
- [UIWritingToolsResultList](uiwritingtoolsresultoptions/list.md) — An option to allow list-style formatting in the returned text.
- [UIWritingToolsResultTable](uiwritingtoolsresultoptions/table.md) — An option to allow tabular layout attributes in the returned text.

### Initializers

- [init(rawValue:)](<uiwritingtoolsresultoptions/init(rawvalue_).md>)

### Type Properties

- [UIWritingToolsResultPresentationIntent](uiwritingtoolsresultoptions/presentationintent.md) — implies `RichText`, `List`, and `Table`, and Writing Tools may provide text with presentation intent attributes. Writing Tools will use `NSPresentationIntent` instead of `NSTextList` and `NSTextTable` to represent lists and tables.

## See Also

### Configuration

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md) — Modify the behavior of Writing Tools in standard iOS text views, and adjust your app’s behavior while the feature is active.
- [UIWritingToolsBehavior](uiwritingtoolsbehavior.md) — Constants that specify the writing tools experience for the underlying view.
