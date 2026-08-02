---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/AnExtremeExample/AnExtremeExample.html
archived_at: '2026-07-18T01:39:28.766358Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Historical%20Footnotes%20and%20Arcana.md)[Previous](Starting%20Points.md)

# An Extreme Example: The Monte Carlo (Bourne) Method for Pi

The Monte Carlo method for calculating Pi is a common example program used in computer science curricula. Most CS professors do not force their students to write it using a shell script, however, and doing so poses a number of challenges.

The Monte Carlo method is fairly straightforward. You take a unit circle and place it inside a 2x2 square and randomly throw darts at it. For any dart that hits within the circle, you add one to the "inside" counter and the "total" counter. For any dart that hits outside the circle, you just add one to the "total" counter. When you divide the number of hits inside the circle by the number of total throws, you get a number that (given an infinite number of sufficiently random throws) will converge towards π/4 (one fourth of pi).

A common simplification of the Monte Carlo method (which is used in this example) is to reduce the square to a single unit in size, and to reduce the unit circle to only a quarter circle. Thus, the circle meets two corners of the square and has its center at the third corner..

The computer version of this problem, instead of throwing darts, uses a random number generator to generate a random point within a certain set of bounds. In this case, the code uses integers from 0-65,535 for both the x and y coordinates of the point. It then calculates the distance from the point (0,0) to (x,y) using the pythagorean theorem (the hypotenuse of a right triangle with edges of lengths x and y). If this distance is greater than the unit circle (65,535, in this case), the point falls outside the "circle". Otherwise, it falls inside the "circle".

To obtain random numbers, this code example uses the `dd` command to read one byte at a time from `/dev/random`. Then, it must calculate the numeric equivalent of these numbers. That process is described in [Finding The Ordinal Rank of a Character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrguwvgvzr).

The following example shows how to read a byte using `dd`:

```
# Read four random bytes.
RAWVAL1="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"
RAWVAL2="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"
RAWVAL3="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"
RAWVAL4="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"

# Calculate the ordinality of the bytes.
XVAL0=$(ord "$RAWVAL1") # more on this subroutine later
XVAL1=$(ord "$RAWVAL2") # more on this subroutine later
YVAL0=$(ord "$RAWVAL3") # more on this subroutine later
YVAL1=$(ord "$RAWVAL4") # more on this subroutine later

# We basically want to get an unsigned 16-bit number out of
# two raw bytes.  Earlier, we got the ord() of each byte.
# Now, we figure out what that unsigned value would be by
# multiplying the high order byte by 256 and adding the
# low order byte.  We don't really care which byte is which,
# since they're just random numbers.
XVAL=$(( ($XVAL0 * 256) + $XVAL1 ))   # use expr for older shells.
YVAL=$(( ($YVAL0 * 256) + $YVAL1 ))   # use expr for older shells.
```


There are many ways to calculate the ordinal rank of a character. This example presents three of those: inline Perl, inline AWK, and a more purist (read "slow") version using only `sed` and `tr`.

The easiest way to find the ordinal rank of a character in a shell script is by using inline Perl code. In the following example, the raw character is echoed to the `perl` interpreter's standard input. (See the `perl` manual page for more information about Perl.)

The short Perl script sets the record separator to undefined, then reads data until EOF, finally printing the ordinal value of the character that it retrieves using the `ord` subroutine.

```
YVAL1=$(echo $RAWVAL4 | perl -e '$/ = undef; my $val = <STDIN>; print ord($val);')
```


The second method for obtaining the ordinal rank of a character is slightly more complicated, but still relatively fast. Performance is only slightly slower than the Perl example.

```
            YVAL0=$(echo $RAWVAL3 | awk '{
                RS="\n"; ch=$0;
                # print "CH IS ";
                # print ch;
                if (!length(ch)) { # must be the record separator.
                        ch="\n"
                };
                s="";
                for (i=1; i<256; i++) {
                        l=sprintf("%c", i);
                        ns = (s l); s = ns;
                };
                pos = index(s, ch); printf("%d", pos)
            }')
```

In this example, the raw character is echoed to an AWK script. (See the `awk` manual page and [How AWK-ward](How%20AWK-ward.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrhawvgvzrga) for more information about AWK.) That script iterates through the numbers 1-255, concatenating the character (`l`) whose ASCII value is that number (`i`) onto a string (`ns`). It then asks for the location of that character in the string. If no value is found, index will return zero (0), which is convenient, as `NULL` (character 0) is excluded from the string.

