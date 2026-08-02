---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tidy/CompositePage.html
archived_at: '2026-07-15T07:23:28.793179Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidy.h - Defines HTML Tidy API implemented by tidy library. | tidy.h - Defines HTML Tidy API implemented by tidy library. | tidy.h - Defines HTML Tidy API implemented by tidy library. | tidy.h - Defines HTML Tidy API implemented by tidy library. | tidy.h - Defines HTML Tidy API implemented by tidy library. |

|  |  |
| --- | --- |
| __Includes:__ | ["platform.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/platform/index.html#//apple_ref/doc/header/platform.h)  ["tidyenum.h"](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/tidyenum/index.html#//apple_ref/doc/header/tidyenum.h) |

## Introduction

Public interface is const-correct and doesn't explicitly depend
on any globals. Thus, thread-safety may be introduced w/out
changing the interface.

Looking ahead to a C++ wrapper, C functions always pass
this-equivalent as 1st arg.

Copyright (c) 1998-2004 World Wide Web Consortium
(Massachusetts Institute of Technology, European Research
Consortium for Informatics and Mathematics, Keio University).
All Rights Reserved.

CVS Info :

$Author: rbraun $
$Date: 2004/05/04 20:05:14 $
$Revision: 1.1.1.1 $

Contributing Author(s):

Dave Raggett

The contributing author(s) would like to thank all those who
helped with testing, bug fixes and suggestions for improvements.
This wouldn't have been possible without your help.

COPYRIGHT NOTICE:

This software and documentation is provided "as is," and
the copyright holders and contributing author(s) make no
representations or warranties, express or implied, including
but not limited to, warranties of merchantability or fitness
for any particular purpose or that the use of the software or
documentation will not infringe any third party patents,
copyrights, trademarks or other rights.

The copyright holders and contributing author(s) will not be held
liable for any direct, indirect, special or consequential damages
arising out of any use of the software or documentation, even if
advised of the possibility of such damage.

Permission is hereby granted to use, copy, modify, and distribute
this source code, or portions hereof, documentation and executables,
for any purpose, without fee, subject to the following restrictions:

1. The origin of this source code must not be misrepresented.
   2. Altered versions must be plainly marked as such and must
      not be misrepresented as being the original source.
      3. This Copyright notice may not be removed or altered from any
      source or altered source distribution.

      The copyright holders and contributing author(s) specifically
      permit, without fee, and encourage the use of this source code
      as a component for supporting the Hypertext Markup Language in
      commercial products. If you use this source code in a product,
      acknowledgment is not required but would be appreciated.

      Created 2001-05-20 by Charles Reitzel
      Updated 2002-07-01 by Charles Reitzel - 1st Implementation

---

## Functions

**[opaque_type( TidyAttr)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobxmjtdgyzq)**
:

**[opaque_type( TidyDoc)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4df)**
:

**[opaque_type( TidyNode)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobshbrdkntd)**
:

**[opaque_type( TidyOption)](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobshbrwkztd)**
:

**[tidyAccessWarningCount](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqldmnsxg42xmfzg42lom5bw65looq)**
:

**[tidyAttrGetHREF](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqluorzeozlujbjekrq)**
:

**[tidyAttrGetId](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsqluorzeozlujfsa)**
:

**[tidyCleanAndRepair](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsq3mmvqw4qlomrjgk4dbnfza)**
:

**[tidyConfigErrorCount](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsq3pnztgsz2fojzg64sdn52w45a)**
:

**[tidyCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsq3smvqxizi)**
:

**[tidyDetectedGenericXml](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsrdforswg5dfmrdwk3tfojuwgwdnnq)**
:

**[tidyDetectedHtmlVersion](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsrdforswg5dfmrehi3lmkzsxe43jn5xa)**
:

**[tidyDetectedXhtml](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsrdforswg5dfmrmgq5dnnq)**
:

**[tidyErrorCount](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsrlsojxxeq3povxhi)**
:

**[tidyErrorSummary](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsrlsojxxeu3vnvwwc4tz)**
:

**[tidyGeneralInfo](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3fnzsxeylmjfxgm3y)**
:

**[tidyGetAppData](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3foraxa4cemf2gc)**
:

**[tidyGetByte](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3forbhs5df)**
:

**[tidyGetNextOption](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3forhgk6duj5yhi2lpny)**
:

**[tidyGetOption](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3forhxa5djn5xa)**
:

**[tidyGetOptionByName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3forhxa5djn5xee6komfwwk)**
:

**[tidyGetOptionList](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3forhxa5djn5xey2ltoq)**
:

**[tidyGetRoot](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsr3forjg633u)**
:

**[tidyInitSink](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsslonf2fg2lonm)**
:

**[tidyInitSource](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsslonf2fg33vojrwk)**
:

**[tidyIsEOF](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshssltivhum)**
:

**[tidyLoadConfig](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshstdpmfseg33omzuwo)**
:

**[tidyLoadConfigEnc](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshstdpmfseg33omzuworlomm)**
:

**[tidyNodeGetType](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsttpmrsuozlukr4xazi)**
:

**[tidyOptCopyConfig](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorbw64dzinxw4ztjm4)**
:

**[tidyOptDiffThanDefault](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorcgsztgkrugc3semvtgc5lmoq)**
:

**[tidyOptDiffThanSnapshot](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorcgsztgkrugc3stnzqxa43in52a)**
:

**[tidyOptGetBool](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5ccn5xwy)**
:

**[tidyOptGetCategory](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cdmf2gkz3poj4q)**
:

**[tidyOptGetCurrPick](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cdovzheudjmnvq)**
:

**[tidyOptGetDeclTagList](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cemvrwyvdbm5ggs43u)**
:

**[tidyOptGetDefault](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cemvtgc5lmoq)**
:

**[tidyOptGetDefaultBool](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cemvtgc5lmorbg633m)**
:

**[tidyOptGetDefaultInt](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cemvtgc5lmorew45a)**
:

**[tidyOptGetEncName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cfnzru4ylnmu)**
:

**[tidyOptGetId](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cjmq)**
:

**[tidyOptGetIdForName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cjmrdg64somfwwk)**
:

**[tidyOptGetInt](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cjnz2a)**
:

**[tidyOptGetName](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5comfwwk)**
:

**[tidyOptGetNextDeclTag](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5comv4hirdfmnwfiylh)**
:

**[tidyOptGetNextPick](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5comv4hiudjmnvq)**
:

**[tidyOptGetPickList](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cqnfrwwtdjon2a)**
:

**[tidyOptGetType](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cupfygk)**
:

**[tidyOptGetValue](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qordwk5cwmfwhkzi)**
:

**[tidyOptIsReadOnly](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorexgutfmfse63tmpe)**
:

**[tidyOptParseValue](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorigc4ttmvlgc3dvmu)**
:

**[tidyOptResetAllToDefault](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjgk43forawy3cun5cgkztbovwhi)**
:

**[tidyOptResetToDefault](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjgk43forkg6rdfmzqxk3du)**
:

**[tidyOptResetToSnapshot](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjgk43forkg6u3omfyhg2dpoq)**
:

**[tidyOptSaveFile](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjwc5tfizuwyzi)**
:

**[tidyOptSaveSink](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjwc5tfknuw42y)**
:

**[tidyOptSetBool](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjwk5ccn5xwy)**
:

**[tidyOptSetInt](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjwk5cjnz2a)**
:

**[tidyOptSetValue](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjwk5cwmfwhkzi)**
:

**[tidyOptSnapshot](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshst3qorjw4ylqonug65a)**
:

**[tidyParseBuffer](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsudbojzwkqtvmztgk4q)**
:

**[tidyParseFile](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsudbojzwkrtjnrsq)**
:

**[tidyParseSource](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsudbojzwku3povzggzi)**
:

**[tidyParseStdin](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsudbojzwku3umruw4)**
:

**[tidyParseString](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsudbojzwku3uojuw4zy)**
:

**[tidyPutByte](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsudvorbhs5df)**
:

**[tidyReleaseDate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsutfnrswc43firqxizi)**
:

**[tidyRunDiagnostics](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsutvnzcgsylhnzxxg5djmnzq)**
:

**[tidySaveBuffer](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3bozsue5lgmzsxe)**
:

**[tidySaveFile](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3bozsum2lmmu)**
:

**[tidySaveSink](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3bozsvg2lonm)**
:

**[tidySaveStdout](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3bozsvg5den52xi)**
:

**[tidySaveString](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3bozsvg5dsnfxgo)**
:

**[tidySetAppData](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3foraxa4cemf2gc)**
:

**[tidySetCharEncoding](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forbwqylsivxgg33enfxgo)**
:

**[tidySetErrorBuffer](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forcxe4tpojbhkztgmvza)**
:

**[tidySetErrorFile](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forcxe4tpojdgs3df)**
:

**[tidySetErrorSink](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forcxe4tpojjws3tl)**
:

**[tidySetFreeCall](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3fordhezlfinqwy3a)**
:

**[tidySetInCharEncoding](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forew4q3imfzek3tdn5sgs3th)**
:

**[tidySetMallocCall](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forgwc3dmn5rugylmnq)**
:

**[tidySetOutCharEncoding](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forhxk5cdnbqxerlomnxwi2lom4)**
:

**[tidySetPanicCall](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forigc3tjmnbwc3dm)**
:

**[tidySetReallocCall](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forjgkylmnrxwgq3bnrwa)**
:

**[tidySetReportFilter](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3forjgk4dpoj2em2lmorsxe)**
:

**[tidyStatus](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsu3umf2hk4y)**
:

**[tidyUngetByte](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsvlom5sxiqtzorsq)**
:

**[tidyWarningCount](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3unfshsv3bojxgs3thinxxk3tu)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| opaque_type( TidyAttr) | opaque_type( TidyAttr) | opaque_type( TidyAttr) | opaque_type( TidyAttr) | opaque_type( TidyAttr) |

---

__See Also:__
> **[opaque_type](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobshbrwkztd)**
> :
>
> **[opaque_type](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobshbrdkntd)**
> :

```
/** @struct TidyAttr
** Opaque attribute datatype
    */
opaque_type(
    TidyAttr );
```

##### Discussion

\*\* Opaque option datatype

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| opaque_type( TidyDoc) | opaque_type( TidyDoc) | opaque_type( TidyDoc) | opaque_type( TidyDoc) | opaque_type( TidyDoc) |

---

```
/** @struct TidyDoc
** Opaque document datatype
    */
opaque_type(
    TidyDoc );
```

##### Discussion

@defgroup Opaque Opaque Types
\*\*
\*\* Cast to implementation types within lib.
\*\* Reduces inter-dependencies/conflicts w/ application code.
\*\* @{

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| opaque_type( TidyNode) | opaque_type( TidyNode) | opaque_type( TidyNode) | opaque_type( TidyNode) | opaque_type( TidyNode) |

---

__See Also:__
> **[opaque_type](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobshbrwkztd)**
> :
>
> **[opaque_type](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobxmjtdgyzq)**
> :

```
/** @struct TidyNode
** Opaque node datatype
    */
opaque_type(
    TidyNode );
```

##### Discussion

\*\* Opaque option datatype

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| opaque_type( TidyOption) | opaque_type( TidyOption) | opaque_type( TidyOption) | opaque_type( TidyOption) | opaque_type( TidyOption) |

---

__See Also:__
> **[opaque_type](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobshbrdkntd)**
> :
>
> **[opaque_type](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl3pobqxc5lfl52hs4dfl5ce6tsujreu4s27gb4dcobxmjtdgyzq)**
> :

```
opaque_type(
    TidyOption );
```

##### Discussion

\*\* Opaque option datatype

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyAccessWarningCount | tidyAccessWarningCount | tidyAccessWarningCount | tidyAccessWarningCount | tidyAccessWarningCount |

---

```
TIDY_EXPORT uint tidyAccessWarningCount(
    TidyDoc tdoc );
```

##### Discussion

Number of Tidy accessibility warnings encountered.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyAttrGetHREF | tidyAttrGetHREF | tidyAttrGetHREF | tidyAttrGetHREF | tidyAttrGetHREF |

---

```
/** @defgroup AttrGet Attribute Retrieval
**
** Lookup an attribute from a given node
** @{
    */
TIDY_EXPORT TidyAttr tidyAttrGetHREF(
    TidyNode tnod );
```

##### Discussion

@} end AttrAsk group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyAttrGetId | tidyAttrGetId | tidyAttrGetId | tidyAttrGetId | tidyAttrGetId |

---

```
/** @defgroup Attribute Attribute Interrogation
**
** Get information about any given attribute.
** @{
    */
TIDY_EXPORT TidyAttrId tidyAttrGetId(
    TidyAttr tattr );
```

##### Discussion

@} End NodeAsk group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyCleanAndRepair | tidyCleanAndRepair | tidyCleanAndRepair | tidyCleanAndRepair | tidyCleanAndRepair |

