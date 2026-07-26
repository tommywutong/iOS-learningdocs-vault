---
title: 'requestSupplementaryLexicon(completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiinputviewcontroller/requestsupplementarylexicon(completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewcontroller/requestsupplementarylexicon(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewcontroller/requestsupplementarylexicon%28completion%3A%29.json'
content_hash: 'sha256:e4ec63bf8a84c337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewController](../uiinputviewcontroller.md)

# requestSupplementaryLexicon(completion:)

<sub>Instance Method</sub>

Obtains a supplementary lexicon of term pairs in a custom keyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestSupplementaryLexicon(completion completionHandler: @escaping (UILexicon) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestSupplementaryLexicon() async -> UILexicon
```

## Parameters

- `completionHandler` — Code that you write to make use of the returned `UILexicon` object.

## Discussion

Call this method to obtain a [UILexicon](../uilexicon.md) object containing a basic set of term pairs for use in autocorrection or textual suggestions based on user input. The [UILexicon](../uilexicon.md) object contains words from various sources, including:

- Unpaired first names and last names from the user’s Address Book database
- Text shortcuts defined in the Settings \> General \> Keyboard \> Shortcuts list
- A common words dictionary

Consider this lexicon as a supplement to a more complete lexicon of your own design.
