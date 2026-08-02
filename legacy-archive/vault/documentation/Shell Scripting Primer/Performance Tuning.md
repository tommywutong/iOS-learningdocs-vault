---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/performance/performance.html
archived_at: '2026-07-18T01:39:31.083460Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Shell%20Script%20Security.md)[Previous](Advanced%20Techniques.md)

# Performance Tuning

Shell scripts, when compared with compiled languages, generally do not perform well. However, most shell scripts also do not perform as well as they could with a bit of performance tuning. This chapter shows some common pitfalls of shell scripting and demonstrates how to fix these mistakes.

Every line of code in a shell script takes time to execute. This section shows two examples in which avoiding unnecessary external commands results in a significant performance improvement.

The Monte Carlo method sample code, found in [An Extreme Example: The Monte Carlo (Bourne) Method for Pi](An%20Extreme%20Example-%20The%20Monte%20Carlo%20%28Bourne%29%20Method%20for%20Pi.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrguwvgvzu), shows a number of ways to calculate the ordinal value of a byte. The version written using a pure shell approach is painfully slow, in large part because of the loops required.

The best way to optimize performance is to find an external utility written in a compiled language that can perform the same task more easily. Thus, the solution to that performance problem was to use the `perl` or `awk` interpreter to do the heavy lifting. Although they are not compiled languages, both Perl and AWK have compiled routines (`ord` and `index`, respectively) to find the index of a character within a string.

However, when using outside utilities is not possible, you can still reduce the complexity by executing outside tools less frequently. For example, once you have an initialized array containing all of the characters from 1–255 (skipping null), you can reduce the number of iterations by removing more than one character at a time until the character disappears, then going back by one batch of characters and working your way forward again, one character at a time.

The following code runs more than twice as fast (on average) as the purely linear search:

```
ord2()
{
    local CH="$1"
    local STRING=""
    local OCCOPY=$ORDSTRING
    local COUNT=0;

    # Delete ten characters at a time.  When this loop
    # completes, the decade containing the character
    # will be stored in LAST.
    CONT=1
    BASE=0
    LAST="$OCCOPY"
    while [ $CONT = 1 ] ; do
        LAST=`echo "$OCCOPY" | sed 's/^\(..........\)/\1/'`
        OCCOPY=`echo "$OCCOPY" | sed 's/^..........//'`
        CONT=`echo "$OCCOPY" | grep -c "$CH"`
        BASE=`expr $BASE + 10`
    done
    BASE=`expr $BASE - 10`

    # Search for the character in LAST.
    CONT=1;
    while [ $CONT = 1 ]; do
        # Copy the string so we know if we've stopped finding
        # nonmatching characters.
        OCTEMP="$LAST"

        # echo "CH WAS $CH"
        # echo "ORDSTRING: $ORDSTRING"

        # If it's a close bracket, quote it; we don't want to
        # break the regexp.
        if [ "x$CH" = "x]" ] ; then
                CH='\]'
        fi

        # Delete a character if possible.
        LAST=$(echo "$LAST" | sed "s/^[^$CH]//");

        # On error, we're done.
        if [ $? != 0 ] ; then CONT=0 ; fi

        # If the string didn't change, we're done.
        if [ "x$OCTEMP" = "x$LAST" ] ; then CONT=0 ; fi

        # Increment the counter so we know where we are.
        COUNT=$((COUNT + 1)) # or COUNT=$(expr $COUNT '+' 1)
        # echo "COUNT: $COUNT"
    done

    COUNT=$(($COUNT + 1 + $BASE)) # or COUNT=$(expr $COUNT '+' 1)
    # If we ran out of characters, it's a null (character 0).
    if [ "x$OCTEMP" = "x" ] ; then COUNT=0; fi

    # echo "ORD IS $COUNT";

    # Return the ord of the character in question....
    echo $COUNT
    # exit 0
}
```

As you tune, you should be cognizant of the average case time. In the case of a linear search, assuming all possible character values are equally likely, the average time is half of the number of items in the list, or about 127 comparisons. Searching in units of 10, the average is about 1/10 of that plus half of 10, or about 17.69 comparisons, with a worst case of 34 comparisons. The optimal value is 16, with an average of 15.9375 comparisons, and a worst case of 30 comparisons.

