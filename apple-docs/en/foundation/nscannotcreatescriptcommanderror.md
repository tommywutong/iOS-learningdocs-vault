---
title: NSCannotCreateScriptCommandError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscannotcreatescriptcommanderror
source_url: 'https://developer.apple.com/documentation/foundation/nscannotcreatescriptcommanderror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscannotcreatescriptcommanderror.json'
content_hash: 'sha256:5a995304df3d2bd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCannotCreateScriptCommandError

<sub>Global Variable</sub>

Could not create the script command; an invalid or unrecognized Apple event was received.

<sub>Mac Catalyst, macOS</sub>

```swift
var NSCannotCreateScriptCommandError: Int { get }
```

## See Also

### Constants

- [NSNoScriptError](nsnoscripterror.md) — No error.
- [NSReceiverEvaluationScriptError](nsreceiverevaluationscripterror.md) — The object or objects specified by the direct parameter to a command could not be found.
- [NSKeySpecifierEvaluationScriptError](nskeyspecifierevaluationscripterror.md) — The object or objects specified by a key (for commands that support key specifiers) could not be found.
- [NSArgumentEvaluationScriptError](nsargumentevaluationscripterror.md) — The object specified by an argument could not be found.
- [NSReceiversCantHandleCommandScriptError](nsreceiverscanthandlecommandscripterror.md) — The receivers don’t support the command sent to them.
- [NSRequiredArgumentsMissingScriptError](nsrequiredargumentsmissingscripterror.md) — An argument (or more than one argument) is missing.
- [NSArgumentsWrongScriptError](nsargumentswrongscripterror.md) — An argument (or more than one argument) is of the wrong type or is otherwise invalid.
- [NSUnknownKeyScriptError](nsunknownkeyscripterror.md) — An unidentified error occurred; indicates an error in the scripting support of your application.
- [NSInternalScriptError](nsinternalscripterror.md) — An unidentified internal error occurred; indicates an error in the scripting support of your application.
- [NSOperationNotSupportedForKeyScriptError](nsoperationnotsupportedforkeyscripterror.md) — The implementation of a scripting command signaled an error.
