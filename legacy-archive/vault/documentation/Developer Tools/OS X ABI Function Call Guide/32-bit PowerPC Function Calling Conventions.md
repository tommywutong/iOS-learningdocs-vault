---
title: OS X ABI Function Call Guide
apple_id: TP40002521
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2010-11-17'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/LowLevelABI/100-32-bit_PowerPC_Function_Calling_Conventions/32bitPowerPC.html
archived_at: '2026-07-15T07:25:12.878687Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X ABI Function Call Guide](Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md)


[Next](64-bit%20PowerPC%20Function%20Calling%20Conventions.md)[Previous](Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md)

# 32-bit PowerPC Function Calling Conventions

When functions (routines) call other functions (subroutines), they may need to pass arguments to the called functions. The called functions access those arguments as _parameters_. Conversely, some functions return a _result_ or return value to their callers. Both arguments and results can be passed using the 32-bit PowerPC architecture registers or the runtime stack, depending on the data type of the values involved. For the successful and efficient passing of values between routines and subroutines, GCC follows strict rules when it generates a program’s object code.

This article describes the data types that can be used to manipulate the arguments and results of function calls, how routines pass arguments to the subroutines they call, and how functions pass results to their callers. It also lists the registers available in the 32-bit PowerPC architecture and whether their value is preserved after a function call.

Using the correct data types for your variables and setting the appropriate _data alignment_ for your data can maximize the performance and portability of your programs. Data alignment specifies how data is laid out in memory.

Table 1 lists the ANSI C scalar data types and their sizes and natural alignment in this environment.

__Table 1__  Size and natural alignment of the scalar data types

| Data type | Size and natural alignment (in bytes) |
| `_Bool`, `bool` | 4 |
| `unsigned char` | 1 |
| `char`, `signed char` | 1 |
| `unsigned short` | 2 |
| `signed short` | 2 |
| `unsigned int` | 4 |
| `signed int` | 4 |
| `unsigned long` | 4 |
| `signed long` | 4 |
| `unsigned long long` | 8 |
| `signed long long` | 8 |
| `float` | 4 |
| `double` | 8 |
| `long double` | 16\* |
| pointer | 4 |

(\*) In OS X v10.4 and later and GCC 4.0 and later, the size of the `long double` extended precision data type is 16 bytes (it’s made up of two 8-byte doubles). In earlier versions of OS X and GCC, `long double` is equivalent to `double`. You should not use the `long double` type when you use GCC 4.0 or later to develop or in programs targeted at OS X versions earlier than 10.4.

These are some important details about the 32-bit PowerPC environment:

- A byte is 8 bits long.
- A null pointer has a value of 0.
- This environment uses the big-endian byte ordering scheme to store numeric and pointer data types. That is, the most significant bytes go first, followed by the least significant bytes.
- This environment uses the two’s-complement binary representation for signed integer data types.
- Arithmetic for the 64-bit integer data types must be synthesized by the compiler since the 32-bit PowerPC architecture does not implement 64-bit integer math operations.
- The `float` and `double` data types conform to the IEEE-754 standard representation. For the value range and precise format of floating-point data types, see _PowerPC Numerics_ in Performance Documentation.

This environment supports multiple data alignment modes. The alignment of data types falls into two categories:

- __Natural alignment.__ The alignment of a data type when allocated in memory or assigned a memory address.

  The natural alignment of a data type is its size. [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomi) shows the natural alignment of each data type supported by this environment.
- __Embedding alignment.__ The alignment of a data type within a composite data structure.

For example, the alignment of an `unsigned short` variable on the stack may differ from that of an `unsigned short` element embedded in a data structure.

The embedding alignment for data structures varies depending on the alignment mode selected. Generally, you can set the alignment mode using compiler options or `#pragma` statements. You should consider the compatibility and performance issues described later in this section when choosing a particular alignment mode.

These are the embedding alignment modes available in the 32-bit PowerPC environment:

