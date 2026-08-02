---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_34.html
archived_at: '2026-07-15T07:31:03.517980Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Remote%20Serial%20Protocol.md), [next](GNU%20GENERAL%20PUBLIC%20LICENSE.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [The GDB Agent Expression Mechanism](Debugging%20with%20GDB.md#apple-krhugmzugm)

In some applications, it is not feasable for the debugger to interrupt
the program's execution long enough for the developer to learn anything
helpful about its behavior. If the program's correctness depends on its
real-time behavior, delays introduced by a debugger might cause the
program to fail, even when the code itself is correct. It is useful to
be able to observe the program's behavior without interrupting it.

Using GDB's `trace` and `collect` commands, the user can
specify locations in the program, and arbitrary expressions to evaluate
when those locations are reached. Later, using the `tfind`
command, she can examine the values those expressions had when the
program hit the trace points. The expressions may also denote objects
in memory -- structures or arrays, for example -- whose values GDB
should record; while visiting a particular tracepoint, the user may
inspect those objects as if they were in memory at that moment.
However, because GDB records these values without interacting with the
user, it can do so quickly and unobtrusively, hopefully not disturbing
the program's behavior.

When GDB is debugging a remote target, the GDB __agent__ code running
on the target computes the values of the expressions itself. To avoid
having a full symbolic expression evaluator on the agent, GDB translates
expressions in the source language into a simpler bytecode language, and
then sends the bytecode to the agent; the agent then executes the
bytecode, and records the values for GDB to retrieve later.

The bytecode language is simple; there are forty-odd opcodes, the bulk
of which are the usual vocabulary of C operands (addition, subtraction,
shifts, and so on) and various sizes of literals and memory reference
operations. The bytecode interpreter operates strictly on machine-level
values -- various sizes of integers and floating point numbers -- and
requires no information about types or symbols; thus, the interpreter's
internal data structures are simple, and each bytecode requires only a
few native machine instructions to implement it. The interpreter is
small, and strict limits on the memory and time required to evaluate an
expression are easy to determine, making it suitable for use by the
debugging agent in real-time applications.

## [General Bytecode Design](Debugging%20with%20GDB.md#apple-krhugmzugq)

The agent represents bytecode expressions as an array of bytes. Each
instruction is one byte long (thus the term __bytecode__). Some
instructions are followed by operand bytes; for example, the `goto`
instruction is followed by a destination for the jump.

The bytecode interpreter is a stack-based machine; most instructions pop
their operands off the stack, perform some operation, and push the
result back on the stack for the next instruction to consume. Each
element of the stack may contain either a integer or a floating point
value; these values are as many bits wide as the largest integer that
can be directly manipulated in the source language. Stack elements
carry no record of their type; bytecode could push a value as an
integer, then pop it as a floating point value. However, GDB will not
generate code which does this. In C, one might define the type of a
stack element as follows:

```
union agent_val {
  LONGEST l;
  DOUBLEST d;
};
```

where `LONGEST` and `DOUBLEST` are `typedef` names for
the largest integer and floating point types on the machine.

By the time the bytecode interpreter reaches the end of the expression,
the value of the expression should be the only value left on the stack.
For tracing applications, `trace` bytecodes in the expression will
have recorded the necessary data, and the value on the stack may be
discarded. For other applications, like conditional breakpoints, the
value may be useful.

Separate from the stack, the interpreter has two registers:

**`pc`**
: The address of the next bytecode to execute.

**`start`**
: The address of the start of the bytecode expression, necessary for
interpreting the `goto` and `if_goto` instructions.

Neither of these registers is directly visible to the bytecode language
itself, but they are useful for defining the meanings of the bytecode
operations.

There are no instructions to perform side effects on the running
program, or call the program's functions; we assume that these
expressions are only used for unobtrusive debugging, not for patching
the running code.

Most bytecode instructions do not distinguish between the various sizes
of values, and operate on full-width values; the upper bits of the
values are simply ignored, since they do not usually make a difference
to the value computed. The exceptions to this rule are:

