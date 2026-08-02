---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/db_view_info/db_view_info.html
archived_at: '2026-07-15T07:29:23.933519Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Shared%20Libraries%20Window.md)[Previous](Controlling%20Execution%20of%20Your%20Code.md)

# Examining Program Data and Information

When execution of your program is paused, Xcode
displays a great deal of information on the current state of your
program. Xcode’s graphical debugging interface makes it easy to examine
the call stack, and view variables and their values. This chapter
describes how to view variables, expressions, and disassembled code.
It also describes how to use the Memory Browser to view the contents
of memory.

For each function call that your program makes, the debugger
stores information about that call in a _stack frame_. These
stack frames are stored in the _call stack_. When
execution of your program is paused in the debugger, Xcode displays
the call stack for the currently running process in the Thread view
display on the left of the debugger window, with the most recent
call at the top.

Selecting any function call in the call stack displays the
stack frame for that function. The stack frame includes information
on the arguments to the function, variables defined in the function,
and the location of the function call. Xcode displays the frame’s
variables in the Variable list and displays its currently executing
statement in the code editor with a red arrow. If a stack frame
is grayed out, no source code is available for it.

In the pop-up menu above the call stack in the debugger window, Xcode displays
all the threads for your application. To view a thread, choose it
from the pop-up menu. Xcode displays its call chain in the Thread
list.

The variables view shows information—such as name, type
and value—about the variables in your program. Variables are displayed
for the stack frame that is currently selected in the debugger window.
The variables view, shown in Figure 34-1, appears in upper-right
portion of the Debugger window by default. The variables view can
have up to four columns:

1. The Variable
   column shows the variable’s name.
2. The Type column displays the type of the variable. This column
   is optional. To display it, choose Debug > Variables View >
   Show Types.
3. The Value column shows the variable’s contents. If a variable’s
   value is in red, it changed when the application was last active.
   You can edit the value of any variable; the changed value is used
   when you resume execution of your program.
4. The Summary column gives more information on a variable’s
   contents. It can be a description of the variable or an English
   language summary of the variable’s value. For example, if a variable
   represents a point, its summary could read “(x = _x value_,
   y = _y value_).” You can edit the summary of
   a variable by double-clicking the Summary column or choosing Debug
   > Variables View > Edit Summary Format. For a description of
   how you can format variable summaries, see [Using Custom Data Formatters to View Variables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugiwueq2jizdeuqkc).

You can choose which columns the debugger shows in the variables
view; Xcode remembers these columns across debugging sessions.

__Figure 34-1__  The variables view

!

Variables in the variables view are grouped by category; to
view variables in any of these groups, click the disclosure triangle
next to that group. These groups are:

- The Arguments group
  contains the arguments to the function that is currently selected in
  the call stack.
- The Locals group contains the local variables declared in
  the function that is currently selected in the call stack.
- The Globals group shows global variables and their values.
  By default, there are no global variables in this section; you must
  select those variables you want to track in the Globals Browser,
  described in [Using the Globals Browser](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugiwueqkcivduersb).
- The File Statics group shows file statics, if any. This group
  is not shown if none are present.

To view the contents of a structured variable, click the disclosure
triangle beside the variable’s name. You can also use a data formatter
to display a variable’s contents in the Summary column, as described
in [Using Custom Data Formatters to View Variables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugiwueq2jizdeuqkc), or you can view a variable in its
own window. Viewing a variable in its own window is particularly
useful for viewing the contents of complex structured variables.
To open a variable in its own window, double-click the variable’s
name or select it and choose Debug > Variables View > View
Variable in Window.

Xcode allows you to customize how variables are displayed
in the debugger by specifying your own format strings for the Value
or Summary columns. In this way, you can display program data in
a readable format. Xcode includes a number of built-in data formatters
for data types defined by various Mac OS X system frameworks. You
can edit these format strings or create your own data formatters.

The menu item Debug > Variables View > Enable Data Formatters
lets you turn data formatters on and off. If a checkmark appears
next to the menu item, data formatters are enabled; select the menu
item again to turn data formatters off. Data formatters are enabled
by default.

If you are debugging heavily threaded code, where more than
one thread is executing the same code, data formatters may cause
threads to run at the wrong time and miss breakpoints. To avoid
this problem, disable data formatters.

You can provide your own data format strings to display data
types defined by your program. To edit the format string associated
with a variable value or variable summary, double-click in the appropriate
column of the variables view. You can also choose Debug > Variables
View > Edit Summary Format.

Data format strings can contain:

- Literal text.
  You can add explanatory text or labels to identify the data presented
  by the format string.
- References to values within a structured data type. You can
  access any member of a structured variable from the format string
  for that variable. The syntax for doing so is _%pathToValue%_,
  where _pathToValue_ is the `.`-delimited
  path to the value you want to access in the current data structure.
- Expressions, including function or method calls. The syntax
  for an expression is _{expression}_. To reference
  the variable itself in the expression, use $VAR. For example, to
  display the name of a notification—of type `NSNotification`—you
  can use _{(NSString \*)[$VAR name]}:s._

