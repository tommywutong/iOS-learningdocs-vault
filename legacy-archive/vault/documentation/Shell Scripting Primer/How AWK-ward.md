---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/Howawk-ward/Howawk-ward.html
archived_at: '2026-07-18T01:39:29.321176Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Designing%20Scripts%20for%20Cross-Platform%20Deployment.md)[Previous](Regular%20Expressions%20Unfettered.md)

# How AWK-ward

This chapter is a primer to help you learn how to use the AWK programming language and the `awk` interpreter. The `awk` interpreter, much like `sed`, `grep`, and `perl`, is a commonly used text processing tool based on regular expressions.

For more detailed reference material, see the manual page for `awk`, the GNU AWK manual ([http://www.gnu.org/software/gawk/manual/](http://www.gnu.org/software/gawk/manual/)), and Brian Kernighan’s book, _The AWK Programming Language_.

This chapter uses the file `poem.txt` from [Regular Expressions Unfettered](Regular%20Expressions%20Unfettered.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrthawvgvzx) as the basis for most of its examples. Be sure to create that file before attempting any of these examples.

These examples are tested primarily on the OS X version of AWK, which is derived from ["The One True AWK”](http://www.cs.princeton.edu/~bwk/btl.mirror/) by Brian Kernighan. Please report any compatibility problems with other versions of AWK using the feedback links at the bottom of each page.

AWK is a language designed primarily for processing structured data records containing text. This language is executed by the `awk` interpreter.

The design of AWK centers around dividing the input text into records, each one containing a number of fields. Each time the `awk` interpreter encounters a record separator, it begins a new record. By default, the record separator is a newline character, though you can change this as described in [Changing the Record and Field Separators in AWK Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzt).

After the `awk` interpreter has read a complete record from the input, it divides that record into fields. The fields are delimited by a field separator, similar to the field separators described in [Variable Expansion and Field Separators](Flow%20Control%2C%20Expansion%2C%20and%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnbnknltemq).

An AWK script is divided into a series of rules. Once the `awk` interpreter has divided a record into fields, it executes these rules in sequence. Each rule has access to variables that contain the record as a whole and the individual fields of that record. The rules can then perform various modifications to that data, print the data, and so on.

At its most basic, the syntax of an AWK script is very similar to C. The major differences are:

- It is an interpreted language, so it is not as fast as C.
- Semicolons at the end of a statement are generally optional. (They are required only if you need to put more than one statement on a single line).
- A newline (line break) ends a statement. Much like shell scripts or C preprocessor macros, if you put a backslash at the end of one line, the statement continues onto the next line.
- Instead of having a `main` function, the main body of code is divided into a series of filter actions surrounded by curly braces. These filters are applied sequentially for _each record_ in an input file. This means that the code between curly braces may execute more than once.
- Variables are all in the global scope except for parameters to functions. (Function-local variables are described more in [Functions in AWK](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzy).)
- Variables maintain their value across multiple records and files. They are set until explicitly cleared.

Unlike shell scripts (but like C), variables in AWK scripts are not preceded by dollar signs when you use them. This means that they cannot be inserted in the middle of strings.

There are a few special variables that are preceded by a dollar sign, however. The variable `$0` represents an entire record read from the input file. Similarly, AWK divides each record up into fields, which are represented by special variables starting with `$1` and numbering upwards.

Here is a simple AWK script:

```
{
        a=$0;
        print "This is a test: a is " a;
}
```

Save this file as `01_simple.awk`, then run it by typing:

```
awk -f 01_simple.awk poem.txt
```

This executes the AWK script `01_simple.awk` and passes the file `poem.txt` as its input. For each record (a single line, by default) in the file, this will print the following:

```
This is a test: a is line from file
```

You should notice four things about this script:

- Strings separated by spaces are concatenated automatically just as they are in C.
- The `print` statement is much like the `print` statement in Perl. (The AWK language also supports `printf`, whose syntax is like the command-line version, `printf`, except that the arguments are separated by commas instead of spaces.)
- The `awk` interpreter always requires an input file even if your script does not actually read anything from it. If you want `awk` to read from standard input, you must pass a hyphen (`-`) as the filename.
- The `awk` interpreter can take either a string of raw code or a file to execute. If you pass in a string of code as the first argument, that code is executed. If you want `awk` to execute code from a file, you must pass the `-f` flag followed by the path of the script file.

You don’t always want to take an action based on every record in a file. Adding a pattern to a filter action is the most efficient way to limit its scope. In AWK scripts, the action specified by such a conditional filter occurs only if the specified pattern matches the record in question.

The format for a conditional filter rule is as follows:

```
pattern { action }
```

The _action_ here is a series of statements just like any other filter rule. The _pattern_ can be blank (in which case it matches every record), or it can contain any combination of regular expressions or relational expressions. These two types of expressions are briefly explained in the following sections.

Conditional filter rules in AWK scripts may contain one or more regular expressions. These expressions _must_ be a simple search-style regular expression (beginning and ending with a slash). It cannot include a command switch or modifier switches. For example, the following will not work the way you might expect:

- `/mary/i`—Case-insensitive match for “mary” will actually match either the word “mary” or the letter “i”, which is probably not what you want.
- `s/lamb//`—Substitutions are not allowed here and will cause a syntax error.

The following AWK script will print every line that contains “lamb”.

```
/lamb/ {
        a=$0;
        print "This is a test: a is " a;
}
```

Save this file as `02_conditional_regex.awk`, then run it using the `awk` interpreter by typing:

```
awk -f 02_conditional_regex.awk poem.txt
```

As with conditionals in C, you can combine multiple regular expressions with the Boolean operators `!` (not), `||` (or), and `&&` (and). For example, the following rule searches for any line that contains “Mary” but contains neither “lamb” nor “had”:

```
/Mary/ && !(/lamb/ || /had/){
        a=$0;
        print "This is a test: a is " a;
}
```

Save this file as `03_conditional_multiregex.awk`, then run it by typing:

```
awk -f 03_conditional_multiregex.awk poem.txt
```

It prints the following text:

```
This is a test: a is and everywhere that Mary went,
This is a test: a is What about Mary, Mary, and Mary?
```

For more information about regular expressions, read [Regular Expressions Unfettered](Regular%20Expressions%20Unfettered.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrthawvgvzx).

In AWK scripts, when you combine two expressions with a comma (`,`), the action is applied to all records beginning with a record that matches the first pattern and continuing through a record that matches the second one.

Consider the following `awk` script:

```
/married/,/lowercase/{ print $0; }
```

Save this file as `05_conditional_range.awk`, then run it by typing:

```
awk -f 05_conditional_range.awk poem.txt
```

The `awk` interpreter prints every line in the poem file beginning with the line containing “married” and ending with the line containing “lowercase”.

In addition to regular expressions, AWK scripts support relational expressions. You can use relational expressions to perform more fine-grained matching, such as matching based on the content of a particular field or variable.

AWK scripts support four basic forms of relational expression:

- _expression_ `~ /`_regexp_`/`—Expression matches the regular expression.
- _expression_ `!~ /`_regexp_`/`—Expression does not match the regular expression.
- _expression_ _comparison_operator_ _expression_—Basic string or numeric comparison between two expressions.
- _expression_ `in` _array_name_—Expression is a key in the specified array. (See [Working with Arrays in AWK](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzr) for more information on working with arrays.)

The _comparison_operator_ can be any of the standard C comparison operators, such as `==`, `!=`, and so on.

The _expression_ is generally either one of the fields or the result of an operation on one of the fields. For example, the following AWK filter rules show, respectively, how to compare the first field to “mary” in a case-insensitive fashion, how to match all records that do not contain “Mary”, and how to do an exact comparison of the first field against “Mary”:

```
tolower($1) ~ /mary/ { print "CI Record: " $0; }
$0 !~ /Mary/ { print "Not Mary: " $0; }
$1 == "Mary" { print "Mary Record: " $0; }
```

Save this file as `04_conditional_insensitive.awk`, then run it with the `awk` interpreter by typing:

```
awk -f 04_conditional_insensitive.awk poem.txt
```

The script outputs a series of lines beginning with the following:

```
CI Record: Mary had a little lamb,
Mary Record: Mary had a little lamb,
Not Mary: its fleece was white as snow,
Mary Record: Mary fleece was white as snow,
Mary Record: Mary everywhere that Mary went,
```


AWK scripts support two special patterns:`BEGIN` and `END`.

Any action associated with the `BEGIN` pattern executes before the first record is read from the file. You should, for example, make any changes to the record or field separators in a `BEGIN` action, as described in [Changing the Record and Field Separators in AWK Scripts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzt).

Similarly, any action associated with the `END` pattern executes after the last record is read and processed. You could use this to output a special end of data record, for example.

The following example shows the use of `BEGIN` and `END` patterns.

```
BEGIN { print "Here is the line we care about."; }
/chocolate/ { print "Mmm.  Chocolate.  " $0; }
END { print "That's all that matters."; }
```

Save this file as `06_beginend.awk`, then run it with the `awk` interpreter by typing:

```
awk -f 06_beginend.awk poem.txt
```

It prints the following:

```
Here is the line we care about.
Mmm.  Chocolate.  I want chocolate for Valentine's day.
That's all that matters.
```


In addition to matching against input fields, AWK scripts also allow you to use arbitrary variables in conditional pattern matches. Consider the following script:

```
BEGIN { lastwasmary = 0; }
(tolower($1) ~ /mary/ && !lastwasmary) { print "Mary appeared."; lastwasmary = 1; }
(tolower($1) ~ /mary/ && lastwasmary) { print "Mary appeared again"; lastwasmary = 1; }
(tolower($1) !~ /mary/ && lastwasmary) { print "No Mary."; lastwasmary = 0; }
```

This script prints the words “Mary appeared” on the first line in which “Mary” is the first word, but performs the matching in a case-insensitive fashion. It prints “Mary appeared again” for each consecutive line in which “Mary” appears as the first word.

If “Mary” does not appear as the first word in a line, it prints “No Mary” and the variable `lastwasmary` is reset to zero. Thus, the next time “Mary” appears after that, it prints “Mary appeared” instead of “Mary appeared again”.

Of course, in this particular case, you may be better off conditionalizing the pattern using an `if`/`then` statement as described in [Control Statements in AWK](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzrge).

You can also use variables to store the pattern for matching by replacing the entire pattern (including slashes) with the name of a variable. For example:

```
BEGIN { maryword = "mary"; keyword=maryword "lamb"; }
(tolower($1) ~ keyword) { print "Mary appeared."; }
(tolower($1) !~ keyword) { print "No mary."; }
```

This searches for any string in which “marylamb” appears as the first word (in a case-insensitive comparison).

You should notice that strings (and variables containing strings) separated by a space are concatenated automatically in the assignment statement. This effectively allows you to synthesize patterns containing variables.

You can also do the concatenation inline if desired. For example:

```
BEGIN { maryword = "mary"; }
(tolower($1) ~ maryword "lamb" ) { print "Mary appeared."; }
(tolower($1) !~ maryword "lamb" ) { print "No mary."; }
```

This code behaves identically to the previous example, but without the intermediate variable assignment.

In AWK scripts, the default record separator is a newline, but you can change this by modifying the regular expression stored in the variable `RS`. Likewise, the default field separator, stored in the variable `FS`, is a regular expression that matches spaces and tabs.

Unless you are doing something particularly unusual, you should generally change the record separator _before_ the first record is read. To do this, you use the special pattern `BEGIN`, as described in [Special Patterns in AWK: BEGIN and END](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzs).

By the time any other filter rule executes, the `awk` interpreter has already read the first record and divided it into fields, using whatever record and field separators were in place at the time. Thus, if you change the record or field separator in a normal rule, that new record separator is not active until the _next_ record is processed.

For example, the following script sets the record separator to the letter “i” and then prints each record:

```
BEGIN {RS="i"; FS=/r/}
{
        print "Record is: " $0;
        print "First field is " $1;
}
```

The `BEGIN` filter rule is evaluated before the first record in the file, thus setting the record separator to the letter “i” and the field separator to the letter “r”. Then, after the first record is read, the second filter rule is evaluated against it based on the altered record separator.

The AWK language also supports separate output separators for both records and fields. The output record and field separator variables are `ORS` and `OFS`, respectively.

The output field separator is automatically printed between fields whenever you print the value of `$0` (the “whole record” variable), and the output record separator is similarly printed at the end of `$0`.

Control statements in AWK scripts are syntactically almost identical to C control statements.

As in C, the `if` statement looks like this:

```
if (expression) statement;
```

Just as in C, you can create compound statements by wrapping them in curly braces. For example, if you want to execute two statements when a given record contains the word Mary, you might write an AWK script that looks like this:

```
{
        if ($0 ~ /Mary/) {
                print "Mary is in this line:";
                print $0;
        } else {
                print "NOMATCH: " $0;
        }
}
```


The `while` statement looks just like the `if` statement. For example:

```
{
        i=4
        if ($0 ~ /Mary/) {
                while (i) {
                        print i ":" $0;
                        i--;
                }
        }
}
```

As in C, you can skip the remaining code in the body of a `while` loop by calling the `continue` function.

The `for` statement syntax has aspects of both the C syntax and the shell script syntax. The C language form of the `for` statement is as follows:

```
for (pre_expression; while_expression; post_expression) statement
```

This statement is equivalent to the following:

```
pre_expression;
while (while_expression) {
                    statement;
                post_expression;
}
```

The first expression, which executes before entering the `while` loop, usually initializes one or more loop iterators. The second expression is then tested for truth. While it is true, the statement executes. After each iteration through the loop, the third expression executes. This usually increments or decrements the loop iterator.

As in C, you can skip the remaining code in the body of a `for` loop by calling the `continue` function.

For example, the following code prints each line that matches “Mary” three times. These are numbered 1, 2, and 4. It skips the case where `i==2`, and thus the number 3 is never printed.

```
{
        if ($0 ~ /Mary/) {
                for (i=0; i<4; i++) {
                        if (i==2) continue;
                        print i+1 ":" $0;
                }
        }
}
```

In addition, AWK supports a shell-like (really, Perl-like) version of the `for` loop, in which it acts as an array iterator. The array iteration syntax is:

```
for (key_variable in array) statement
```

This syntax is described in more detail in [Working with Arrays in AWK](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzr).

At any point in your filter rules, you can skip processing of all remaining rules (effectively skipping to the next record) by using the `next` statement. For example:

```
if (i > 4) next;
```

Likewise, at any time, you can skip processing of the remainder of an input file by using the `nextfile` statement. For example:

```
if (i > 4) nextfile;
```

The `if` statement syntax is described in [Control Statements in AWK](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzrge).

In addition to providing a number of standard functions (described in the manual page for `awk`), the AWK language allows you to define your own custom functions. The syntax for a function declaration is:

```
function function_name(parameter1 [, parameter2, ...]) {
                    action
}
```

Because variables are in the global scope except for function parameters, if you want to define a local variable in a function, you _must_ declare it as an extra parameter to the function. You do not have to pass in a value. If you do not declare the variable as a parameter, it affects execution outside of the function and its value is persistent across multiple invocations of the function.

For example, this function takes two parameters, subtracts them, and then adds one (`1`):

```
function subtractAndAddOne(a, b, c) {
        c = 1
        return (a-b+c);
}
BEGIN {
        print subtractAndAddOne(3, 2);
}
```


Arrays in AWK scripts are syntactically very similar to arrays in C. Don’t let that fool you, though. Under the hood, they behave very differently.

Arrays in AWK scripts are associative. This means that each array element is stored as a key-value pair, resulting in three major differences when compared to C:

- Arrays are allocated and grow dynamically as space is needed.
- Arrays can be sparse; you can have an array with a value at index `711` and a value at index `1116` with nothing between them.
- You cannot populate an array in a single operation except by splitting a string.

There are two ways to create an array. The first is by simply using it. The second is by using the `split` function. These methods are described in the sections that follow, along with useful tips about working with arrays.

The following code creates and prints an array called `my_array` containing the values “Partridge”, “tree”, “pear”, and “Cassidy”:

```
BEGIN {
        my_array[0] = "Partridge";
        my_array[1] = "pear";
        my_array[2] = "tree";
        my_array["David"] = "Cassidy";

        for ( my_index in my_array ) {
                print my_index "=" my_array[my_index];
        }
}
```

The first thing you will notice is that the array is not printed in order. In fact, it is printed in the order in which the underlying data is stored internally. If you want to print the values in key order, you must walk through the index numerically instead.

The second thing you will notice is that the `for` statement can be used to iterate through all of the keys in the array. In this usage, the `for` statement in AWK scripts is like the `for` statement in a shell script. The `for` statement array-iterator usage is:

```
for (key_variable in array_name) statement
```

The third thing you will notice is that, unlike C, array elements can take arbitrary strings as their key (array index). If you need to iterate through the array in key order, however, you should limit yourself to numeric keys.

As a side effect, the keys are _always_ stored as a string even if they only contain numbers. Thus, if you want to compare them numerically to each other (for example, to find the smallest key for which a value exists), you must add zero (0) to the key prior to making the comparison.

For example, the following code iterates through this sparse array in key order by finding the minimum and maximum key values and then iterating from the minimum to the maximum:

```
BEGIN {
        my_array[0] = "Partridge";
        my_array[1] = "pear";
        my_array[2] = "tree";
        my_array[13] = "Cassidy";

        min = 0; max = 0;
        for ( my_index in my_array ) {
                if (my_index+0 < min) min = my_index;
                if (my_index+0 > max) max = my_index;
        }
        for (i=min; i<= max; i++) {
                if (i in my_array) {
                        print i "=" my_array[i];
                }
                if (!(i in my_array)) {
                        print i " is unset.";
                }
        }
}
```

In this example, you should note the `if` statement syntax near the end. Before printing an array value, the example checks to see if a value has ever been stored for that key value:

```
if (i in my_array) { ... }
```

As with any expression, you can invert matching with an exclamation point. For example, to check to see if a particular index has never been stored in an array, you could write the following:

```
if (!(i in my_array)) { ... }
```


Assigning array elements individually can be very tedious. A more common (read “less painful”) way to create an array is with the `split` function. The `split` syntax is as follows:

```
count = split( string, array_name, regexp );
```

For example, the following code splits the string “Mary lamb freezer” into words separated by spaces.

```
BEGIN {
        arr_len = split( "Mary lamb freezer", my_array, / / );
}
```

The result is that `arr_len` contains the number three (`3`). The variable `my_array[1]` contains “Mary”, `my_array[2]` contains “lamb”, and so on.

The AWK language does not support assignment of arrays. Thus, to copy an array, you must copy the individual values from one array to the next. For example, the following code initializes `my_array` and then copies its contents to `copy_array` before printing the array:

```
BEGIN {
        arr_len = split( "Mary lamb freezer", my_array, / / );
        for (word in my_array) {
                copy_array[word] = my_array[word];
        }
        for (word in copy_array) {
                print copy_array[word];
        }
}
```

Similarly, the AWK language does not provide functions to join an array. To join an array, you should write a simple function like this one:

```
function join(input_array, separator) {
        string = "";
        first = 1;

        # Note: the array items are in no particular
        # order when joined with this function.
        for (i in input_array) {
                if (first) first = 0;
                else string = string separator;
                string = string input_array[i];
        }
        return string;
}
BEGIN {
        arr_len = split( "foo bar baz", my_array, / /);

        for (word in my_array) {
                print my_array[word];
        }

        print join(my_array, " ");
}
```

Like all array functions written using the array-iterator form of the `for` statement, this join does not occur in any particular order. If you need to join the array values in a particular order, you must write your own custom `join` function either using a numeric iterator or a manually specified list of fields. For example:

```
function count_elements(input_array)
{
    counter=0;
    for (word in input_array) {
        counter++;
    }
    return counter;
}
function join(input_array, separator) {
        string = "";
        first = 1;

        # Note: this preserves order, but does not
        # work with nonnumeric or sparse arrays.
        for (i=1; i<=count_elements(input_array); i++) {
                if (first) first = 0;
                else string = string separator;
                string = string input_array[i];
        }
        return string;
}
BEGIN {
        arr_len = split( "foo bar baz", my_array, / /);

        for (word in my_array) {
                print my_array[word];
        }

        print join(my_array, " ");
}
```


As you saw in [Array Basics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzx), you can add values to an array using arbitrary keys. You can also check to see if a value exists for a given key using the `if (key in array)` syntax.

If you need to delete a key-value pair, you could assign an empty value. However, the `if (key in array)` syntax still evaluates to true because there is still a value for that key (albeit an empty value). Thus, you probably want to remove the key entirely.

The AWK programming language solves this problem with the `delete` function. The syntax for `delete` is:

```
delete array_name[key];
```

For example, the following script prints only the key-value pairs “purple = Partridge” and “majesties = tree”.

```
BEGIN {
        my_array["purple"] = "Partridge";
        my_array["mountain"] = "pear";
        my_array["majesties"] = "tree";
        my_array["fruited"] = "Cassidy";

        mykey = "fruited";
        delete my_array["mountain"];
        delete my_array[mykey];

        for (i in my_array) {
                print i "=" my_array[i];
        }
}
```

If you need to clear all values from an array simultaneously, though, you don’t have to delete them one at a time. Instead, you can simply do the following:

```
delete array_name;
```

This statement leaves the array specified by _array_name_ empty for future use. You might do this if, for example, you want an array to be reset for each record.

The AWK programming language was primarily intended as a filter between one or more input files (or standard input) and standard output. However, it does provide some basic input and output capability.

As in shell scripts, any print statement can be written to a file using the redirection (`>`) operator (which destroys any previous contents of the file) or concatenated onto the end of an existing file using the concatenation (`>>`) operator.

Also, as in shell scripts, any print statement can be piped to an outside tool using the pipe (`|`) operator.

Pipes and redirections, however, behave differently in AWK scripts than in shell scripts; they remain open for future use until you explicitly close them or `awk` exits. This means, among other things, that the concatenation (`>>`) operator is only necessary if you want to retain an existing file and is not necessary to continue adding to a file that you create in `awk`.

For example, this script does the following:

- Sends two strings to `/bin/tail -n 1`. The `tail` tool prints the last line sent (which contains the second string). This demonstrates that the first two print statements both sent their output to the same instance of `tail`.
- Closes the output to that pipe and sends another message to tail. This shows that a new instance of `tail` processed this command (because otherwise, the previous line would not have been printed).
- Writes two lines to the file `/tmp/testfile-awk`. If this file exists, it is overwritten. By using the redirect operator, the script demonstrates that additional output (after the first redirect) is appended to the file until the file is closed (regardless of whether you use the redirect or concatenation operator).

```
BEGIN {
        print "This is a test." | "/usr/bin/tail -n 1";
        print "This is only a test." | "/usr/bin/tail -n 1";
        close("/usr/bin/tail -n 1");
        print "Yikes!" | "/usr/bin/tail -n 1";

        print "This is another test" > "/tmp/testfile-awk"
        print "This is yet another test entirely" > "/tmp/testfile-awk"
}
```

In a similar way, you can read input from a file using the redirection or pipe operator by combining the operator with the `getline` function. The `getline` reads a record from an outside file or pipe under programmatic control.

When you call `getline`, the `awk` interpreter sets the variable `$0` to the next record from the specified file. The function returns `1` if a record was read, `0` if the end of file was reached, or `-1` if an error occurred (for example, if the file does not exist).

The following AWK script reads a record from `/tmp/testfile-awk`, and then reads a record from the output of the `echo` command:

```
BEGIN {
        getline < "/tmp/testfile-awk";
        print "The record was " $0;

        "/bin/echo 'This is a test line'" | getline
        print "The second record was " $0;
}
```


It is often useful to combine AWK scripts with shell scripts to perform various tasks. This creates two challenges: getting information into an AWK script (beyond the bulk data read via standard input) and getting information back out in a form that is usable by the shell. These topics are covered in the sections that follow.

Much like the similarly named C variables, the `ARGV` variable is an array of arguments passed to an AWK script, and the `ARGC` variable contains the number of arguments in `ARGV`. These variables are demonstrated in Listing 9-1.

__Listing 9-1__  Test script for arguments (`23_arguments.awk`)

```
{
    for (i=0; i<ARGC; i++) {
        print "ARGUMENT " i " is " ARGV[i];
    }
}
```

Save this script as `23_arguments.awk` and then issue the following commands:

```
echo > myinputfile
awk -f 23_arguments.awk myinputfile
```

You should see the following output:

```
ARGUMENT 0 is awk
ARGUMENT 1 is myinputfile
```


As in shell scripts, AWK scripts have access to environment variables. The AWK interpreter stores a copy of its environment in the `ENVIRON` associative array, indexed by the name of the variable.

For example, to print the value of the `PATH` environment variable, you would write code like the following:

```
{
    print "PATH IS: " ENVIRON["PATH"];
}
```


When writing shell scripts, one of the trickiest things to get right is handling the output of tools that your scripts call. Fortunately, the tabular data format commonly used by AWK scripts is also easy to read in shell scripts. The UNIX command-line environment provides the `cut` tool, which is specifically designed to extract tabular data from lines of text.

Consider the following AWK script. It reads a file containing five tab-delimited data fields, then outputs three of those fields (also in a tab-delimited format).


```
BEGIN {
    RS="\n";
    FS="\t";
}
{
    print $1 "\t" $3 "\t" $5;
}
```

You can parse its output as shown in Listing 9-2.

__Listing 9-2__  Parsing the output of an AWK script

```
#!/bin/sh

# Store the output in a variable.

OUTPUT="$(awk 'BEGIN { \
        RS="\n"; \
        FS="\t"; \
     } \
     { \
        print $1 "\t" $3 "\t" $5; \
     }' tab_delimited_file)"

# Set the field separator to a newline so that
# the "for" statement below will put one line
# at a time in the "LINE" variable.
IFS="
"

# Parse and print the records.
RECORD=1
for LINE in $OUTPUT ; do
        # By default, cut uses tab as its delimiter,
        # so these commands take the first,
        # second, and third tab-delimited fields
        # from a single line of input, respectively.
        FIELD_1="$(echo "$LINE" | cut -f 1)"
        FIELD_2="$(echo "$LINE" | cut -f 2)"
        FIELD_3="$(echo "$LINE" | cut -f 3)"

        echo "RECORD $RECORD"
        echo "    FIELD 1: $FIELD_1"
        echo "    FIELD 2: $FIELD_2"
        echo "    FIELD 3: $FIELD_3"
        echo
        RECORD="$(expr $RECORD '+' 1)"
done
```

Another useful technique when dealing with complex result sets is to write different pieces of data to different files. Parsing several simple files can sometimes be easier than parsing a single complex result set, particularly when parsing it in a shell script.

[Next](Designing%20Scripts%20for%20Cross-Platform%20Deployment.md)[Previous](Regular%20Expressions%20Unfettered.md)