**memory reference instructions (`ref`n)**
: There are distinct instructions to fetch different word sizes from
memory. Once on the stack, however, the values are treated as full-size
integers. They may need to be sign-extended; the `ext` instruction
exists for this purpose.

**the sign-extension instruction (`ext` n)**
: These clearly need to know which portion of their operand is to be
extended to occupy the full length of the word.

If the interpreter is unable to evaluate an expression completely for
some reason (a memory location is inaccessible, or a divisor is zero,
for example), we say that interpretation "terminates with an error".
This means that the problem is reported back to the interpreter's caller
in some helpful way. In general, code using agent expressions should
assume that they may attempt to divide by zero, fetch arbitrary memory
locations, and misbehave in other ways.

Even complicated C expressions compile to a few bytecode instructions;
for example, the expression `x + y * z` would typically produce
code like the following, assuming that `x` and `y` live in
registers, and `z` is a global variable holding a 32-bit
`int`:

```
reg 1
reg 2
const32 address of z
ref32
ext 32
mul
add
end
```

In detail, these mean:

**`reg 1`**
: Push the value of register 1 (presumably holding `x`) onto the
stack.

**`reg 2`**
: Push the value of register 2 (holding `y`).

**`const32 address of z`**
: Push the address of `z` onto the stack.

**`ref32`**
: Fetch a 32-bit word from the address at the top of the stack; replace
the address on the stack with the value. Thus, we replace the address
of `z` with `z`'s value.

**`ext 32`**
: Sign-extend the value on the top of the stack from 32 bits to full
length. This is necessary because `z` is a signed integer.

**`mul`**
: Pop the top two numbers on the stack, multiply them, and push their
product. Now the top of the stack contains the value of the expression
`y * z`.

**`add`**
: Pop the top two numbers, add them, and push the sum. Now the top of the
stack contains the value of `x + y * z`.

**`end`**
: Stop executing; the value left on the stack top is the value to be
recorded.

## [Bytecode Descriptions](Debugging%20with%20GDB.md#apple-krhugmzugu)

Each bytecode description has the following form:

**`add` (0x02): a b => a+b**
: Pop the top two stack items, a and b, as integers; push
their sum, as an integer.

In this example, `add` is the name of the bytecode, and
`(0x02)` is the one-byte value used to encode the bytecode, in
hexidecimal. The phrase "a b => a+b" shows
the stack before and after the bytecode executes. Beforehand, the stack
must contain at least two values, a and b; since the top of
the stack is to the right, b is on the top of the stack, and
a is underneath it. After execution, the bytecode will have
popped a and b from the stack, and replaced them with a
single value, a+b. There may be other values on the stack below
those shown, but the bytecode affects only those shown.

Here is another example:

**`const8` (0x22) n: => n**
: Push the 8-bit integer constant n on the stack, without sign
extension.

In this example, the bytecode `const8` takes an operand n
directly from the bytecode stream; the operand follows the `const8`
bytecode itself. We write any such operands immediately after the name
of the bytecode, before the colon, and describe the exact encoding of
the operand in the bytecode stream in the body of the bytecode
description.

For the `const8` bytecode, there are no stack items given before
the =>; this simply means that the bytecode consumes no values
from the stack. If a bytecode consumes no values, or produces no
values, the list on either side of the => may be empty.

If a value is written as a, b, or n, then the bytecode
treats it as an integer. If a value is written is addr, then the
bytecode treats it as an address.

We do not fully describe the floating point operations here; although
this design can be extended in a clean way to handle floating point
values, they are not of immediate interest to the customer, so we avoid
describing them, to save time.

**`float` (0x01): =>**
: Prefix for floating-point bytecodes. Not implemented yet.

**`add` (0x02): a b => a+b**
: Pop two integers from the stack, and push their sum, as an integer.

**`sub` (0x03): a b => a-b**
: Pop two integers from the stack, subtract the top value from the
next-to-top value, and push the difference.

**`mul` (0x04): a b => a\*b**
: Pop two integers from the stack, multiply them, and push the product on
the stack. Note that, when one multiplies two n-bit numbers
yielding another n-bit number, it is irrelevant whether the
numbers are signed or not; the results are the same.

