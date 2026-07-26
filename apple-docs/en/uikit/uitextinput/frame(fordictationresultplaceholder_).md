---
title: 'frame(forDictationResultPlaceholder:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/frame(fordictationresultplaceholder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/frame(fordictationresultplaceholder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/frame%28fordictationresultplaceholder%3A%29.json'
content_hash: 'sha256:516f47558307e801'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# frame(forDictationResultPlaceholder:)

<sub>Instance Method</sub>

Asks for the rectangle for displaying the dictation placeholder animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func frame(forDictationResultPlaceholder placeholder: Any) -> CGRect
```

## Parameters

- `placeholder` — A placeholder object provided by your app and used to identify the location of the dictation results.

## Return Value

The rectangle, in the coordinate system of your input view, at which to display the dictation placeholder animation.

## Discussion

While dictation results are being generated, UIKit displays the built-in dictation placeholder animation. Your implementation of this method should provide the rectangle at which to display this animation (at the location where the dictation results will be inserted).

> [!important] Important
> This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [- dictationRecordingDidEnd](<dictationrecordingdidend().md>) and [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) to implement a custom placeholder.

## See Also

### Using dictation

- [- dictationRecordingDidEnd](<dictationrecordingdidend().md>) — Tells the object when there is a pending dictation result.
- [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) — Tells the object when dictation ends, but recognition fails.
- [- insertDictationResult:](<insertdictationresult(__).md>) — Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [insertDictationResultPlaceholder](insertdictationresultplaceholder.md) — Asks for the placeholder object to use while generating dictation results.
- [- removeDictationResultPlaceholder:willInsertResult:](<removedictationresultplaceholder(__willinsertresult_).md>) — Tells the view that the specified placeholder object is unnecessary.