- __Power alignment mode__ is derived from the alignment rules used by the IBM XLC compiler for the AIX operating system. It is the default alignment mode for the PowerPC-architecture version of GCC used on AIX and OS X. Because this mode is most likely to be compatible between PowerPC-architecture compilers from different vendors, it’s typically used with data structures that are shared between different programs.

  The rules for power alignment are:

  - The embedding alignment of the first element in a data structure is equal to the element’s natural alignment.
  - For subsequent elements with a natural alignment less than 4 bytes, the embedding alignment of each element is equal to its natural alignment.
  - For subsequent elements that have a natural alignment greater than 4 bytes, the embedding alignment is 4, unless the element is a `vector`.
  - The embedding alignment for `vector` elements is always 16 bytes.
  - The embedding alignment of a composite data type (array or data structure) is determined by the largest embedding alignment of its members.
  - The total size of a composite type is rounded up to a multiple of its embedding alignment, and is padded with null bytes.

  Because the natural alignment of the `double` and `long long` data types is greater than 4 bytes, they may not be appropriately aligned in power alignment mode. Any misalignment impairs performance when such data members are accessed. When you use these data types for any element after the first element, the compiler pads the structure to align the elements to the next multiple of their natural alignment.
- __Mac68K alignment mode__ is usually used with legacy data structures inherited from Mac OS 9 and earlier systems. New code should not need to use this alignment mode except to preserve compatibility with older data structures.

  The rules for Mac68K alignment are:

  - The embedding alignment of the `char` data type is 1 byte.
  - The embedding alignment of all other data types (except `vector`) is 2 bytes.
  - The embedding alignment for the `vector` data type is 16 bytes.
  - The total size of a composite data type is rounded up to a multiple of 2 bytes.
- __Natural alignment mode__ uses the natural alignment of each data type as its embedding alignment. Use this alignment mode to obtain the highest performance when using the `double`, `long long`, and `long double` data types.
- __Packed alignment mode__ contains no alignment padding between elements (the alignment for all data types is 1 byte). Use this alignment mode when you need a data structure to use as little memory as possible. Note, however, that packed alignment can significantly lower the performance of your application.

Table 2 lists the alignment for structure fields of the fundamental data types and composite data types in the supported alignment modes.

__Table 2__  Alignment for structure fields

| Data type | Power alignment | Natural alignment | Mac68K alignment | Packed alignment |
| `_Bool`, `bool` | 4 | 4 | 2 | 1 |
| `char` | 1 | 1 | 1 | 1 |
| `short` | 2 | 2 | 2 | 1 |
| `int` | 4 | 4 | 2 | 1 |
| `long` | 4 | 4 | 2 | 1 |
| `long long` | 4 or 8 | 8 | 2 | 1 |
| `float` | 4 | 4 | 2 | 1 |
| `double` | 4 or 8 | 8 | 2 | 1 |
| `long double` |  |  | 2 | 1 |
| `vector` | 16 | 16 | 16 | 1 |
| Composite (data structure or array) | 4, 8, or 16 | 1, 2, 4, 8, or 16 | 2 | 1 |

With GCC you can control data-structure alignment by adding `#pragma` statements to your source code or by using command-line options. The power alignment mode is used if you do not specify otherwise.

To set the alignment mode, use the `gcc` flags `-malign-power`, `-malign-mac68k`, and `-malign-natural`. To use a specific alignment mode in a data structure, add this statement just before the data-structure declaration:

```
#pragma option align=<mode>
```

Replace `<mode>` with `power`, `mac68k`, `natural`, or `packed`. To restore the previous alignment mode, use `reset` as the alignment mode in a `#pragma` statement:

```
#pragma option align=reset
```


This section details the process of calling a function and passing arguments to it, and how functions return values to their callers.

This environment uses a stack that grows downward and contains linkage information, local variables, and a function’s parameter information, as shown in Figure 1. (To help prevent the execution of malicious code on the stack, GCC protects the stack against execution.)

