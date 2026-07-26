---
title: NSScriptCommand—General Command Execution Errors
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/general-command-execution-errors
source_url: 'https://developer.apple.com/documentation/foundation/general-command-execution-errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/general-command-execution-errors.json'
content_hash: 'sha256:750cd06072ce2772'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Scripting Support](scripting-support.md) · [NSScriptCommand](nsscriptcommand.md)

# NSScriptCommand—General Command Execution Errors

<sub>API Collection</sub>

`NSScriptCommand` uses the following error codes for general command execution problems:

## Topics

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
- [NSCannotCreateScriptCommandError](nscannotcreatescriptcommanderror.md) — Could not create the script command; an invalid or unrecognized Apple event was received.
