---
title: NSExceptionName
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexceptionname
source_url: 'https://developer.apple.com/documentation/foundation/nsexceptionname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexceptionname.json'
content_hash: 'sha256:134bc7241b2538d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExceptionName

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSExceptionName
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSCharacterConversionException](nsexceptionname/characterconversionexception.md) — `NSString` raises an `NSCharacterConversionException` if a string cannot be represented in a file-system or string encoding.
- [NSDecimalNumberDivideByZeroException](nsexceptionname/decimalnumberdividebyzeroexception.md) — The exception raised on divide by zero.
- [NSDecimalNumberExactnessException](nsexceptionname/decimalnumberexactnessexception.md) — The exception raised if there is an exactness error.
- [NSDecimalNumberOverflowException](nsexceptionname/decimalnumberoverflowexception.md) — The exception raised on overflow.
- [NSDecimalNumberUnderflowException](nsexceptionname/decimalnumberunderflowexception.md) — The exception raised on underflow.
- [NSDestinationInvalidException](nsexceptionname/destinationinvalidexception.md) — Name of an exception that occurs when an internal assertion fails and implies an unexpected condition within the distributed objects.
- [NSFileHandleOperationException](nsexceptionname/filehandleoperationexception.md) — Raised by `NSFileHandle` if attempts to determine file-handle type fail or if attempts to read from a file or channel fail.
- [NSGenericException](nsexceptionname/genericexception.md) — A generic name for an exception.
- [NSInternalInconsistencyException](nsexceptionname/internalinconsistencyexception.md) — Name of an exception that occurs when an internal assertion fails and implies an unexpected condition within the called code.
- [NSInvalidArchiveOperationException](nsexceptionname/invalidarchiveoperationexception.md) — The name of the exception raised by `NSKeyedArchiver` if there is a problem creating an archive.
- [NSInvalidArgumentException](nsexceptionname/invalidargumentexception.md) — Name of an exception that occurs when you pass an invalid argument to a method, such as a `nil` pointer where a non-`nil` object is required.
- [NSInvalidReceivePortException](nsexceptionname/invalidreceiveportexception.md) — Name of an exception that occurs when the receive port of an `NSConnection` has become invalid.
- [NSInvalidSendPortException](nsexceptionname/invalidsendportexception.md) — Name of an exception that occurs when the send port of an `NSConnection` has become invalid.
- [NSInvalidUnarchiveOperationException](nsexceptionname/invalidunarchiveoperationexception.md) — The name of the exception raised by `NSKeyedArchiver` if there is a problem extracting an archive.
- [NSInvocationOperationCancelledException](nsexceptionname/invocationoperationcancelledexception.md) — The name of the exception raised if the [result](nsinvocationoperation/result.md) method is called after the operation was cancelled.
- [NSInvocationOperationVoidResultException](nsexceptionname/invocationoperationvoidresultexception.md) — The name of the exception raised if the [result](nsinvocationoperation/result.md) method is called for an invocation method with a `void` return type.
- [NSMallocException](nsexceptionname/mallocexception.md) — Obsolete; not currently used.
- [NSObjectInaccessibleException](nsexceptionname/objectinaccessibleexception.md) — Name of an exception that occurs when a remote object is accessed from a thread that should not access it.
- [NSObjectNotAvailableException](nsexceptionname/objectnotavailableexception.md) — Name of an exception that occurs when the remote side of the `NSConnection` refused to send the message to the object because the object has never been vended.
- [NSOldStyleException](nsexceptionname/oldstyleexception.md) — No longer used.
- [NSParseErrorException](nsexceptionname/parseerrorexception.md) — `NSString` raises an `NSParseErrorException` if a string cannot be parsed as a property list.
- [NSPortReceiveException](nsexceptionname/portreceiveexception.md) — Generic error occurred on receive.
- [NSPortSendException](nsexceptionname/portsendexception.md) — Generic error occurred on send.
- [NSPortTimeoutException](nsexceptionname/porttimeoutexception.md) — Name of an exception that occurs when a timeout set on a port expires during a send or receive operation.
- [NSRangeException](nsexceptionname/rangeexception.md) — Name of an exception that occurs when attempting to access outside the bounds of some data, such as beyond the end of a string.
- [NSUndefinedKeyException](nsexceptionname/undefinedkeyexception.md) — Raised when a key value coding operation fails.
- [NSInconsistentArchiveException](nsexceptionname/inconsistentarchiveexception.md) — The name of an exception raised by [NSArchiver](nsarchiver.md) if there are problems initializing or encoding.
- [NSPPDIncludeNotFoundException](nsexceptionname/nsppdincludenotfoundexception.md)
- [NSPPDIncludeStackOverflowException](nsexceptionname/nsppdincludestackoverflowexception.md)
- [NSPPDIncludeStackUnderflowException](nsexceptionname/nsppdincludestackunderflowexception.md)
- [NSPPDParseException](nsexceptionname/nsppdparseexception.md)
- [NSRTFPropertyStackOverflowException](nsexceptionname/nsrtfpropertystackoverflowexception.md)
- [NSTIFFException](nsexceptionname/nstiffexception.md)
- [abortModalException](nsexceptionname/abortmodalexception.md)
- [abortPrintingException](nsexceptionname/abortprintingexception.md)
- [accessibilityException](nsexceptionname/accessibilityexception.md) _(deprecated)_
- [appKitIgnoredException](nsexceptionname/appkitignoredexception.md)
- [appKitVirtualMemoryException](nsexceptionname/appkitvirtualmemoryexception.md)
- [badBitmapParametersException](nsexceptionname/badbitmapparametersexception.md)
- [badComparisonException](nsexceptionname/badcomparisonexception.md)
- [badRTFColorTableException](nsexceptionname/badrtfcolortableexception.md)
- [badRTFDirectiveException](nsexceptionname/badrtfdirectiveexception.md)
- [badRTFFontTableException](nsexceptionname/badrtffonttableexception.md)
- [badRTFStyleSheetException](nsexceptionname/badrtfstylesheetexception.md)
- [browserIllegalDelegateException](nsexceptionname/browserillegaldelegateexception.md)
- [colorListIOException](nsexceptionname/colorlistioexception.md)
- [colorListNotEditableException](nsexceptionname/colorlistnoteditableexception.md)
- [draggingException](nsexceptionname/draggingexception.md)
- [fontUnavailableException](nsexceptionname/fontunavailableexception.md)
- [illegalSelectorException](nsexceptionname/illegalselectorexception.md)
- [imageCacheException](nsexceptionname/imagecacheexception.md)
- [nibLoadingException](nsexceptionname/nibloadingexception.md)
- [pasteboardCommunicationException](nsexceptionname/pasteboardcommunicationexception.md)
- [printOperationExistsException](nsexceptionname/printoperationexistsexception.md) — The name of an exception raised when there is already a print operation in process.
- [printPackageException](nsexceptionname/printpackageexception.md)
- [printingCommunicationException](nsexceptionname/printingcommunicationexception.md)
- [textLineTooLongException](nsexceptionname/textlinetoolongexception.md) — Exception generated if a line is too long in a `NSText` object.
- [textNoSelectionException](nsexceptionname/textnoselectionexception.md)
- [textReadException](nsexceptionname/textreadexception.md)
- [textWriteException](nsexceptionname/textwriteexception.md)
- [typedStreamVersionException](nsexceptionname/typedstreamversionexception.md)
- [windowServerCommunicationException](nsexceptionname/windowservercommunicationexception.md)
- [wordTablesReadException](nsexceptionname/wordtablesreadexception.md)
- [wordTablesWriteException](nsexceptionname/wordtableswriteexception.md)
- [hierarchyInconsistencyException](../uikit/uiviewcontroller/hierarchyinconsistencyexception.md) — Raised if the view controller hierarchy is inconsistent with the view hierarchy.
- [invalidInterfaceOrientationException](../uikit/uiapplication/invalidinterfaceorientationexception.md) — An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.

### Initializers

- [init(_:)](<nsexceptionname/init(__).md>)
- [init(rawValue:)](<nsexceptionname/init(rawvalue_).md>)

## See Also

### Related Types

- [NSUncaughtExceptionHandler](nsuncaughtexceptionhandler.md) — The type for uncaught exception handler functions.
