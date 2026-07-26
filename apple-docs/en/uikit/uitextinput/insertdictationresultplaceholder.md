---
title: insertDictationResultPlaceholder
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/insertdictationresultplaceholder
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/insertdictationresultplaceholder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/insertdictationresultplaceholder.json'
content_hash: 'sha256:5d583bd1abd7f0e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# insertDictationResultPlaceholder

<sub>Instance Property</sub>

Asks for the placeholder object to use while generating dictation results.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var insertDictationResultPlaceholder: Any { get }
```

## Return Value

A placeholder object to use to identify the dictation results. This value must not be `nil`.

## Discussion

Implementation of this method is optional but can be done when you want to provide a specific rectangle for the placeholder animation while the dictation results are being processed. The object you return from this method is passed to the [- frameForDictationResultPlaceholder:](<frame(fordictationresultplaceholder_).md>) method later. The actual contents of the object are not accessed by UIKit but you can use the object to store whatever information you need to identify the location for the animation.

UIKit maintains a strong reference to your placeholder object until the [- removeDictationResultPlaceholder:willInsertResult:](<removedictationresultplaceholder(__willinsertresult_).md>) method is called. You must implement both this method and the [- removeDictationResultPlaceholder:willInsertResult:](<removedictationresultplaceholder(__willinsertresult_).md>) method for placeholders to be used.

## See Also

### Using dictation

- [- dictationRecordingDidEnd](<dictationrecordingdidend().md>) — Tells the object when there is a pending dictation result.
- [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) — Tells the object when dictation ends, but recognition fails.
- [- insertDictationResult:](<insertdictationresult(__).md>) — Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [- frameForDictationResultPlaceholder:](<frame(fordictationresultplaceholder_).md>) — Asks for the rectangle for displaying the dictation placeholder animation.
- [- removeDictationResultPlaceholder:willInsertResult:](<removedictationresultplaceholder(__willinsertresult_).md>) — Tells the view that the specified placeholder object is unnecessary.
