---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Processor-pipeline-description.html
archived_at: '2026-07-15T07:31:02.607441Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Delay Slots](Delay-Slots.md#apple-irswyylzfvjwy33uom),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 14.19.8 Specifying processor pipeline description

To achieve better performance, most modern processors
(super-pipelined, superscalar RISC, and VLIW
processors) have many functional units on which several
instructions can be executed simultaneously. An instruction starts
execution if its issue conditions are satisfied. If not, the
instruction is stalled until its conditions are satisfied. Such
interlock (pipeline) delay causes interruption of the fetching
of successor instructions (or demands nop instructions, e.g. for some
MIPS processors).

There are two major kinds of interlock delays in modern processors.
The first one is a data dependence delay determining instruction
latency time. The instruction execution is not started until all
source data have been evaluated by prior instructions (there are more
complex cases when the instruction execution starts even when the data
are not available but will be ready in given time after the
instruction execution start). Taking the data dependence delays into
account is simple. The data dependence (true, output, and
anti-dependence) delay between two instructions is given by a
constant. In most cases this approach is adequate. The second kind
of interlock delays is a reservation delay. The reservation delay
means that two instructions under execution will be in need of shared
processors resources, i.e. buses, internal registers, and/or
functional units, which are reserved for some time. Taking this kind
of delay into account is complex especially for modern RISC
processors.

The task of exploiting more processor parallelism is solved by an
instruction scheduler. For a better solution to this problem, the
instruction scheduler has to have an adequate description of the
processor parallelism (or pipeline description). GCC
machine descriptions describe processor parallelism and functional
unit reservations for groups of instructions with the aid of
regular expressions.