__Figure 1__  Stack layout

!

The _stack pointer_ (SP) points to the bottom of the stack. The stack has a fixed frame size, which is known at compile time.

The calling routine’s stack frame includes a _parameter area_ and some linkage information. The parameter area has the arguments the caller passes to the called function or space for them, depending on the type of each argument and the availability of registers (see [Passing Arguments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomju) for details). Since the calling routine may call several functions, in the 32-bit PowerPC environment the parameter area is normally large enough to accommodate the largest argument list of all the functions the caller calls. It is the calling routine’s responsibility to set up the parameter area before each function call. The called function is responsible for accessing the arguments placed in the parameter area.

The first 32 bytes in the parameter area correspond to the general-purpose registers GPR3 through GPR10. When data is placed in a general-purpose register and not duplicated in the parameter area, the corresponding section in the parameter area is reserved in case the called function needs to copy the value in the register to the stack. Table 3 shows the correspondence of parameter area locations to the general-purpose registers that can be used to pass arguments.

__Table 3__  Parameter area to general-purpose register mapping

| Stack frame location | Register |
| `SP+24` | GPR3 |
| `SP+28` | GPR4 |
| `SP+32` | GPR5 |
| `SP+36` | GPR6 |
| `SP+40` | GPR7 |
| `SP+44` | GPR8 |
| `SP+48` | GPR9 |
| `SP+52` | GPR10 |

These are the alignment rules followed when parameters are placed in the parameter area or in GPR3 through GPR10:

1. All nonvector parameters are aligned on 4-byte boundaries.
2. Vector parameters are aligned on 16-byte boundaries.
3. Noncomposite parameters (that is, parameters that are not arrays or data structures) smaller than 4 bytes occupy the high-order bytes of their 4-byte area.
4. Composite parameters (arrays, structures, and unions) 1 or 2 bytes in size occupy the low-order bytes of their 4-byte area. They are preceded by padding to 4 bytes.

   This rule is inconsistent with other 32-bit PowerPC binary interfaces. In AIX and Mac OS 9 (and earlier), padding bytes always follow the data structure even in the case of composite parameters smaller than 4 bytes.
5. Composite parameters 3 bytes or larger in size occupy the high-order bytes of their 4-byte area. They are followed by padding to make a multiple of 4 bytes, with the padding bytes being undefined.

For example, consider the `foo` function, declared like this:

```
void foo(SInt32 i1, float  f1, double d1, SInt16 s1, double d2,
         UInt8  c1, UInt16 s2, float  f2, SInt32 i2);
```

Table 4 shows how the function’s arguments are assigned locations in the parameter area. The assignment takes into account the 4-byte alignment required for each argument.

__Table 4__  Parameter area layout for the `foo` call

| Parameter | Type | Location | Data size and padding (in bytes) |
| `i1` | `SInt32` | `SP+24` | 4, 0 |
| `f1` | `float` | `SP+28` | 4, 0 |
| `d1` | `double` | `SP+32` | 8, 0 |
| `s1` | `SInt16` | `SP+40` | 2, 2 |
| `d2` | `double` | `SP+44` | 8, 0 |
| `c1` | `UInt8` | `SP+52` | 1, 3 |
| `s2` | `UInt16` | `SP+56` | 2, 2 |
| `f2` | `float` | `SP+60` | 4, 0 |
| `i2` | `SInt32` | `SP+64` | 4, 0 |

The calling routine’s _linkage area_ holds a number of values, some of which are saved by the calling routine and some by the called function. The elements within the linkage area are:

- __The link register (LR).__ Its value is saved at `8(SP)` by the called function if it chooses to do so. The link register holds the return address of the instruction that follows a branch and link instruction.
- __The condition register (CR).__ Its value may be saved at `4(SP)` by the called function. The condition register holds the results of comparison operations. As with the link register, the called procedure is not required to save this value.
- __The stack pointer (SP).__ Its value may be saved at `0(SP)` by the called function as part of its stack frame. _Leaf functions_ are not required to save the the stack pointer. A leaf function is a function that does not call any other functions.

