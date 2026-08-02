---
title: JSaver
apple_id: DTS10000219
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JSaver/Listings/Source_StringListResource_h.html
archived_at: '2026-07-18T03:13:13.845046Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JSaver](JSaver.md)


[Next](Source-StubMod.c.md)[Previous](Source-StringListResource.cp.md)

# Source/StringListResource.h

```
/*
 * StringListResource.h
 * By Patrick Beard
 */

#pragma once

struct StringList {
    short count;
    unsigned char strings[1];
};

typedef struct StringList StringList;

class StringListResource {
public:
    StringListResource(short id);
    ~StringListResource();

    StringPtr First();
    StringPtr Next();

private:
    void operator delete(void *) {}

private:
    Handle fStrings;
    int fCount;
    unsigned char* pText;
};
```

[Next](Source-StubMod.c.md)[Previous](Source-StringListResource.cp.md)

