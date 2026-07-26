---
title: CGError.invalidConnection
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgerror/invalidconnection
source_url: 'https://developer.apple.com/documentation/coregraphics/cgerror/invalidconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgerror/invalidconnection.json'
content_hash: 'sha256:fc4166d9d7f781fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGError](../cgerror.md)

# CGError.invalidConnection

<sub>Case</sub>

The parameter representing a connection to the window server is invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case invalidConnection
```

## See Also

### Constants

- [kCGErrorCannotComplete](cannotcomplete.md) — The requested operation is inappropriate for the parameters passed in, or the current system state.
- [kCGErrorFailure](failure.md) — A general failure occurred.
- [kCGErrorIllegalArgument](illegalargument.md) — One or more of the parameters passed to a function are invalid. Check for `NULL` pointers.
- [kCGErrorInvalidContext](invalidcontext.md) — The `CPSProcessSerNum` or context identifier parameter is not valid.
- [kCGErrorInvalidOperation](invalidoperation.md) — The requested operation is not valid for the parameters passed in, or the current system state.
- [kCGErrorNoneAvailable](noneavailable.md) — The requested operation could not be completed as the indicated resources were not found.
- [kCGErrorNotImplemented](notimplemented.md) — Return value from obsolete function stubs present for binary compatibility, but not typically called.
- [kCGErrorRangeCheck](rangecheck.md) — A parameter passed in has a value that is inappropriate, or which does not map to a useful operation or value.
- [kCGErrorSuccess](success.md) — The requested operation was completed successfully.
- [kCGErrorTypeCheck](typecheck.md) — A data type or token was encountered that did not match the expected type or token.
