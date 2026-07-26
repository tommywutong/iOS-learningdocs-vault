---
title: NSErrorRecoveryAttempting
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserrorrecoveryattempting
source_url: 'https://developer.apple.com/documentation/foundation/nserrorrecoveryattempting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserrorrecoveryattempting.json'
content_hash: 'sha256:64cd9e6f9dc5aa9d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Errors and Exceptions](errors-and-exceptions.md) · [NSError](nserror.md)

# NSErrorRecoveryAttempting

A set of methods that provide options to recover from an error.

## Overview

The `NSErrorRecoveryAttempting` informal protocol provides methods that allow your application to attempt to recover from an error. These methods are invoked when an `NSError` object is returned that specifies the implementing object as the error `recoveryAttempter` and the user has selected one of the error’s localized recovery options. The method invoked depends on how the error is presented to the user. If the error is presented in a document-modal sheet, [attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_delegate_didrecoverselector_contextinfo_).md>) is invoked. If the error is presented in an application-modal dialog, [attemptRecovery(fromError:optionIndex:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_).md>) is invoked.

## Topics

### Attempting Recovery From Errors

- [attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_delegate_didrecoverselector_contextinfo_).md>) — Implemented to attempt a recovery from an error noted in a document-modal sheet.
- [attemptRecovery(fromError:optionIndex:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_).md>) — Implemented to attempt a recovery from an error noted in an application-modal dialog.

## See Also

### Getting the Error Recovery Attempter

- [recoveryAttempter](nserror/recoveryattempter.md) — The object in the user info dictionary corresponding to the [NSRecoveryAttempterErrorKey](nsrecoveryattemptererrorkey.md) key.
