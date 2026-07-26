---
title: NSError
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror
source_url: 'https://developer.apple.com/documentation/foundation/nserror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror.json'
content_hash: 'sha256:8014a821b1114ab3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSError

<sub>Class</sub>

Information about an error condition including a domain, a domain-specific error code, and application-specific information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSError
```

## Overview

Objective-C methods can signal an error condition by returning an [NSError](nserror.md) object by reference, which provides additional information about the kind of error and any underlying cause, if one can be determined. An [NSError](nserror.md) object may also provide localized error descriptions suitable for display to the user in its user info dictionary. See [Error Handling Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/ErrorHandling/ErrorHandling.html#//apple_ref/doc/uid/TP40001806) for more information.

Methods in Foundation and other Cocoa frameworks most often produce errors in the Cocoa error domain ([NSCocoaErrorDomain](nscocoaerrordomain.md)); error codes for the Cocoa Error Domain are documented in the [Foundation Constants](foundation-constants.md). There are also predefined domains corresponding to Mach ([NSMachErrorDomain](nsmacherrordomain.md)), POSIX ([NSPOSIXErrorDomain](nsposixerrordomain.md)), and Carbon ([NSOSStatusErrorDomain](nsosstatuserrordomain.md)) errors.

[NSError](nserror.md) is “toll-free bridged” with its Core Foundation counterpart, [CFError](../corefoundation/cferror.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

### Subclassing Notes

Applications may choose to create subclasses of `NSError`, for example, to provide better localized error strings by overriding [localizedDescription](nserror/localizeddescription.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Error Objects

- [- initWithDomain:code:userInfo:](<nserror/init(domain_code_userinfo_).md>) — Returns an `NSError` object initialized for a given domain and code with a given `userInfo` dictionary.

### Getting Error Properties

- [code](nserror/code.md) — The error code.
- [domain](nserror/domain.md) — A string containing the error domain.
- [userInfo](nserror/userinfo.md) — The user info dictionary.

### Getting a Localized Error Description

- [localizedDescription](nserror/localizeddescription.md) — A string containing the localized description of the error.
- [localizedRecoveryOptions](nserror/localizedrecoveryoptions.md) — An array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [localizedRecoverySuggestion](nserror/localizedrecoverysuggestion.md) — A string containing the localized recovery suggestion for the error.
- [localizedFailureReason](nserror/localizedfailurereason.md) — A string containing the localized explanation of the reason for the error.

### Providing Error User Info

- [+ setUserInfoValueProviderForDomain:provider:](<nserror/setuserinfovalueprovider(fordomain_provider_).md>) — Specifies a block to call when the corresponding property is not present in the user info dictionary.
- [+ userInfoValueProviderForDomain:](<nserror/userinfovalueprovider(fordomain_).md>) — Returns any user info provider specified for a given error domain.
- [ErrorUserInfoKey](erroruserinfokey.md) — These keys may exist in the user info dictionary.
- [UserInfoKey](nserror/userinfokey.md) — These keys may exist in the user info dictionary.

### Getting the Error Recovery Attempter

- [recoveryAttempter](nserror/recoveryattempter.md) — The object in the user info dictionary corresponding to the [NSRecoveryAttempterErrorKey](nsrecoveryattemptererrorkey.md) key.
- [NSErrorRecoveryAttempting](nserrorrecoveryattempting.md) — A set of methods that provide options to recover from an error.

### Displaying a Help Anchor

- [helpAnchor](nserror/helpanchor.md) — A string to display in response to an alert panel help anchor button being pressed.

### Supporting Types

- [ErrorPointer](errorpointer.md)
- [NSErrorPointer](nserrorpointer.md)
- [NSErrorDomain](nserrordomain.md)

### Error Domains

- [NSCocoaErrorDomain](nscocoaerrordomain.md) — Cocoa errors
- [NSPOSIXErrorDomain](nsposixerrordomain.md) — POSIX/BSD errors
- [NSOSStatusErrorDomain](nsosstatuserrordomain.md) — Mac OS 9/Carbon errors
- [NSMachErrorDomain](nsmacherrordomain.md) — Mach errors
- [NSURLErrorDomain](nsurlerrordomain.md) — URL loading system errors
- [NSStreamSOCKSErrorDomain](nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.
- [NSStreamSocketSSLErrorDomain](nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.

### Error Codes

- [CocoaError](cocoaerror.md) — Describes errors within the Cocoa error domain.
- [MachError](macherror.md) — Describes an error in the Mach error domain.
- [POSIXError](posixerror.md) — Describes an error in the POSIX error domain.
- [NSError Codes](1448136-nserror-codes.md) — Error codes in the Cocoa error domain.

### Initializers

- [- init](<nserror/init().md>) _(deprecated)_
- [init(coder:)](<nserror/init(coder_).md>)

### Instance Properties

- [underlyingErrors](nserror/underlyingerrors.md)

### Type Methods

- [+ fileProviderErrorForCollisionWithItem:](<nserror/fileprovidererrorforcollision(with_).md>) — Returns a properly formatted error object with a `NSFileProviderItemCollisionError` error code.
- [+ fileProviderErrorForNonExistentItemWithIdentifier:](<nserror/fileprovidererrorfornonexistentitem(withidentifier_).md>)
- [+ fileProviderErrorForRejectedDeletionOfItem:](<nserror/fileprovidererrorforrejecteddeletion(of_).md>)
- [+ new](<nserror/new().md>) _(deprecated)_

## See Also

### User-Relevant Errors

- [Error](../swift/error.md) — A type representing an error value that can be thrown.
- [LocalizedError](localizederror.md) — A specialized error that provides localized messages describing the error and why it occurred.
- [RecoverableError](recoverableerror.md) — A specialized error that may be recoverable by presenting several potential recovery options to the user.
- [CustomNSError](customnserror.md) — A specialized error that provides a domain, error code, and user-info dictionary.