---

```
/** @defgroup Clean Diagnostics and Repair
**
** @{
    */
/** Execute configured cleanup and repair operations on parsed markup
    */
TIDY_EXPORT int tidyCleanAndRepair(
    TidyDoc tdoc );
```

##### Discussion

@} End Parse group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyConfigErrorCount | tidyConfigErrorCount | tidyConfigErrorCount | tidyConfigErrorCount | tidyConfigErrorCount |

---

```
TIDY_EXPORT uint tidyConfigErrorCount(
    TidyDoc tdoc );
```

##### Discussion

Number of Tidy configuration errors encountered.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyCreate | tidyCreate | tidyCreate | tidyCreate | tidyCreate |

---

```
TIDY_EXPORT TidyDoc tidyCreate(
    void);
```

##### Discussion

@defgroup Basic Basic Operations
\*\*
\*\* Tidy public interface
\*\*
\*\* Several functions return an integer document status:
\*\*
\*\*

```swift
** 0    -> SUCCESS
** >0   -> 1 == TIDY WARNING, 2 == TIDY ERROR
** <0   -> SEVERE ERROR
**
```

\*\*
The following is a short example program.

```c
#include <tidy.h>
#include <buffio.h>
#include <stdio.h>
#include <errno.h>

int main(int argc, char **argv )
{
  const char* input = "<title>Foo</title><p>Foo!";
  TidyBuffer output = {0};
  TidyBuffer errbuf = {0};
  int rc = -1;
  Bool ok;

  TidyDoc tdoc = tidyCreate();                     // Initialize "document"
  printf( "Tidying:\t\%s\\n", input );

  ok = tidyOptSetBool( tdoc, TidyXhtmlOut, yes );  // Convert to XHTML
  if ( ok )
    rc = tidySetErrorBuffer( tdoc, &errbuf );      // Capture diagnostics
  if ( rc >= 0 )
    rc = tidyParseString( tdoc, input );           // Parse the input
  if ( rc >= 0 )
    rc = tidyCleanAndRepair( tdoc );               // Tidy it up!
  if ( rc >= 0 )
    rc = tidyRunDiagnostics( tdoc );               // Kvetch
  if ( rc > 1 )                                    // If error, force output.
    rc = ( tidyOptSetBool(tdoc, TidyForceOutput, yes) ? rc : -1 );
  if ( rc >= 0 )
    rc = tidySaveBuffer( tdoc, &output );          // Pretty Print

  if ( rc >= 0 )
  {
    if ( rc > 0 )
      printf( "\\nDiagnostics:\\n\\n\%s", errbuf.bp );
    printf( "\\nAnd here is the result:\\n\\n\%s", output.bp );
  }
  else
    printf( "A severe error (\%d) occurred.\\n", rc );

  tidyBufFree( &output );
  tidyBufFree( &errbuf );
  tidyRelease( tdoc );
  return rc;
}
```

