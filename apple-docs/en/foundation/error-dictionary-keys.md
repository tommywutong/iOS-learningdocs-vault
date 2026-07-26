---
title: Error Dictionary Keys
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/error-dictionary-keys
source_url: 'https://developer.apple.com/documentation/foundation/error-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/error-dictionary-keys.json'
content_hash: 'sha256:73700e6e2a0b9b84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Scripting Support](scripting-support.md) · [NSAppleScript](nsapplescript.md)

# Error Dictionary Keys

<sub>API Collection</sub>

If the result of [- initWithContentsOfURL:error:](<nsapplescript/init(contentsof_error_).md>), [- compileAndReturnError:](<nsapplescript/compileandreturnerror(__).md>), [- executeAndReturnError:](<nsapplescript/executeandreturnerror(__).md>), or [- executeAppleEvent:error:](<nsapplescript/executeappleevent(__error_).md>), signals failure (`nil`, [false](../swift/false.md), `nil`, or `nil`, respectively), a pointer to an autoreleased dictionary is put at the location pointed to by the error parameter. The error info dictionary may contain entries that use any combination of the following keys, including no entries at all.

## Topics

### Constants

- [NSAppleScriptErrorMessage](nsapplescript/errormessage.md) — An `NSString` that supplies a detailed description of the error condition.
- [NSAppleScriptErrorNumber](nsapplescript/errornumber.md) — An `NSNumber` that specifies the error number.
- [NSAppleScriptErrorAppName](nsapplescript/errorappname.md) — An `NSString` that specifies the name of the application that generated the error.
- [NSAppleScriptErrorBriefMessage](nsapplescript/errorbriefmessage.md) — An `NSString` that provides a brief description of the error.
- [NSAppleScriptErrorRange](nsapplescript/errorrange.md) — An `NSValue` that specifies a range.
