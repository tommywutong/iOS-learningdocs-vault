---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/PaintbyNumbers/PaintbyNumbers.html
archived_at: '2026-07-18T01:39:29.739395Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Regular%20Expressions%20Unfettered.md)[Previous](Subroutines%2C%20Scoping%2C%20and%20Sourcing.md)

# Paint by Numbers

Using math in shell scripts is one area that is often ignored by shell scripting documentation—probably because so few people actually understand the subject. Shell scripts were designed more for string-based processing, with numerical computation as a bit of an afterthought, so this should come as no surprise.

This chapter mainly covers basic integer math operations in shell scripts. More complicated math is largely beyond the ability of shell scripting in general, though you can do such math through the use of inline Perl scripts or by running the `bc` command. These two techniques are described in [Beyond Basic Math](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrgiwvgvzt).

In shell scripts, numeric calculations are done using the command `expr`. This command takes a series of arguments, each of which must contain a single token from the expression to be evaluated. Each number, or symbol must thus be a separate argument.

For example, the expression `(3*4)+2` is written as:

```
expr '(' '3' '*' '4' ')' '+' '2'
```

The command will print the result (`14`) to its standard output,

For numerical comparisons, the same basic syntax is used. To test the truth of the inequality `3 < -2`, use the following statement:

```
expr '3' '<' '-2'
```

This will return a zero (`0`) because the statement is not true. If it were true, it would return a one (`1`).

The most common place to use this command is as part of a loop in a shell script. What follows is a simple example of a for-next loop written in a shell script:

```
COUNT=0
while [ $COUNT -lt '4' ] ; do
    echo "COUNT IS $COUNT"
    COUNT="$(expr "$COUNT" '+' '1')"
done
```

This script is equivalent to the following bit of C:

```
int i;
for (i=0; i<4; i++) {
    printf("COUNT IS %d\n", i);
}
```


Another way to do math operations in `some` Bourne shell dialects is with double parentheses inline. The example below illustrates this technique:

```
echo $((3 + 4))
```

This form is much easier to use than the `expr` command because it is somewhat less strict in terms of formatting. In particular, with the exception of variable decoding, shell expansion is disabled. Thus, operators like less than and greater than do not need to be quoted.

This form is not without its problems, however. In particular, it is not as broadly compatible as the use of `expr`. This form is an extension added by the Korn shell (`ksh`), and later adopted by the Z shell (`zsh`) and the Bourne Again shell (`bash`). In a pure Bourne shell environment, this syntax will probably fail.

While most modern UNIX-based and UNIX-like operating systems use BASH to emulate the Bourne shell, if you are trying to write scripts that are more generally usable, you should use `expr` to do integer math, as described in [The expr Command Also Does Math](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrgiwvgvzs).

As mentioned in,[Shell Script Basics](Shell%20Script%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzt), the shell scripting language contains basic equality testing without the use of the `expr` command. For example:

```
if [ 1 = 2 ] ; then
    echo "equal"
else
    echo "not equal"
fi
```

This code will work as expected. However, it isn't doing what you might initially think it is doing; it is performing a string comparison, _not_ a numeric comparison. Thus the following code will not behave the way you might expect if you assumed a numerical comparison:

```
if [ 1 = "01" ] ; then
    echo "equal"
else
    echo "not equal"
fi
```

It will print the words "not equal", as the strings "1" and "01" are not the same string.

This can also be a problem even when working with the `expr` command if your script takes user input. The `expr` command expects a number or symbol per argument. If you feed it something that isn't just a number or symbol, it will treat it as a string, and will perform string comparison instead of numeric comparison.

The following code demonstrates this in action:

```
expr '1' '+' '2'
expr ' 1' '+' '2'
expr '2' '<' '1'
expr ' 2' '<' '1'
```

The first line will print the number `3`. The second line produces an error message. When doing addition, this mistake is easy to detect. When doing comparisons, however, as shown in the following two lines, the results are more insidious. The number `2` is clearly greater than the number `1`. In string comparison, however, a space sorts before any letter or number. Thus, the third line prints a `0`, while the fourth line prints a `1`. This is probably not what you want.

