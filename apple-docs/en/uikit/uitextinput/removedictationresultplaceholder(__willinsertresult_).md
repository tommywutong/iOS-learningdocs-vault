---
title: 'removeDictationResultPlaceholder(_:willInsertResult:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/removedictationresultplaceholder(_:willinsertresult:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/removedictationresultplaceholder(_:willinsertresult:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/removedictationresultplaceholder%28_%3Awillinsertresult%3A%29.json'
content_hash: 'sha256:3eca58e7f031b3d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# removeDictationResultPlaceholder(_:willInsertResult:)

<sub>Instance Method</sub>

Tells the view that the specified placeholder object is unnecessary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func removeDictationResultPlaceholder(_ placeholder: Any, willInsertResult: Bool)
```

## Parameters

- `placeholder` — The placeholder object that is no longer needed.

- `willInsertResult` — The value of this parameter is [true](../../swift/true.md) if the dictation value was generated successfully or [false](../../swift/false.md) if an error occurred.

## Discussion

If the value in the `willInsertResult` parameter is [false](../../swift/false.md), the placeholder animation is not replaced by an actual dictation result. When this happens, the system still removes the placeholder animation and removes the strong reference to your placeholder object.

> [!important] Important
> This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [- dictationRecordingDidEnd](<dictationrecordingdidend().md>) and [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) to implement a custom placeholder.

## See Also

### Using dictation

- [- dictationRecordingDidEnd](<dictationrecordingdidend().md>) — Tells the object when there is a pending dictation result.
- [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) — Tells the object when dictation ends, but recognition fails.
- [- insertDictationResult:](<insertdictationresult(__).md>) — Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [insertDictationResultPlaceholder](insertdictationresultplaceholder.md) — Asks for the placeholder object to use while generating dictation results.
- [- frameForDictationResultPlaceholder:](<frame(fordictationresultplaceholder_).md>) — Asks for the rectangle for displaying the dictation placeholder animation.