When it displays the data format string, Xcode replaces the
member reference or expression with the contents of the Variable
view’s Value column for the value obtained by evaluating the reference
or expression. You can, however, specify that Xcode use the contents
of any column in the Variables view—Variable name, Type, Value,
or Summary. To do so, add _:referencedColumn_ after
the expression or member reference, where _referencedColumn_ is
a letter indicating which Variables view column to access. So, the syntax
for accessing a value in a structured data type becomes _%pathToValue%:referencedColumn_. Table 34-1 shows
the possible values for referencing variable display columns.

__Table 34-1__

| Reference | Variables view column |
| n | Variable (shows the variable name) |
| v | Value |
| t | Type |
| s | Summary |

The following example uses the `CGRect` data
type to illustrate how you can build format strings using member
references and expressions. (Note that Apple provides format strings
for the `CGRect` data type,
so Xcode’s debugger already knows how to display the contents
of variables of that type). The `CGRect` data
type is defined as follows:

`struct CGRect {
CGPoint origin;
CGSize size;
};
typedef struct CGRect CGRect;`

Assuming that the goal is to create a format string that displays
the origin and size of variables of type `CGRect`,
there are many ways you can write such a format string. For example,
you can reference to members of the `origin` and `size` fields
directly. Of course, each of these two fields also contain data
structures, so simply referencing the values of those fields isn’t
very interesting; the values you actually want are in those data
structures. One way you can access those values is to simply include
the full path to the desired field from the `CGRect` type.
For example, to access the height and width of the rectangle, in
the `height` and `width` fields
of the `CGSize` structure
in the `size` field, you
could use the references _%size.height%_ and _%size.width%_.
An example format string using these references might be similar
to the following:

_height = %size.height%, width = %size.width%_

You could write a similar reference to access the x and y-coordinates
of the origin. Or, if you already have data formatter for values
of type `CGPoint` that
displays the x and y coordinates of the point in the Summary column
of the Variables view—such as “_(%x%, %y%)_”—
you can leverage that format string to display the contents of the `origin` field
in the data formatter for the `CGRect` type.
You can do so by referencing the Summary column for `CGPoint`,
as in the following format string:

_origin: %origin%:s_

When Xcode evaluates this format string, it accesses the `origin` field
and retrieves the contents of the Summary column for the `CGPoint` data
type, substituting it for the reference to the `origin` field.
The end result is equivalent to writing the format string _origin: (%origin.x%,
%origin.y%)_.

You can combine this with the format string for the size field
and create a data format string for the `CGRect` type
similar to the following:

_origin: %origin%:s, height = %size.height%, width
= %size.width%_

Given a rectangle with the origin (1,2 ), a width of 3, and
a height of 4, this results in the following display: _origin:
(1, 2), width=3, height=4_. You can also write a data formatter
to display the exact same information using an expression, such
as the following:

_origin: {$VAR.origin}:s, height = {$VAR.size.height},
width = {$VAR.size.width}_

When Xcode evaluates this expression for a variable, it replaces
$VAR with a reference to the variable itself. Of course, using an
expression to perform a simple value reference is not necessary.
Another example of an expression in a format string is _{(NSString
\*)[$VAR name]}:s_, to display the name of a notification,
of type `NSNotification`.

When you specify a custom format string for a variable of
a given type, that format string is also used for all other variables
of the same type. Note, however, that you cannot specify a custom
format for string types, such as `NSString`, `char*`,
and so on. Custom format strings that you enter in Xcode’s debugger
window are stored at `~/Library/Application Support/Apple/Developer
Tools/CustomDataViews/CustomDataViews.plist`.

In addition to supplying custom format strings to display
variables in the debugger, you can also write your own code that
constructs descriptions for variables displayed in the debugger.
These functions can be packaged as a bundle that is loaded into
the process being debugged and can be invoked from format strings.

You can view the value of a variable in a variety of formats,
including hexadecimal, octal, and unsigned decimal. To display a
variable’s value in a different numeric format, select the variable
in the variables view and choose the numeric format from the Debug
> Variables View menu. Choose Debug > Variables View >
Natural to use the default format for a variable’s value, based
on the type of that variable.

You can also cast a variable to a type that’s not included
in the menu. For example, a variable may be declared as `void
*`, but you know it contains a `char
*` value. To cast a variable to a type, select
the variable, choose Debug > Variables View > View Value As
and enter the type.

In addition to changing the display format used for a variable’s
contents in the Value column, Xcode lets you track the value of
the variable as an expression or see the contents of the variable
in memory. To open the Expressions window and add a variable to
it, select the variable and choose Debug > Variables View >
View Variable As Expression. The Expressions window is described
further in [Using the Expressions Window](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugiwviucykjcummjrge). To see the contents of a variable
in memory, using the Memory Browser window, select the variable and
choose Debug > Variables View > View As Memory. See [Browsing the Contents of Memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugiwugsceijbeeqsf) for
more information on the Memory Browser window.