The linkage area is at the top of the stack, adjacent to the stack pointer. This positioning is necessary so that the calling routine can find and restore the values stored there and also allow the called function to find the caller’s parameter area. This placement means that a routine cannot push and pop parameters from the stack once the stack frame is set up.

The stack frame also includes space for the called function’s local variables. However, some registers are also available for use by the called function; see [Register Preservation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomjy) for details. If the subroutine contains more local variables than would fit in the registers, it uses additional space on the stack. The size of the local-variable area is determined at compile time. Once a stack frame is allocated, the size of the local-variable area does not change.

The called function is responsible for allocating its own stack frame, making sure to preserve 16-byte alignment in the stack. This operation is accomplished by a section of code called the _prolog_, which the compiler places before the body of the subroutine. After the body of the subroutine, the compiler places an _epilog_ to restore the processor to the state it was prior to the subroutine call.

The compiler-generated prolog code does the following:

1. Decrements the stack pointer to account for the new stack frame and writes the previous value of the stack pointer to its own linkage area, which ensures the stack can be restored to its original state after returning from the call.

   It is important that the decrement and update tasks happen atomically (for example, with `stwu`, `stwux`, `stdu`, or `stdux`) so that the stack pointer and back-link are in a consistent state. Otherwise, asynchronous signals or interrupts could corrupt the stack.
2. Saves all nonvolatile general-purpose and floating-point registers into the saved-registers area. Note that if the called function does not change a particular nonvolatile register, it does not save it.
3. Saves the link-register and condition-register values in the caller’s linkage area, if needed.

Listing 1 shows an example of a subroutine prolog. Notice that the order of these actions differs from the order previously described.

__Listing 1__  Example prolog

```
linkageArea = 24                                           ; size in 32-bit PowerPC ABI
params = 32                                                ; callee parameter area
localVars = 0                                              ; callee local variables
numGPRs = 0                                                ; volatile GPRs used by callee
numFPRs = 0                                                ; volatile FPRs used by callee

spaceToSave = linkageArea + params + localVars + 4*numGPRs + 8*numFPRs
spaceToSaveAligned = ((spaceToSave+15) & (-16))            ; 16-byte-aligned stack

_functionName:                                             ; PROLOG
    mflr        r0                                         ; extract return address
    stw         r0, 8(SP)                                  ; save the return address
    stwu        SP, -spaceToSaveAligned(SP)                ; skip over caller save area
```

At the end of the subroutine, the compiler-generated epilog does the following:

1. Restores the nonvolatile general-purpose and floating-point registers that were saved in the stack frame.

   Nonvolatile registers are saved in the new stack frame before the stack pointer is updated only when they fit within the space beneath the stack pointer, where a new stack frame would normally be allocated, also known as the _red zone_. The red zone is by definition large enough to hold all nonvolatile general-purpose and floating-point registers but not the nonvolatile vector registers. See [The Red Zone](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvonq) for details.
2. Restores the condition-register and link-register values that were stored in the linkage area.
3. Restores the stack pointer to its previous value.
4. Returns control to the the calling routine using the address stored in the link register.

Listing 2 shows an example epilog.

__Listing 2__  Example epilog

```
                                                   ; EPILOG
lwz            r0, spaceToSaveAligned + 8(SP)      ; get the return address
mtlr           r0                                  ;    into the link register
addi           SP, SP, spaceToSaveAligned          ; restore stack pointer
blr                                                ;    and branch to the return address
```

The VRSAVE register is used to specify which vector registers must be saved during a thread or process context switch.Listing 3 shows an example prolog that sets up VRSAVE so that vector registers V0 through V2 are saved. Listing 3 also includes the epilog that restores VRSAVE to its previous state.

