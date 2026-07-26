---
title: shouldMoveFile
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcecreationoptions/shouldmovefile
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcecreationoptions/shouldmovefile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcecreationoptions/shouldmovefile.json'
content_hash: 'sha256:ef1db7c431f6e441'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceCreationOptions](../phassetresourcecreationoptions.md)

# shouldMoveFile

<sub>Instance Property</sub>

A Boolean value that determines whether Photos moves or duplicates files when creating an asset resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var shouldMoveFile: Bool { get set }
```

## Discussion

This property applies only when creating an asset resource with the [- addResourceWithType:fileURL:options:](<../phassetcreationrequest/addresource(with_fileurl_options_).md>) method. If this value is `true`, Photos moves the specified file into the Photos library to create the asset resource, removing the original file after the asset has been successfully created. When using this option, Photos does not make an intermediary copy of the resource data, so no additional storage space is required.

If this value is `false` (the default), Photos copies the contents of the original file into the Photos library.

> [!note] Note
> Attempting to move a file that is currently open or has hard links fails.
