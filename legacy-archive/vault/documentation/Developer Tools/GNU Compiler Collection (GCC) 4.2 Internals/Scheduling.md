---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Scheduling.html
archived_at: '2026-07-15T07:31:02.753978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Sections](Sections.md#apple-knswg5djn5xhg),
Previous: [Costs](Costs.md#apple-inxxg5dt),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.18 Adjusting the Instruction Scheduler

The instruction scheduler may need a fair amount of machine-specific
adjustment in order to produce good code. GCC provides several target
hooks for this purpose. It is usually enough to define just a few of
them: try the first ones in this list first.

— Target Hook: int __TARGET_SCHED_ISSUE_RATE__ (void)
> This hook returns the maximum number of instructions that can ever
> issue at the same time on the target machine. The default is one.
> Although the insn scheduler can define itself the possibility of issue
> an insn on the same cycle, the value can serve as an additional
> constraint to issue insns on the same simulated processor cycle (see
> hooks ``TARGET_SCHED_REORDER`' and ``TARGET_SCHED_REORDER2`').
> This value must be constant over the entire compilation. If you need
> it to vary depending on what the instructions are, you must use
> ``TARGET_SCHED_VARIABLE_ISSUE`'.

— Target Hook: int __TARGET_SCHED_VARIABLE_ISSUE__ (FILE \*file, int verbose, rtx insn, int more)
> This hook is executed by the scheduler after it has scheduled an insn
> from the ready list. It should return the number of insns which can
> still be issued in the current cycle. The default is
> ``more - 1`' for insns other than `CLOBBER` and
> `USE`, which normally are not counted against the issue rate.
> You should define this hook if some insns take more machine resources
> than others, so that fewer insns can follow them in the same cycle.
> file is either a null pointer, or a stdio stream to write any
> debug output to. verbose is the verbose level provided by
> `-fsched-verbose-n`. insn is the instruction that
> was scheduled.

— Target Hook: int __TARGET_SCHED_ADJUST_COST__ (rtx insn, rtx link, rtx dep_insn, int cost)
> This function corrects the value of cost based on the
> relationship between insn and dep_insn through the
> dependence link. It should return the new value. The default
> is to make no adjustment to cost. This can be used for example
> to specify to the scheduler using the traditional pipeline description
> that an output- or anti-dependence does not incur the same cost as a
> data-dependence. If the scheduler using the automaton based pipeline
> description, the cost of anti-dependence is zero and the cost of
> output-dependence is maximum of one and the difference of latency
> times of the first and the second insns. If these values are not
> acceptable, you could use the hook to modify them too. See also
> see [Processor pipeline description](Processor-pipeline-description.md#apple-kbzg6y3fonzw64rnobuxazlmnfxgkllemvzwg4tjob2gs33o).

— Target Hook: int __TARGET_SCHED_ADJUST_PRIORITY__ (rtx insn, int priority)
> This hook adjusts the integer scheduling priority priority of
> insn. It should return the new priority. Increase the priority to
> execute insn earlier, reduce the priority to execute insn
> later. Do not define this hook if you do not need to adjust the
> scheduling priorities of insns.

— Target Hook: int __TARGET_SCHED_REORDER__ (FILE \*file, int verbose, rtx \*ready, int \*n_readyp, int clock)
> This hook is executed by the scheduler after it has scheduled the ready
> list, to allow the machine description to reorder it (for example to
> combine two small instructions together on ``VLIW`' machines).
> file is either a null pointer, or a stdio stream to write any
> debug output to. verbose is the verbose level provided by
> `-fsched-verbose-n`. ready is a pointer to the ready
> list of instructions that are ready to be scheduled. n_readyp is
> a pointer to the number of elements in the ready list. The scheduler
> reads the ready list in reverse order, starting with
> ready[\*n_readyp-1] and going to ready[0]. clock
> is the timer tick of the scheduler. You may modify the ready list and
> the number of ready insns. The return value is the number of insns that
> can issue this cycle; normally this is just `issue_rate`. See also
> ``TARGET_SCHED_REORDER2`'.

— Target Hook: int __TARGET_SCHED_REORDER2__ (FILE \*file, int verbose, rtx \*ready, int \*n_ready, clock)
> Like ``TARGET_SCHED_REORDER`', but called at a different time. That
> function is called whenever the scheduler starts a new cycle. This one
> is called once per iteration over a cycle, immediately after
> ``TARGET_SCHED_VARIABLE_ISSUE`'; it can reorder the ready list and
> return the number of insns to be scheduled in the same cycle. Defining
> this hook can be useful if there are frequent situations where
> scheduling one insn causes other insns to become ready in the same
> cycle. These other insns can then be taken into account properly.

— Target Hook: void __TARGET_SCHED_DEPENDENCIES_EVALUATION_HOOK__ (rtx head, rtx tail)
> This hook is called after evaluation forward dependencies of insns in
> chain given by two parameter values (head and tail
> correspondingly) but before insns scheduling of the insn chain. For
> example, it can be used for better insn classification if it requires
> analysis of dependencies. This hook can use backward and forward
> dependencies of the insn scheduler because they are already
> calculated.

— Target Hook: void __TARGET_SCHED_INIT__ (FILE \*file, int verbose, int max_ready)
> This hook is executed by the scheduler at the beginning of each block of
> instructions that are to be scheduled. file is either a null
> pointer, or a stdio stream to write any debug output to. verbose
> is the verbose level provided by `-fsched-verbose-n`.
> max_ready is the maximum number of insns in the current scheduling
> region that can be live at the same time. This can be used to allocate
> scratch space if it is needed, e.g. by ``TARGET_SCHED_REORDER`'.

— Target Hook: void __TARGET_SCHED_FINISH__ (FILE \*file, int verbose)
> This hook is executed by the scheduler at the end of each block of
> instructions that are to be scheduled. It can be used to perform
> cleanup of any actions done by the other scheduling hooks. file
> is either a null pointer, or a stdio stream to write any debug output
> to. verbose is the verbose level provided by
> `-fsched-verbose-n`.

— Target Hook: void __TARGET_SCHED_INIT_GLOBAL__ (FILE \*file, int verbose, int old_max_uid)
> This hook is executed by the scheduler after function level initializations.
> file is either a null pointer, or a stdio stream to write any debug output to.
> verbose is the verbose level provided by `-fsched-verbose-n`.
> old_max_uid is the maximum insn uid when scheduling begins.

— Target Hook: void __TARGET_SCHED_FINISH_GLOBAL__ (FILE \*file, int verbose)
> This is the cleanup hook corresponding to `TARGET_SCHED_INIT_GLOBAL`.
> file is either a null pointer, or a stdio stream to write any debug output to.
> verbose is the verbose level provided by `-fsched-verbose-n`.

— Target Hook: int __TARGET_SCHED_DFA_PRE_CYCLE_INSN__ (void)
> The hook returns an RTL insn. The automaton state used in the
> pipeline hazard recognizer is changed as if the insn were scheduled
> when the new simulated processor cycle starts. Usage of the hook may
> simplify the automaton pipeline description for some VLIW
> processors. If the hook is defined, it is used only for the automaton
> based pipeline description. The default is not to change the state
> when the new simulated processor cycle starts.

— Target Hook: void __TARGET_SCHED_INIT_DFA_PRE_CYCLE_INSN__ (void)
> The hook can be used to initialize data used by the previous hook.

— Target Hook: int __TARGET_SCHED_DFA_POST_CYCLE_INSN__ (void)
> The hook is analogous to ``TARGET_SCHED_DFA_PRE_CYCLE_INSN`' but used
> to changed the state as if the insn were scheduled when the new
> simulated processor cycle finishes.

— Target Hook: void __TARGET_SCHED_INIT_DFA_POST_CYCLE_INSN__ (void)
> The hook is analogous to ``TARGET_SCHED_INIT_DFA_PRE_CYCLE_INSN`' but
> used to initialize data used by the previous hook.

— Target Hook: int __TARGET_SCHED_FIRST_CYCLE_MULTIPASS_DFA_LOOKAHEAD__ (void)
> This hook controls better choosing an insn from the ready insn queue
> for the DFA-based insn scheduler. Usually the scheduler
> chooses the first insn from the queue. If the hook returns a positive
> value, an additional scheduler code tries all permutations of
> ``TARGET_SCHED_FIRST_CYCLE_MULTIPASS_DFA_LOOKAHEAD ()`'
> subsequent ready insns to choose an insn whose issue will result in
> maximal number of issued insns on the same cycle. For the
> VLIW processor, the code could actually solve the problem of
> packing simple insns into the VLIW insn. Of course, if the
> rules of VLIW packing are described in the automaton.
>
> This code also could be used for superscalar RISC
> processors. Let us consider a superscalar RISC processor
> with 3 pipelines. Some insns can be executed in pipelines A or
> B, some insns can be executed only in pipelines B or
> C, and one insn can be executed in pipeline B. The
> processor may issue the 1st insn into A and the 2nd one into
> B. In this case, the 3rd insn will wait for freeing B
> until the next cycle. If the scheduler issues the 3rd insn the first,
> the processor could issue all 3 insns per cycle.
>
> Actually this code demonstrates advantages of the automaton based
> pipeline hazard recognizer. We try quickly and easy many insn
> schedules to choose the best one.
>
> The default is no multipass scheduling.

— Target Hook: int __TARGET_SCHED_FIRST_CYCLE_MULTIPASS_DFA_LOOKAHEAD_GUARD__ (rtx)
> This hook controls what insns from the ready insn queue will be
> considered for the multipass insn scheduling. If the hook returns
> zero for insn passed as the parameter, the insn will be not chosen to
> be issued.
>
> The default is that any ready insns can be chosen to be issued.

— Target Hook: int __TARGET_SCHED_DFA_NEW_CYCLE__ (FILE \*, int, rtx, int, int, int \*)
> This hook is called by the insn scheduler before issuing insn passed
> as the third parameter on given cycle. If the hook returns nonzero,
> the insn is not issued on given processors cycle. Instead of that,
> the processor cycle is advanced. If the value passed through the last
> parameter is zero, the insn ready queue is not sorted on the new cycle
> start as usually. The first parameter passes file for debugging
> output. The second one passes the scheduler verbose level of the
> debugging output. The forth and the fifth parameter values are
> correspondingly processor cycle on which the previous insn has been
> issued and the current processor cycle.

— Target Hook: bool __TARGET_SCHED_IS_COSTLY_DEPENDENCE__ (rtx insn1, rtx insn2, rtx dep_link, int dep_cost, int distance)
> This hook is used to define which dependences are considered costly by
> the target, so costly that it is not advisable to schedule the insns that
> are involved in the dependence too close to one another. The parameters
> to this hook are as follows: The second parameter insn2 is dependent
> upon the first parameter insn1. The dependence between insn1
> and insn2 is represented by the third parameter dep_link. The
> fourth parameter cost is the cost of the dependence, and the fifth
> parameter distance is the distance in cycles between the two insns.
> The hook returns `true` if considering the distance between the two
> insns the dependence between them is considered costly by the target,
> and `false` otherwise.
>
> Defining this hook can be useful in multiple-issue out-of-order machines,
> where (a) it's practically hopeless to predict the actual data/resource
> delays, however: (b) there's a better chance to predict the actual grouping
> that will be formed, and (c) correctly emulating the grouping can be very
> important. In such targets one may want to allow issuing dependent insns
> closer to one another—i.e., closer than the dependence distance; however,
> not in cases of "costly dependences", which this hooks allows to define.

— Target Hook: int __TARGET_SCHED_ADJUST_COST_2__ (rtx insn, int dep_type, rtx dep_insn, int cost)
> This hook is a modified version of ``TARGET_SCHED_ADJUST_COST`'. Instead
> of passing dependence as a second parameter, it passes a type of that
> dependence. This is useful to calculate cost of dependence between insns
> not having the corresponding link. If ``TARGET_SCHED_ADJUST_COST_2`' is
> defined it is used instead of ``TARGET_SCHED_ADJUST_COST`'.

— Target Hook: void __TARGET_SCHED_H_I_D_EXTENDED__ (void)
> This hook is called by the insn scheduler after emitting a new instruction to
> the instruction stream. The hook notifies a target backend to extend its
> per instruction data structures.

— Target Hook: int __TARGET_SCHED_SPECULATE_INSN__ (rtx insn, int request, rtx \*new_pat)
> This hook is called by the insn scheduler when insn has only
> speculative dependencies and therefore can be scheduled speculatively.
> The hook is used to check if the pattern of insn has a speculative
> version and, in case of successful check, to generate that speculative
> pattern. The hook should return 1, if the instruction has a speculative form,
> or -1, if it doesn't. request describes the type of requested
> speculation. If the return value equals 1 then new_pat is assigned
> the generated speculative pattern.

— Target Hook: int __TARGET_SCHED_NEEDS_BLOCK_P__ (rtx insn)
> This hook is called by the insn scheduler during generation of recovery code
> for insn. It should return nonzero, if the corresponding check
> instruction should branch to recovery code, or zero otherwise.

— Target Hook: rtx __TARGET_SCHED_GEN_CHECK__ (rtx insn, rtx label, int mutate_p)
> This hook is called by the insn scheduler to generate a pattern for recovery
> check instruction. If mutate_p is zero, then insn is a
> speculative instruction for which the check should be generated.
> label is either a label of a basic block, where recovery code should
> be emitted, or a null pointer, when requested check doesn't branch to
> recovery code (a simple check). If mutate_p is nonzero, then
> a pattern for a branchy check corresponding to a simple check denoted by
> insn should be generated. In this case label can't be null.

— Target Hook: int __TARGET_SCHED_FIRST_CYCLE_MULTIPASS_DFA_LOOKAHEAD_GUARD_SPEC__ (rtx insn)
> This hook is used as a workaround for
> ``TARGET_SCHED_FIRST_CYCLE_MULTIPASS_DFA_LOOKAHEAD_GUARD`' not being
> called on the first instruction of the ready list. The hook is used to
> discard speculative instruction that stand first in the ready list from
> being scheduled on the current cycle. For non-speculative instructions,
> the hook should always return nonzero. For example, in the ia64 backend
> the hook is used to cancel data speculative insns when the ALAT table
> is nearly full.

— Target Hook: void __TARGET_SCHED_SET_SCHED_FLAGS__ (unsigned int \*flags, spec_info_t spec_info)
> This hook is used by the insn scheduler to find out what features should be
> enabled/used. flags initially may have either the SCHED_RGN or SCHED_EBB
> bit set. This denotes the scheduler pass for which the data should be
> provided. The target backend should modify flags by modifying
> the bits corresponding to the following features: USE_DEPS_LIST, USE_GLAT,
> DETACH_LIFE_INFO, and DO_SPECULATION. For the DO_SPECULATION feature
> an additional structure spec_info should be filled by the target.
> The structure describes speculation types that can be used in the scheduler.
