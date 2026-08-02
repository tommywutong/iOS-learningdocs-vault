---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/InputMethodKit.html
archived_at: '2026-07-18T02:54:29.566483Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# InputMethodKit Changes

## InputMethodKit

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

IMKCandidates.hAdded [-[IMKCandidates attachChild:toCandidate:type:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385455-attachchild)Added [-[IMKCandidates candidateFrame]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385426-candidateframe)Added [-[IMKCandidates candidateIdentifierAtLineNumber:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385471-candidateidentifieratlinenumber)Added [-[IMKCandidates candidateStringIdentifier:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385512-candidatestringidentifier)Added [-[IMKCandidates clearSelection]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385356-clearselection)Added [-[IMKCandidates detachChild:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385457-detachchild)Added [-[IMKCandidates hideChild]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385494-hidechild)Added [-[IMKCandidates initWithServer:panelType:styleType:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385467-init)Added [-[IMKCandidates lineNumberForCandidateWithIdentifier:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385488-linenumberforcandidatewithidenti)Added [-[IMKCandidates selectCandidate:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385543-selectcandidate)Added [-[IMKCandidates selectCandidateWithIdentifier:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385559-selectcandidatewithidentifier)Added [-[IMKCandidates selectedCandidate]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385514-selectedcandidate)Added [-[IMKCandidates selectedCandidateString]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385402-selectedcandidatestring)Added [-[IMKCandidates setCandidateData:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385508-setcandidatedata)Added [-[IMKCandidates setCandidateFrameTopLeft:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385459-setcandidateframetopleft)Added [-[IMKCandidates showCandidates]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385404-showcandidates)Added [-[IMKCandidates showChild]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385518-showchild)Added [-[IMKCandidates showSublist:subListDelegate:]](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/1385492-showsublist)Added [IMKStyleType](https://developer.apple.com/documentation/inputmethodkit/imkstyletype)Added [kIMKAnnotation](https://developer.apple.com/documentation/inputmethodkit/1448301-anonymous/kimkannotation)Added [kIMKMain](https://developer.apple.com/documentation/inputmethodkit/1448301-anonymous/kimkmain)Added [kIMKSubList](https://developer.apple.com/documentation/inputmethodkit/kimksublist)Modified [IMKCandidates](https://developer.apple.com/documentation/inputmethodkit/imkcandidates)

|  | Superclass |
| --- | --- |
| From | NSObject |
| To | NSResponder |

IMKInputController.hAdded [-[IMKInputController inputControllerWillClose]](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/1385375-inputcontrollerwillclose)IMKServer.hAdded [-[IMKServer lastKeyEventWasDeadKey]](https://developer.apple.com/documentation/inputmethodkit/imkserver/1385506-lastkeyeventwasdeadkey)Added [-[IMKServer paletteWillTerminate]](https://developer.apple.com/documentation/inputmethodkit/imkserver/1385358-palettewillterminate)

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
