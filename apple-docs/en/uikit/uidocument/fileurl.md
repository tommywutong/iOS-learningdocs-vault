---
title: fileURL
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/fileurl
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/fileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/fileurl.json'
content_hash: 'sha256:2d8c44fcab0474f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# fileURL

<sub>Instance Property</sub>

The file URL you use to initialize the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var fileURL: URL { get }
```

## Discussion

The URL identifies the location of the document in the application sandbox. It includes the file extension, from which the file type is determined.

UIKit sets this property before it calls the completion handlers of the [- openWithCompletionHandler:](<open(completionhandler_).md>), [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>), and [- revertToContentsOfURL:completionHandler:](<revert(tocontentsof_completionhandler_).md>). If, outside of these methods or their completion handlers, you want to wait for any pending file operations to complete before you access this property, you can call [- performAsynchronousFileAccessUsingBlock:](<performasynchronousfileaccess(__).md>) and access the property value in the block parameter.

## See Also

### Related Documentation

- [- initWithFileURL:](<init(fileurl_).md>) — Returns a document object initialized with its file-system location.

### Accessing document attributes

- [localizedName](localizedname.md) — The localized name of the document.
- [fileType](filetype.md) — The file type of the document.
- [fileModificationDate](filemodificationdate.md) — The date and time your app last modified the document file.
- [documentState](documentstate.md) — The current state of the document.
- [progress](progress.md) — The upload or download progress of a document.