Of course, you could write the code as a binary search. Because splitting a string is not easy to do quickly, a binary search works best with strings of known length in which you can cache a series of strings containing some number of periods. If you are searching a string of arbitrary length, this technique would probably be much, much slower than a linear search (unless you use BASH-specific substring expansion, as described in [Truncating Strings](Advanced%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjsgewvgvzrgy)).

Caching the strings of periods used in the splitting process increases initialization time slightly, but after that, the execution time of the search itself improves by about a factor of 2 compared to the “skip 16” version. Whether that tradeoff is appropriate depends largely on how many times you need to perform this operation. If the answer is once, then the extra initialization time will likely erase any performance gain from using the binary search. If the answer is more than once, the binary search is preferable.

Listing 12-1 contains the binary search version.

__Listing 12-1__  A binary search version of the Bourne shell `ord` subroutine

```
# Initialize the split strings.
# This block of code should be
# added to the end of ord_init.

    SPLIT=128
    while [ $SPLIT -ge 1 ] ; do
        COUNT=$SPLIT
        STRING=""
        while [ $COUNT -gt 0 ] ; do
                STRING="$STRING""."
                COUNT=$((COUNT - 1))
        done
        eval "SPLIT_$SPLIT=\"$STRING\"";
        SPLIT=$((SPLIT / 2))
    done

# End of content to add to ord_init

split_str()
{
        STR="$1"
        NUM="$2"
        SPLIT="$(eval "echo \"\$SPLIT_$NUM\"")"
        LEFT="$(echo "$STR" | sed "s/^\\($SPLIT\\).*$/\\1/")"
        RIGHT="$(echo "$STR" | sed "s/^$SPLIT//")"
}


ord3()
{
    local CH="$1"
    OCCOPY="$ORDSTRING"
    FIRST=1;
    LAST=257

    ord3_sub "$CH" "$ORDSTRING" $FIRST $LAST
}


ord3_sub()
{
    local CH="$1"
    OCCOPY="$2"
    FIRST=$3
    LAST=$4

    # echo "FIRST: $FIRST, LAST: $LAST"

    if [ $FIRST -ne $(($LAST - 1)) ] ; then
        SPLITWIDTH=$((($LAST - $FIRST) / 2))
        split_str "$OCCOPY" $SPLITWIDTH
        if [ $(echo "$LEFT" | grep -c "$CH") -eq 1 ] ; then
                # echo "left"
                ord3_sub "$CH" "$LEFT" $FIRST $(( $FIRST + $SPLITWIDTH ))
        else
                # echo "right"
                ord3_sub "$CH" "$RIGHT" $(( $FIRST + $SPLITWIDTH )) $LAST
        fi
    else
        echo $(( $FIRST + 1 ))
    fi
}
```

As expected, this performs significantly better, decreasing execution time by about ten percent in this case. The improved performance, however, is almost precisely offset by the extra initialization costs to enable you to split the list. That is why you should never assume that a theoretically optimal algorithm will perform better than a theoretically less optimal algorithm. In shell scripting, the performance impact of constant cost differences can and often do easily outweigh improvements in algorithmic complexity.

Of course, using a Perl or AWK script to find the ordinal rank is much faster than any of these methods. The purpose of this example is to demonstrate methods for improving efficiency of similar operations, not to show the best way to find the ordinal rank of a character.

The `eval` builtin is a very powerful tool. However, it adds considerable overhead when you use it.

If you are executing the `eval` builtin repeatedly in a loop and do not need to use the results for intermediate calculations, it is significantly faster to store each expression as a series of semicolon-separated commands, then execute them all in a single pass at the end.

For example, the following code shifts the entries in a pseudo-array by one row:

```

test1()
{
        X=1; XA=0
        while [ $X -lt 5 ] ; do
                Y=1;
                while [ $Y -lt 5 ] ; do
                        eval "FOO_$X""_$Y=FOO_$XA""_$Y"
                        Y=`expr $Y + 1`
                done
                X=`expr $X + 1`
                XA=`expr $XA + 1`
        done
}
```

You can speed up this subroutine by about 20% by concatenating the assignment statements into a single string and running `eval` only once, as show in the following example:

```

test3()
{
        X=1; XA=0
        LIST=""
        while [ $X -lt 5 ] ; do
                Y=1;
                while [ $Y -lt 5 ] ; do
                        LIST="$LIST$SEMI""FOO_$X""_$Y=\$FOO_$XA""_$Y"
                        SEMI=";"
                        Y=`expr $Y + 1`
                done
                X=`expr $X + 1`
                XA=`expr $XA + 1`
        done
        # echo $LIST
        eval $LIST
}
```