__Listing 3__  Example usage of the VRSAVE register

```
#define VRSAVE 256                           //  VRSAVE IS SPR# 256

    _functionName:
        mfspr    r2, VRSAVE                  ; get vector of live VRs
        oris         r0, r2, 0xE000          ; set bits 0-2 since we use V0..V2
        mtspr    VRSAVE, r0                  ; update live VR vector before using any VRs

        ; Now, V0..V2 can be safely used.
        ; Function body goes here.

        mtspr    VRSAVE, r2                  ; restore VRSAVE
        blr                                  ; return to caller
```


The space beneath the stack pointer, where a new stack frame would normally be allocated by a subroutine, is called the _red zone_. The red zone, shown in Figure 2, is considered part of the current stack frame. This area is not modified by asynchronous pushes, such as signals or interrupt handlers. Therefore, the red zone may be used for any purpose as long as a new stack frame does not need to be added to the stack. However, the contents of the red zone are assumed to be destroyed by any synchronous call.

__Figure 2__  The red zone

!

For example, because a leaf function does not call any other functions—and, therefore, does not allocate a parameter area on the stack—it can use the red zone. Furthermore, such a function does not need to use the stack to store local variables; it needs to save only the nonvolatile registers it uses for local variables. Since, by definition, no more than one leaf function is active at any time within a thread, there is no possibility of multiple leaf functions competing for the same red zone space.

A leaf function may or may not allocate a stack frame and decrement the stack pointer. When it doesn’t allocate a stack frame, a leaf function stores the link register and condition register values in the linkage area of the routine that calls it (if necessary) and stores the values of any nonvolatile registers it uses in the red zone. This streamlining means that a leaf function’s prolog and epilog do minimal work; they do not have to set up and take down a stack frame.

The size of the red zone is 224 bytes, which is enough space to store the values of nineteen 32-bit general-purpose registers and eighteen 64-bit floating-point registers, rounded up to the nearest 16-byte boundary. If a leaf function’s red zone usage would exceed the red zone size, it must set up a stack frame, just as functions that call other functions do.

In the C language, functions can declare their parameters using one of three conventions:

- The types of all parameters is specified in the function’s prototype. For example:

```
int foo(int, short);
```

  In this case, the type of all the function’s parameters is known at compile time.
- The function’s prototype declares some fixed parameters and some nonfixed parameters. The group of nonfixed parameters is also called a _variable argument list_. For example:

```
int foo(int, ...);
```

  In this case, the type of one of the function’s parameters in known at compile time. The type of the nonfixed parameters is not known.
- The function has no prototype or uses a pre–ANSI C declaration. For example:

```
int foo();
```

  In this case, the type of all the function’s parameters is unknown at compile time.

When the compiler generates the prolog for a function call, it uses the information from the function’s declaration to decide how arguments are passed to the function. When the compiler knows the type of a parameter, it passes it in the most efficient way possible. But when the type is unknown, it passes the parameter using the safest approach, which may involve placing data both in registers and in the parameter area. For called functions to access their parameters correctly, it’s important that they know when parameters are passed in the stack or in registers.

Arguments are passed in the stack, in registers, or both, depending on their types and the availability of registers. There are three types of registers: general purpose, floating point, and vector. General-purpose registers (GPRs) are 32-bit registers that can manipulate integral values and pointers. Floating-point registers (FPRs) are 64-bit registers that can manipulate single-precision and double-precision floating-point values. Vector registers are 128-bit registers that can manipulate 4 through 16 chunks of data in parallel.

The registers that can be used to pass arguments to called functions are the general-purpose registers GPR3 through GPR10, the floating-point registers FPR1 through FPR13, and the vector registers V2 through V13 (see [Register Preservation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomjy) for details). These registers are also known as _parameter registers_.

