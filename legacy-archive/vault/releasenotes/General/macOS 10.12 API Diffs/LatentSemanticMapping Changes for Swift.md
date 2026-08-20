---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/LatentSemanticMapping.html
archived_at: '2026-07-18T02:51:27.955468Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# LatentSemanticMapping Changes for Swift

### LatentSemanticMapping

Modified [LSMMapAddCategory(_: LSMMap) -> LSMCategory](https://developer.apple.com/documentation/latentsemanticmapping/1508571-lsmmapaddcategory)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapAddCategory(_ mapref: LSMMap!) -> LSMCategory ``` |
| To | ``` func LSMMapAddCategory(_ mapref: LSMMap) -> LSMCategory ``` |

Modified [LSMMapAddText(_: LSMMap, _: LSMText, _: LSMCategory) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508597-lsmmapaddtext)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapAddText(_ mapref: LSMMap!, _ textref: LSMText!, _ category: LSMCategory) -> OSStatus ``` |
| To | ``` func LSMMapAddText(_ mapref: LSMMap, _ textref: LSMText, _ category: LSMCategory) -> OSStatus ``` |

Modified [LSMMapAddTextWithWeight(_: LSMMap, _: LSMText, _: LSMCategory, _: Float) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508601-lsmmapaddtextwithweight)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapAddTextWithWeight(_ mapref: LSMMap!, _ textref: LSMText!, _ category: LSMCategory, _ weight: Float) -> OSStatus ``` |
| To | ``` func LSMMapAddTextWithWeight(_ mapref: LSMMap, _ textref: LSMText, _ category: LSMCategory, _ weight: Float) -> OSStatus ``` |

Modified [LSMMapApplyClusters(_: LSMMap, _: CFArray) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508554-lsmmapapplyclusters)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapApplyClusters(_ mapref: LSMMap!, _ clusters: CFArray!) -> OSStatus ``` |
| To | ``` func LSMMapApplyClusters(_ mapref: LSMMap, _ clusters: CFArray) -> OSStatus ``` |

Modified [LSMMapCompile(_: LSMMap) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508589-lsmmapcompile)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapCompile(_ mapref: LSMMap!) -> OSStatus ``` |
| To | ``` func LSMMapCompile(_ mapref: LSMMap) -> OSStatus ``` |

Modified [LSMMapCreate(_: CFAllocator?, _: CFOptionFlags) -> Unmanaged<LSMMap>](https://developer.apple.com/documentation/latentsemanticmapping/1508609-lsmmapcreate)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapCreate(_ alloc: CFAllocator!, _ flags: CFOptionFlags) -> Unmanaged<LSMMap>! ``` |
| To | ``` func LSMMapCreate(_ alloc: CFAllocator?, _ flags: CFOptionFlags) -> Unmanaged<LSMMap> ``` |

Modified [LSMMapCreateClusters(_: CFAllocator?, _: LSMMap, _: CFArray?, _: CFIndex, _: CFOptionFlags) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/latentsemanticmapping/1508580-lsmmapcreateclusters)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapCreateClusters(_ alloc: CFAllocator!, _ mapref: LSMMap!, _ subset: CFArray!, _ numClusters: CFIndex, _ flags: CFOptionFlags) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSMMapCreateClusters(_ alloc: CFAllocator?, _ mapref: LSMMap, _ subset: CFArray?, _ numClusters: CFIndex, _ flags: CFOptionFlags) -> Unmanaged<CFArray>? ``` |

Modified [LSMMapCreateFromURL(_: CFAllocator?, _: CFURL, _: CFOptionFlags) -> Unmanaged<LSMMap>?](https://developer.apple.com/documentation/latentsemanticmapping/1508590-lsmmapcreatefromurl)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapCreateFromURL(_ alloc: CFAllocator!, _ file: CFURL!, _ flags: CFOptionFlags) -> Unmanaged<LSMMap>! ``` |
| To | ``` func LSMMapCreateFromURL(_ alloc: CFAllocator?, _ file: CFURL, _ flags: CFOptionFlags) -> Unmanaged<LSMMap>? ``` |

Modified [LSMMapGetCategoryCount(_: LSMMap) -> CFIndex](https://developer.apple.com/documentation/latentsemanticmapping/1508618-lsmmapgetcategorycount)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapGetCategoryCount(_ mapref: LSMMap!) -> CFIndex ``` |
| To | ``` func LSMMapGetCategoryCount(_ mapref: LSMMap) -> CFIndex ``` |

Modified [LSMMapGetProperties(_: LSMMap) -> Unmanaged<CFDictionary>](https://developer.apple.com/documentation/latentsemanticmapping/1508588-lsmmapgetproperties)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapGetProperties(_ mapref: LSMMap!) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func LSMMapGetProperties(_ mapref: LSMMap) -> Unmanaged<CFDictionary> ``` |

Modified [LSMMapSetProperties(_: LSMMap, _: CFDictionary)](https://developer.apple.com/documentation/latentsemanticmapping/1508581-lsmmapsetproperties)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapSetProperties(_ mapref: LSMMap!, _ properties: CFDictionary!) ``` |
| To | ``` func LSMMapSetProperties(_ mapref: LSMMap, _ properties: CFDictionary) ``` |

Modified [LSMMapSetStopWords(_: LSMMap, _: LSMText) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508598-lsmmapsetstopwords)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapSetStopWords(_ mapref: LSMMap!, _ textref: LSMText!) -> OSStatus ``` |
| To | ``` func LSMMapSetStopWords(_ mapref: LSMMap, _ textref: LSMText) -> OSStatus ``` |

Modified [LSMMapStartTraining(_: LSMMap) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508560-lsmmapstarttraining)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapStartTraining(_ mapref: LSMMap!) -> OSStatus ``` |
| To | ``` func LSMMapStartTraining(_ mapref: LSMMap) -> OSStatus ``` |

Modified [LSMMapWriteToStream(_: LSMMap, _: LSMText?, _: CFWriteStream, _: CFOptionFlags) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508582-lsmmapwritetostream)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapWriteToStream(_ mapref: LSMMap!, _ textref: LSMText!, _ stream: CFWriteStream!, _ options: CFOptionFlags) -> OSStatus ``` |
| To | ``` func LSMMapWriteToStream(_ mapref: LSMMap, _ textref: LSMText?, _ stream: CFWriteStream, _ options: CFOptionFlags) -> OSStatus ``` |

Modified [LSMMapWriteToURL(_: LSMMap, _: CFURL, _: CFOptionFlags) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508610-lsmmapwritetourl)

|  | Declaration |
| --- | --- |
| From | ``` func LSMMapWriteToURL(_ mapref: LSMMap!, _ file: CFURL!, _ flags: CFOptionFlags) -> OSStatus ``` |
| To | ``` func LSMMapWriteToURL(_ mapref: LSMMap, _ file: CFURL, _ flags: CFOptionFlags) -> OSStatus ``` |

Modified [LSMResultCopyToken(_: LSMResult, _: CFIndex) -> Unmanaged<CFData>?](https://developer.apple.com/documentation/latentsemanticmapping/1508620-lsmresultcopytoken)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultCopyToken(_ mapref: LSMResult!, _ n: CFIndex) -> Unmanaged<CFData>! ``` |
| To | ``` func LSMResultCopyToken(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFData>? ``` |

Modified [LSMResultCopyTokenCluster(_: LSMResult, _: CFIndex) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/latentsemanticmapping/1508546-lsmresultcopytokencluster)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultCopyTokenCluster(_ mapref: LSMResult!, _ n: CFIndex) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSMResultCopyTokenCluster(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFArray>? ``` |

Modified [LSMResultCopyWord(_: LSMResult, _: CFIndex) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/latentsemanticmapping/1508603-lsmresultcopyword)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultCopyWord(_ result: LSMResult!, _ n: CFIndex) -> Unmanaged<CFString>! ``` |
| To | ``` func LSMResultCopyWord(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFString>? ``` |

Modified [LSMResultCopyWordCluster(_: LSMResult, _: CFIndex) -> Unmanaged<CFArray>?](https://developer.apple.com/documentation/latentsemanticmapping/1508587-lsmresultcopywordcluster)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultCopyWordCluster(_ result: LSMResult!, _ n: CFIndex) -> Unmanaged<CFArray>! ``` |
| To | ``` func LSMResultCopyWordCluster(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFArray>? ``` |

Modified [LSMResultCreate(_: CFAllocator?, _: LSMMap, _: LSMText, _: CFIndex, _: CFOptionFlags) -> Unmanaged<LSMResult>](https://developer.apple.com/documentation/latentsemanticmapping/1508579-lsmresultcreate)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultCreate(_ alloc: CFAllocator!, _ mapref: LSMMap!, _ textref: LSMText!, _ numResults: CFIndex, _ flags: CFOptionFlags) -> Unmanaged<LSMResult>! ``` |
| To | ``` func LSMResultCreate(_ alloc: CFAllocator?, _ mapref: LSMMap, _ textref: LSMText, _ numResults: CFIndex, _ flags: CFOptionFlags) -> Unmanaged<LSMResult> ``` |

Modified [LSMResultGetCategory(_: LSMResult, _: CFIndex) -> LSMCategory](https://developer.apple.com/documentation/latentsemanticmapping/1508592-lsmresultgetcategory)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultGetCategory(_ result: LSMResult!, _ n: CFIndex) -> LSMCategory ``` |
| To | ``` func LSMResultGetCategory(_ result: LSMResult, _ n: CFIndex) -> LSMCategory ``` |

Modified [LSMResultGetCount(_: LSMResult) -> CFIndex](https://developer.apple.com/documentation/latentsemanticmapping/1508621-lsmresultgetcount)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultGetCount(_ result: LSMResult!) -> CFIndex ``` |
| To | ``` func LSMResultGetCount(_ result: LSMResult) -> CFIndex ``` |

Modified [LSMResultGetScore(_: LSMResult, _: CFIndex) -> Float](https://developer.apple.com/documentation/latentsemanticmapping/1508600-lsmresultgetscore)

|  | Declaration |
| --- | --- |
| From | ``` func LSMResultGetScore(_ result: LSMResult!, _ n: CFIndex) -> Float ``` |
| To | ``` func LSMResultGetScore(_ result: LSMResult, _ n: CFIndex) -> Float ``` |

Modified [LSMTextAddToken(_: LSMText, _: CFData) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508608-lsmtextaddtoken)

|  | Declaration |
| --- | --- |
| From | ``` func LSMTextAddToken(_ textref: LSMText!, _ token: CFData!) -> OSStatus ``` |
| To | ``` func LSMTextAddToken(_ textref: LSMText, _ token: CFData) -> OSStatus ``` |

Modified [LSMTextAddWord(_: LSMText, _: CFString) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508577-lsmtextaddword)

|  | Declaration |
| --- | --- |
| From | ``` func LSMTextAddWord(_ textref: LSMText!, _ word: CFString!) -> OSStatus ``` |
| To | ``` func LSMTextAddWord(_ textref: LSMText, _ word: CFString) -> OSStatus ``` |

Modified [LSMTextAddWords(_: LSMText, _: CFString, _: CFLocale?, _: CFOptionFlags) -> OSStatus](https://developer.apple.com/documentation/latentsemanticmapping/1508585-lsmtextaddwords)

|  | Declaration |
| --- | --- |
| From | ``` func LSMTextAddWords(_ textref: LSMText!, _ words: CFString!, _ locale: CFLocale!, _ flags: CFOptionFlags) -> OSStatus ``` |
| To | ``` func LSMTextAddWords(_ textref: LSMText, _ words: CFString, _ locale: CFLocale?, _ flags: CFOptionFlags) -> OSStatus ``` |

Modified [LSMTextCreate(_: CFAllocator?, _: LSMMap) -> Unmanaged<LSMText>](https://developer.apple.com/documentation/latentsemanticmapping/1508574-lsmtextcreate)

|  | Declaration |
| --- | --- |
| From | ``` func LSMTextCreate(_ alloc: CFAllocator!, _ mapref: LSMMap!) -> Unmanaged<LSMText>! ``` |
| To | ``` func LSMTextCreate(_ alloc: CFAllocator?, _ mapref: LSMMap) -> Unmanaged<LSMText> ``` |

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
