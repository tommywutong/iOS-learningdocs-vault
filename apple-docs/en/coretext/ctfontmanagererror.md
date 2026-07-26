---
title: CTFontManagerError
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontmanagererror
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagererror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagererror.json'
content_hash: 'sha256:638a75399b20ffcb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerError

<sub>Enumeration</sub>

Errors that prevent unregistration of fonts for a specified font file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFontManagerError
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCTFontManagerErrorFileNotFound](ctfontmanagererror/filenotfound.md) — An error that indicates the file doesn’t exist at the specified URL.
- [kCTFontManagerErrorInsufficientPermissions](ctfontmanagererror/insufficientpermissions.md) — An error that indicates insufficient permissions to access the file.
- [kCTFontManagerErrorUnrecognizedFormat](ctfontmanagererror/unrecognizedformat.md) — An error that indicates the file’s format is unrecognized or unsupported.
- [kCTFontManagerErrorInvalidFontData](ctfontmanagererror/invalidfontdata.md) — An error that indicates the file contains invalid font data that could cause system problems.
- [kCTFontManagerErrorAlreadyRegistered](ctfontmanagererror/alreadyregistered.md) — An error that indicates the file is already registered in the specified scope.
- [kCTFontManagerErrorExceededResourceLimit](ctfontmanagererror/exceededresourcelimit.md) — An error that indicates an operation failure due to a system limitation.
- [kCTFontManagerErrorAssetNotFound](ctfontmanagererror/assetnotfound.md) — An error that indicates the asset isn’t found.
- [kCTFontManagerErrorNotRegistered](ctfontmanagererror/notregistered.md) — An error that indicates the file isn’t registered in the specified scope.
- [kCTFontManagerErrorInUse](ctfontmanagererror/inuse.md) — An error that indicates the font file is actively in use and can’t be unregistered.
- [kCTFontManagerErrorSystemRequired](ctfontmanagererror/systemrequired.md) — An error that indicates the file is required by the system and can’t be unregistered.
- [kCTFontManagerErrorRegistrationFailed](ctfontmanagererror/registrationfailed.md) — An error that indicates the file can’t be processed due to an unexpected FontProvider error.
- [kCTFontManagerErrorMissingEntitlement](ctfontmanagererror/missingentitlement.md) — An error that indicates the file can’t be processed because the provider doesn’t have a necessary entitlement.
- [kCTFontManagerErrorInsufficientInfo](ctfontmanagererror/insufficientinfo.md) — An error that indicates the font descriptor doesn’t have the necessary information to specify a font file.
- [kCTFontManagerErrorCancelledByUser](ctfontmanagererror/cancelledbyuser.md) — An error that indicates the user cancelled the operation.
- [kCTFontManagerErrorDuplicatedName](ctfontmanagererror/duplicatedname.md) — An error that indicates the file can’t register because of a duplicate font name.
- [kCTFontManagerErrorInvalidFilePath](ctfontmanagererror/invalidfilepath.md) — An error that indicates the file isn’t in an allowed location, which must be either in the app’s bundle or an on-demand resource.
- [kCTFontManagerErrorUnsupportedScope](ctfontmanagererror/unsupportedscope.md) — An error that indicates the specified scope isn’t supported.

### Initializers

- [init(rawValue:)](<ctfontmanagererror/init(rawvalue_).md>)

## See Also

### Enumerations

- [CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md) — Constants that track the progress of font descriptor matching.
- [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) — Sets the auto-activation for the specified bundle identifier.
- [CTFontManagerScope](ctfontmanagerscope.md) — Constants that define the scope for font registration.
- [CTLineBoundsOptions](ctlineboundsoptions.md) — Options for getting the bounds of a line of text.
- [CTRubyAlignment](ctrubyalignment.md) — Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [CTRubyOverhang](ctrubyoverhang.md) — Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [CTRubyPosition](ctrubyposition.md) — Constants that specify the position of the ruby text relative to to the base text.
