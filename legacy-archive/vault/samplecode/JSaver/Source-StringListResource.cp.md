---
title: JSaver
apple_id: DTS10000219
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JSaver/Listings/Source_StringListResource_cp.html
archived_at: '2026-07-18T03:13:13.812522Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JSaver](JSaver.md)


[Next](Source-StringListResource.h.md)[Previous](Source-NewAppletDialog.h.md)

# Source/StringListResource.cp

```c
/*
 * StringListResource.cp
 */

#include "StringListResource.h"

StringListResource::StringListResource(short id) : fStrings(NULL), fCount(0)
{
    fStrings = ::GetResource('STR#', id);
    if (fStrings != NULL) {
        HLockHi(fStrings);
        StringList* strings = *(StringList**)fStrings;
        fCount = strings->count;
        pText = strings->strings;
    }
}

StringListResource::~StringListResource()
{
    if (fStrings != NULL) ::ReleaseResource(fStrings);
}

StringPtr StringListResource::First()
{
    if (fStrings != NULL) {
        StringList* strings = *(StringList**)fStrings;
        fCount = strings->count;
        pText = strings->strings;
    }
    return Next();
}

StringPtr StringListResource::Next()
{
    StringPtr result = NULL;

    if (fCount > 0) {
        result = pText;
        pText += (1 + *pText);
        --fCount;
    }

    return result;
}
```

[Next](Source-StringListResource.h.md)[Previous](Source-NewAppletDialog.h.md)

