---
title: Code Size Performance Guidelines
apple_id: 10000149i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/SharedPages.html
archived_at: '2026-07-18T01:46:40.266574Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Size Performance Guidelines](Introduction%20to%20Code%20Size%20Performance%20Guidelines.md)


[Next](Minimizing%20Your%20Exported%20Symbols.md)[Previous](Improving%20Locality%20of%20Reference.md)

# Reducing Shared Memory Pages

As noted in [Overview of the Mach-O Executable Format](Overview%20of%20the%20Mach-O%20Executable%20Format.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dalkciffeossfjjbq), the data in the `__DATA` segment of a Mach-O binary is writable and thus shareable (via copy-on-write). Writable data slows down paging performance in low-memory situations by increasing the number of pages that may need to be written to disk. For frameworks, writable data is shared initially but has the potential to be replicated to the memory space of each process.

Reducing the amount of dynamic or non-constant data in an executable can have a significant impact on performance, especially for frameworks The following sections show you how to reduce the size of your executable’s `__DATA` segment, and thus reduced the number of shared memory pages.

The easiest way to make the `__DATA` segment smaller is to mark more globally scoped data as constant. Most of the time, it’s easy to mark data as constant. For example, if you’re never going to modify the elements in an array, you should include the `const` keyword in the array declaration, as shown here:

```
const int fibonacci_table[8] = {1, 1, 2, 3, 5, 8, 13, 21};
```

Remember to mark pointers as constant (when appropriate). In the following example, the strings `"a"` and `"b"` are constant, but the array pointer `foo` is not:

```
static const char *foo[] = {"a", "b"};
foo[1] = "c";       // OK: foo[1] is not constant.
```

To mark the entire declaration as constant, you need to add the `const` keyword to the pointer to make the pointer constant. In the following example, both the array and its contents are constant:

```
static const char *const foo[] = {"a", "b"};
foo[1] = "c";       // NOT OK: foo[1] is constant.
```

Sometimes you may want to rewrite your code to separate out the constant data. The following example contains an array of structures in which only one field is declared `const`. Because the entire array isn’t declared `const`, it is stored in the `__DATA` segment.

```
struct {
    const char *imageName;
    NSImage *image;
} images[100] = {
    {"FooImage", nil},
    {"FooImage2", nil}
    // and so on
};
```

To store as much of this data as possible in the `__TEXT` segment, create two parallel arrays, one marked constant and one not:

```
const char *const imageNames[100] = { "FooImage", /* . . . */ };
NSImage *imageInstances[100] = { nil, /* . . . */ };
```

If an uninitialized data item contains pointers, the compiler can’t store the item in the `__TEXT` segment. Strings end up in the `__TEXT` segment’s `__cstring` section but the rest of the data item, including the pointers to the strings, ends up in the `__DATA` segment’s `const` section. In the following example, `daytimeTable` would end up split between the `__TEXT` and `__DATA` segments, even though it’s constant:

```
struct daytime {
    const int value;
    const char *const name;
};

const struct daytime daytimeTable[] = {
    {1, "dawn"},
    {2, "day"},
    {3, "dusk"},
    {4, "night"}
};
```

To place the whole array in the `__TEXT` segment, you must rewrite this structure so it uses a fixed-size char array instead of a string pointer, as shown in the following example:

```
struct daytime {
    const int value;
    const char name[6];
};

const struct daytime daytimeTable[] = {
    {1, {'d', 'a', 'w', 'n', '\0'}},
    {2, {'d', 'a', 'y', '\0'}},
    {3, {'d', 'u', 's', 'k', '\0'}},
    {4, {'n', 'i', 'g', 'h', 't', '\0'}}
};
```

Unfortunately, there’s no good solution if the strings are of widely varying sizes, because this solution would leave a lot of unused space.

