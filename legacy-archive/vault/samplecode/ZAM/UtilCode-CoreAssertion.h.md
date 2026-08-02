---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/UtilCode_CoreAssertion_h.html
archived_at: '2026-07-18T03:28:34.597902Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](UtilCode-DialogUtil.c.md)[Previous](UtilCode-CoreAssertion.c.md)

# UtilCode/CoreAssertion.h

```

#define CoreDebug 1


#ifdef CoreDebug

    void CoreAssert(short, char *, char *, short);

    #define Assert(x)   if(!(x)) CoreAssert((short)(x),#x, __FILE__, __LINE__)
    #define ASSERT(x)   if(!(x)) CoreAssert((short)(x),#x, __FILE__, __LINE__)
    #define AssertErr(x) if(x) CoreAssert((short)(x),#x, __FILE__, __LINE__)
#else
    #define Assert      //
    #define ASSERT      //
    #define AssertErr   //

#endif
```

[Next](UtilCode-DialogUtil.c.md)[Previous](UtilCode-CoreAssertion.c.md)