Typically, the called routine obtains arguments from registers. However, the caller generates a parameter area in the caller’s stack frame that is large enough to hold all the arguments passed to the called function, regardless of how many of the arguments are actually passed in registers. (You can think of the parameter area as a data structure that has space to hold all the arguments in a given call.) There are several reasons for these scheme:

- It provides the called function with space in the stack to store a register-based parameter if it wants to use one of the parameter registers for some other purpose. For example, the callee can use these space to pass arguments to a function it calls.
- Functions with variable argument lists must often access their parameters from RAM, not from registers. Such functions must reserve 32 bytes (8 registers) in the parameter area to hold the parameter values.

To simplify debugging, GCC writes parameters from the parameter registers into the parameter area in the stack frame. This allows you to see all the parameters by looking only at the parameter area.

The compiler uses the following rules when passing arguments to subroutines:

- Parameters whose type is known at compile time are processed as follows:

  1. Scalar, non–floating-point elements are placed in the general-purpose registers GPR3 through GPR10. As each register is used, the caller allocates the register’s corresponding section in the parameter area, as described in [Stack Structure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomjz). When general-purpose registers are exhausted, the caller places scalar, non–floating-point elements in the parameter area.
  2. The caller places floating-point parameters in the floating-point registers FPR1 through FPR13. As each floating-point register is used, the caller skips one or more general-purpose registers, based on the size of the parameter. (For example, a `float` element causes one (4-byte) general-purpose register to be skipped. A `double` element causes two general-purpose registers to be skipped.) When floating-point registers are exhausted, the caller places floating-point elements in the parameter area.
  3. The caller places structures (`struct` elements) with only one noncomposite member in general-purpose or floating-point registers, depending on whether the member is an integer or a floating-point value. For example, the caller places a structure comprised of a `float` member in a floating-point register, not a general-purpose register. When registers of the required type are exhausted, the caller places structures in the parameter area.
  4. The caller places `vector` parameters in vector registers V2 through V13. For procedures with a fixed number of parameters, the presence of vectors doesn’t affect the allocation of general-purpose registers and floating-point registers. The caller doesn’t allocate space for `vector` elements in the parameter area of its stack frame unless the number of `vector` elements exceeds the number of usable vector registers.
  5. When the number of parameters exceeds the number of usable registers, the caller places the excess parameters in the parameter area.
