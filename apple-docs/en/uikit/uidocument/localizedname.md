---
title: localizedName
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/localizedname
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/localizedname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/localizedname.json'
content_hash: 'sha256:e1fbdf1ba4ce3500'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# localizedName

<sub>Instance Property</sub>

The localized name of the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var localizedName: String { get }
```

## Discussion

By default, UIKit obtains the value from the filename component of [fileURL](fileurl.md). You can override the getter accessor method of this property to provide a custom name for presentation to the user, such as in error strings. See [UIDocument](../uidocument.md) for overriding advice.

UIKit sets this property before it calls the completion handlers of the [- openWithCompletionHandler:](<open(completionhandler_).md>), [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>), and [- revertToContentsOfURL:completionHandler:](<revert(tocontentsof_completionhandler_).md>). If, outside of these methods or their completion handlers, you want to wait for any pending file operations to complete before you access this property, you can call [- performAsynchronousFileAccessUsingBlock:](<performasynchronousfileaccess(__).md>) and access the property value in the block parameter.

## See Also

### Accessing document attributes

- [fileURL](fileurl.md) — The file URL you use to initialize the document.
- [fileType](filetype.md) — The file type of the document.
- [fileModificationDate](filemodificationdate.md) — The date and time your app last modified the document file.
- [documentState](documentstate.md) — The current state of the document.
- [progress](progress.md) — The upload or download progress of a document.
