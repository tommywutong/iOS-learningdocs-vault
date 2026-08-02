---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Option-properties.html
archived_at: '2026-07-15T07:31:02.462177Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Option file format](Option-file-format.md#apple-j5yhi2lpnywwm2lmmuwwm33snvqxi),
Up: [Options](Options.md#apple-j5yhi2lpnzzq)

---

### 7.2 Option properties

The second field of an option record can specify the following properties:

**`Common`**
: The option is available for all languages and targets.

**`Target`**
: The option is available for all languages but is target-specific.

**language**
: The option is available when compiling for the given language.

It is possible to specify several different languages for the same
option. Each language must have been declared by an earlier
`Language` record. See [Option file format](Option-file-format.md#apple-j5yhi2lpnywwm2lmmuwwm33snvqxi).

**`RejectNegative`**
: The option does not have a “no-” form. All options beginning with
“f”, “W” or “m” are assumed to have a “no-” form unless this
property is used.

**`Negative(`othername`)`**
: The option will turn off another option othername, which is the
the option name with the leading “-” removed. This chain action will
propagate through the `Negative` property of the option to be
turned off.

**`Joined`

**`Separate`****
: The option takes a mandatory argument. `Joined` indicates
that the option and argument can be included in the same `argv`
entry (as with `-mflush-func=`name, for example).
`Separate` indicates that the option and argument can be
separate `argv` entries (as with `-o`). An option is
allowed to have both of these properties.

**`JoinedOrMissing`**
: The option takes an optional argument. If the argument is given,
it will be part of the same `argv` entry as the option itself.

This property cannot be used alongside `Joined` or `Separate`.

**`UInteger`**
: The option's argument is a non-negative integer. The option parser
will check and convert the argument before passing it to the relevant
option handler.

**`Var(`var`)`**
: The state of this option should be stored in variable var.
The way that the state is stored depends on the type of option:

- If the option uses the `Mask` or `InverseMask` properties,
  var is the integer variable that contains the mask.
- If the option is a normal on/off switch, var is an integer
  variable that is nonzero when the option is enabled. The options
  parser will set the variable to 1 when the positive form of the
  option is used and 0 when the “no-” form is used.
- If the option takes an argument and has the `UInteger` property,
  var is an integer variable that stores the value of the argument.
- Otherwise, if the option takes an argument, var is a pointer to
  the argument string. The pointer will be null if the argument is optional
  and wasn't given.

The option-processing script will usually declare var in
`options.c` and leave it to be zero-initialized at start-up time.
You can modify this behavior using `VarExists` and `Init`.

**`Var(`var`,` set`)`**
: The option controls an integer variable var and is active when
var equals set. The option parser will set var to
set when the positive form of the option is used and `!`set
when the “no-” form is used.

var is declared in the same way as for the single-argument form
described above.

**`VarExists`**
: The variable specified by the `Var` property already exists.
No definition should be added to `options.c` in response to
this option record.

You should use this property only if the variable is declared outside
`options.c`.

**`Init(`value`)`**
: The variable specified by the `Var` property should be statically
initialized to value.

**`Mask(`name`)`**
: The option is associated with a bit in the `target_flags`
variable (see [Run-time Target](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a)) and is active when that bit is set.
You may also specify `Var` to select a variable other than
`target_flags`.

The options-processing script will automatically allocate a unique bit
for the option. If the option is attached to ``target_flags`',
the script will set the macro `MASK_`name to the appropriate
bitmask. It will also declare a `TARGET_`name macro that has
the value 1 when the option is active and 0 otherwise. If you use `Var`
to attach the option to a different variable, the associated macros are
called `OPTION_MASK_`name and `OPTION_`name respectively.

You can disable automatic bit allocation using `MaskExists`.

**`InverseMask(`othername`)`

**`InverseMask(`othername`,` thisname`)`****
: The option is the inverse of another option that has the
`Mask(`othername`)` property. If thisname is given,
the options-processing script will declare a `TARGET_`thisname
macro that is 1 when the option is active and 0 otherwise.

**`MaskExists`**
: The mask specified by the `Mask` property already exists.
No `MASK` or `TARGET` definitions should be added to
`options.h` in response to this option record.

The main purpose of this property is to support synonymous options.
The first option should use ``Mask(name)`' and the others
should use ``Mask(name) MaskExists`'.

**`Report`**
: The state of the option should be printed by `-fverbose-asm`.

**`Undocumented`**
: The option is deliberately missing documentation and should not
be included in the `--help` output.

**`Condition(`cond`)`**
: The option should only be accepted if preprocessor condition
cond is true. Note that any C declarations associated with the
option will be present even if cond is false; cond simply
controls whether the option is accepted and whether it is printed in
the `--help` output.
