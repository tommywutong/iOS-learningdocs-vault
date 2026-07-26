---
title: fileModificationDate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/filemodificationdate
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/filemodificationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/filemodificationdate.json'
content_hash: 'sha256:c6a349fbe1c70208'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# fileModificationDate

<sub>Instance Property</sub>

The date and time your app last modified the document file.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var fileModificationDate: Date? { get set }
```

## Discussion

The modification date is updated by the [- openWithCompletionHandler:](<open(completionhandler_).md>), [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>), and [- revertToContentsOfURL:completionHandler:](<revert(tocontentsof_completionhandler_).md>) methods. Its value is `nil` if none of these methods has completed successfully at least once. If you override any of these methods, you should be sure to set this property in your implementation.

UIKit sets this property before it calls the completion handlers of the [- openWithCompletionHandler:](<open(completionhandler_).md>), [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>), and [- revertToContentsOfURL:completionHandler:](<revert(tocontentsof_completionhandler_).md>). If, outside of these methods or their completion handlers, you want to wait for any pending file operations to complete before you access this property, you can call [- performAsynchronousFileAccessUsingBlock:](<performasynchronousfileaccess(__).md>) and access the property value in the block parameter.

> [!important] Important
> This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [Describing use of required reason API](../../bundleresources/describing-use-of-required-reason-api.md).

## See Also

### Accessing document attributes

- [fileURL](fileurl.md) — The file URL you use to initialize the document.
- [localizedName](localizedname.md) — The localized name of the document.
- [fileType](filetype.md) — The file type of the document.
- [documentState](documentstate.md) — The current state of the document.
- [progress](progress.md) — The upload or download progress of a document.