\*\* @{

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyDetectedGenericXml | tidyDetectedGenericXml | tidyDetectedGenericXml | tidyDetectedGenericXml | tidyDetectedGenericXml |

---

```
TIDY_EXPORT Bool tidyDetectedGenericXml(
    TidyDoc tdoc );
```

##### Discussion

Input is generic XML (not HTML or XHTML)?

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyDetectedHtmlVersion | tidyDetectedHtmlVersion | tidyDetectedHtmlVersion | tidyDetectedHtmlVersion | tidyDetectedHtmlVersion |

---

```
TIDY_EXPORT int tidyDetectedHtmlVersion(
    TidyDoc tdoc );
```

##### Discussion

Detected HTML version: 0, 2, 3 or 4

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyDetectedXhtml | tidyDetectedXhtml | tidyDetectedXhtml | tidyDetectedXhtml | tidyDetectedXhtml |

---

```
TIDY_EXPORT Bool tidyDetectedXhtml(
    TidyDoc tdoc );
```

##### Discussion

Input is XHTML?

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyErrorCount | tidyErrorCount | tidyErrorCount | tidyErrorCount | tidyErrorCount |

---

```
TIDY_EXPORT uint tidyErrorCount(
    TidyDoc tdoc );
```

##### Discussion

Number of Tidy errors encountered. If > 0, output is suppressed
\*\* unless TidyForceOutput is set.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyErrorSummary | tidyErrorSummary | tidyErrorSummary | tidyErrorSummary | tidyErrorSummary |

---

```
TIDY_EXPORT void tidyErrorSummary(
    TidyDoc tdoc );
```

##### Discussion

Write more complete information about errors to current error sink.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGeneralInfo | tidyGeneralInfo | tidyGeneralInfo | tidyGeneralInfo | tidyGeneralInfo |

---

```
TIDY_EXPORT void tidyGeneralInfo(
    TidyDoc tdoc );
```

##### Discussion

Write more general information about markup to current error sink.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGetAppData | tidyGetAppData | tidyGetAppData | tidyGetAppData | tidyGetAppData |

---

```
TIDY_EXPORT ulong tidyGetAppData(
    TidyDoc tdoc );
```

##### Discussion

Get application data set previously

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGetByte | tidyGetByte | tidyGetByte | tidyGetByte | tidyGetByte |

---

```
TIDY_EXPORT uint tidyGetByte(
    TidyInputSource*source );
```

##### Discussion

Helper: get next byte from input source

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGetNextOption | tidyGetNextOption | tidyGetNextOption | tidyGetNextOption | tidyGetNextOption |

---

```
TIDY_EXPORT TidyOption tidyGetNextOption(
    TidyDoc tdoc,
    TidyIterator*pos );
```

##### Discussion

Get next Option

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGetOption | tidyGetOption | tidyGetOption | tidyGetOption | tidyGetOption |

---

```
TIDY_EXPORT TidyOption tidyGetOption(
    TidyDoc tdoc,
    TidyOptionId optId );
```

##### Discussion

Lookup option by ID

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGetOptionByName | tidyGetOptionByName | tidyGetOptionByName | tidyGetOptionByName | tidyGetOptionByName |

---

```
TIDY_EXPORT TidyOption tidyGetOptionByName(
    TidyDoc tdoc,
    ctmbstr optnam );
```

##### Discussion

Lookup option by name

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGetOptionList | tidyGetOptionList | tidyGetOptionList | tidyGetOptionList | tidyGetOptionList |

---

```
/**
Example:
<pre>
TidyIterator itOpt = tidyGetOptionList( tdoc )
while ( itOpt )
{
 TidyOption opt = tidyGetNextOption( tdoc, &itOpt )
 .. get/set option values ..
}
</pre>
    */
TIDY_EXPORT TidyIterator tidyGetOptionList(
    TidyDoc tdoc );
```

##### Discussion

Get iterator for list of option

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyGetRoot | tidyGetRoot | tidyGetRoot | tidyGetRoot | tidyGetRoot |

---

```
/** @defgroup Tree Document Tree
**
** A parsed and, optionally, repaired document is
** represented by Tidy as a Tree, much like a W3C DOM.
** This tree may be traversed using these functions.
** The following snippet gives a basic idea how these
** functions can be used.
**
<pre>
void dumpNode( TidyNode tnod, int indent )
{
 TidyNode child

 for ( child = tidyGetChild(tnod) child child = tidyGetNext(child) )
 {
 ctmbstr name = tidyNodeGetName( child )
 if ( !name )
 {
 switch ( tidyNodeGetType(child) )
 {
 case TidyNode_Root: name = "Root" break
 case TidyNode_DocType: name = "DOCTYPE" break
 case TidyNode_Comment: name = "Comment" break
 case TidyNode_ProcIns: name = "Processing Instruction" break
 case TidyNode_Text: name = "Text" break
 case TidyNode_CDATA: name = "CDATA" break
 case TidyNode_Section: name = "XML Section" break
 case TidyNode_Asp: name = "ASP" break
 case TidyNode_Jste: name = "JSTE" break
 case TidyNode_Php: name = "PHP" break
 case TidyNode_XmlDecl: name = "XML Declaration" break

 case TidyNode_Start:
 case TidyNode_End:
 case TidyNode_StartEnd:
 default:
 assert( name != NULL ) // Shouldn't get here
 break
 }
 }
 assert( name != NULL )
 printf( "\%*.*sNode: \%s\\n", indent, indent, tidy )
 dumpNode( child, indent + 4 )
 }
}

void dumpDoc( TidyDoc tdoc )
{
 dumpNode( tidyGetRoot(tdoc), 0 )
}

void dumpBody( TidyDoc tdoc )
{
 dumpNode( tidyGetBody(tdoc), 0 )
}
</pre>

@{

    */
TIDY_EXPORT TidyNode tidyGetRoot(
    TidyDoc tdoc );
```

##### Discussion

@} end Basic group (again)

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyInitSink | tidyInitSink | tidyInitSink | tidyInitSink | tidyInitSink |