The array is split onto two segments because the compiler always stores constant strings in the `__TEXT` segment’s `__cstring` section. If the compiler stored the rest of the array in the `__DATA` segment’s `__data` section, it’s possible that the strings and the pointers to the strings would end up on different pages. If that happened, the system would have to update the pointers to the strings with the new addresses, and it can’t do that if the pointers are in the `__TEXT` segment because the `__TEXT` segment is marked read-only. So the pointers to the strings, and the rest of the array along with it, must be stored in the `const` section of the `__DATA` segment. The `__const` section is reserved for data declared `const` that couldn’t be placed in the `__TEXT` segment.

As is pointed out in [Overview of the Mach-O Executable Format](Overview%20of%20the%20Mach-O%20Executable%20Format.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dalkciffeossfjjbq), the compiler stores uninitialized static data in the `__bss` section of the `__DATA` segment and stores initialized data in the `__data` section. If you have only a small amount of static data in the `__bss` section, you might want to consider moving it to the `__data` section instead. Storing data in two different sections increases the number of memory pages used by the executable, which in turn increases the potential for paging.

The goal of merging the `__bss` and `__data` sections is to reduce the number of memory pages used by your application. If moving data into the `__data` section increases the number of memory pages in that section, there is no benefit to this technique. In fact, adding to the pages in the `__data` section increases the amount of time spent reading and initializing that data at launch time.

Suppose you declare the following static variables:

```
static int x;
static short conv_table[128];
```

To move these variables into the `__data` section of your executable’s `__DATA` segment, you would change the definition to the following:

```
static int x = 0;
static short conv_table[128] = {0};
```


The compiler puts any duplicate symbols it encounters in the `__common` section of the `__DATA` segment (see [Overview of the Mach-O Executable Format](Overview%20of%20the%20Mach-O%20Executable%20Format.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dalkciffeossfjjbq)). The problem here is the same as with uninitialized static variables. If an executable’s non-constant global data is distributed among several sections, it is more likely that this data will be on different memory pages; consequently, the pages may have to be swapped in and out separately. The goal for the `__common` section is the same as that for the `__bss` section: to eliminate it from your executable if you have a small amount of data in it.

A common source of a tentative-definition symbol is the definition of that symbol in a header file. Typically, headers declare a symbol but do not include the definition of that symbol; the definition is instead provided in an implementation file. But definitions appearing in header files can result in that code or data appearing in every implementation file that includes the header file. The solution to this problem is to ensure that header files contain only declarations, not definitions.

For functions, you would obviously declare a prototype for that function in your header file and put the definition of that function in your implementation file. For global variables and data structures, you should do something similar. Rather than defining the variable in your header file, define it in your implementation file and initialize it appropriately. Then, declare that variable in your header file, preceding the declaration with the `extern` keyword. This technique localizes the variable definition to one file while still allowing access to that variable from other files.

You can also get tentative-definition symbols when you accidentally import the same header file twice. To make sure you do not do this, include preprocessor directives to prohibit the inclusion of files that have already been included. Thus, in your header file, you would have the following code:

```
#ifndef MYHEADER_H
#define MYHEADER_H
// Your header file declarations. . .
#endif
```

Then when you want to include that header file, include it in the following way:

```c
#ifndef MYHEADER_H
#include "MyHeader.h"
#endif
```


You have several tools at your disposal for finding out how much memory your non-constant data is occupying. These tools report on various aspects of data usage.

While your application or framework is running, use the `size` and `pagestuff` tools to see how big your various data sections are and which symbols they contain. Some things to look for include the following:

- To find executables with lots of non-constant data, check for files with large `__data` sections in the `__DATA` segment.
- Check for variables and symbols in the `__bss` and `__common` sections that can be removed or moved to the `__data` section.
- To locate data that, although declared constant, the compiler can’t treat as constant, check for executables or object files with a `__const` section in the `__DATA` segment.

Some of the bigger consumers of memory in the `__DATA` segment are fixed-size global arrays initialized but not declared `const`. You can sometimes find these tables by searching your source code for “`[] = {`“.

You can also let the compiler help you find where arrays can be made constant. Put `const` in front of all the initialized arrays you suspect might be read-only and recompile. If an array is not truly read-only, it will not compile. Remove the offending `const` and retry.

[Next](Minimizing%20Your%20Exported%20Symbols.md)[Previous](Improving%20Locality%20of%20Reference.md)

