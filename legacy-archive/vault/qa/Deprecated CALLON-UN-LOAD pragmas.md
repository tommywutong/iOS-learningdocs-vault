---
title: Deprecated CALL_ON_[UN]LOAD pragmas
apple_id: DTS10003576
resource_type: QA
platform: macOS
topic: Xcode
technology: null
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/qa/qa1429/_index.html
archived_at: '2026-07-18T02:30:40.748895Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1429

# Deprecated CALL_ON_[UN]LOAD pragmas

## Q:  I'm trying to build an old project that used the CALL_ON_LOAD and CALL_ON_UNLOAD pragmas and I'm getting warnings that these pragmas are deprecated and that I should use constructor and destructor attributes instead. What are constructor and destructor attributes?

A: The CALL_ON_LOAD and CALL_ON_UNLOAD #pragmas were added to GCC by Apple prior to the release of Mac OS X 10.0. They were used to specify routines to be called when a dynamic library was loaded or unloaded. They have now been deprecated and replaced by the constructor and destructor function attributes. A function with the constructor attribute is called when a dynamic library is loaded. Similarly, a function with the destructor attribute is called when a dynamic library is unloaded. When the constructor or destructor function is called, the return value of the function is ignored, and any parameters of the function are undefined. Note: This is a syntactical change for the compiler only; the pragmas and the attributes generate binary compatible code.

The constructor and destructor attributes are supported by gcc as of version 2.5.

__Listing 1__  Using #pragmas (deprecated, don't use)

```
// (deprecated, don't use) #pragma CALL_ON_LOAD my_mod_init_func static void my_mod_init_func(void) {     /* do my init stuff */ }  #pragma CALL_ON_UNLOAD my_mod_term_func static void my_mod_term_func(void) {     /* do my termination stuff */ }
```


__Listing 2__  Using constructor and destructor attributes

```
void MyInitFunc(void) __attribute__ ((constructor)) {     /* do my init stuff */ }  void MyTermFunc(void) __attribute__ ((destructor)) {     /* do my termination stuff */ }
```


__Listing 3__  Using constructor and destructor attributes with gcc 4.0

```
extern void MyInitFunc(void) __attribute__ ((constructor)); extern void MyTermFunc(void) __attribute__ ((destructor));  void MyInitFunc(void) {     /* do my init stuff */ }  void MyTermFunc(void) {     /* do my termination stuff */ }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-01-10 |  |
| 2005-08-10 | Adding gcc 4.0 information |
| 2005-07-05 | New document that replace deprecated CALL_ON_[UN]LOAD pragmas with constructor [destructor] function attributes. |

