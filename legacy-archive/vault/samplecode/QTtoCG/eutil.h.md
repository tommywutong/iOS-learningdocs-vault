---
title: QTtoCG
apple_id: DTS10000504
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTtoCG/Listings/eutil_h.html
archived_at: '2026-07-18T03:21:24.440540Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTtoCG](QTtoCG.md)


[Next](Document%20Revision%20History.md)[Previous](eutil.c.md)

# eutil.h

```
#ifndef EUTIL_H_
#define EUTIL_H_

//??#include "getopt.h"

extern const char *program_name;

void set_program_name(const char *p);

int int_value(int c, char *arg, void (*usage)(void));

float float_value(int c, const char *arg, void (*usage)(void));

void invalid_number_of_arguments(void (*usage)(void))
    __attribute__((noreturn));

void eprintf(const char *format, ...)
    __attribute__((format(printf, 1, 2)));

void error(const char *format, ...)
    __attribute__((format(printf, 1, 2)));

void fatal(const char *format, ...)
    __attribute__((format(printf, 1, 2), noreturn));


#endif  /* EUTIL_H_ */
```

[Next](Document%20Revision%20History.md)[Previous](eutil.c.md)

