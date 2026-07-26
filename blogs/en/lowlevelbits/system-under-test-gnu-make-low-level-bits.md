---
title: 'System Under Test: GNU Make - Low Level Bits 🇺🇦'
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/system-under-test-gnu-make/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:722b4258dfab1522'
translated: false
---

> 原文：[System Under Test: GNU Make - Low Level Bits 🇺🇦](https://lowlevelbits.org/system-under-test-gnu-make/)　·　Low Level Bits (Alex Denisov)

# System Under Test: GNU Make

_Published on Jun 12, 2016_

**UPD:** The series of blog-posts “System Under Test” became a full-fledged project and has moved to its own [domain](http://systemundertest.org). The most recent version of this article lives [here](http://systemundertest.org/gnu-make) now.

_Note: This is a guest post written by a good friend and colleague of mine [Stanislav Pankevich](https://twitter.com/sbpankevich)_

### Introduction

This article is part of series [System Under Test](https://lowlevelbits.org/system-under-test/). It provides an overview of how GNU Make is tested.

**Disclaimer:** the author of this post is not involved into a development of GNU Make project. All of the following is merely a high-level report about what a curious developer can see from looking at the GNU Make’s sources. The author didn’t go very deep into the topic, could overlook something etc. Having that said, we always appreciate feedback from our colleagues who have advanced experience with the projects we write about, especially from the developers and maintainers.

### Getting GNU Make’s sources

GNU Make’s source code is available from git repository and can be found 2 links away from the Make’s main home page: [GNU Make](https://www.gnu.org/software/make/):

> Development

> For development sources, issue trackers, and other information, please see the Make project page at savannah.gnu.org.

On [Make’s Savannah’s page](http://savannah.gnu.org/projects/make):

> [Git Source Code Manager: Git Repository](http://savannah.gnu.org/git/?group=make)

To get Make’s sources:

```
git clone git://git.savannah.gnu.org/make.git GNUMake
cd make
```

### Good news: Make has tests

```
$ ls -l tests/
total 376
-rw-r--r--   1 Stanislaw  staff  35147 May 27 20:54 COPYING
-rw-r--r--   1 Stanislaw  staff  48828 May 27 20:54 ChangeLog.1
-rw-r--r--   1 Stanislaw  staff   6765 May 27 20:54 NEWS
-rw-r--r--   1 Stanislaw  staff   4677 May 27 20:54 README
-rw-r--r--   1 Stanislaw  staff    470 May 27 20:54 config-flags.pm.in
-rwxr-xr-x   1 Stanislaw  staff   1705 May 27 20:54 config_flags_pm.com
-rw-r--r--   1 Stanislaw  staff    359 May 27 20:54 guile.supp
-rwxr-xr-x   1 Stanislaw  staff   1424 May 27 20:54 mkshadow
-rwxr-xr-x   1 Stanislaw  staff     36 May 27 20:54 run_make_tests
-rwxr-xr-x   1 Stanislaw  staff   8330 May 27 20:54 run_make_tests.com
-rw-r--r--   1 Stanislaw  staff  14179 May 27 20:54 run_make_tests.pl
drwxr-xr-x  10 Stanislaw  staff    340 May 27 20:54 scripts
-rw-r--r--   1 Stanislaw  staff  40197 May 27 20:54 test_driver.pl
```

The actual tests are located in `tests/scripts` directory:

```
$ ls -l tests/scripts
total 8
drwxr-xr-x  40 Stanislaw  staff  1360 Jun  2 21:47 features
drwxr-xr-x  31 Stanislaw  staff  1054 May 27 20:54 functions
drwxr-xr-x  10 Stanislaw  staff   340 May 27 20:54 misc
drwxr-xr-x  18 Stanislaw  staff   612 May 29 10:22 options
drwxr-xr-x  12 Stanislaw  staff   408 Jun 10 20:42 targets
-rw-r--r--   1 Stanislaw  staff  1015 May 27 20:54 test_template
drwxr-xr-x  22 Stanislaw  staff   748 May 27 20:54 variables
drwxr-xr-x   3 Stanislaw  staff   102 May 27 20:54 vms
```

The following are interesting notes I found before running the tests.

#### The oldest update in NEWS file dates back to 1992

```
Changes from 0.1 to 0.2 (5-4-92):

README corrected to require perl 4.019, not 4.010.

-make_path replaces -old.

errors_in_commands test updated for change in format introduced in
make 3.62.6.

test_driver_core now uses a better way of figuring what OS it is
running on (thanks to [email protected] (Jim Meyering) for
suggesting this, as well as discovering the hard way that the old
way (testing for /mnt) fails on his machine).

Some new tests were added.
```

This means that **tests in Make were introduced as early as of 1992!** which is a very good sign given some other tools are likely to not have a good coverage even in present days as described in another article of this series: [System Under Test: FreeBSD](https://lowlevelbits.org/system-under-test-freebsd) (see Conclusion there).

#### The test suite requires Perl and can be run on UNIX, Windows and DOS systems

```
To run the test suite on a UNIX system, use "perl ./run_make_tests"
(or just "./run_make_tests" if you have a perl on your PATH).

To run the test suite on Windows NT or DOS systems, use
"perl.exe ./run_make-tests.pl".
```

#### The test suite is run against Make executable

```
By default, the test engine picks up the first executable called "make"
that it finds in your path.  You may use the -make_path option (i.e.,
"perl run_make_tests -make_path /usr/local/src/make-3.78/make") if
you want to run a particular copy.  This now works correctly with
relative paths and when make is called something other than "make" (like
"gmake").
```

This observation leads us to conclusion that these **GNU Make’s tests are actually integration tests** - it is the final `make` executable that is tested, not its parts like they would be with unit testing (depending on terminology this kind of testing of a final product can also be called functional or acceptance testing).

#### Build artefacts

```
A directory named "work" will be created when the tests are run which
will contain any makefiles and "diff" files of tests that fail so that
you may look at them afterward to see the output of make and the
expected result.
```

### Running tests against default OSX Make

Having read both documents: `tests/NEWS` and `tests/README` let’s try to run the tests. As we learned earlier, by default the test suite will pick up first `make` from path so it will default to default make of OSX system which is on my machine:

```
make -v
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-apple-darwin11.3.0
```

If you ever wondered why default `make` on OS X is so old, you are in good company - see [What is the reason for some of the Linux tools on OS X being so old? Is this related to GPL licensing?](https://www.quora.com/What-is-the-reason-for-some-of-the-Linux-tools-on-OS-X-being-so-old-Is-this-related-to-GPL-licensing).

To run tests:

```
$ cd tests/
$ # The following has to be done otherwise script will complain with:
$ # "Can't locate config-flags.pm in @INC..."
$ cp config-flags.pm.in config-flags.pm
$ ./run_make_tests
...
output with lots of errors and finally:
212 Tests in 66 Categories Failed (See .diff* files in work dir for details) :-(
```

We see here that oldness of default Make on OS X does cost 212 failing tests. I assume that the reason why most of these failing tests are failing is not a regression in core functionality of Make but rather because of new features were added to GNU Make since 2006.

To understand how that is different for latest Make let’s build it from source and run tests against it.

### Running tests against latest Make built from source

Let’s get back from `tests` directory one level up to the root directory of source tree. Inspired by the instructions in INSTALL and after some additional googling we need to run `autoreconf` so that it creates proper `configure` script for us:

```
$ pwd # /Users/Stanislaw/Projects/GNUMake
$ brew install automake
$ # gettext is needed by autoreconf to locate gettext,
$ # be careful with force linking it on your system.
$ brew install gettext
$ brew link gettext --force
$ autoreconf # creates 'configure' script
```

Then we want to run this newly created script with `--prefix` parameter so that it will not install make to the `/usr/local/bin` directory but rather to `./Build` directory (to not conflict with OSX’s Make which we don’t want within the scope of this post).

```
$ ./configure --prefix=$(pwd)/Build
```

At this point if you run `make` the very first time you will likely see errors about some localization files missing:

```
Making all in doc
Updating ./version.texi
make[2]: *** No rule to make target `fdl.texi', needed by `make.info'.  Stop.
make[1]: *** [all-recursive] Error 1
make: *** [all] Error 2
```

To fix that you have to first run (solution found at [GNU Make forums](http://gnu-make.2324884.n4.nabble.com/NLS-related-failure-when-building-make-from-CVS-tp2157p2158.html)):

```
make update
```

Everything should work fine since then, finally we run:

```
$ make && make install
...
  /usr/bin/install -c make '/Users/Stanislaw/Projects/Make/GNUMake/Build/bin'
...
$ ./Build/bin/make --version
GNU Make 4.2
Built for x86_64-apple-darwin15.3.0
Copyright (C) 1988-2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later 
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

Which is 2006’s Make 3.81 that has just been used to build 2016’s Make 4.2!

Let’s run the tests!

```
$ cd tests
$ ./run_make_tests -make ../Build/bin/make
```

The results are quite pleasant to look at - **GNU Make built from latest source code on Mac OS X machine, passes all of its tests**:

```
581 Tests in 118 Categories Complete ... No Failures :-)
```

### Test case template

The file `tests/scripts/test_template` is a generic template, most of the tests are based on it:

```
#                                                                    -*-perl-*-

$description = "<FILL IN SHORT DESCRIPTION HERE>";
$details = "<FILL IN DETAILS OF HOW YOU TEST WHAT YOU SAY YOU ARE TESTING>";

# Run a make test.  See the documentation of run_make_test() in
# run_make_tests.pl, but briefly the first argument is a string with the
# contents of a makefile to be tested, the second is a string containing the
# arguments to be passed to the make invocation, the third is a string
# containing the expected output.  The fourth is the expected exit code for
# make.  If not specified, it's assumed that the make program should succeed
# (exit with 0).

run_make_test('Your test makefile goes here',
              'Arguments to pass to make go here',
              'Expected output from the invocation goes here');

# There are various special tokens, options, etc.  See the full documentation
# in run_make_tests.pl.

# This tells the test driver that the perl test script executed properly.
1;
```

Other tests follow a bit different approach: they use `run_make_with_options`/`compare_output` pair of functions to verify the expected output that Make produces. My assumption is that this alternative way is the old way of writing tests - we can clearly see that it is the easier and cleaner way to write tests using the test template from above. Below I have collected 3 examples which use both approaches based on either:

- `run_make_test`

or

- `run_make_with_options`/`compare_output`

These functions are located in the file: `tests/run_make_tests.pl` which is a test driver file for the whole test suite (the file is too long so it is not discussed in this post).

#### Test case example #1: Simple functionality of make

The following test is located at `tests/scripts/misc/general1`.

```
#                                                                    -*-perl-*-

$description = "The following test creates a makefile to test the
simple functionality of make.  It mimics the
rebuilding of a product with dependencies.
It also tests the simple definition of VPATH.";

open(MAKEFILE,"> $makefile");

print MAKEFILE <<EOF;
VPATH = $workdir
edit:  main.o kbd.o commands.o display.o \\
       insert.o
\t\@echo cc -o edit main.o kbd.o commands.o display.o \\
                  insert.o
main.o : main.c defs.h
\t\@echo cc -c main.c
kbd.o : kbd.c defs.h command.h
\t\@echo cc -c kbd.c
commands.o : command.c defs.h command.h
\t\@echo cc -c commands.c
display.o : display.c defs.h buffer.h
\t\@echo cc -c display.c
insert.o : insert.c defs.h buffer.h
\t\@echo cc -c insert.c
EOF

close(MAKEFILE);

@files_to_touch = ("$workdir${pathsep}main.c","$workdir${pathsep}defs.h",
               "$workdir${pathsep}kbd.c","$workdir${pathsep}command.h",
               "$workdir${pathsep}commands.c","$workdir${pathsep}display.c",
               "$workdir${pathsep}buffer.h","$workdir${pathsep}insert.c",
	       "$workdir${pathsep}command.c");

&touch(@files_to_touch);

&run_make_with_options($makefile,"",&get_logfile);

# Create the answer to what should be produced by this Makefile
$answer = "cc -c main.c\ncc -c kbd.c\ncc -c commands.c\ncc -c display.c
cc -c insert.c\ncc -o edit main.o kbd.o commands.o display.o insert.o\n";

# COMPARE RESULTS

if (&compare_output($answer,&get_logfile(1))) {
  unlink @files_to_touch;
}

1;
```

#### Test case example #2: PHONY targets

The following test is located at `tests/scripts/targets/PHONY`.

```
#                                                                    -*-perl-*-

$description = "The following tests the use of a PHONY target.  It makes\n"
              ."sure that the rules under a target get executed even if\n"
              ."a filename of the same name of the target exists in the\n"
              ."directory.\n";

$details = "This makefile in this test declares the target clean to be a \n"
          ."PHONY target.  We then create a file named \"clean\" in the \n"
          ."directory.  Although this file exists, the rule under the target\n"
          ."clean should still execute because of it's phony status.";

$example = "EXAMPLE_FILE";

open(MAKEFILE,"> $makefile");

# The Contents of the MAKEFILE ...

print MAKEFILE ".PHONY : clean \n";
print MAKEFILE "all: \n";
print MAKEFILE "\t\@echo This makefile did not clean the dir ... good\n";
print MAKEFILE "clean: \n";
print MAKEFILE "\t$delete_command $example clean\n";

# END of Contents of MAKEFILE

close(MAKEFILE);

&touch($example);

# Create a file named "clean".  This is the same name as the target clean
# and tricks the target into thinking that it is up to date.  (Unless you
# use the .PHONY target.
&touch("clean");

$answer = "$delete_command $example clean\n";
&run_make_with_options($makefile,"clean",&get_logfile);

if (-f $example) {
  $test_passed = 0;
}

&compare_output($answer,&get_logfile(1));

1;
```

#### Test case example #3: –warn-undefined-variables option

The following test is located at `tests/scripts/options/warn-undefined-variables`.

```
#                                                                    -*-perl-*-

$description = "Test the --warn-undefined-variables option.";

$details = "Verify that warnings are printed for referencing undefined variables.";

# Without --warn-undefined-variables, nothing should happen
run_make_test('
EMPTY =
EREF = $(EMPTY)
UREF = $(UNDEFINED)

SEREF := $(EREF)
SUREF := $(UREF)

all: ; @echo ref $(EREF) $(UREF)',
              '', 'ref');

# With --warn-undefined-variables, it should warn me
run_make_test(undef, '--warn-undefined-variables',
              "#MAKEFILE#:7: warning: undefined variable 'UNDEFINED'
#MAKEFILE#:9: warning: undefined variable 'UNDEFINED'
ref");

1;
```

### Open issues

The file `tests/README` contains interesting section that one may read as high-level TODO list for the project (bold below is mine). It seems that there is some interesting stuff waiting for someone to contribute ;)

> ## Open Issues

> The test suite has a number of problems which should be addressed. **One VERY serious one is that there is no real documentation**. You just have to see the existing tests. Use the newer tests: many of the tests haven’t been updated to use the latest/greatest test methods. See the ChangeLog in the tests directory for pointers.

> **The second serious problem is that it’s not parallelizable**: it scribbles all over its installation directory and so can only test one make at a time. **The third serious problem is that it’s not relocatable**: the only way it works when you build out of the source tree is to create symlinks, which doesn’t work on every system and is bogus to boot. **The fourth serious problem is that it doesn’t create its own sandbox when running tests**, so that if a test forgets to clean up after itself that can impact future tests.

### Conclusion

1. GNU Make has 581 tests: solid test suite introduced as early as of 1992.
2. All of these tests are integration tests: the final executable `make` is tested, not the parts of C code.
3. Default GNU Make 3.81 on OSX machine is 10 years old, it fails 212 tests compared to the latest GNU Make 4.2 build from source which passes all of its tests green.
4. There is always space for contribution: more documentation is needed, tests should have better sandboxing to achieve parallelism and removability.

So far we have Rust and Javascript programming languages, NeoVim editor and XTerm terminal emulator in our plans. Let us know what projects or tools you would like to see covered in this series: [System Under Test](https://lowlevelbits.org/system-under-test/).
