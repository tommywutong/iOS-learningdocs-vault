---
title: PHLivePhotoEditingErrorCode
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.12+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingerrorcode
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingerrorcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingerrorcode.json'
content_hash: 'sha256:d9389610372385a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoEditingErrorCode

<sub>Enumeration</sub>

Error codes for Live Photo editing errors.

<sub>macOS</sub>

```swift
enum PHLivePhotoEditingErrorCode
```

## Overview

These error codes appear for errors in the completion handlers of the [- initWithLivePhotoEditingInput:](<phlivephotoeditingcontext/init(livephotoeditinginput_).md>) and [- saveLivePhotoToOutput:options:completionHandler:](<phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) methods.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHLivePhotoEditingErrorCodeUnknown](phlivephotoeditingerrorcode/unknown.md) — No further information is available about the cause of the error. _(deprecated)_
- [PHLivePhotoEditingErrorCodeAborted](phlivephotoeditingerrorcode/aborted.md) — Live Photo processing was canceled by the Processing an Editing Context’s Live Photo method. _(deprecated)_

### Initializers

- [init(rawValue:)](<phlivephotoeditingerrorcode/init(rawvalue_).md>)

## See Also

### Errors

- [PHLivePhotoEditingErrorDomain](phlivephotoeditingerrordomain.md) — The domain value for error objects produced by a Live Photo editing context. _(deprecated)_
