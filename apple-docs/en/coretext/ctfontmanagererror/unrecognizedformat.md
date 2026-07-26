---
title: CTFontManagerError.unrecognizedFormat
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagererror/unrecognizedformat
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagererror/unrecognizedformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagererror/unrecognizedformat.json'
content_hash: 'sha256:046d9876827dab1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontManagerError](../ctfontmanagererror.md)

# CTFontManagerError.unrecognizedFormat

<sub>Case</sub>

An error that indicates the file’s format is unrecognized or unsupported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case unrecognizedFormat
```

## See Also

### Constants

- [kCTFontManagerErrorFileNotFound](filenotfound.md) — An error that indicates the file doesn’t exist at the specified URL.
- [kCTFontManagerErrorInsufficientPermissions](insufficientpermissions.md) — An error that indicates insufficient permissions to access the file.
- [kCTFontManagerErrorInvalidFontData](invalidfontdata.md) — An error that indicates the file contains invalid font data that could cause system problems.
- [kCTFontManagerErrorAlreadyRegistered](alreadyregistered.md) — An error that indicates the file is already registered in the specified scope.
- [kCTFontManagerErrorExceededResourceLimit](exceededresourcelimit.md) — An error that indicates an operation failure due to a system limitation.
- [kCTFontManagerErrorAssetNotFound](assetnotfound.md) — An error that indicates the asset isn’t found.
- [kCTFontManagerErrorNotRegistered](notregistered.md) — An error that indicates the file isn’t registered in the specified scope.
- [kCTFontManagerErrorInUse](inuse.md) — An error that indicates the font file is actively in use and can’t be unregistered.
- [kCTFontManagerErrorSystemRequired](systemrequired.md) — An error that indicates the file is required by the system and can’t be unregistered.
- [kCTFontManagerErrorRegistrationFailed](registrationfailed.md) — An error that indicates the file can’t be processed due to an unexpected FontProvider error.
- [kCTFontManagerErrorMissingEntitlement](missingentitlement.md) — An error that indicates the file can’t be processed because the provider doesn’t have a necessary entitlement.
- [kCTFontManagerErrorInsufficientInfo](insufficientinfo.md) — An error that indicates the font descriptor doesn’t have the necessary information to specify a font file.
- [kCTFontManagerErrorCancelledByUser](cancelledbyuser.md) — An error that indicates the user cancelled the operation.
- [kCTFontManagerErrorDuplicatedName](duplicatedname.md) — An error that indicates the file can’t register because of a duplicate font name.
- [kCTFontManagerErrorInvalidFilePath](invalidfilepath.md) — An error that indicates the file isn’t in an allowed location, which must be either in the app’s bundle or an on-demand resource.