An even more dramatic performance improvement comes when you can precache these commands into a variable. If you need to repeatedly execute a fairly well-defined series of statements in this way (but don’t want to waste hundreds of lines of space in your code), you can create the list of commands once, then use it repeatedly.

By caching the list of commands, the second and subsequent executions improve by about a factor of 200, which puts its performance at or near the speed of a subroutine call with all of the assignment statements written out.

Another useful technique is to precache a dummy version of the commands, with placeholder text instead of certain values. For example, in the above code you could cache a series of statements in the form `ROW_X_COL_1=ROW_Y_COL_1;`, repeating for each column value. Then, when you needed to copy one row to another, you could do this:

```
eval `echo $ROWCOPY | sed "s/X/$DEST_ROW/g" | sed "s/Y/$SRC_ROW/g"`
```

If you don’t have separate variables for source and destination rows, you might write something like the following:

```
eval `echo $ROWCOPY | sed "s/X/$ROW/g" | sed "s/Y/$(expr $ROW + 1)/g"`
```

By writing the code in this way, you have replaced several lines of iterator code and dozens of `eval` instructions with a single `eval` instruction and two executions of `sed`. The resulting performance improvement is dramatic.

Here are a few more performance tuning tips.

Output to files takes time, output to the console doubly so. If you are writing code where performance is a consideration, you should either execute output commands in the background by adding an ampersand (`&`) to the end of the command or group multiple output statements together.

For example, if you are drawing a game board, the fastest way is to store your draw commands in a single variable and output the data at once. In this way, you avoid taking multiple execution penalties. A very fast way to do this is to disable buffering and set newline to shift down a line without returning to the left edge (run `stty raw` to set both of these parameters), then store the first row into a variable, followed by a newline, followed by backspace characters to shift left to the start of the next row, followed by the next row, and so on.

If the results of a series of instructions may never be used, do not perform those instructions.

For example, consider code that uses the `eval` builtin to obtain the values from a series of variables in a pseudo-array. Suppose that the code returns immediately if any of the variables has a value of 2 or more.

Unless you are accumulating multiple assignment statements into a single call to `eval` (as described in [Reducing Use of the eval Builtin](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjsgawvgvzt)), you should call `eval` on the first statement by itself, make the comparison, run `eval` for the next statement, and so on. By doing so, you are reducing the average number of calls to `eval`.

If you have a subroutine that performs an expensive test two or more times, cache the results of that test and perform the most lightweight comparison possible from then on.

Also, if you have two possible execution paths through your code that share some code in common, it may be faster to use only a single `if` statement and duplicate the small amount of common code rather than repeatedly performing the same comparison. In general, however, such changes will only result in a single-digit percentage improvement in performance, so it is usually not worth the decrease in maintainability to duplicate code in this way.

The performance impact varies depending on the expense of the test. Tests that perform computations or outside execution are particularly expensive and thus should be minimized as much as possible. Of course, you can reduce the additional impact by performing the calculation once and doing a lightweight test multiple times.

A simple test case produced the results shown in Table 12-1.

__Table 12-1__  Performance (in seconds) impact of duplicating common code to avoid redundant tests

| Test performed twice with one copy of shared code in-between | Test performed once with two copies of shared code |
| 7.003 | 6.957 |

In most situations, the appropriate control statement is obvious. To test to see whether a variable contains one of two or three values, you generally choose an `if` statement with a small number of `elif` statements. For larger number of values, you generally choose a `case` statement. This not only leads to more readable code, but also results in _faster_ code.

For small numbers of cases (5), as expected, the difference between a series of `if` statements, an `if` statement with a series of `elif` statements, and a `case` statement is largely lost in the noise, performance-wise, even after 1000 iterations. Although the results shown in Table 12-2 are in the expected order, this was only true approximately half the time. For a smaller number of cases, the differences can largely be ignored.

__Table 12-2__  Performance (in seconds) comparisons of 1000 executions of various control statement sequences

|  | eval builtin executing multiple subroutines | series of if statements | if, then series of elif statements | case statement |
| Five cases | 6.945 | 6..846 | 6.831 | 6.807 |
| Ten cases | 7.094 | 7.224 | 6.980 | 6.903 |
| Fifty cases | 7.023 | 8.03 | 7.392 | 6.704 |

