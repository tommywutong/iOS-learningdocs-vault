---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Host-Misc.html
archived_at: '2026-07-15T07:31:02.064151Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Filesystem](Filesystem.md#apple-izuwyzltpfzxizln),
Up: [Host Config](Host-Config.md#apple-jbxxg5bninxw4ztjm4)

---

### 16.3 Host Misc

**`FATAL_EXIT_CODE`**
: A C expression for the status code to be returned when the compiler
exits after serious errors. The default is the system-provided macro
``EXIT_FAILURE`', or ``1`' if the system doesn't define that
macro. Define this macro only if these defaults are incorrect.

**`SUCCESS_EXIT_CODE`**
: A C expression for the status code to be returned when the compiler
exits without serious errors. (Warnings are not serious errors.) The
default is the system-provided macro ``EXIT_SUCCESS`', or ``0`' if
the system doesn't define that macro. Define this macro only if these
defaults are incorrect.

**`USE_C_ALLOCA`**
: Define this macro if GCC should use the C implementation of `alloca`
provided by `libiberty.a`. This only affects how some parts of the
compiler itself allocate memory. It does not change code generation.

When GCC is built with a compiler other than itself, the C `alloca`
is always used. This is because most other implementations have serious
bugs. You should define this macro only on a system where no
stack-based `alloca` can possibly work. For instance, if a system
has a small limit on the size of the stack, GCC's builtin `alloca`
will not work reliably.

**`COLLECT2_HOST_INITIALIZATION`**
: If defined, a C statement (sans semicolon) that performs host-dependent
initialization when `collect2` is being initialized.

**`GCC_DRIVER_HOST_INITIALIZATION`**
: If defined, a C statement (sans semicolon) that performs host-dependent
initialization when a compilation driver is being initialized.

**`HOST_LONG_LONG_FORMAT`**
: If defined, the string used to indicate an argument of type `long
long` to functions like `printf`. The default value is
`"ll"`.

In addition, if `configure` generates an incorrect definition of
any of the macros in `auto-host.h`, you can override that
definition in a host configuration header. If you need to do this,
first see if it is possible to fix `configure`.
