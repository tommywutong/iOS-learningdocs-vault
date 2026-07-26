---
title: UIAccessibilityTextualContext
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitytextualcontext
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitytextualcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitytextualcontext.json'
content_hash: 'sha256:353ce6a355ec1dee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityTextualContext

<sub>Structure</sub>

Constants that describe a named context that helps identify and classify the type of text inside an element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct UIAccessibilityTextualContext
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIAccessibilityTextualContextConsole](uiaccessibilitytextualcontext/console.md) — A constant that indicates the text appears in a console context.
- [UIAccessibilityTextualContextFileSystem](uiaccessibilitytextualcontext/filesystem.md) — A constant that indicates the text appears in a file-system context.
- [UIAccessibilityTextualContextMessaging](uiaccessibilitytextualcontext/messaging.md) — A constant that indicates the text appears in a messaging context.
- [UIAccessibilityTextualContextNarrative](uiaccessibilitytextualcontext/narrative.md) — A constant that indicates the text appears in a narrative speech context.
- [UIAccessibilityTextualContextSourceCode](uiaccessibilitytextualcontext/sourcecode.md) — A constant that indicates the text appears in a source-code context.
- [UIAccessibilityTextualContextSpreadsheet](uiaccessibilitytextualcontext/spreadsheet.md) — A constant that indicates the text appears in a spreadsheet context.
- [UIAccessibilityTextualContextWordProcessing](uiaccessibilitytextualcontext/wordprocessing.md) — A constant that indicates the text appears in a word-processing context.

### Initializers

- [init(_:)](<uiaccessibilitytextualcontext/init(__).md>) — Creates a textual context.
- [init(rawValue:)](<uiaccessibilitytextualcontext/init(rawvalue_).md>) — Creates a textual context with the specified raw value.

## See Also

### Behaviors

- [UIAccessibilityFocus](../objectivec/uiaccessibilityfocus.md) — An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityIdentification](uiaccessibilityidentification.md) — Methods that associate a unique identifier with elements in your user interface.
- [UIAccessibilityReadingContent](uiaccessibilityreadingcontent.md) — Methods to implement for an object that represents content that users read, such as a book or an article.
- [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md) — Methods to determine when to adjust images for different content size categories.