With a larger number of cases, the results more predictably resemble what one might expect. The `case` version is fastest, followed by the `elif` version, followed by the `if` version, with the `eval` version still coming in last. These results tended to be more consistent, though `eval` was often faster than the series of `if` statements.

Although the performance differences (shown in Table 12-2) are relatively small, in a sufficiently complex script with a large number of cases, they can make a sizable difference. In particular, the `case` statement tends to degrade more gracefully, whereas the series of `if` statements by themselves tends to cause an ever-increasing performance penalty.

For example, if you have a subroutine that includes `expr $ROW + 1` in two or more lines of code, you should define a local variable `ROW_PLUS_1` and store the value of the expression in that variable. Caching the results of computation is particularly important if you are using `expr` for more portable math, but doing so consistently results in a small performance improvement even when using shell math.

__Table 12-3__  Performance (in seconds) of 1000 iterations, performing each computation once or twice

| Twice with expr | Once with expr | Twice with shell math | Once with shell math |
| 23.744 | 12.820 | 6.596 | 6.486 |

Using `echo` by itself is typically about 30 times faster than explicitly executing `/bin/echo`. This improved performance also applies to other builtins such as `umask` or `test`.

Of course, `test` is particularly important because it doubles as the bracket (`[`) command, which is essential for most control statements in the shell. If you explicitly write a control statement using `/bin/[`, the script’s performance degrades immensely, Fortunately, it is unlikely that anyone would ever do that accidentally.

__Table 12-4__  Relative performance (in seconds) of 1000 iterations of the `echo` builtin and the `echo` command

| echo (builtin) | /bin/echo | printf (builtin) | /usr/bin/printf |
| 0.285 | 6.212 | 0.230 | 6.359 |

On a related note, the `printf` builtin is significantly faster than the `echo` builtin if your shell provides it (most do). Thus, for maximum performance, you should use `printf` instead of `echo`.

Although significantly less portable, code that uses the ZSH- and BASH-specific `$(( $VAR + 1))` math notation executes up to 125 times faster than identical code written with the `expr` command and up to 225 times faster than identical code written with the `bc` command.

Use `expr` in preference to `bc` for any integer math that exceeds the capabilities of the shell’s math capabilities. The floating-point math used by `bc` tends to be significantly slower.

__Table 12-5__  Relative performance (in seconds) of 1000 iterations of shell math, `expr`, and `bc`

| shell math | expr command | bc command |
| 0.111 | 14.106 | 25.008 |

The `sed` tool, like any other external tool, is expensive to start up. If you are processing a large chunk of data, this penalty is lost in the noise, but if you are processing a short quantity of data, it can be a sizable percentage of script execution time. Thus, if you can process multiple regular expressions in a single instance of `sed`, it is much faster than processing each expression separately.

Consider, for example, the following code, which changes “This is a test” into “This is burnt toast” and then throws away the results by redirecting them to `/dev/null`.

```

function1()
{
    LOOP=0
    while [ $LOOP -lt 1000 ] ; do
        echo "This is a test." | sed 's/a/burnt/g' | sed 's/e/oa/g' > /dev/null

        LOOP=$((LOOP + 1))
    done
}
```

You can speed this up dramatically by rewriting the processing line to look like this:

```
echo "This is a test." | sed -e 's/a/burnt/g' -e 's/e/oa/g' > /dev/null
```

By passing multiple expressions to `sed`, it processes them in a single execution. In this case, the processing of the second expression can be reduced by more than 60% on a typical computer.

As explained in [Avoiding Unnecessary External Commands](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjsgawvgvzr), you can improve performance further by concatenating these strings into a single string and processing the output of all 1000 lines in a single invocation of `sed` (with two expressions). This change reduces the total execution time by nearly a factor of 20 compared with the original version.

For small inputs, the execution penalty is relatively large, so combining expressions results in a significant improvement. For large inputs, the execution penalty is relatively small, so combining expressions generally results in negligible improvement. However, even with large inputs, if the `sed` statements are executed in a loop, the cumulative performance difference could be noticeable.

__Table 12-6__  Relative performance (in seconds) of different use cases for `sed`

|  | Two calls per line (2000 calls total) | One call per line (1000 calls total) | Two calls on accumulated text | One call on accumulated text |
| Single-processor system | 16.874 | 9.983 | 0.670 | 0.665 |
| Dual-processor system | 11.460 | 8.143 | 0.619 | 0.612 |

[Next](Shell%20Script%20Security.md)[Previous](Advanced%20Techniques.md)