---

```
TIDY_EXPORT Bool tidyInitSink(
    TidyOutputSink*sink,
    void*snkData,
    TidyPutByteFunc pbFunc );
```

##### Discussion

Facilitates user defined sinks by providing
\*\* an entry point to marshal pointers-to-functions.
\*\* Needed by .NET and possibly other language bindings.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyInitSource | tidyInitSource | tidyInitSource | tidyInitSource | tidyInitSource |

---

```
TIDY_EXPORT Bool tidyInitSource(
    TidyInputSource*source,
    void*srcData,
    TidyGetByteFunc gbFunc,
    TidyUngetByteFunc ugbFunc,
    TidyEOFFunc endFunc );
```

##### Discussion

Facilitates user defined source by providing
\*\* an entry point to marshal pointers-to-functions.
\*\* Needed by .NET and possibly other language bindings.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyIsEOF | tidyIsEOF | tidyIsEOF | tidyIsEOF | tidyIsEOF |

---

```
TIDY_EXPORT Bool tidyIsEOF(
    TidyInputSource*source );
```

##### Discussion

Helper: check if input source at end

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyLoadConfig | tidyLoadConfig | tidyLoadConfig | tidyLoadConfig | tidyLoadConfig |

---

```
TIDY_EXPORT int tidyLoadConfig(
    TidyDoc tdoc,
    ctmbstr configFile );
```

##### Discussion

Load an ASCII Tidy configuration file

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyLoadConfigEnc | tidyLoadConfigEnc | tidyLoadConfigEnc | tidyLoadConfigEnc | tidyLoadConfigEnc |

---

```
TIDY_EXPORT int tidyLoadConfigEnc(
    TidyDoc tdoc,
    ctmbstr configFile,
    ctmbstr charenc );
```

##### Discussion

Load a Tidy configuration file with the specified character encoding

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyNodeGetType | tidyNodeGetType | tidyNodeGetType | tidyNodeGetType | tidyNodeGetType |