**`div_signed` (0x05): a b => a/b**
: Pop two signed integers from the stack; divide the next-to-top value by
the top value, and push the quotient. If the divisor is zero, terminate
with an error.

**`div_unsigned` (0x06): a b => a/b**
: Pop two unsigned integers from the stack; divide the next-to-top value
by the top value, and push the quotient. If the divisor is zero,
terminate with an error.

**`rem_signed` (0x07): a b => a modulo b**
: Pop two signed integers from the stack; divide the next-to-top value by
the top value, and push the remainder. If the divisor is zero,
terminate with an error.

**`rem_unsigned` (0x08): a b => a modulo b**
: Pop two unsigned integers from the stack; divide the next-to-top value
by the top value, and push the remainder. If the divisor is zero,
terminate with an error.

**`lsh` (0x09): a b => a<<b**
: Pop two integers from the stack; let a be the next-to-top value,
and b be the top value. Shift a left by b bits, and
push the result.

**`rsh_signed` (0x0a): a b => `(signed)`a>>b**
: Pop two integers from the stack; let a be the next-to-top value,
and b be the top value. Shift a right by b bits,
inserting copies of the top bit at the high end, and push the result.

**`rsh_unsigned` (0x0b): a b => a>>b**
: Pop two integers from the stack; let a be the next-to-top value,
and b be the top value. Shift a right by b bits,
inserting zero bits at the high end, and push the result.

**`log_not` (0x0e): a => !a**
: Pop an integer from the stack; if it is zero, push the value one;
otherwise, push the value zero.

**`bit_and` (0x0f): a b => a&b**
: Pop two integers from the stack, and push their bitwise `and`.

**`bit_or` (0x10): a b => a|b**
: Pop two integers from the stack, and push their bitwise `or`.

**`bit_xor` (0x11): a b => a^b**
: Pop two integers from the stack, and push their bitwise
exclusive-`or`.

**`bit_not` (0x12): a => ~a**
: Pop an integer from the stack, and push its bitwise complement.

**`equal` (0x13): a b => a=b**
: Pop two integers from the stack; if they are equal, push the value one;
otherwise, push the value zero.

**`less_signed` (0x14): a b => a<b**
: Pop two signed integers from the stack; if the next-to-top value is less
than the top value, push the value one; otherwise, push the value zero.

**`less_unsigned` (0x15): a b => a<b**
: Pop two unsigned integers from the stack; if the next-to-top value is less
than the top value, push the value one; otherwise, push the value zero.

**`ext` (0x16) n: a => a, sign-extended from n bits**
: Pop an unsigned value from the stack; treating it as an n-bit
twos-complement value, extend it to full length. This means that all
bits to the left of bit n-1 (where the least significant bit is bit
0) are set to the value of bit n-1. Note that n may be
larger than or equal to the width of the stack elements of the bytecode
engine; in this case, the bytecode should have no effect.
The number of source bits to preserve, n, is encoded as a single
byte unsigned integer following the `ext` bytecode.

**`zero_ext` (0x2a) n: a => a, zero-extended from n bits**
: Pop an unsigned value from the stack; zero all but the bottom n
bits. This means that all bits to the left of bit n-1 (where the
least significant bit is bit 0) are set to the value of bit n-1.
The number of source bits to preserve, n, is encoded as a single
byte unsigned integer following the `zero_ext` bytecode.

**`ref8` (0x17): addr => a**
:

**`ref16` (0x18): addr => a**
:

**`ref32` (0x19): addr => a**
:

**`ref64` (0x1a): addr => a**
: Pop an address addr from the stack. For bytecode
`ref`n, fetch an n-bit value from addr, using the
natural target endianness. Push the fetched value as an unsigned
integer.
Note that addr may not be aligned in any particular way; the
`refn` bytecodes should operate correctly for any address.
If attempting to access memory at addr would cause a processor
exception of some sort, terminate with an error.

**`ref_float` (0x1b): addr => d**
:

**`ref_double` (0x1c): addr => d**
:

**`ref_long_double` (0x1d): addr => d**
:

**`l_to_d` (0x1e): a => d**
:

