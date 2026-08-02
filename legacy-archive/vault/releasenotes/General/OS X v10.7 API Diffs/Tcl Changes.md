---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Tcl.html
archived_at: '2026-07-18T02:54:40.614802Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Tcl Changes

## Tcl

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

tclInt.hRemoved ExtIndexRemoved #def WORDS_BIGENDIANAdded #def CLL_ENDAdded ContLineLocAdded #def TCL_MAX_TOKENSAdded TclAdvanceContinuations()Added TclContinuationsCopy()Added TclContinuationsEnter()Added TclContinuationsEnterDerived()Added TclContinuationsGet()Added TclCreateLateExitHandler()Added TclDeleteLateExitHandler()Added TclFinalizeThreadObjects()Modified TclArgumentBCEnter()

|  | Declaration |
| --- | --- |
| From | void TclArgumentBCEnter ( Tcl_Interp \*interp, void \*codePtr, CmdFrame \*cfPtr); |
| To | void TclArgumentBCEnter ( Tcl_Interp \*interp, Tcl_Obj \*objv[], int objc, void \*codePtr, CmdFrame \*cfPtr, int pc); |

Modified TclListLines()

|  | Declaration |
| --- | --- |
| From | void TclListLines ( const char \*listStr, int line, int n, int \*lines); |
| To | void TclListLines ( Tcl_Obj \*listObj, int line, int n, int \*lines, Tcl_Obj \*const \*elems); |

Modified TclDbInitNewObj()

|  | Declaration |
| --- | --- |
| From | MODULE_SCOPE void TclDbInitNewObj ( Tcl_Obj \*objPtr); |
| To | MODULE_SCOPE void TclDbInitNewObj ( Tcl_Obj \*objPtr, CONST char \*file, int line); |

Modified TclSubstTokens()

|  | Declaration |
| --- | --- |
| From | int TclSubstTokens ( Tcl_Interp \*interp, Tcl_Token \*tokenPtr, int count, int \*tokensLeftPtr, int line); |
| To | int TclSubstTokens ( Tcl_Interp \*interp, Tcl_Token \*tokenPtr, int count, int \*tokensLeftPtr, int line, int \*clNextOuter, const char \*outerScript); |

Modified TclEvalEx()

|  | Declaration |
| --- | --- |
| From | int TclEvalEx ( Tcl_Interp \*interp, const char \*script, int numBytes, int flags, int line); |
| To | int TclEvalEx ( Tcl_Interp \*interp, const char \*script, int numBytes, int flags, int line, int \*clNextOuter, const char \*outerScript); |

Modified TclArgumentBCRelease()

|  | Declaration |
| --- | --- |
| From | void TclArgumentBCRelease ( Tcl_Interp \*interp, void \*codePtr); |
| To | void TclArgumentBCRelease ( Tcl_Interp \*interp, Tcl_Obj \*objv[], int objc, void \*codePtr, int pc); |

tclIntDecls.hAdded TclDbDumpActiveObjects()Added #def TclDbDumpActiveObjects_TCL_DECLAREDtclIntPlatDecls.hModified TclWinAddProcess()

|  | Declaration |
| --- | --- |
| From | EXTERN void TclWinAddProcess ( HANDLE hProcess, DWORD id); |
| To | EXTERN void TclWinAddProcess ( void \*hProcess, unsigned long id); |

Modified TclWinConvertError()

|  | Declaration |
| --- | --- |
| From | EXTERN void TclWinConvertError ( DWORD errCode); |
| To | EXTERN void TclWinConvertError ( unsigned long errCode); |

Modified TclWinConvertWSAError()

|  | Declaration |
| --- | --- |
| From | EXTERN void TclWinConvertWSAError ( DWORD errCode); |
| To | EXTERN void TclWinConvertWSAError ( unsigned long errCode); |

tclPort.hAdded cygwin_conv_to_win32_path() (no architecture available)Modified #def environ

|  | Header |
| --- | --- |
| From | tclUnixPort.h |
| To | tclPort.h |

Modified #def USE_PUTENV

|  | Header |
| --- | --- |
| From | tclUnixPort.h |
| To | tclPort.h |

tclUnixPort.hRemoved WEAK_IMPORT_ATTRIBUTE (no architecture available)Removed defined()Removed state (no architecture available)Removed to (no architecture available)Added [socklen_t](https://developer.apple.com/documentation/kernel/socklen_t) (no architecture available)Modified copyfile()

|  | Declaration |
| --- | --- |
| From | int copyfile ( const char \*from, const char \*to, void \*state, uint32_t flags); |
| To | int copyfile ( const char \*from, const char \*to, copyfile_state_t state, copyfile_flags_t flags); |

Modified TclpMutex

|  | 32/64-bit | Architectures |
| --- | --- | --- |
| From | _Unknown_ | Unknown |
| To | Both | i386,x86_64 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