---

```
/** @defgroup NodeAsk Node Interrogation
**
** Get information about any givent node.
** @{
    */
/* Node info */
TIDY_EXPORT TidyNodeType tidyNodeGetType(
    TidyNode tnod );
```

##### Discussion

@} end Tree group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptCopyConfig | tidyOptCopyConfig | tidyOptCopyConfig | tidyOptCopyConfig | tidyOptCopyConfig |

---

```
TIDY_EXPORT Bool tidyOptCopyConfig(
    TidyDoc tdocTo,
    TidyDoc tdocFrom );
```

##### Discussion

Copy current configuration settings from one document to another

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptDiffThanDefault | tidyOptDiffThanDefault | tidyOptDiffThanDefault | tidyOptDiffThanDefault | tidyOptDiffThanDefault |

---

```
TIDY_EXPORT Bool tidyOptDiffThanDefault(
    TidyDoc tdoc );
```

##### Discussion

Any settings different than default?

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptDiffThanSnapshot | tidyOptDiffThanSnapshot | tidyOptDiffThanSnapshot | tidyOptDiffThanSnapshot | tidyOptDiffThanSnapshot |

---

```
TIDY_EXPORT Bool tidyOptDiffThanSnapshot(
    TidyDoc tdoc );
```

##### Discussion

Any settings different than snapshot?

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetBool | tidyOptGetBool | tidyOptGetBool | tidyOptGetBool | tidyOptGetBool |

---

```
TIDY_EXPORT Bool tidyOptGetBool(
    TidyDoc tdoc,
    TidyOptionId optId );
```

##### Discussion

Get current Option value as a Boolean flag

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetCategory | tidyOptGetCategory | tidyOptGetCategory | tidyOptGetCategory | tidyOptGetCategory |

---

```
TIDY_EXPORT TidyConfigCategory tidyOptGetCategory(
    TidyOption opt );
```

##### Discussion

Get category of given Option

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetCurrPick | tidyOptGetCurrPick | tidyOptGetCurrPick | tidyOptGetCurrPick | tidyOptGetCurrPick |

---

```
TIDY_EXPORT ctmbstr tidyOptGetCurrPick(
    TidyDoc tdoc,
    TidyOptionId optId);
```

##### Discussion

Get current pick list value for option by ID. Useful for enum types.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetDeclTagList | tidyOptGetDeclTagList | tidyOptGetDeclTagList | tidyOptGetDeclTagList | tidyOptGetDeclTagList |

---

```
TIDY_EXPORT TidyIterator tidyOptGetDeclTagList(
    TidyDoc tdoc );
```

##### Discussion

Iterate over user declared tags

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetDefault | tidyOptGetDefault | tidyOptGetDefault | tidyOptGetDefault | tidyOptGetDefault |

---

```
TIDY_EXPORT ctmbstr tidyOptGetDefault(
    TidyOption opt );
```

##### Discussion

Get default value of given Option as a string

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetDefaultBool | tidyOptGetDefaultBool | tidyOptGetDefaultBool | tidyOptGetDefaultBool | tidyOptGetDefaultBool |

---

```
TIDY_EXPORT Bool tidyOptGetDefaultBool(
    TidyOption opt );
```

##### Discussion

Get default value of given Option as a Boolean value

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetDefaultInt | tidyOptGetDefaultInt | tidyOptGetDefaultInt | tidyOptGetDefaultInt | tidyOptGetDefaultInt |

---

```
TIDY_EXPORT ulong tidyOptGetDefaultInt(
    TidyOption opt );
```

##### Discussion

Get default value of given Option as an unsigned integer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetEncName | tidyOptGetEncName | tidyOptGetEncName | tidyOptGetEncName | tidyOptGetEncName |

---

```
TIDY_EXPORT ctmbstr tidyOptGetEncName(
    TidyDoc tdoc,
    TidyOptionId optId );
```

##### Discussion

Get character encoding name. Used with TidyCharEncoding,
\*\* TidyOutCharEncoding, TidyInCharEncoding

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetId | tidyOptGetId | tidyOptGetId | tidyOptGetId | tidyOptGetId |

---

```
TIDY_EXPORT TidyOptionId tidyOptGetId(
    TidyOption opt );
```

##### Discussion

Get ID of given Option

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetIdForName | tidyOptGetIdForName | tidyOptGetIdForName | tidyOptGetIdForName | tidyOptGetIdForName |

---

```
TIDY_EXPORT TidyOptionId tidyOptGetIdForName(
    ctmbstr optnam );
```

##### Discussion

Get option ID by name

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetInt | tidyOptGetInt | tidyOptGetInt | tidyOptGetInt | tidyOptGetInt |

---

```
TIDY_EXPORT ulong tidyOptGetInt(
    TidyDoc tdoc,
    TidyOptionId optId );
```

##### Discussion

Get current Option value as an integer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetName | tidyOptGetName | tidyOptGetName | tidyOptGetName | tidyOptGetName |

---

```
TIDY_EXPORT ctmbstr tidyOptGetName(
    TidyOption opt );
```

##### Discussion

Get name of given Option

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetNextDeclTag | tidyOptGetNextDeclTag | tidyOptGetNextDeclTag | tidyOptGetNextDeclTag | tidyOptGetNextDeclTag |

---

```
TIDY_EXPORT ctmbstr tidyOptGetNextDeclTag(
    TidyDoc tdoc,
    TidyOptionId optId,
    TidyIterator*iter );
```

##### Discussion

Get next declared tag of specified type: TidyInlineTags, TidyBlockTags,
\*\* TidyEmptyTags, TidyPreTags

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetNextPick | tidyOptGetNextPick | tidyOptGetNextPick | tidyOptGetNextPick | tidyOptGetNextPick |

---

```
TIDY_EXPORT ctmbstr tidyOptGetNextPick(
    TidyOption opt,
    TidyIterator*pos );
```