**`d_to_l` (0x1f): d => a**
: Not implemented yet.

**`dup` (0x28): a => a a**
: Push another copy of the stack's top element.

**`swap` (0x2b): a b => b a**
: Exchange the top two items on the stack.

**`pop` (0x29): a =>**
: Discard the top value on the stack.

**`if_goto` (0x20) offset: a =>**
: Pop an integer off the stack; if it is non-zero, branch to the given
offset in the bytecode string. Otherwise, continue to the next
instruction in the bytecode stream. In other words, if a is
non-zero, set the `pc` register to `start` + offset.
Thus, an offset of zero denotes the beginning of the expression.
The offset is stored as a sixteen-bit unsigned value, stored
immediately following the `if_goto` bytecode. It is always stored
most significant byte first, regardless of the target's normal
endianness. The offset is not guaranteed to fall at any particular
alignment within the bytecode stream; thus, on machines where fetching a
16-bit on an unaligned address raises an exception, you should fetch the
offset one byte at a time.

**`goto` (0x21) offset: =>**
: Branch unconditionally to offset; in other words, set the
`pc` register to `start` + offset.
The offset is stored in the same way as for the `if_goto` bytecode.

**`const8` (0x22) n: => n**
:

**`const16` (0x23) n: => n**
:

**`const32` (0x24) n: => n**
:

**`const64` (0x25) n: => n**
: Push the integer constant n on the stack, without sign extension.
To produce a small negative value, push a small twos-complement value,
and then sign-extend it using the `ext` bytecode.
The constant n is stored in the appropriate number of bytes
following the `const`b bytecode. The constant n is
always stored most significant byte first, regardless of the target's
normal endianness. The constant is not guaranteed to fall at any
particular alignment within the bytecode stream; thus, on machines where
fetching a 16-bit on an unaligned address raises an exception, you
should fetch n one byte at a time.

**`reg` (0x26) n: => a**
: Push the value of register number n, without sign extension. The
registers are numbered following GDB's conventions.
The register number n is encoded as a 16-bit unsigned integer
immediately following the `reg` bytecode. It is always stored most
significant byte first, regardless of the target's normal endianness.
The register number is not guaranteed to fall at any particular
alignment within the bytecode stream; thus, on machines where fetching a
16-bit on an unaligned address raises an exception, you should fetch the
register number one byte at a time.

**`trace` (0x0c): addr size =>**
: Record the contents of the size bytes at addr in a trace
buffer, for later retrieval by GDB.

**`trace_quick` (0x0d) size: addr => addr**
: Record the contents of the size bytes at addr in a trace
buffer, for later retrieval by GDB. size is a single byte
unsigned integer following the `trace` opcode.
This bytecode is equivalent to the sequence `dup const8 size
trace`, but we provide it anyway to save space in bytecode strings.

**`trace16` (0x30) size: addr => addr**
: Identical to trace_quick, except that size is a 16-bit big-endian
unsigned integer, not a single byte. This should probably have been
named `trace_quick16`, for consistency.

**`end` (0x27): =>**
: Stop executing bytecode; the result should be the top element of the
stack. If the purpose of the expression was to compute an lvalue or a
range of memory, then the next-to-top of the stack is the lvalue's
address, and the top of the stack is the lvalue's size, in bytes.

## [Using Agent Expressions](Debugging%20with%20GDB.md#apple-krhugmzugy)

Here is a sketch of a full non-stop debugging cycle, showing how agent
expressions fit into the process.

- The user selects trace points in the program's code at which GDB should
  collect data.
- The user specifies expressions to evaluate at each trace point. These
  expressions may denote objects in memory, in which case those objects'
  contents are recorded as the program runs, or computed values, in which
  case the values themselves are recorded.
- GDB transmits the tracepoints and their associated expressions to the
  GDB agent, running on the debugging target.
