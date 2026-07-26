---
title: 'insertDictationResult(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.1+, iPadOS 5.1+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/insertdictationresult(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/insertdictationresult(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/insertdictationresult%28_%3A%29.json'
content_hash: 'sha256:61be4506d69dda0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# insertDictationResult(_:)

<sub>Instance Method</sub>

Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func insertDictationResult(_ dictationResult: [UIDictationPhrase])
```

## Parameters

- `dictationResult` — An array of [UIDictationPhrase](../uidictationphrase.md) objects.

## Discussion

Implement this optional method if you want to support dictation phrase alternatives. If you do not implement this method, iOS inserts the most likely interpretation of the dictated phrase.

> [!important] Important
> This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [- dictationRecordingDidEnd](<dictationrecordingdidend().md>) and [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) to implement a custom placeholder.

## See Also

### Using dictation

- [- dictationRecordingDidEnd](<dictationrecordingdidend().md>) — Tells the object when there is a pending dictation result.
- [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) — Tells the object when dictation ends, but recognition fails.
- [insertDictationResultPlaceholder](insertdictationresultplaceholder.md) — Asks for the placeholder object to use while generating dictation results.
- [- frameForDictationResultPlaceholder:](<frame(fordictationresultplaceholder_).md>) — Asks for the rectangle for displaying the dictation placeholder animation.
- [- removeDictationResultPlaceholder:willInsertResult:](<removedictationresultplaceholder(__willinsertresult_).md>) — Tells the view that the specified placeholder object is unnecessary.