##### Discussion

Get next string value of Option "pick list"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetPickList | tidyOptGetPickList | tidyOptGetPickList | tidyOptGetPickList | tidyOptGetPickList |

---

```
TIDY_EXPORT TidyIterator tidyOptGetPickList(
    TidyOption opt );
```

##### Discussion

Iterate over Option "pick list"

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetType | tidyOptGetType | tidyOptGetType | tidyOptGetType | tidyOptGetType |

---

```
TIDY_EXPORT TidyOptionType tidyOptGetType(
    TidyOption opt );
```

##### Discussion

Get datatype of given Option

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptGetValue | tidyOptGetValue | tidyOptGetValue | tidyOptGetValue | tidyOptGetValue |

---

```
TIDY_EXPORT ctmbstr tidyOptGetValue(
    TidyDoc tdoc,
    TidyOptionId optId );
```

##### Discussion

Get current Option value as a string

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptIsReadOnly | tidyOptIsReadOnly | tidyOptIsReadOnly | tidyOptIsReadOnly | tidyOptIsReadOnly |

---

```
TIDY_EXPORT Bool tidyOptIsReadOnly(
    TidyOption opt );
```

##### Discussion

Is Option read-only?

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptParseValue | tidyOptParseValue | tidyOptParseValue | tidyOptParseValue | tidyOptParseValue |

---

```
TIDY_EXPORT Bool tidyOptParseValue(
    TidyDoc tdoc,
    ctmbstr optnam,
    ctmbstr val );
```

##### Discussion

Set named Option value as a string. Good if not sure of type.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptResetAllToDefault | tidyOptResetAllToDefault | tidyOptResetAllToDefault | tidyOptResetAllToDefault | tidyOptResetAllToDefault |

---

```
TIDY_EXPORT Bool tidyOptResetAllToDefault(
    TidyDoc tdoc );
```

##### Discussion

Reset all options to their default values

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptResetToDefault | tidyOptResetToDefault | tidyOptResetToDefault | tidyOptResetToDefault | tidyOptResetToDefault |

---

```
TIDY_EXPORT Bool tidyOptResetToDefault(
    TidyDoc tdoc,
    TidyOptionId opt );
```

##### Discussion

Reset option to default value by ID

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptResetToSnapshot | tidyOptResetToSnapshot | tidyOptResetToSnapshot | tidyOptResetToSnapshot | tidyOptResetToSnapshot |

---

```
TIDY_EXPORT Bool tidyOptResetToSnapshot(
    TidyDoc tdoc );
```

##### Discussion

Reset config settings to snapshot (after document processing)

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptSaveFile | tidyOptSaveFile | tidyOptSaveFile | tidyOptSaveFile | tidyOptSaveFile |

---

```
/** @addtogroup Basic
** @{
    */
/** Save current settings to named file.
    */
TIDY_EXPORT int tidyOptSaveFile(
    TidyDoc tdoc,
    ctmbstr cfgfil );
```

##### Discussion

@} end Save group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptSaveSink | tidyOptSaveSink | tidyOptSaveSink | tidyOptSaveSink | tidyOptSaveSink |

---

```
TIDY_EXPORT int tidyOptSaveSink(
    TidyDoc tdoc,
    TidyOutputSink*sink );
```

##### Discussion

Save current settings to given output sink.
Only non-default values are written.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptSetBool | tidyOptSetBool | tidyOptSetBool | tidyOptSetBool | tidyOptSetBool |

---

```
TIDY_EXPORT Bool tidyOptSetBool(
    TidyDoc tdoc,
    TidyOptionId optId,
    Bool val );
```

##### Discussion

Set Option value as a Boolean flag

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptSetInt | tidyOptSetInt | tidyOptSetInt | tidyOptSetInt | tidyOptSetInt |

---

```
TIDY_EXPORT Bool tidyOptSetInt(
    TidyDoc tdoc,
    TidyOptionId optId,
    ulong val );
```

##### Discussion

Set Option value as an integer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptSetValue | tidyOptSetValue | tidyOptSetValue | tidyOptSetValue | tidyOptSetValue |

---

```
TIDY_EXPORT Bool tidyOptSetValue(
    TidyDoc tdoc,
    TidyOptionId optId,
    ctmbstr val );
```

##### Discussion

Set Option value as a string

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyOptSnapshot | tidyOptSnapshot | tidyOptSnapshot | tidyOptSnapshot | tidyOptSnapshot |

---

```
TIDY_EXPORT Bool tidyOptSnapshot(
    TidyDoc tdoc );
```

##### Discussion

Take a snapshot of current config settings

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyParseBuffer | tidyParseBuffer | tidyParseBuffer | tidyParseBuffer | tidyParseBuffer |

---

```
TIDY_EXPORT int tidyParseBuffer(
    TidyDoc tdoc,
    TidyBuffer*buf );
```

##### Discussion

Parse markup in given buffer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyParseFile | tidyParseFile | tidyParseFile | tidyParseFile | tidyParseFile |

---

```
/* TODO: Catalog all messages for easy translation
TIDY_EXPORT ctmbstr tidyLookupMessage( int errorNo )
    */
/** @defgroup Parse Document Parse
**
** Parse markup from a given input source. String and filename
** functions added for convenience. HTML/XHTML version determined
** from input.
** @{
    */
/** Parse markup in named file */
TIDY_EXPORT int tidyParseFile(
    TidyDoc tdoc,
    ctmbstr filename );
```

##### Discussion

@} end Memory group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyParseSource | tidyParseSource | tidyParseSource | tidyParseSource | tidyParseSource |

---

```
TIDY_EXPORT int tidyParseSource(
    TidyDoc tdoc,
    TidyInputSource*source);
```

##### Discussion

Parse markup in given generic input source

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyParseStdin | tidyParseStdin | tidyParseStdin | tidyParseStdin | tidyParseStdin |

---

```
TIDY_EXPORT int tidyParseStdin(
    TidyDoc tdoc );
```

