---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/Accelerate.html
archived_at: '2026-07-18T02:53:49.955442Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# Accelerate Changes for Swift

### Accelerate

Added [vS1024.init(s: vS1024.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vs1024/1546624-init)Added [vS1024.init(vs: vS1024.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vs1024/1546695-init)Added [vS1024.s](https://developer.apple.com/documentation/accelerate/vs1024/1546642-s)Added [vS1024.vs](https://developer.apple.com/documentation/accelerate/1545885-vs1024/1546723-vs)Added [vS128.init(s: vS128.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vs128/1546810-init)Added [vS128.init(vs: vS128.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vs128/1544990-init)Added [vS128.s](https://developer.apple.com/documentation/accelerate/1544758-vs128/1546623-s)Added [vS128.vs](https://developer.apple.com/documentation/accelerate/vs128/1545085-vs)Added [vS256.init(s: vS256.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vs256/1546315-init)Added [vS256.init(vs: vS256.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vs256/1546590-init)Added [vS256.s](https://developer.apple.com/documentation/accelerate/vs256/1545089-s)Added [vS256.vs](https://developer.apple.com/documentation/accelerate/vs256/1546458-vs)Added [vS512.init(s: vS512.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vs512/1544802-init)Added [vS512.init(vs: vS512.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vs512/1546055-init)Added [vS512.s](https://developer.apple.com/documentation/accelerate/1545872-vs512/1544589-s)Added [vS512.vs](https://developer.apple.com/documentation/accelerate/1545872-vs512/1546549-vs)Added [vU1024.init(s: vU1024.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vu1024/1546989-init)Added [vU1024.init(vs: vU1024.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vu1024/1545859-init)Added [vU1024.s](https://developer.apple.com/documentation/accelerate/vu1024/1546710-s)Added [vU1024.vs](https://developer.apple.com/documentation/accelerate/vu1024/1546637-vs)Added [vU128.init(s: vU128.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vu128/1545137-init)Added [vU128.init(vs: vU128.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vu128/1545827-init)Added [vU128.s](https://developer.apple.com/documentation/accelerate/1546704-vu128/1546741-s)Added [vU128.vs](https://developer.apple.com/documentation/accelerate/vu128/1544409-vs)Added [vU256.init(s: vU256.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vu256/1546196-init)Added [vU256.init(vs: vU256.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vu256/1546674-init)Added [vU256.s](https://developer.apple.com/documentation/accelerate/vu256/1546612-s)Added [vU256.vs](https://developer.apple.com/documentation/accelerate/1545748-vu256/1546517-vs)Added [vU512.init(s: vU512.__Unnamed_struct_s)](https://developer.apple.com/documentation/accelerate/vu512/1546849-init)Added [vU512.init(vs: vU512.__Unnamed_struct_vs)](https://developer.apple.com/documentation/accelerate/vu512/1545877-init)Added [vU512.s](https://developer.apple.com/documentation/accelerate/1544674-vu512/1546607-s)Added [vU512.vs](https://developer.apple.com/documentation/accelerate/vu512/1546778-vs)Modified [vImageConstCVImageFormat](https://developer.apple.com/documentation/accelerate/vimageconstcvimageformatref)

|  | Name | Declaration |
| --- | --- | --- |
| From | vImageConstCVImageFormatRef | ``` typealias vImageConstCVImageFormatRef = vImageConstCVImageFormat ``` |
| To | vImageConstCVImageFormat | ``` class vImageConstCVImageFormat { } ``` |

Modified [vImageConverter](https://developer.apple.com/documentation/accelerate/vimageconverterref)

|  | Name | Declaration |
| --- | --- | --- |
| From | vImageConverterRef | ``` typealias vImageConverterRef = vImageConverter ``` |
| To | vImageConverter | ``` class vImageConverter { } ``` |

Modified [vImageCVImageFormat](https://developer.apple.com/documentation/accelerate/vimagecvimageformat)

|  | Name | Declaration |
| --- | --- | --- |
| From | vImageCVImageFormatRef | ``` typealias vImageCVImageFormatRef = vImageCVImageFormat ``` |
| To | vImageCVImageFormat | ``` class vImageCVImageFormat { } ``` |

Modified [vS1024 [struct]](https://developer.apple.com/documentation/accelerate/1545885-vs1024)

|  | Declaration |
| --- | --- |
| From | ``` struct vS1024 {     init() } ``` |
| To | ``` struct vS1024 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: Int32         var d31: UInt32         var d30: UInt32         var d29: UInt32         var d28: UInt32         var d27: UInt32         var d26: UInt32         var d25: UInt32         var d24: UInt32         var d23: UInt32         var d22: UInt32         var d21: UInt32         var d20: UInt32         var d19: UInt32         var d18: UInt32         var d17: UInt32         var d16: UInt32         var d15: UInt32         var d14: UInt32         var d13: UInt32         var d12: UInt32         var d11: UInt32         var d10: UInt32         var d9: UInt32         var d8: UInt32         var d7: UInt32         var d6: UInt32         var d5: UInt32         var d4: UInt32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: Int32, d31 d31: UInt32, d30 d30: UInt32, d29 d29: UInt32, d28 d28: UInt32, d27 d27: UInt32, d26 d26: UInt32, d25 d25: UInt32, d24 d24: UInt32, d23 d23: UInt32, d22 d22: UInt32, d21 d21: UInt32, d20 d20: UInt32, d19 d19: UInt32, d18 d18: UInt32, d17 d17: UInt32, d16 d16: UInt32, d15 d15: UInt32, d14 d14: UInt32, d13 d13: UInt32, d12 d12: UInt32, d11 d11: UInt32, d10 d10: UInt32, d9 d9: UInt32, d8 d8: UInt32, d7 d7: UInt32, d6 d6: UInt32, d5 d5: UInt32, d4 d4: UInt32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vS1024.__Unnamed_struct_vs     var s: vS1024.__Unnamed_struct_s     init(vs vs: vS1024.__Unnamed_struct_vs)     init(s s: vS1024.__Unnamed_struct_s)     init() } ``` |

Modified [vS128 [struct]](https://developer.apple.com/documentation/accelerate/vs128)

|  | Declaration |
| --- | --- |
| From | ``` struct vS128 {     init() } ``` |
| To | ``` struct vS128 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: Int32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: Int32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vS128.__Unnamed_struct_vs     var s: vS128.__Unnamed_struct_s     init(vs vs: vS128.__Unnamed_struct_vs)     init(s s: vS128.__Unnamed_struct_s)     init() } ``` |

Modified [vS256 [struct]](https://developer.apple.com/documentation/accelerate/1545997-vs256)

|  | Declaration |
| --- | --- |
| From | ``` struct vS256 {     init() } ``` |
| To | ``` struct vS256 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: Int32         var d7: UInt32         var d6: UInt32         var d5: UInt32         var d4: UInt32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: Int32, d7 d7: UInt32, d6 d6: UInt32, d5 d5: UInt32, d4 d4: UInt32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vS256.__Unnamed_struct_vs     var s: vS256.__Unnamed_struct_s     init(vs vs: vS256.__Unnamed_struct_vs)     init(s s: vS256.__Unnamed_struct_s)     init() } ``` |

Modified [vS512 [struct]](https://developer.apple.com/documentation/accelerate/vs512)

|  | Declaration |
| --- | --- |
| From | ``` struct vS512 {     init() } ``` |
| To | ``` struct vS512 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: Int32         var d15: UInt32         var d14: UInt32         var d13: UInt32         var d12: UInt32         var d11: UInt32         var d10: UInt32         var d9: UInt32         var d8: UInt32         var d7: UInt32         var d6: UInt32         var d5: UInt32         var d4: UInt32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: Int32, d15 d15: UInt32, d14 d14: UInt32, d13 d13: UInt32, d12 d12: UInt32, d11 d11: UInt32, d10 d10: UInt32, d9 d9: UInt32, d8 d8: UInt32, d7 d7: UInt32, d6 d6: UInt32, d5 d5: UInt32, d4 d4: UInt32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vS512.__Unnamed_struct_vs     var s: vS512.__Unnamed_struct_s     init(vs vs: vS512.__Unnamed_struct_vs)     init(s s: vS512.__Unnamed_struct_s)     init() } ``` |

Modified [vU1024 [struct]](https://developer.apple.com/documentation/accelerate/1545000-vu1024)

|  | Declaration |
| --- | --- |
| From | ``` struct vU1024 {     init() } ``` |
| To | ``` struct vU1024 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: UInt32         var d31: UInt32         var d30: UInt32         var d29: UInt32         var d28: UInt32         var d27: UInt32         var d26: UInt32         var d25: UInt32         var d24: UInt32         var d23: UInt32         var d22: UInt32         var d21: UInt32         var d20: UInt32         var d19: UInt32         var d18: UInt32         var d17: UInt32         var d16: UInt32         var d15: UInt32         var d14: UInt32         var d13: UInt32         var d12: UInt32         var d11: UInt32         var d10: UInt32         var d9: UInt32         var d8: UInt32         var d7: UInt32         var d6: UInt32         var d5: UInt32         var d4: UInt32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: UInt32, d31 d31: UInt32, d30 d30: UInt32, d29 d29: UInt32, d28 d28: UInt32, d27 d27: UInt32, d26 d26: UInt32, d25 d25: UInt32, d24 d24: UInt32, d23 d23: UInt32, d22 d22: UInt32, d21 d21: UInt32, d20 d20: UInt32, d19 d19: UInt32, d18 d18: UInt32, d17 d17: UInt32, d16 d16: UInt32, d15 d15: UInt32, d14 d14: UInt32, d13 d13: UInt32, d12 d12: UInt32, d11 d11: UInt32, d10 d10: UInt32, d9 d9: UInt32, d8 d8: UInt32, d7 d7: UInt32, d6 d6: UInt32, d5 d5: UInt32, d4 d4: UInt32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vU1024.__Unnamed_struct_vs     var s: vU1024.__Unnamed_struct_s     init(vs vs: vU1024.__Unnamed_struct_vs)     init(s s: vU1024.__Unnamed_struct_s)     init() } ``` |

Modified [vU128 [struct]](https://developer.apple.com/documentation/accelerate/1546704-vu128)

|  | Declaration |
| --- | --- |
| From | ``` struct vU128 {     init() } ``` |
| To | ``` struct vU128 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: UInt32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: UInt32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vU128.__Unnamed_struct_vs     var s: vU128.__Unnamed_struct_s     init(vs vs: vU128.__Unnamed_struct_vs)     init(s s: vU128.__Unnamed_struct_s)     init() } ``` |

Modified [vU256 [struct]](https://developer.apple.com/documentation/accelerate/vu256)

|  | Declaration |
| --- | --- |
| From | ``` struct vU256 {     init() } ``` |
| To | ``` struct vU256 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: UInt32         var d7: UInt32         var d6: UInt32         var d5: UInt32         var d4: UInt32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: UInt32, d7 d7: UInt32, d6 d6: UInt32, d5 d5: UInt32, d4 d4: UInt32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vU256.__Unnamed_struct_vs     var s: vU256.__Unnamed_struct_s     init(vs vs: vU256.__Unnamed_struct_vs)     init(s s: vU256.__Unnamed_struct_s)     init() } ``` |

Modified [vU512 [struct]](https://developer.apple.com/documentation/accelerate/1544674-vu512)

|  | Declaration |
| --- | --- |
| From | ``` struct vU512 {     init() } ``` |
| To | ``` struct vU512 {     struct __Unnamed_struct_vs {         init()     }     struct __Unnamed_struct_s {         var LSW: UInt32         var d15: UInt32         var d14: UInt32         var d13: UInt32         var d12: UInt32         var d11: UInt32         var d10: UInt32         var d9: UInt32         var d8: UInt32         var d7: UInt32         var d6: UInt32         var d5: UInt32         var d4: UInt32         var d3: UInt32         var d2: UInt32         var MSW: UInt32         init()         init(LSW LSW: UInt32, d15 d15: UInt32, d14 d14: UInt32, d13 d13: UInt32, d12 d12: UInt32, d11 d11: UInt32, d10 d10: UInt32, d9 d9: UInt32, d8 d8: UInt32, d7 d7: UInt32, d6 d6: UInt32, d5 d5: UInt32, d4 d4: UInt32, d3 d3: UInt32, d2 d2: UInt32, MSW MSW: UInt32)     }     var vs: vU512.__Unnamed_struct_vs     var s: vU512.__Unnamed_struct_s     init(vs vs: vU512.__Unnamed_struct_vs)     init(s s: vU512.__Unnamed_struct_s)     init() } ``` |

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
