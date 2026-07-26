---
title: PHLivePhotoEditingErrorDomain
framework: Photos
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.12+（10.15 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/photos/phlivephotoeditingerrordomain
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingerrordomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingerrordomain.json'
content_hash: 'sha256:1c467455e388bac2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoEditingErrorDomain

<sub>Global Variable</sub>

The domain value for error objects produced by a Live Photo editing context.

<sub>macOS</sub>

```swift
let PHLivePhotoEditingErrorDomain: String
```

## Discussion

This domain appears for errors in the completion handlers of the [- initWithLivePhotoEditingInput:](<phlivephotoeditingcontext/init(livephotoeditinginput_).md>) and [- saveLivePhotoToOutput:options:completionHandler:](<phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) methods.

## See Also

### Errors

- [PHLivePhotoEditingErrorCode](phlivephotoeditingerrorcode.md) — Error codes for Live Photo editing errors.