##### Discussion

Parse markup from the standard input

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyParseString | tidyParseString | tidyParseString | tidyParseString | tidyParseString |

---

```
TIDY_EXPORT int tidyParseString(
    TidyDoc tdoc,
    ctmbstr content );
```

##### Discussion

Parse markup in given string

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyPutByte | tidyPutByte | tidyPutByte | tidyPutByte | tidyPutByte |

---

```
TIDY_EXPORT void tidyPutByte(
    TidyOutputSink*sink,
    uint byteValue );
```

##### Discussion

Helper: send a byte to output

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyReleaseDate | tidyReleaseDate | tidyReleaseDate | tidyReleaseDate | tidyReleaseDate |

---

```
TIDY_EXPORT ctmbstr tidyReleaseDate(
    void);
```

##### Discussion

Get release date (version) for current library

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyRunDiagnostics | tidyRunDiagnostics | tidyRunDiagnostics | tidyRunDiagnostics | tidyRunDiagnostics |

---

```
TIDY_EXPORT int tidyRunDiagnostics(
    TidyDoc tdoc );
```

##### Discussion

Run configured diagnostics on parsed and repaired markup.
\*\* Must call tidyCleanAndRepair() first.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySaveBuffer | tidySaveBuffer | tidySaveBuffer | tidySaveBuffer | tidySaveBuffer |

---

```
TIDY_EXPORT int tidySaveBuffer(
    TidyDoc tdoc,
    TidyBuffer*buf );
```

##### Discussion

Save to given TidyBuffer object

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySaveFile | tidySaveFile | tidySaveFile | tidySaveFile | tidySaveFile |

---

```
/** @defgroup Save Document Save Functions
**
** Save currently parsed document to the given output sink. File name
** and string/buffer functions provided for convenience.
** @{
    */
/** Save to named file */
TIDY_EXPORT int tidySaveFile(
    TidyDoc tdoc,
    ctmbstr filename );
```

##### Discussion

@} end Clean group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySaveSink | tidySaveSink | tidySaveSink | tidySaveSink | tidySaveSink |

---

```
TIDY_EXPORT int tidySaveSink(
    TidyDoc tdoc,
    TidyOutputSink*sink );
```

##### Discussion

Save to given generic output sink

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySaveStdout | tidySaveStdout | tidySaveStdout | tidySaveStdout | tidySaveStdout |

---

```
TIDY_EXPORT int tidySaveStdout(
    TidyDoc tdoc );
```

##### Discussion

Save to standard output (FILE\*)

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySaveString | tidySaveString | tidySaveString | tidySaveString | tidySaveString |

---

```
TIDY_EXPORT int tidySaveString(
    TidyDoc tdoc,
    tmbstr buffer,
    uint*buflen );
```

##### Discussion

Save document to application buffer. If buffer is not big enough,
\*\* ENOMEM will be returned and the necessary buffer size will be placed
\*\* in \*buflen.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetAppData | tidySetAppData | tidySetAppData | tidySetAppData | tidySetAppData |

---

```
TIDY_EXPORT void tidySetAppData(
    TidyDoc tdoc,
    ulong appData );
```

##### Discussion

Let application store a chunk of data w/ each Tidy instance.
\*\* Useful for callbacks.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetCharEncoding | tidySetCharEncoding | tidySetCharEncoding | tidySetCharEncoding | tidySetCharEncoding |

---

```
TIDY_EXPORT int tidySetCharEncoding(
    TidyDoc tdoc,
    ctmbstr encnam );
```

##### Discussion

Set the input/output character encoding for parsing markup.
\*\* Values include: ascii, latin1, raw, utf8, iso2022, mac,
\*\* win1252, utf16le, utf16be, utf16, big5 and shiftjis. Case in-sensitive.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetErrorBuffer | tidySetErrorBuffer | tidySetErrorBuffer | tidySetErrorBuffer | tidySetErrorBuffer |

---

```
TIDY_EXPORT int tidySetErrorBuffer(
    TidyDoc tdoc,
    TidyBuffer*errbuf );
```

##### Discussion

Set error sink to given buffer

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetErrorFile | tidySetErrorFile | tidySetErrorFile | tidySetErrorFile | tidySetErrorFile |

---

```
TIDY_EXPORT FILE* tidySetErrorFile(
    TidyDoc tdoc,
    ctmbstr errfilnam );
```

##### Discussion

Set error sink to named file

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetErrorSink | tidySetErrorSink | tidySetErrorSink | tidySetErrorSink | tidySetErrorSink |

---

```
TIDY_EXPORT int tidySetErrorSink(
    TidyDoc tdoc,
    TidyOutputSink*sink );
```

##### Discussion

Set error sink to given generic sink

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetFreeCall | tidySetFreeCall | tidySetFreeCall | tidySetFreeCall | tidySetFreeCall |

---

```
TIDY_EXPORT Bool tidySetFreeCall(
    TidyFree ffree );
```

##### Discussion

Give Tidy a free() replacement

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetInCharEncoding | tidySetInCharEncoding | tidySetInCharEncoding | tidySetInCharEncoding | tidySetInCharEncoding |

---

```
TIDY_EXPORT int tidySetInCharEncoding(
    TidyDoc tdoc,
    ctmbstr encnam );
```

##### Discussion

Set the input encoding for parsing markup.
\*\* As for tidySetCharEncoding but only affects the input encoding
\*

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetMallocCall | tidySetMallocCall | tidySetMallocCall | tidySetMallocCall | tidySetMallocCall |

---

```
TIDY_EXPORT Bool tidySetMallocCall(
    TidyMalloc fmalloc );
```

##### Discussion

Give Tidy a malloc() replacement

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetOutCharEncoding | tidySetOutCharEncoding | tidySetOutCharEncoding | tidySetOutCharEncoding | tidySetOutCharEncoding |

---

```
TIDY_EXPORT int tidySetOutCharEncoding(
    TidyDoc tdoc,
    ctmbstr encnam );
```