You can also access any of the menu items described in this
section from the contextual menu displayed when you Control-click
a variable.

By default, Xcode does not display global variables in the
variables view. The variables view contains a Globals group, but
it is empty. You can choose which global variables to display in
the Globals section of the debugger’s variable view using the
Globals Browser, shown in Figure 34-2. The Globals
Browser lets you search for global variables by library.

__Figure 34-2__  The Globals Browser

!

You can open the Globals Browser by choosing Debug > Tools
> Global Variables. The debugger must be running and execution
of the program being debugged must be paused for this item to be
available. If you attempt to disclose the contents of the Globals
group in the variables view, Xcode automatically opens the Globals
Browser.

The list on the left of the Globals Browser window, titled
“Library,” lists the available libraries, including system libraries
and your own libraries. To see a library’s global variables, select
that library in the list; the global variables defined by that library
are shown in the table to the right. In the globals table, you can
see:

1. The name
   of the global variable.
2. The file in which the global variable is defined.
3. The current value of the global variable.
4. The type of the global variable.

You can use the search field at the top of the Globals Browser
window to filter the contents of the global variables table. To
the right of the search field, Xcode displays the number of global
variables currently visible, as a fraction of the total number of
global variables in the currently selected library.

To add a global variable to the Globals list in the debugger
window’s variable view, select the checkbox in the “View”
column next to the global variable. You can remove the global variable
from this Globals list by deselecting this checkbox at any time.

When you select a library in the Library list, the full path
to that library is displayed below the list.

The Expressions window lets you view and track the value of
an expression, including a global value or a function result, over
the course of a debugging session. To open the Expressions window,
choose Debug >Tools > Expressions. Type the expression you
wish to track in the Expression field. Xcode adds the expression,
evaluates it, and displays the value and summary for that expression.
The display format of the value and summary information is determined
by any data formatters in effect.

The expression can include any variables that are in scope
at the current statement and can use any function in your project.
To view processor registers, enter an expression such as `'$r0',
'$r1'`.

You can also add a variable to the Expressions window by selecting
the variable in the variables view and choosing Debug > Variables
View > View As Expression. To remove an expression, select it
and press Delete.

Here are some tips on using the Expressions window:

- The expression
  is evaluated in the current frame. As the frame changes, the expression may
  go in and out of scope. When an expression goes out of scope, Xcode
  notes this in the Summary column.
- Always cast a function to its proper return type. The debugger
  doesn’t know the return type for many functions. For example,
  use `(int)getpid()` instead
  of `getpid()`.
- Expressions and functions can have side effects. For example, `i++`,
  increments `i` each time
  it’s evaluated. If you step though 10 lines of code, `i` is
  incremented 10 times.

The disassembly view of the debugger window allows you to
observe disassembled code. The editor in the debugger window supports
three states: Code, Disassembly, and Code and Disassembly. To change
the state of the disassembly view choose Debug > Toggle Disassembly
Display. The mark next to this menu item indicates the current state
of the disassembly view: a line for Disassembly, a checkmark for
Code and Disassembly, and no mark for Code.

When there’s no source code available for the function or
method selected in the Thread list, Xcode displays the disassembled
code in the editor. Figure 34-3 shows disassembled code
in the Xcode debugger.

__Figure 34-3__  Viewing disassembled code in the
debugger

!!

When disassembly view is enabled, the Variables list contains
a Registers group containing all the processor registers.

When execution of the current program is paused in the debugger,
you can browse the contents of memory using the memory browser.
To open the memory browser, shown here, choose Debug > Tools
> Memory Browser. You can also open the Memory Browser to the
location of a particular variable; in the Debugger window, select
the variable and choose Debug > Variables View > View As Memory.

__Figure 34-4__  The
memory browser window

!

In the Memory Browser, you can see:

- A contiguous
  block of memory addresses.
- The contents of memory at those addresses, represented in
  hexadecimal.
- The contents of memory at those addresses, represented in
  ASCII.
- The Address field controls the starting address of the memory
  displayed in the table below. You can enter an address, a variable
  name or expression. Hexadecimal values must be preceded by `0x`.
- The arrows next to the Address field “step” through memory;
  clicking the up arrow shows the previous page of memory, while clicking
  the down arrow returns the next page of memory.
- The Bytes field controls the number of bytes displayed in
  the memory browser. You can choose one of the options from the pop-up
  menu in the Bytes field or type a number directly into the field.
  However, the number of bytes will be rounded up to the next full row
  of memory fetched.
- The Word Size and Columns menus control how the memory is
  divided up and displayed. The Word Size menu specifies the size,
  in bytes, of a single chunk of memory. The Columns menu controls
  how many units, of the size specified by the Word Size menu, are
  displayed for an address.

[Next](Shared%20Libraries%20Window.md)[Previous](Controlling%20Execution%20of%20Your%20Code.md)