- Parameters whose type is not known at compile time (functions with variable-argument lists or using pre–ANSI C prototypes) are processed as follows:

  1. The caller places nonvector elements both in general-purpose registers and in floating-point registers.

     Because the compiler doesn’t know the type of the parameter, it cannot determine whether the argument should be passed in a general-purpose register or in a floating-point register. Therefore, callers place each argument in a floating-point register _and_ the corresponding general-purpose registers based on the argument’s size.
  2. The caller places `vector` elements in vector registers _and_ general-purpose registers (each vector element requires four general-purpose registers. The caller also allocates space in the parameter area that corresponds to the general-purpose registers used.

For example, consider the `foo` function, declared like this:

```
void foo(SInt32 i1, float  f1, double d1, SInt16 s1, double d2,
         UInt8  c1, UInt16 s2, float  f2, SInt32 i2);
```

The caller places each argument to `foo` in a general-purpose register, a floating-point register, or the parameter area, depending on the parameter’s data type and register availability. Table 5 describes this process.

__Table 5__  Assigning parameters to registers and the parameter area

| Parameter | Type | Placed in | Reason |
| `i1` | `SInt32` | GPR3 | Noncomposite, non–floating-point element. |
| `f1` | `float` | FPR1 | Floating-point element. GPR4 is skipped. |
| `d1` | `double` | FPR2 | Double-precision, floating-point element. GPR5 and GPR6 are skipped. |
| `s1` | `SInt16` | GPR7 | Noncomposite, non–floating-point element. |
| `d2` | `double` | FPR3 | Double-precision, floating-point element. GPR8 and GPR9 are skipped. |
| `c1` | `UInt8` | GPR10 | Noncomposite, non–floating-point element. |
| `s2` | `UInt16` | `SP+56`, low half of word | No general-purpose registers available. |
| `f2` | `float` | FPR4 | Floating-point element. |
| `i2` | `SInt32` | `SP+60` | No general-purpose registers available. |

Figure 3 illustrates the assignment of the `foo` parameters to registers and the parameter area. Keep in mind that the only parameters placed in the parameter area are `s2` and `i2`.

__Figure 3__  Assignment of parameters to registers and the parameter area

!

The called function can access the fixed parameters as usual. But it copies the general-purpose registers to the parameter area and accesses the values from there. Listing 4 shows a routine that accesses undefined parameters by walking through the stack.

__Listing 4__  A variable-argument procedure

```c
#include <stdarg.h>
double dsum(int count, ...) {
    double sum = 0.0;
    double val;
    va_list arg;
    va_start(arg, count);
    while (count > 0) {
        val = va_arg(arg, double);
        sum += val;
        count--;
    }
    va_end(arg);
    return sum;
}
```


The following list describes where a function’s return value is passed to the caller.

- Scalars smaller than 4 bytes (such as `char` and `short`) are placed in the low word of GPR3. The register’s high word is undefined.
- Scalars 4 bytes in size (such as `long`, `int`, and pointers, including array pointers) are placed in GPR3.
- Values of type `long long` are returned in the high word of GPR3 and the low word of GPR4.
- Floating-point values are placed in FPR1.
- Composite values (such as `struct` and `union`) and values larger than 4 bytes are placed at the location pointed to by GPR3. See [Passing Arguments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomju) for more information.

Table 6 lists the 32-bit PowerPC architecture registers used in this environment and their volatility in function calls. Registers that must preserve their value after a function call are called _nonvolatile_.

__Table 6__  Processor registers in the 32-bit PowerPC architecture

| Type | Name | Preserved | Notes |
| General-purpose register | GPR0 | No |  |
|  | GPR1 | Yes | Used as the stack pointer to store parameters and other temporary data items. |
|  | GPR2 | No | Available for general use. |
|  | GPR3 | No | The caller passes parameter values to the called procedure in GPR3 through GPR10. The caller may also pass the address to storage where the callee places its return value in this register. |
|  | GPR4–GPR10 | No | Used by callers to pass parameter values to called functions (see notes for GPR3). |
|  | GPR11 | Yes in nested functions. No in leaf functions. | In nested functions, the caller passes its stack frame to the nested function in this register. In leaf functions, the register is available. For details on nested functions, see the GCC documentation. This register is also used by lazy stubs in dynamic code generation to point to the lazy pointer. |
|  | GPR12 | No | Set to the address of the branch target before an indirect call for dynamic code generation. This register is not set for a function that has been called directly; therefore, functions that may be called directly should not depend on this register being set up correctly. See _[Mach-O Programming Topics](../Mach-O%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjz)_ for more information. |
|  | GPR13–GPR31 | Yes |  |
| Floating-point register | FPR0 | No |  |
|  | FPR1–FPR13 | No | Used to pass floating-point parameters in function calls. |
|  | FPR14–FPR31 | Yes |  |
| Vector register | V0–V19 | No | The caller passes vector parameters in V2 to V13 during a function call. |
|  | V20–V31 | Yes |  |
| Special-purpose vector register | VRSAVE | Yes | 32-bit special-purpose register. Each bit in this register indicates whether the corresponding vector register must be saved during a thread or process context switch. |
| Link register | LR | No | Stores the return address of the calling routine that called the current subroutine. |
| Count register | CTR | No |  |
| Fixed-point exception register | XER | No |  |
| Condition register fields | CR0, CR1 | No |  |
|  | CR2–CR4 | Yes |  |
|  | CR5–CR7 | No |  |

[Next](64-bit%20PowerPC%20Function%20Calling%20Conventions.md)[Previous](Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md)

