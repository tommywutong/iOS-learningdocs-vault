---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/gle_copy_h.html
archived_at: '2026-07-18T03:29:15.515476Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](gle-exangle.c.md)[Previous](ReadMe.txt.md)

# gle/copy.h

```

/*
 *
 * Written By Linas Vepstas November 1991 
 */


#define COPY_THREE_WORDS(A,B) {                     \
    struct three_words { int a, b, c, };                \
    *(struct three_words *) (A) = *(struct three_words *) (B);  \
}

#define COPY_FOUR_WORDS(A,B) {                      \
    struct four_words { int a, b, c, d, };              \
    *(struct four_words *) (A) = *(struct four_words *) (B);    \
}

/* ============================================================= */
```

[Next](gle-exangle.c.md)[Previous](ReadMe.txt.md)