As with most things in shell scripting, there are many ways to solve this problem, depending on your needs. If you are only worried about spaces, and if the purpose for the comparison is to control shell execution, you can use the numeric evaluation routines built into `test`, as described in the `test` man page.

For example:

```
MYNUMBER=" 2" # Note this is a string, not a number.
# Force an integer comparison.
if [ "$MYNUMBER" -gt '1' ] ; then
    echo 'greater'
fi
```

However, while this works for trivial cases, there are a number of places where this is not sufficient. For example, this cannot be used if:

- Floating point comparison is needed (as described in [Beyond Basic Math](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrgiwvgvzt)).
- The value is preceded by a dollar sign or similar.
- The intended use is as a numerical truth value in a more complicated mathematical expression (without splitting the expression).

A common way to solve such problems is to process the arguments with a regular expression. For example, to strip any nonnumeric characters from a number, you could do the following:

```
MYRAWNUMBER=" 2" # Note this is a string, not a number.

# Strip off any characters that aren't in the range of 0-9
MYNUMBER="$(echo "$MYRAWNUMBER" | sed 's/[^0-9]//g')"

expr "$MYNUMBER" '<' '1'
```

This results in a comparison between the number `2` and the number `1`, as expected.

For more information on regular expressions, see [Regular Expressions Unfettered](Regular%20Expressions%20Unfettered.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrthawvgvzx).

The shell scripting language provides only the most basic mathematical operations on integer values. In most cases, integer operations are sufficient. However, sometimes you may need to exceed those limitations to perform more complicated mathematical operations.

There are two main ways to do floating point math (and other, more sophisticated math). The first is through the use of inline Perl code, the second is through the use of the `bc` command. This section presents both forms briefly.

The first method of doing shell floating point math, inline Perl, is the easiest to grasp. To use this method, you essentially write a short Perl script, then substitute shell variables into the script, then pass it to the `perl` interpreter, either by writing it to a file or by passing it in as a command-line argument.

The following example demonstrates basic floating point math using inline Perl. It assumes a basic understanding of the Perl programming language.

```
#!/bin/sh
PI=3.141592654
RAD=7
AREA=$(perl -e "print \"The value is \".($PI * ($RAD*$RAD)).\"\n\";")
echo $AREA
```

Under normal circumstances, you probably do not want to print an entire string when doing this. However, the use of the string was to demonstrate an important point. Perl evaluates strings between single and double quote marks differently, so when doing inline Perl, it is often necessary to use double quotes. However, the shell only evaluates shell variables within double quotes. Thus, the double quote marks in the script must be quoted so that they actually get passed to the Perl interpreter instead of ending or beginning new command-line arguments.

This need for quoting can prove to be a challenge for more complex inline code, particularly when regular expressions is involved. In particular, it can often be tricky figuring out how many backslashes to use when quoting the quoting of a quotation mark within a regular expression. Such issues are beyond the scope of this document, however.

The `bc` command, short for basic calculator, is a POSIX command for doing various mathematical operations. The `bc` command offers arbitrary precision floating point math, along with a built-in library of common mathematical functions to make programming easier.

The `bc` command takes its input from its standard input, not from the command line. If you pass it command line arguments, they are interpreted as file names to be executed, which is probably not what you want to do when executing math operations inline in a shells script.

Here is an example of using `bc` in a shell script:

```
#!/bin/sh

PI=3.141592654
RAD=7
AREA=$(echo "$PI * ($RAD ^ 2)" | bc)
echo "The area is $AREA"
```

The `bc` command offers much more functionality than described in this section. This section is only intended as a brief synopsis of the available functionality. For full usage notes, see the man page for `bc`.

[Next](Regular%20Expressions%20Unfettered.md)[Previous](Subroutines%2C%20Scoping%2C%20and%20Sourcing.md)