The GCC instruction scheduler uses a pipeline hazard recognizer to
figure out the possibility of the instruction issue by the processor
on a given simulated processor cycle. The pipeline hazard recognizer is
automatically generated from the processor pipeline description. The
pipeline hazard recognizer generated from the machine description
is based on a deterministic finite state automaton (DFA):
the instruction issue is possible if there is a transition from one
automaton state to another one. This algorithm is very fast, and
furthermore, its speed is not dependent on processor
complexity[1](#apple-mzxc2mi).

The rest of this section describes the directives that constitute
an automaton-based processor pipeline description. The order of
these constructions within the machine description file is not
important.

The following optional construction describes names of automata
generated and used for the pipeline hazards recognition. Sometimes
the generated finite state automaton used by the pipeline hazard
recognizer is large. If we use more than one automaton and bind functional
units to the automata, the total size of the automata is usually
less than the size of the single automaton. If there is no one such
construction, only one finite state automaton is generated.

```
     (define_automaton automata-names)
```

automata-names is a string giving names of the automata. The
names are separated by commas. All the automata should have unique names.
The automaton name is used in the constructions `define_cpu_unit` and
`define_query_cpu_unit`.

Each processor functional unit used in the description of instruction
reservations should be described by the following construction.

```
     (define_cpu_unit unit-names [automaton-name])
```

unit-names is a string giving the names of the functional units
separated by commas. Don't use name ``nothing`', it is reserved
for other goals.

automaton-name is a string giving the name of the automaton with
which the unit is bound. The automaton should be described in
construction `define_automaton`. You should give
automaton-name, if there is a defined automaton.

The assignment of units to automata are constrained by the uses of the
units in insn reservations. The most important constraint is: if a
unit reservation is present on a particular cycle of an alternative
for an insn reservation, then some unit from the same automaton must
be present on the same cycle for the other alternatives of the insn
reservation. The rest of the constraints are mentioned in the
description of the subsequent constructions.

The following construction describes CPU functional units analogously
to `define_cpu_unit`. The reservation of such units can be
queried for an automaton state. The instruction scheduler never
queries reservation of functional units for given automaton state. So
as a rule, you don't need this construction. This construction could
be used for future code generation goals (e.g. to generate
VLIW insn templates).

```
     (define_query_cpu_unit unit-names [automaton-name])
```

unit-names is a string giving names of the functional units
separated by commas.

automaton-name is a string giving the name of the automaton with
which the unit is bound.

The following construction is the major one to describe pipeline
characteristics of an instruction.

```
     (define_insn_reservation insn-name default_latency
                              condition regexp)
```

default_latency is a number giving latency time of the
instruction. There is an important difference between the old
description and the automaton based pipeline description. The latency
time is used for all dependencies when we use the old description. In
the automaton based pipeline description, the given latency time is only
used for true dependencies. The cost of anti-dependencies is always
zero and the cost of output dependencies is the difference between
latency times of the producing and consuming insns (if the difference
is negative, the cost is considered to be zero). You can always
change the default costs for any description by using the target hook
`TARGET_SCHED_ADJUST_COST` (see [Scheduling](Scheduling.md#apple-knrwqzleovwgs3th)).

insn-name is a string giving the internal name of the insn. The
internal names are used in constructions `define_bypass` and in
the automaton description file generated for debugging. The internal
name has nothing in common with the names in `define_insn`. It is a
good practice to use insn classes described in the processor manual.

condition defines what RTL insns are described by this
construction. You should remember that you will be in trouble if
condition for two or more different
`define_insn_reservation` constructions is TRUE for an insn. In
this case what reservation will be used for the insn is not defined.
Such cases are not checked during generation of the pipeline hazards
recognizer because in general recognizing that two conditions may have
the same value is quite difficult (especially if the conditions
contain `symbol_ref`). It is also not checked during the
pipeline hazard recognizer work because it would slow down the
recognizer considerably.

regexp is a string describing the reservation of the cpu's functional
units by the instruction. The reservations are described by a regular
expression according to the following syntax:

```
            regexp = regexp "," oneof
                   | oneof

            oneof = oneof "|" allof
                  | allof

            allof = allof "+" repeat
                  | repeat

            repeat = element "*" number
                   | element

            element = cpu_function_unit_name
                    | reservation_name
                    | result_name
                    | "nothing"
                    | "(" regexp ")"
```

- ``,`' is used for describing the start of the next cycle in
  the reservation.
- ``|`' is used for describing a reservation described by the first
  regular expression __or__ a reservation described by the second
  regular expression __or__ etc.
- ``+`' is used for describing a reservation described by the first
  regular expression __and__ a reservation described by the
  second regular expression __and__ etc.
- ``*`' is used for convenience and simply means a sequence in which
  the regular expression are repeated number times with cycle
  advancing (see ``,`').
- ``cpu_function_unit_name`' denotes reservation of the named
  functional unit.
- ``reservation_name`' — see description of construction
  ``define_reservation`'.
- ``nothing`' denotes no unit reservations.

Sometimes unit reservations for different insns contain common parts.
In such case, you can simplify the pipeline description by describing
the common part by the following construction

```
     (define_reservation reservation-name regexp)
```

reservation-name is a string giving name of regexp.
Functional unit names and reservation names are in the same name
space. So the reservation names should be different from the
functional unit names and can not be the reserved name ``nothing`'.

The following construction is used to describe exceptions in the
latency time for given instruction pair. This is so called bypasses.

```
     (define_bypass number out_insn_names in_insn_names
                    [guard])
```

number defines when the result generated by the instructions
given in string out_insn_names will be ready for the
instructions given in string in_insn_names. The instructions in
the string are separated by commas.

guard is an optional string giving the name of a C function which
defines an additional guard for the bypass. The function will get the
two insns as parameters. If the function returns zero the bypass will
be ignored for this case. The additional guard is necessary to
recognize complicated bypasses, e.g. when the consumer is only an address
of insn ``store`' (not a stored value).

The following five constructions are usually used to describe
VLIW processors, or more precisely, to describe a placement
of small instructions into VLIW instruction slots. They
can be used for RISC processors, too.

```
     (exclusion_set unit-names unit-names)
     (presence_set unit-names patterns)
     (final_presence_set unit-names patterns)
     (absence_set unit-names patterns)
     (final_absence_set unit-names patterns)
```

unit-names is a string giving names of functional units
separated by commas.

patterns is a string giving patterns of functional units
separated by comma. Currently pattern is one unit or units
separated by white-spaces.

The first construction (``exclusion_set`') means that each
functional unit in the first string can not be reserved simultaneously
with a unit whose name is in the second string and vice versa. For
example, the construction is useful for describing processors
(e.g. some SPARC processors) with a fully pipelined floating point
functional unit which can execute simultaneously only single floating
point insns or only double floating point insns.

The second construction (``presence_set`') means that each
functional unit in the first string can not be reserved unless at
least one of pattern of units whose names are in the second string is
reserved. This is an asymmetric relation. For example, it is useful
for description that VLIW ``slot1`' is reserved after
``slot0`' reservation. We could describe it by the following
construction

```
     (presence_set "slot1" "slot0")
```

Or ``slot1`' is reserved only after ``slot0`' and unit ``b0`'
reservation. In this case we could write

```
     (presence_set "slot1" "slot0 b0")
```

The third construction (``final_presence_set`') is analogous to
``presence_set`'. The difference between them is when checking is
done. When an instruction is issued in given automaton state
reflecting all current and planned unit reservations, the automaton
state is changed. The first state is a source state, the second one
is a result state. Checking for ``presence_set`' is done on the
source state reservation, checking for ``final_presence_set`' is
done on the result reservation. This construction is useful to
describe a reservation which is actually two subsequent reservations.
For example, if we use

```
     (presence_set "slot1" "slot0")
```

the following insn will be never issued (because ``slot1`' requires
``slot0`' which is absent in the source state).

```
     (define_reservation "insn_and_nop" "slot0 + slot1")
```

but it can be issued if we use analogous ``final_presence_set`'.

The forth construction (``absence_set`') means that each functional
unit in the first string can be reserved only if each pattern of units
whose names are in the second string is not reserved. This is an
asymmetric relation (actually ``exclusion_set`' is analogous to
this one but it is symmetric). For example it might be useful in a
VLIW description to say that ``slot0`' cannot be reserved
after either ``slot1`' or ``slot2`' have been reserved. This
can be described as:

```
     (absence_set "slot0" "slot1, slot2")
```

Or ``slot2`' can not be reserved if ``slot0`' and unit ``b0`'
are reserved or ``slot1`' and unit ``b1`' are reserved. In
this case we could write

```
     (absence_set "slot2" "slot0 b0, slot1 b1")
```

All functional units mentioned in a set should belong to the same
automaton.

The last construction (``final_absence_set`') is analogous to
``absence_set`' but checking is done on the result (state)
reservation. See comments for ``final_presence_set`'.

You can control the generator of the pipeline hazard recognizer with
the following construction.

```
     (automata_option options)
```

options is a string giving options which affect the generated
code. Currently there are the following options:

- no-minimization makes no minimization of the automaton. This is
  only worth to do when we are debugging the description and need to
  look more accurately at reservations of states.
- time means printing additional time statistics about
  generation of automata.
- v means a generation of the file describing the result automata.
  The file has suffix ``.dfa`' and can be used for the description
  verification and debugging.
- w means a generation of warning instead of error for
  non-critical errors.
- ndfa makes nondeterministic finite state automata. This affects
  the treatment of operator ``|`' in the regular expressions. The
  usual treatment of the operator is to try the first alternative and,
  if the reservation is not possible, the second alternative. The
  nondeterministic treatment means trying all alternatives, some of them
  may be rejected by reservations in the subsequent insns.
- progress means output of a progress bar showing how many states
  were generated so far for automaton being processed. This is useful
  during debugging a DFA description. If you see too many
  generated states, you could interrupt the generator of the pipeline
  hazard recognizer and try to figure out a reason for generation of the
  huge automaton.

As an example, consider a superscalar RISC machine which can
issue three insns (two integer insns and one floating point insn) on
the cycle but can finish only two insns. To describe this, we define
the following functional units.

```
     (define_cpu_unit "i0_pipeline, i1_pipeline, f_pipeline")
     (define_cpu_unit "port0, port1")
```

All simple integer insns can be executed in any integer pipeline and
their result is ready in two cycles. The simple integer insns are
issued into the first pipeline unless it is reserved, otherwise they
are issued into the second pipeline. Integer division and
multiplication insns can be executed only in the second integer
pipeline and their results are ready correspondingly in 8 and 4
cycles. The integer division is not pipelined, i.e. the subsequent
integer division insn can not be issued until the current division
insn finished. Floating point insns are fully pipelined and their
results are ready in 3 cycles. Where the result of a floating point
insn is used by an integer insn, an additional delay of one cycle is
incurred. To describe all of this we could specify

```
     (define_cpu_unit "div")

     (define_insn_reservation "simple" 2 (eq_attr "type" "int")
                              "(i0_pipeline | i1_pipeline), (port0 | port1)")

     (define_insn_reservation "mult" 4 (eq_attr "type" "mult")
                              "i1_pipeline, nothing*2, (port0 | port1)")

     (define_insn_reservation "div" 8 (eq_attr "type" "div")
                              "i1_pipeline, div*7, div + (port0 | port1)")

     (define_insn_reservation "float" 3 (eq_attr "type" "float")
                              "f_pipeline, nothing, (port0 | port1))

     (define_bypass 4 "float" "simple,mult,div")
```

To simplify the description we could describe the following reservation

```
     (define_reservation "finish" "port0|port1")
```

and use it in all `define_insn_reservation` as in the following
construction

```
     (define_insn_reservation "simple" 2 (eq_attr "type" "int")
                              "(i0_pipeline | i1_pipeline), finish")
```

---

#### Footnotes

[[1](#apple-mzxgiljr)] However, the size of the automaton depends on
processor complexity. To limit this effect, machine descriptions
can split orthogonal parts of the machine description among several
automata: but then, since each of these must be stepped independently,
this does cause a small decrease in the algorithm's performance.

---