The surprising thing is that this code, while seemingly far more complicated than the Perl equivalent, performs almost as well (less than half a second slower per 100 iterations).

This example was written less out of a desire to actually use such a method and more out of a desire to prove that such code is possible. It is, by far, the most roundabout way to calculate the ordinal rank of a character that you are likely to ever encounter. It behaves much like the `awk` program described in [Finding Ordinal Rank Using AWK](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrguwvgvzs), but without using any other programming languages other than Bourne shell scripts.

The first part of this example is a small code snippet to convert an integer into its octal equivalent. This will be important later.

__Listing E-1__  An Integer to Octal Conversion subroutine

```
# Convert an int to an octal value.
inttooct()
{
        echo $(echo "obase=8; $1" | bc)
}
```

This code is relatively straightforward. It tells the basic calculator, `bc`, to print the specified number, converting the output to base 8 (octal).

The next part of this example is the code to initialize a string containing a list of all of the possible ASCII characters except `NULL` (character 0) in order. This subroutine is called only once at program initialization; the shell version of this code is very slow as it is, and calling this subroutine each time you try to find the ordinal rank of a character would make this code completely unusable.

```
# Initializer for the scary shell ord subroutine.
ord_init()
{
    I=1
    ORDSTRING=""
    while [ $I -lt 256 ] ; do
        # local HEX=$(inttohex $I);
        local OCT=$(inttooct $I);
        # The following should work with GNU sed, but
        # OS X's sed doesn't support \x.
        # local CH=$(echo ' ' | sed "s/ /\\x$HEX/")
        # How about this?
        # local CH=$(perl -e  "\$/=undef; \$x = ' '; \$x =~ s/ /\x$HEX/g; print \$x;")
        # Yes, that works, but it's cheating.  Here's a better one.
        local CH=$(echo ' ' | tr ' ' "\\$OCT");
        ORDSTRING=$ORDSTRING$CH
        I=$(($I + 1)) # or I=$(expr $I '+' 1)
        # echo "ORDSTRING: $ORDSTRING"
    done
}
```

This version shows three possible ways to generate a raw character from the numeric equivalent. The first way works in Perl and works with GNU `sed`, but does not work with the `sed` implementation in OS X. The second way uses the `perl` interpreter. While this way works, the intent was to avoid using other scripting languages if possible.

The third way is an interesting trick. A string containing a single space is passed to `tr`. The `tr` command, in its normal use, substitutes all instances of a particular character with another one. It also recognizes character codes in the form of a backslash followed by three octal digits. Thus, in this case, its arguments tell it to replace every instance of a space in the input (which consists of a single space) with the character equivalent of the octal number `$OCT`. This octal number, in turn, was calculated from the loop index (`I`) using the octal conversion subroutine shown in [Listing E-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrguwvgvzt).

When this subroutine returns, the global variable `$ORDSTRING` contains every ASCII character beginning with character 1 and ending with character 255.

The final piece of this code is a subroutine to locate a character within a string and to return its index. Again, this can be done easily with inline Perl code, but the goal of this code is to do it without using any other programming language.

```
ord()
{
    local CH="$1"
    local STRING=""
    local OCCOPY=$ORDSTRING
    local COUNT=0;

    # Some shells can't handle NULL characters,
    # so this code gets an empty argument.
    if [ "x$CH" = "x" ] ; then
        echo 0
        return
    fi

    # Delete the first character from a copy of ORDSTRING if that
    # character doesn't match the one we're looking for.  Loop
    # until we don't have any more leading characters to delete.
    # The count will be the ASCII character code for the letter.
    CONT=1;
    while [ $CONT = 1 ]; do
        # Copy the string so we know if we've stopped finding
        # nonmatching characters.
        OCTEMP="$OCCOPY"

        # echo "CH WAS $CH"
        # echo "ORDSTRING: $ORDSTRING"

        # Delete a character if possible.
        OCCOPY=$(echo "$OCCOPY" | sed "s/^[^$CH]//");

        # On error, we're done.
        if [ $? != 0 ] ; then CONT=0 ; fi

        # If the string didn't change, we're done.
        if [ "x$OCTEMP" = "x$OCCOPY" ] ; then CONT=0 ; fi

        # Increment the counter so we know where we are.
        COUNT=$((COUNT + 1)) # or COUNT=$(expr $COUNT '+' 1)
        # echo "COUNT: $COUNT"
    done

    COUNT=$(($COUNT + 1)) # or COUNT=$(expr $COUNT '+' 1)
    # If we ran out of characters, it's a null (character 0).
    if [ "x$OCTEMP" = "x" ] ; then COUNT=0; fi

    # echo "ORD IS $COUNT";

    # Return the ord of the character in question....
    echo $COUNT
    # exit 0
}
```