##### Discussion

Set the output encoding.
\*

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetPanicCall | tidySetPanicCall | tidySetPanicCall | tidySetPanicCall | tidySetPanicCall |

---

```
TIDY_EXPORT Bool tidySetPanicCall(
    TidyPanic fpanic );
```

##### Discussion

Give Tidy an "out of memory" handler

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetReallocCall | tidySetReallocCall | tidySetReallocCall | tidySetReallocCall | tidySetReallocCall |

---

```
TIDY_EXPORT Bool tidySetReallocCall(
    TidyRealloc frealloc );
```

##### Discussion

Give Tidy a realloc() replacement

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidySetReportFilter | tidySetReportFilter | tidySetReportFilter | tidySetReportFilter | tidySetReportFilter |

---

```
TIDY_EXPORT Bool tidySetReportFilter(
    TidyDoc tdoc,
    TidyReportFilter filtCallback );
```

##### Discussion

Give Tidy a filter callback to use

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyStatus | tidyStatus | tidyStatus | tidyStatus | tidyStatus |

---

```
TIDY_EXPORT int tidyStatus(
    TidyDoc tdoc );
```

##### Discussion

Get status of current document.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyUngetByte | tidyUngetByte | tidyUngetByte | tidyUngetByte | tidyUngetByte |

---

```
TIDY_EXPORT void tidyUngetByte(
    TidyInputSource*source,
    uint byteValue );
```

##### Discussion

Helper: unget byte back to input source

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tidyWarningCount | tidyWarningCount | tidyWarningCount | tidyWarningCount | tidyWarningCount |

---

```
TIDY_EXPORT uint tidyWarningCount(
    TidyDoc tdoc );
```

##### Discussion

Number of Tidy warnings encountered.

## Typedefs

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyEOFFunc | TidyEOFFunc | TidyEOFFunc | TidyEOFFunc | TidyEOFFunc |

---

```
typedef Bool (*TidyEOFFunc)(
    ulong sourceData );
```

##### Discussion

Input Callback: is end of input?

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyFree | TidyFree | TidyFree | TidyFree | TidyFree |

---

```
typedef void (*TidyFree)(
    void*buf );
```

##### Discussion

Callback for "free" replacement

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyGetByteFunc | TidyGetByteFunc | TidyGetByteFunc | TidyGetByteFunc | TidyGetByteFunc |

---

```
/** @defgroup IO I/O and Messages
**
** By default, Tidy will define, create and use
** instances of input and output handlers for
** standard C buffered I/O (i.e. FILE* stdin,
** FILE* stdout and FILE* stderr for content
** input, content output and diagnostic output,
** respectively. A FILE* cfgFile input handler
** will be used for config files. Command line
** options will just be set directly.
**
** @{
    */
/*****************
 Input Source
    */
/** Input Callback: get next byte of input */
typedef int (*TidyGetByteFunc)(
    ulong sourceData );
```

##### Discussion

@} end Configuration group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyMalloc | TidyMalloc | TidyMalloc | TidyMalloc | TidyMalloc |

---

```
/** @defgroup Memory Memory Allocation
**
** By default, Tidy will use its own wrappers
** around standard C malloc/free calls.
** These wrappers will abort upon any failures.
** If any are set, all must be set.
** Pass NULL to clear previous setting.
**
** May be used to set environment-specific allocators
** such as used by web server plugins, etc.
**
** @{
    */
/** Callback for "malloc" replacement */
typedef void* (*TidyMalloc)(
    size_t len );
```

##### Discussion

@} end IO group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyOptCallback | TidyOptCallback | TidyOptCallback | TidyOptCallback | TidyOptCallback |

---

```
/** @defgroup Configuration Configuration Options
**
** Functions for getting and setting Tidy configuration options.
** @{
    */
/** Applications using TidyLib may want to augment command-line and
** configuration file options. Setting this callback allows an application
** developer to examine command-line and configuration file options after
** TidyLib has examined them and failed to recognize them.
    */
typedef Bool (*TidyOptCallback)(
    ctmbstr option,
    ctmbstr value );
```

##### Discussion

@} end Basic group

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyPanic | TidyPanic | TidyPanic | TidyPanic | TidyPanic |

---

```
typedef void (*TidyPanic)(
    ctmbstr mssg );
```

##### Discussion

Callback for "out of memory" panic state

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyPutByteFunc | TidyPutByteFunc | TidyPutByteFunc | TidyPutByteFunc | TidyPutByteFunc |

---

```
typedef void (*TidyPutByteFunc)(
    ulong sinkData,
    byte bt );
```

##### Discussion

Output callback: send a byte to output

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyRealloc | TidyRealloc | TidyRealloc | TidyRealloc | TidyRealloc |

---

```
typedef void* (*TidyRealloc)(
    void*buf,
    size_t len );
```

##### Discussion

Callback for "realloc" replacement

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyReportFilter | TidyReportFilter | TidyReportFilter | TidyReportFilter | TidyReportFilter |

---

```
typedef Bool (*TidyReportFilter)(
    TidyDoc tdoc,
    TidyReportLevel lvl,
    uint line,
    uint col,
    ctmbstr mssg );
```

##### Discussion

Callback to filter messages by diagnostic level:
\*\* info, warning, etc. Just set diagnostic output
\*\* handler to redirect all diagnostics output. Return true
\*\* to proceed with output, false to cancel.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TidyUngetByteFunc | TidyUngetByteFunc | TidyUngetByteFunc | TidyUngetByteFunc | TidyUngetByteFunc |

---

```
typedef void (*TidyUngetByteFunc)(
    ulong sourceData,
    byte bt );
```

##### Discussion

Input Callback: unget a byte of input

## #defines

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EndOfStream | EndOfStream | EndOfStream | EndOfStream | EndOfStream |

---

__Value:__ 0xffffffff (-1)

```
#define EndOfStream
```

##### Discussion

End of input "character"

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

Last Updated: 2006-06-20
