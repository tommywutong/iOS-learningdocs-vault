---
title: AppleScript Language Guide
apple_id: TP40000983
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-01-25'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_keywords.html
archived_at: '2026-07-15T05:19:32.636349Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Language Guide](Introduction%20to%20AppleScript%20Language%20Guide.md)


[Next](Error%20Numbers%20and%20Error%20Messages.md)[Previous](Folder%20Actions%20Reference.md)

# AppleScript Keywords

This appendix lists AppleScript keywords (or _reserved words_), provides a brief description for each, and points to related information, where available. (See also [Keywords](AppleScript%20Lexical%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzx) in [AppleScript Lexical Conventions](AppleScript%20Lexical%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzr).)

The keywords in [Table A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgiwvgvzr) are part of the AppleScript language. You should not attempt to reuse them in your scripts for variable names or other purposes. Developers should not re-define keywords in the terminology for their scriptable applications. You can view many additional scripting terms defined by Apple, but not part of the AppleScript language, in [AppleScript Terminology and Apple Event Codes](https://developer.apple.com/releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html).

__Table A-1__  AppleScript reserved words, with descriptions

| `about` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `above` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `after` | used to describe position in the [Relative](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2ii5cuisi) reference form; used as part of operator (`comes after`, `does not come after`) with classes such as `[date](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2hivbusra)`, `[integer](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)`, and `[text](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)` |
| `against` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `and` | logical _and_ operator—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `apart from` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `around` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `as` | coercion operator—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `aside from` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `at` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `back` | used with [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) and [Relative](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2ii5cuisi) reference forms; `in back of` is synonymous with `after` and `behind` |
| `before` | used to describe position in the [Relative](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2ii5cuisi) reference form; used as an operator (`comes before`, `does not come before`) with classes such as `[date](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2hivbusra)`, `[integer](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2iijcegsq)`, and `[text](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2jifeeurq)`; synonymous with `in front of` |
| `beginning` | specifies an insertion location at the beginning of a container—see the boundary specifier descriptions for the [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) reference form |
| `behind` | synonymous with `after` and `in back of` |
| `below` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `beneath` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `beside` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `between` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `but` | used in [considering and ignoring Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytgmbsgi2a) |
| `by` | used with binary containment operator `[contains, is contained by](ASLR_operators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenjqge4q)`; also used as handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `considering` | a control statement—see [considering and ignoring Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytgmbsgi2a) |
| `contain, contains` | binary containment operator—see `[contains, is contained by](ASLR_operators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenjqge4q)` |
| `continue` | changes the flow of execution—see `[continue](ASLR_handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomi)` |
| `copy` | an AppleScript command—see `[copy](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` |
| `div` | division operator—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `does` | used with operators such as `does not equal`, `does not come before`, and `does not contain`—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `eighth` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `else` | used with `if` control statement—see [if Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytkobsgq2a) |
| `end` | marks the end of a script or handler definition, or of a compound statement, such as a `tell` or `repeat` statement; also specifies an insertion location at the end of a container—see the boundary specifier descriptions for the [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) reference form |
| `equal, equals` | binary comparison operator—see `[equal, is not equal to](ASLR_operators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfuytenbqhe2q)` |
| `error` | `[error](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteojwg44a)` control statement; also used with`[try](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteojsgmza)` statement |
| `every` | specifies every object in a container—see [Every](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizeussa) reference form |
| `exit` | terminates a `repeat` loop—see `[exit](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteobygqzq)` |
| `false` | a Boolean literal—see [Boolean](AppleScript%20Lexical%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzrgq) |
| `fifth` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `first` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `for` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `fourth` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `from` | used in specifying a range of objects in a container—see [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) reference form; also used as handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `front` | `in front of` is used to describe position in the [Relative](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2ii5cuisi) reference form; synonymous with `before` |
| `get` | an AppleScript command—see `[get](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgy)` |
| `given` | a special handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `global` | specifies the scope for a variable (see also `local`)—see [Global Variables](Variables%20and%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzrgm) |
| `if` | a control statement—see [if Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytkobsgq2a) |
| `ignoring` | a control statement—see [considering and ignoring Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytgmbsgi2a) |
| `in` | used in construction object specifiers—see [Containers](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzsgq); also used with the [Relative](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2ii5cuisi) reference form—for example `in front of` and `in back of` |
| `instead of` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `into` | `put into` is a deprecated synonym for the `[copy](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` command; also used as handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `is` | used with various comparison operators—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `it` | refers to the current target (`of it`)—see [The it and me Keywords](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzu) |
| `its` | synonym for `of it`—see [The it and me Keywords](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzu) |
| `last` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `local` | specifies the scope for a variable (see also `global`)—see [Local Variables](Variables%20and%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrsgmwvgvzrgi) |
| `me` | refers to the current script (`of me`)—see [The it and me Keywords](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzu) |
| `middle` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `mod` | remainder operator—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `my` | synonym for `of me`—see [The it and me Keywords](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzu) |
| `ninth` | specifies a position in a container—see [Middle](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2kizceeqi) reference form |
| `not` | logical negation operator—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `of` | used in construction object specifiers—see [Containers](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzsgq); used with or as part of many other terms, including `of me` , `in front of` , and so on |
| `on` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `onto` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `or` | logical _or_ operator—see [Table 9-1](Operators%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnlhfvjvomq) |
| `out of` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `over` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `prop, property` | `prop` is an abbreviation for `property`—see [The it and me Keywords](AppleScript%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrhawvgvzu) |
| `put` | `put into` is a deprecated synonym for the `[copy](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` command |
| `ref/reference` | `ref` is an abbreviation for `reference`—see `[reference](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvbeeq2ejjfeiri)` |
| `repeat` | a control statement—see [repeat Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytenztgyza) |
| `return` | exits from a handler—see `[return](ASLR_handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfuytmmzzgm3q)` |
| `returning` | deprecated |
| `script` | used to declare a script object; also the class of a script object—see the `[script](ASLR_classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmlhfvjvoni)` class and [Script Objects](Script%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqg4wueqkkjjbusqkb) |
| `second` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `set` | an AppleScript command—see `[set](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` |
| `seventh` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `since` | handler parameter label—see [Handler Syntax (Labeled Parameters)](Handler%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqn3hfvjvomq) |
| `sixth` | specifies an index position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `some` | specifies an object in a container—see [Arbitrary](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbegskkivcuqri) reference form |
| `tell` | a control statement—see [tell Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytkobwgm3q) |
| `tenth` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `that` | synonym for `whose` |
| `the` | syntactic no-op, used to make script statements look more like natural language |
| `then` | used with `if` control statement—see [if Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytkobsgq2a) |
| `third` | specifies a position in a container—see [Index](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2hjbducrq) reference form |
| `through, thru` | used in specifying a range of objects in a container—see [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) reference form |
| `timeout` | used with `with timeout` control statement—see `[with timeout](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytgmjqhe2a)` |
| `times` | used with `repeat` control statement—see `[repeat (number) times](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytenzwg43a)` |
| `to` | used in many places, including `[copy](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgm)` and `[set](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzvgi)` commands; in the [Range](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbeeq2iirfeusq) reference form; by operators such as `is equal to` and `a reference to`; with the control statement `[repeat with loopVariable (from startValue to stopValue)](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteobsga3q)`; with the partial result parameter in [try Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteobzg4zq) |
| `transaction` | used with `with transaction` control statement—see `[with transaction](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytgmjtgazq)` |
| `true` | a Boolean literal—see [Boolean](AppleScript%20Lexical%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgqwvgvzrgq) |
| `try` | an error-handling statement—see [try Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteobzg4zq) |
| `until` | used with `repeat` control statement—see `[repeat until](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuyteobqge2a)` |
| `use` | a requirement statement—see [use Statements](Control%20Statements%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfvjvona) |
| `where` | used with the [Filter](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbecsskjbcumri) reference form to specify a Boolean test expression (synonymous with `whose`) |
| `while` | used with `repeat` control statement—see `[repeat while](ASLR_control_statements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqnthfuytenzygq2q)` |
| `whose` | used with the [Filter](Reference%20Forms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqndhfvbecsskjbcumri) reference form to specify a Boolean test expression (synonymous with `where`) |
| `with` | used in commands to specify various kinds of parameters, including `true` for some Boolean for parameters—see, for example, the `with prompt` and `multiple selections allowed` parameters to the `[choose from list](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzx)` command; also used with application `make` commands to specify properties (`with properties`) |
| `without` | used in commands to specify `false` for a Boolean for a parameter—see, for example, the `multiple selections allowed` parameter to the `[choose from list](ASLR_cmds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrrgywvgvzx)` command |

[Next](Error%20Numbers%20and%20Error%20Messages.md)[Previous](Folder%20Actions%20Reference.md)