- The agent arranges to be notified when a trace point is hit. Note that,
  on some systems, the target operating system is completely responsible
  for collecting the data; see section [Tracing on Symmetrix](#apple-kncugmzuha).
- When execution on the target reaches a trace point, the agent evaluates
  the expressions associated with that trace point, and records the
  resulting values and memory ranges.
- Later, when the user selects a given trace event and inspects the
  objects and expression values recorded, GDB talks to the agent to
  retrieve recorded data as necessary to meet the user's requests. If the
  user asks to see an object whose contents have not been recorded, GDB
  reports an error.

## [Varying Target Capabilities](Debugging%20with%20GDB.md#apple-krhugmzug4)

Some targets don't support floating-point, and some would rather not
have to deal with `long long` operations. Also, different targets
will have different stack sizes, and different bytecode buffer lengths.

Thus, GDB needs a way to ask the target about itself. We haven't worked
out the details yet, but in general, GDB should be able to send the
target a packet asking it to describe itself. The reply should be a
packet whose length is explicit, so we can add new information to the
packet in future revisions of the agent, without confusing old versions
of GDB, and it should contain a version number. It should contain at
least the following information:

- whether floating point is supported
- whether `long long` is supported
- maximum acceptable size of bytecode stack
- maximum acceptable length of bytecode expressions
- which registers are actually available for collection
- whether the target supports disabled tracepoints

## [Tracing on Symmetrix](Debugging%20with%20GDB.md#apple-krhugmzuha)

This section documents the API used by the GDB agent to collect data on
Symmetrix systems.

Cygnus originally implemented these tracing features to help EMC
Corporation debug their Symmetrix high-availability disk drives. The
Symmetrix application code already includes substantial tracing
facilities; the GDB agent for the Symmetrix system uses those facilities
for its own data collection, via the API described here.

**Function: DTC_RESPONSE __adbg_find_memory_in_frame__ _(FRAME_DEF \*frame, char \*address, char \*\*buffer, unsigned int \*size)_**
: 
Search the trace frame frame for memory saved from address.
If the memory is available, provide the address of the buffer holding
it; otherwise, provide the address of the next saved area.

- If the memory at address was saved in frame, set
  `*buffer` to point to the buffer in which that memory was
  saved, set `*size` to the number of bytes from address
  that are saved at `*buffer`, and return
  `OK_TARGET_RESPONSE`. (Clearly, in this case, the function will
  always set `*size` to a value greater than zero.)
- If frame does not record any memory at address, set
  `*size` to the distance from address to the start of
  the saved region with the lowest address higher than address. If
  there is no memory saved from any higher address, set `*size`
  to zero. Return `NOT_FOUND_TARGET_RESPONSE`.

These two possibilities allow the caller to either retrieve the data, or
walk the address space to the next saved area.

This function allows the GDB agent to map the regions of memory saved in
a particular frame, and retrieve their contents efficiently.

This function also provides a clean interface between the GDB agent and
the Symmetrix tracing structures, making it easier to adapt the GDB
agent to future versions of the Symmetrix system, and vice versa. This
function searches all data saved in frame, whether the data is
there at the request of a bytecode expression, or because it falls in
one of the format's memory ranges, or because it was saved from the top
of the stack. EMC can arbitrarily change and enhance the tracing
mechanism, but as long as this function works properly, all collected
memory is visible to GDB.

The function itself is straightforward to implement. A single pass over
the trace frame's stack area, memory ranges, and expression blocks can
yield the address of the buffer (if the requested address was saved),
and also note the address of the next higher range of memory, to be
returned when the search fails.

As an example, suppose the trace frame `f` has saved sixteen bytes
from address `0x8000` in a buffer at `0x1000`, and thirty-two
bytes from address `0xc000` in a buffer at `0x1010`. Here are
some sample calls, and the effect each would have:

**`adbg_find_memory_in_frame (f, (char*) 0x8000, &buffer, &size)`**
: This would set `buffer` to `0x1000`, set `size` to
sixteen, and return `OK_TARGET_RESPONSE`, since `f` saves
sixteen bytes from `0x8000` at `0x1000`.

**`adbg_find_memory_in_frame (f, (char *) 0x8004, &buffer, &size)`**
: This would set `buffer` to `0x1004`, set `size` to
twelve, and return `OK_TARGET_RESPONSE`, since `f' saves the
twelve bytes from `0x8004` starting four bytes into the buffer at
`0x1000`. This shows that request addresses may fall in the middle
of saved areas; the function should return the address and size of the
remainder of the buffer.

**`adbg_find_memory_in_frame (f, (char *) 0x8100, &buffer, &size)`**
: This would set `size` to `0x3f00` and return
`NOT_FOUND_TARGET_RESPONSE`, since there is no memory saved in
`f` from the address `0x8100`, and the next memory available
is at `0x8100 + 0x3f00`, or `0xc000`. This shows that request
addresses may fall outside of all saved memory ranges; the function
should indicate the next saved area, if any.

**`adbg_find_memory_in_frame (f, (char *) 0x7000, &buffer, &size)`**
: This would set `size` to `0x1000` and return
`NOT_FOUND_TARGET_RESPONSE`, since the next saved memory is at
`0x7000 + 0x1000`, or `0x8000`.

**`adbg_find_memory_in_frame (f, (char *) 0xf000, &buffer, &size)`**
: This would set `size` to zero, and return
`NOT_FOUND_TARGET_RESPONSE`. This shows how the function tells the
caller that no further memory ranges have been saved.

As another example, here is a function which will print out the
addresses of all memory saved in the trace frame `frame` on the
Symmetrix INLINES console:

```
void
print_frame_addresses (FRAME_DEF *frame)
{
  char *addr;
  char *buffer;
  unsigned long size;

  addr = 0;
  for (;;)
    {
      /* Either find out how much memory we have here, or discover
         where the next saved region is.  */
      if (adbg_find_memory_in_frame (frame, addr, &buffer, &size)
          == OK_TARGET_RESPONSE)
        printp ("saved %x to %x\n", addr, addr + size);
      if (size == 0)
        break;
      addr += size;
    }
}
```

Note that there is not necessarily any connection between the order in
which the data is saved in the trace frame, and the order in which
`adbg_find_memory_in_frame` will return those memory ranges. The
code above will always print the saved memory regions in order of
increasing address, while the underlying frame structure might store the
data in a random order.

[[This section should cover the rest of the Symmetrix functions the stub
relies upon, too.]]

## [Rationale](Debugging%20with%20GDB.md#apple-krhugmzuhe)

Some of the design decisions apparent above are arguable.

**__What about stack overflow/underflow?__**
: GDB should be able to query the target to discover its stack size.
Given that information, GDB can determine at translation time whether a
given expression will overflow the stack. But this spec isn't about
what kinds of error-checking GDB ought to do.

**__Why are you doing everything in LONGEST?__**
: Speed isn't important, but agent code size is; using LONGEST brings in a
bunch of support code to do things like division, etc. So this is a
serious concern.
First, note that you don't need different bytecodes for different
operand sizes. You can generate code without _knowing_ how big the
stack elements actually are on the target. If the target only supports
32-bit ints, and you don't send any 64-bit bytecodes, everything just
works. The observation here is that the MIPS and the Alpha have only
fixed-size registers, and you can still get C's semantics even though
most instructions only operate on full-sized words. You just need to
make sure everything is properly sign-extended at the right times. So
there is no need for 32- and 64-bit variants of the bytecodes. Just
implement everything using the largest size you support.
GDB should certainly check to see what sizes the target supports, so the
user can get an error earlier, rather than later. But this information
is not necessary for correctness.

**__Why don't you have `>` or `<=` operators?__**
: I want to keep the interpreter small, and we don't need them. We can
combine the `less_` opcodes with `log_not`, and swap the order
of the operands, yielding all four asymmetrical comparison operators.
For example, `(x <= y)` is `! (x > y)`, which is `! (y <
x)`.

**__Why do you have `log_not`?__**
:

**__Why do you have `ext`?__**
:

**__Why do you have `zero_ext`?__**
: These are all easily synthesized from other instructions, but I expect
them to be used frequently, and they're simple, so I include them to
keep bytecode strings short.
`log_not` is equivalent to `const8 0 equal`; it's used in half
the relational operators.
`ext n` is equivalent to `const8 s-n lsh const8
s-n rsh_signed`, where s is the size of the stack elements;
it follows `refm` and reg bytecodes when the value
should be signed. See the next bulleted item.
`zero_ext n` is equivalent to `constm mask
log_and`; it's used whenever we push the value of a register, because we
can't assume the upper bits of the register aren't garbage.

**__Why not have sign-extending variants of the `ref` operators?__**
: Because that would double the number of `ref` operators, and we
need the `ext` bytecode anyway for accessing bitfields.

**__Why not have constant-address variants of the `ref` operators?__**
: Because that would double the number of `ref` operators again, and
`const32 address ref32` is only one byte longer.

**__Why do the `refn` operators have to support unaligned fetches?__**
: GDB will generate bytecode that fetches multi-byte values at unaligned
addresses whenever the executable's debugging information tells it to.
Furthermore, GDB does not know the value the pointer will have when GDB
generates the bytecode, so it cannot determine whether a particular
fetch will be aligned or not.
In particular, structure bitfields may be several bytes long, but follow
no alignment rules; members of packed structures are not necessarily
aligned either.
In general, there are many cases where unaligned references occur in
correct C code, either at the programmer's explicit request, or at the
compiler's discretion. Thus, it is simpler to make the GDB agent
bytecodes work correctly in all circumstances than to make GDB guess in
each case whether the compiler did the usual thing.

**__Why are there no side-effecting operators?__**
: Because our current client doesn't want them? That's a cheap answer. I
think the real answer is that I'm afraid of implementing function
calls. We should re-visit this issue after the present contract is
delivered.

**__Why aren't the `goto` ops PC-relative?__**
: The interpreter has the base address around anyway for PC bounds
checking, and it seemed simpler.

**__Why is there only one offset size for the `goto` ops?__**
: Offsets are currently sixteen bits. I'm not happy with this situation
either:
Suppose we have multiple branch ops with different offset sizes. As I
generate code left-to-right, all my jumps are forward jumps (there are
no loops in expressions), so I never know the target when I emit the
jump opcode. Thus, I have to either always assume the largest offset
size, or do jump relaxation on the code after I generate it, which seems
like a big waste of time.
I can imagine a reasonable expression being longer than 256 bytes. I
can't imagine one being longer than 64k. Thus, we need 16-bit offsets.
This kind of reasoning is so bogus, but relaxation is pathetic.
The other approach would be to generate code right-to-left. Then I'd
always know my offset size. That might be fun.

**__Where is the function call bytecode?__**
: When we add side-effects, we should add this.

**__Why does the `reg` bytecode take a 16-bit register number?__**
: Intel's IA-64 architecture has 128 general-purpose registers,
and 128 floating-point registers, and I'm sure it has some random
control registers.

**__Why do we need `trace` and `trace_quick`?__**
: Because GDB needs to record all the memory contents and registers an
expression touches. If the user wants to evaluate an expression
`x->y->z`, the agent must record the values of `x` and
`x->y` as well as the value of `x->y->z`.

**__Don't the `trace` bytecodes make the interpreter less general?__**
: They do mean that the interpreter contains special-purpose code, but
that doesn't mean the interpreter can only be used for that purpose. If
an expression doesn't use the `trace` bytecodes, they don't get in
its way.

**__Why doesn't `trace_quick` consume its arguments the way everything else does?__**
: In general, you do want your operators to consume their arguments; it's
consistent, and generally reduces the amount of stack rearrangement
necessary. However, `trace_quick` is a kludge to save space; it
only exists so we needn't write `dup const8 SIZE trace`
before every memory reference. Therefore, it's okay for it not to
consume its arguments; it's meant for a specific context in which we
know exactly what it should do with the stack. If we're going to have a
kludge, it should be an effective kludge.

**__Why does `trace16` exist?__**
: That opcode was added by the customer that contracted Cygnus for the
data tracing work. I personally think it is unnecessary; objects that
large will be quite rare, so it is okay to use `dup const16
size trace` in those cases.
Whatever we decide to do with `trace16`, we should at least leave
opcode 0x30 reserved, to remain compatible with the customer who added
it.

---

Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Remote%20Serial%20Protocol.md), [next](GNU%20GENERAL%20PUBLIC%20LICENSE.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