Basically, this code repeatedly deletes the first character from a copy of the string generated by the `ord_init` subroutine unless that character matches the pattern. As soon as it fails to delete a character, the number of characters deleted (before finding the matching character) is equal to one less than the ASCII value of the input character. If the code runs out of characters, the input character must have been the one character omitted from the ASCII lookup string: `NULL` (character 0).


```
#!/bin/sh

ITERATIONS=1000
SCALE=6

# Prevent sed from caring about high ASCII characters not
# being valid UTF-8 sequences
export LANG="C"

# Set FAST to "slow", "medium", or "fast".  This controls
# which ord() subroutine to use.
#
# slow-use a combination of Perl, AWK, and shell methods
# medium-use only Perl and AWK methods.
# fast-use only Perl

# FAST="slow"
# FAST="medium"
FAST="fast"

# 100 iterations - FAST
# real    0m9.850s
# user    0m2.162s
# sys     0m8.388s

# 100 iterations - MEDIUM
# real    0m10.362s
# user    0m2.375s
# sys     0m8.726s

# 100 iterations - SLOW
# real    2m25.556s
# user    0m32.545s
# sys     2m12.802s

# Calculate the distance from point 0,0 to point X,Y.
# In other words, calculate the hypotenuse of a right
# triangle whose legs are of length X and Y.
distance()
{
    local X=$1
    local Y=$2

    DISTANCE=$(echo "sqrt(($X ^ 2) + ($Y ^ 2))" | bc)

    echo $DISTANCE
}

# Convert an int to a hex value.  (Not used.)
inttohex()
{
    echo $(echo "obase=16; $1" | bc)
}

# Convert an int to an octal value.
inttooct()
{
    echo $(echo "obase=8; $1" | bc)
}

# Initializer for the scary shell ord subroutine.
ord_init()
{
    I=1
    ORDSTRING=""
    while [ $I -lt 256 ] ; do
    # local HEX=$(inttohex $I);
    local OCT=$(inttooct $I);
    # The following should work with GNU sed, but
    # OS X's sed doesn't support \x.
    # local CH=$(echo ' ' | sed "s/ /\\x$HEX/")
    # How about this?
    # local CH=$(perl -e  "\$/=undef; \$x = ' '; \$x =~ s/ /\x$HEX/g; print \$x;")
    # Yes, that works, but it's cheating.  Here's a better one.
    local CH=$(echo ' ' | tr ' ' "\\$OCT");
    ORDSTRING=$ORDSTRING$CH
    I=$(($I + 1)) # or I=$(expr $I '+' 1)
    # echo "ORDSTRING: $ORDSTRING"
    done
}

# This is a scary little lovely piece of shell script.
# It finds the ord of a character using only the shell,
# tr, and sed.  The variable ORDSTRING must be initialized
# prior to first use with a call to ord_init.  This string
# is not modified.
ord()
{
    local CH="$1"
    local STRING=""
    local OCCOPY=$ORDSTRING
    local COUNT=0;


    # Some shells can't handle NULL characters,
    # so this code gets an empty argument.
    if [ "x$CH" = "x" ] ; then
        echo 0
        return
    fi

    # Delete the first character from a copy of ORDSTRING if that
    # character doesn't match the one we're looking for.  Loop
    # until we don't have any more leading characters to delete.
    # The count will be the ASCII character code for the letter.
    CONT=1;
    while [ $CONT = 1 ]; do
    # Copy the string so we know if we've stopped finding
    # nonmatching characters.
    OCTEMP="$OCCOPY"

    # echo "CH WAS $CH"
    # echo "ORDSTRING: $ORDSTRING"

    # Delete a character if possible.
    OCCOPY=$(echo "$OCCOPY" | sed "s/^[^$CH]//");

    # On error, we're done.
    if [ $? != 0 ] ; then CONT=0 ; fi

    # If the string didn't change, we're done.
    if [ "x$OCTEMP" = "x$OCCOPY" ] ; then CONT=0 ; fi

    # Increment the counter so we know where we are.
    COUNT=$((COUNT + 1)) # or COUNT=$(expr $COUNT '+' 1)
    # echo "COUNT: $COUNT"
    done

    COUNT=$(($COUNT + 1)) # or COUNT=$(expr $COUNT '+' 1)
    # If we ran out of characters, it's a null (character 0).
    if [ "x$OCTEMP" = "x" ] ; then COUNT=0; fi

    # echo "ORD IS $COUNT";

    # Return the ord of the character in question....
    echo $COUNT
    # exit 0
}

# If we're using the shell ord subroutine, we need to
# initialize it on launch.  We also do a quick sanity
# check just to make sure it is working.
if [ "x$FAST" = "xslow" ] ; then
    echo "Initializing Bourne ord subroutine."
    ord_init

    # Test our ord subroutine
    echo "Testing ord subroutine"
    ORDOFA=$(ord "a")
    # That better be 97.
    if [ "$ORDOFA" != "97" ] ; then
        echo "Shell ord subroutine broken.  Try fast mode."
    fi

    echo "ord_init done"
fi

COUNT=0
IN=0

# For the Monte Carlo method, we check to see if a random point between
# 0,0 and 1,1 lies within a unit circle distance from 0,0.  This allows
# us to approximate pi.
while [ $COUNT -lt $ITERATIONS ] ; do
    # Read four random bytes.
    RAWVAL1="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"
    RAWVAL2="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"
    RAWVAL3="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"
    RAWVAL4="$(dd if=/dev/random bs=1 count=1 2> /dev/null)"

    # ord "$RAWVAL4";
    # exit 0;

    # The easy method for doing an ord() of a character: use Perl.
    XVAL0=$(echo $RAWVAL1 | perl -e '$/ = undef; my $val = <STDIN>; print ord($val);')
    XVAL1=$(echo $RAWVAL2 | perl -e '$/ = undef; my $val = <STDIN>; print ord($val);')

    # The not-so-easy way using AWK (but still almost as fast as Perl)
    if [ "x$FAST" != "xfast" ] ; then
        # Run this for FAST = medium or slow.
        echo "AWK ord"
        # Fun little AWK program for calculating ord of a letter.
        YVAL0=$(echo $RAWVAL3 | awk '{
        RS="\n"; ch=$0;
        # print "CH IS ";
        # print ch;
        if (!length(ch)) { # must be the record separator.
            ch="\n"
        };
        s="";
        for (i=1; i<256; i++) {
            l=sprintf("%c", i);
            ns = (s l); s = ns;
        };
        pos = index(s, ch); printf("%d", pos)
        }')
        # Fun little shell script for calculating ord of a letter.
    else
        YVAL0=$(echo $RAWVAL3 | perl -e '$/ = undef; my $val = <STDIN>; print ord($val);')
    fi

    # The evil way---slightly faster than looking it up by hand....
    if [ "x$FAST" = "xslow" ] ; then
        # Run this ONLY for FAST = slow.  This is REALLY slow!
        YVAL1=$(ord "$RAWVAL4")
    else
        YVAL1=$(echo $RAWVAL4 | perl -e '$/ = undef; my $val = <STDIN>; print ord($val);')
    fi

    # echo "YV3: $VAL3"
    # YVAL1="0"

    # We basically want to get an unsigned 16-bit number out of
    # two raw bytes.  Earlier, we got the ord() of each byte.
    # Now, we figure out what that unsigned value would be by
    # multiplying the high order byte by 256 and adding the
    # low order byte.  We don't really care which byte is which,
    # since they're just random numbers.
    XVAL=$(( ($XVAL0 * 256) + $XVAL1 ))   # use expr for older shells.
    YVAL=$(( ($YVAL0 * 256) + $YVAL1 ))   # use expr for older shells.

    # This doesn't work well, since we can't seed AWK's PRNG
    # in any useful way.
    # YVAL=$(awk '{printf("%d", rand() * 65535)}')

    # Calculate the difference.
    DISTANCE=$(distance $XVAL $YVAL)
    echo "X: $XVAL, Y: $YVAL, DISTANCE: $DISTANCE"

    if [ $DISTANCE -le 65535 ] ; then # use expr for older shells
        echo "In circle.";
        IN=$(($IN + 1))
    else
        echo "Outside circle.";
    fi

    COUNT=$(($COUNT + 1))                # use expr for older shells.
done

# Calculate PI.
PI=$(echo "scale=$SCALE; ($IN / $ITERATIONS) * 4" | bc)

# Print the results.
echo "IN: $IN, ITERATIONS: $ITERATIONS"
echo "PI is about $PI"
```

[Next](Historical%20Footnotes%20and%20Arcana.md)[Previous](Starting%20Points.md)

