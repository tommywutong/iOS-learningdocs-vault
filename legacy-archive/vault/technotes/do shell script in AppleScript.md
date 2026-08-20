---
title: do shell script in AppleScript
apple_id: DTS10003093
resource_type: Technical Note
platform: macOS
topic: Interapplication Communication
technology: null
published: '2018-05-11'
source_url: https://developer.apple.com/library/archive/technotes/tn2065/_index.html
archived_at: '2026-07-26T19:53:49.923017Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2065

# do shell script in AppleScript

This Technote answers frequently asked questions about AppleScript’s do shell script command.

This technical note addresses common questions about how to use `do shell script`. It does not attempt to explain what you can do with a Unix shell script or how to write one; for that, find an appropriate text or consult a local expert. It is structured as question-and-answer, so you can either skip right to your problem, or read through from beginning to end.

Some answers refer to specific commands in the form `echo`(1) or to a “man page”; these are reference documents included in macOS. (The “man” is short for "manual.”) To see the man page for a command, search for the command in Terminal’s Help menu, or open a Terminal window and type `man` followed by the command name, for example, `man echo`.

[Issuing Commands](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4yq)[How do I pass an AppleScript variable to my shell command?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2scpk5puit27jfpvaqktknpucts7ififatcfknbveskqkrpvmqksjfauetcfl5ke6x2nlfpvgscfjrgf6q2pjvguctsel4)[My command works fine in Terminal, but when I try to use it in do shell script, I get an error about “command not found.” What’s going on?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2tkzl5bu6tknifheix2xj5jewu27izeu4rk7jfhf6vcfkjgustsbjrpv6qsvkrpvoscfjzpusx2ukjmv6vcpl5kvgrk7jfkf6skol5ce6x2tjbcuytc7knbveskqkrpv6sk7i5cvix2bjzpukussj5jf6qkcj5kvix27l5pugt2njvau4rc7jzhvix2gj5ku4rc7l5pv6x27k5eecvc7l5pvgx2hj5eu4r27j5hf6)[Why doesn’t do shell script work exactly like Terminal?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2v2ilfpuit2fknhf6x27krpuit27kneektcml5jugusjkbkf6v2pkjfv6rkyifbvitczl5gess2fl5kekusnjfhectc7)[How do I run my command with a shell other than sh?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2scpk5puit27jfpvevkol5gvsx2dj5gu2qkoirpvoskujbpucx2tjbcuytc7j5keqrksl5keqqkol5juqxy)[Does changing the environment in one do shell script affect the environment of other ones?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2rcpivjv6q2iifheoskoi5pviscfl5cu4vsjkjhu4tkfjzkf6skol5hu4rk7irhv6u2iivgeyx2tinjesucul5aumrsfinkf6vciivpuktswjfje6tsnivhfix2pizpu6vciivjf6t2oivjv6)[How long can my command be?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2scpk5puyt2oi5pugqkol5gvsx2dj5gu2qkoirpuerk7)[How do I get administrator privileges for a command?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2scpk5puit27jfpuorkul5auitkjjzevgvcsifke6us7kbjesvsjjrcuorktl5de6us7ifpugt2njvau4rc7)[How do I get administrator privileges without prompting?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4ys2scpk5puit27jfpuorkul5auitkjjzevgvcsifke6us7kbjesvsjjrcuorktl5lusvcij5kvix2qkjhu2ucujfheoxy)[Getting an Answer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4za)[How does do shell script get the result? How do I return a shell variable to my AppleScript?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zc2scpk5puit2fknpuit27kneektcml5jugusjkbkf6r2fkrpviscfl5jeku2vjrkf6x27jbhvox2ej5pusx2sivkfkusol5av6u2iivgeyx2wifjesqkcjrcv6vcpl5gvsx2bkbieyrktinjesucul4)[How does do shell script report errors?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zc2scpk5puit2fknpuit27kneektcml5jugusjkbkf6usfkbhvevc7ivjfet2sknpq)[When I run my command in Terminal, I get a bunch of output, but when using do shell script, some of it is missing.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zc2v2iivhf6sk7kjku4x2nlfpugt2njvau4rc7jfhf6vcfkjgustsbjrpv6sk7i5cvix2bl5bfktsdjbpu6rs7j5kviucvkrpv6qsvkrpvoscfjzpvku2jjzdv6rcpl5juqrkmjrpvgq2sjfifix27knhu2rk7j5df6skul5evgx2njfjvgskoi5pq)[How much output can a command return?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zc2scpk5pu2vkdjbpu6vkukbkvix2difhf6qk7inhu2tkbjzcf6usfkrkvets7)[Dealing with Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zq)[My command doesn’t work right when a parameter has spaces or certain punctuation — parentheses, $, \*, etc.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zs2tkzl5bu6tknifheix2ej5cvgts7l5pvix2xj5jewx2sjfduqvc7k5eekts7ifpvaqksifgukvcfkjpuqqktl5jvaqkdivjv6t2sl5bukusuifeu4x2qkvhegvcvifkest2ol5pv6x27kbaverkokreeku2fknpv6x27l5pv6x2fkrbv6)[I need to put double quotes and backslashes in my shell command, but AppleScript gives me a syntax error when I try.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zs2sk7jzcukrc7krhv6ucvkrpuit2vijgekx2rkvhvirktl5au4rc7ijaugs2tjravgscfknpusts7jvmv6u2iivgeyx2dj5gu2qkoirpv6qsvkrpucucqjrcvgq2sjfifix2hjfleku27jvcv6qk7knmu4vcblbpukussj5jf6v2iivhf6sk7krjfsxy)[Whenever my shell script returns a double quote or backslash, it comes out with an extra backslash in front of it.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zs2v2iivhekvsfkjpu2wk7kneektcml5jugusjkbkf6usfkrkvetstl5av6rcpkvbeyrk7kfku6vcfl5hvex2cifbuwu2mifjuqx27jfkf6q2pjvcvgx2pkvkf6v2jkref6qkol5cvqvcsifpueqkdjnjuyqktjbpusts7izje6tsul5humx2jkrpq)[What does do shell script do with non-ASCII text (accented characters, Japanese, etc.)?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zs2v2iifkf6rcpivjv6rcpl5juqrkmjrpvgq2sjfifix2ej5pvoskujbpu4t2ol5avgq2jjfpvirkykrpv6qkdincu4vcfirpugscbkjaugvcfkjjv6x2kifiectsfkncv6x2fkrbv6x27)[What are the rules for line endings?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zs2v2iifkf6qksivpviscfl5jfktcfknpumt2sl5gestsfl5cu4rcjjzdvgxy)[Dealing with Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42a)[I have an AppleScript file or alias object; how do I pass it to a shell command?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42c2sk7jbavmrk7ifhf6qkqkbgeku2dkjevavc7izeuyrk7j5jf6qkmjfavgx2pijfekq2ul5puqt2xl5ce6x2jl5iecu2tl5evix2uj5pucx2tjbcuytc7inhu2tkbjzcf6)[POSIX path doesn’t work right if the file has certain characters in its name — spaces, parentheses, $, \*, etc.](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42c2ucpknevqx2qifkeqx2ej5cvgts7l5pvix2xj5jewx2sjfduqvc7jfdf6vciivpumskmivpuqqktl5bukusuifeu4x2djbaveqkdkrcveu27jfhf6skuknpu4qknivpv6x27l5jvaqkdivjv6x2qifjektsujbcvgrktl5pv6x27l5pv6rkuinpq)[Why doesn’t POSIX path just quote everything for me?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42c2v2ilfpuit2fknhf6x27krpvat2tjfmf6ucbkref6ssvknkf6ukvj5kekx2fkzcvewkujbeu4r27izhvex2nivpq)[Other Concerns](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42q)[How do I control an interactive tool like ftp or telnet with do shell script?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42s2scpk5puit27jfpugt2okrje6tc7ifhf6skokrcveqkdkrevmrk7krhu6tc7jreuwrk7izkfax2pkjpvirkmjzcvix2xjfkeqx2ej5pvgscfjrgf6u2dkjevavc7)[My script will produce output over a long time. How do I read the results as they come in?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42s2tkzl5jugusjkbkf6v2jjrgf6ucsj5cfkq2fl5hvkvcqkvkf6t2wivjf6qk7jrhu4r27kreu2rk7l5ee6v27irhv6sk7kjcucrc7kreekx2sivjvktcuknpucu27kreekwk7inhu2rk7jfhf6)[I want to start a background server process; how do I make do shell script not wait until the command completes?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42s2sk7k5au4vc7krhv6u2uifjfix2bl5becq2li5je6vkoirpvgrkskzcvex2qkjhugrktknpv6scpk5puit27jfpu2qklivpuit27kneektcml5jugusjkbkf6tspkrpvoqkjkrpvktsujfgf6vciivpugt2njvau4rc7inhu2ucmivkeku27)[I have started a background process; how do I get its process ID so I can control it with other shell commands?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42s2sk7jbavmrk7knkecusuivcf6qk7ijaugs2hkjhvktsel5ifet2divjvgx27jbhvox2ej5pusx2hivkf6skuknpvauspincvgu27jfcf6u2pl5ev6q2bjzpugt2okrje6tc7jfkf6v2jkref6t2ujbcvex2tjbcuytc7inhu2tkbjzcfgxy)[I’m trying to use top, but it fails saying “can’t get terminal attributes” or “error opening terminal: unknown.”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42s2sk7l5pu2x2ukjmustshl5ke6x2vkncv6vcpkbpv6qsvkrpusvc7izaustctl5jucwkjjzdv6x27l5bucts7l5pvix2hivkf6vcfkjgustsbjrpucvcukjeuevkuivjv6x27l5hvex27l5pukussj5jf6t2qivhestshl5kekusnjfhectc7l5ku4s2oj5lu4x27l5pq)[What’s the default working directory for do shell script commands?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42s2v2iifkf6x27knpviscfl5cekrsbkvgfix2xj5jewskoi5puisksivbvit2slfpumt2sl5ce6x2tjbcuytc7knbveskqkrpugt2njvau4rctl4)[Does it make a difference which application I tell to do shell script?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42s2rcpivjv6skul5gucs2fl5av6rcjizdekusfjzbukx2xjbeugsc7ififatcjinaviskpjzpusx2uivgeyx2uj5puit27kneektcml5jugusjkbkf6)[Gory Details](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi43a)[What shell does do shell script use, really?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi43c2v2iifkf6u2iivgeyx2ej5cvgx2ej5pvgscfjrgf6u2dkjevavc7kvjukx27kjcuctcmlfpq)[How long can my command be, really?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi43c2scpk5puyt2oi5pugqkol5gvsx2dj5gu2qkoirpuerk7l5jekqkmjrmv6)[Where does the shell environment come from — environment variables, working directory, and so on?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi43c2v2iivjekx2ej5cvgx2ujbcv6u2iivgeyx2fjzlesuspjzguktsul5bu6tkfl5dfet2nl5pv6x27ivhfmsksj5he2rkokrpvmqksjfauetcfknpv6v2pkjfustshl5cesusfinke6uszl5puctsel5ju6x2pjzpq)[Historical Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi43q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Issuing Commands

### How do I pass an AppleScript variable to my shell command?

Since the command argument to `do shell script` is really just a string, you can build the string at run time using the AppleScript concatenation operator `&`. For example, to pass the variable as a command parameter, you would do this:

```
set hostname to "www.apple.com"
do shell script "ping -c1 " & hostname
```

Some commands require data to be fed to standard input. `do shell script` does not directly support this, but you can fake it using `echo` and a pipe:

```
set input to "hello"
do shell script "echo " & input & " | tr a-z A-Z"
-- "HELLO"
```

In general, you should quote any variables using `quoted form of`; see [Dealing with Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zq) for details.

### My command works fine in Terminal, but when I try to use it in do shell script, I get an error about “command not found.” What’s going on?

There are two possibilities. First, `do shell script` always uses /bin/sh to interpret your command, not your default shell, which Terminal uses. (To find out what your default shell is, say `echo $SHELL` in Terminal.) While some commands are the same between shells, others are not, and you may have used one of them. If you write your `do shell script` scripts in Terminal first, always use sh. You can start sh by typing `/bin/sh`; type `exit` to get back to your normal shell.

Second, when you use just a command name instead of a complete path, the shell uses a list of directories (known as your PATH) to try and find the complete path to the command. For security and portability reasons, `do shell script` ignores the configuration files that an interactive shell would read, so you don’t get the customizations you would have in Terminal. Use the full path to the command, for example, `/sbin/ifconfig` instead of just `ifconfig`. To find the full path in Terminal, say `which command-name`, for example, `which ifconfig`; to see the list of places `do shell script` will search, say `do shell script "echo $PATH"`.

(This answer glosses over a few details — see [Gory Details](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi43a) if you care.)

### Why doesn’t do shell script work exactly like Terminal?

For two reasons: first, it helps guarantee that scripts will run on different systems without modification. If `do shell script` used your default shell or PATH, your script would probably break if you gave it to someone else. Second, it matches shell escape mechanisms in other languages, such as Perl.

### How do I run my command with a shell other than sh?

Include the shell you want to use explicitly in the command. There are a variety of ways to pass commands to your shell of choice. You could write the command to a file and then execute the file like this:

```
do shell script "/bin/tcsh my-command-file-path"
```

Some shells will accept a script as a parameter, like this:

```
do shell script "/bin/tcsh -c 'my-command'"
```

And most will accept a script from standard input, like this:

```
do shell script "echo my-command | /bin/tcsh"
```

When in doubt, read the documentation for your preferred shell. When you put the command in the `do shell script` string, you will probably have to quote the command as described below, or the shell will interpret special characters in the command.

### Does changing the environment in one do shell script affect the environment of other ones?

No. Each invocation of `do shell script` uses a new shell process, so state such as changes to variables and the working directory is not saved from one to the next. For example, the `pwd` here is not affected by the `cd` in the previous command:

```
do shell script "cd ~/Documents"
do shell script "pwd"
-- result: "/"
```

To share state between shell scripts, combine the scripts into one, separating the commands with either semicolons or linefeeds, like this:

```
do shell script "cd ~/Documents ; pwd"
-- result: "/Users/me/Documents"
```

### How long can my command be?

There is no precise answer to this question. (See [Gory Details](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi43a) for the reasons why.) However, the approximate answer is that a single command can be up to about 262,000 characters long — technically, 262,000 bytes, assuming one byte per character. Non-ASCII characters will use at least two bytes per character — see [Dealing with Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zq) for more details.

__Note:__ This limit is subject to change. The shell command `sysctl kern.argmax` will give you the current limit in bytes.

Overrunning the limit will cause `do shell script` to return an error of type 255. Most people who hit the limit are trying to feed inline data to their command. Consider writing the data to a file and reading it from there instead.

### How do I get administrator privileges for a command?

Use the `administrator privileges` parameter like this:

```
do shell script "command" with administrator privileges
```

This runs the command as the root user, giving it additional privileges. Once a script is correctly authenticated, it will not ask for authentication again for five minutes. The authentication only applies to that specific script: a different script, or a modified version of the same one, will ask for its own authentication.

Bear in mind that administrator privileges allow you to make potentially catastrophic changes, so exercise caution. Better yet, don’t use administrator privileges unless you absolutely have to. Unless you are doing system-level development, you should never need to change anything in /System — changing /Library should suffice.

__Note:__ Using `sudo`(8) with `with administrator privileges` is generally unnecessary and creates security holes; simply remove the `sudo`.

### How do I get administrator privileges without prompting?

There are two ways to effectively pre-supply the administrator password for a particular machine. One is to supply an explicit user and password to `do shell script` like this:

```
do shell script "command" user name "me" password "mypassword" with administrator privileges
```

However, doing this means putting the plaintext password in your script, which is a security risk. The other way is to modify the sudo security policy to allow the relevant command without a password: you can then say `do shell script "sudo command"` (without `with administrator privileges`) and the command will run without prompting. See `sudoers`(5) for details.

[Back to Top](#)

## Getting an Answer

### How does do shell script get the result? How do I return a shell variable to my AppleScript?

Shell commands can write their results to one of two output streams: standard output and standard error. Standard output is for normal output, while standard error is for error messages and diagnostics. Assuming your script completes successfully — if it doesn’t, see the next question — the result is whatever text was printed to standard output, possibly with some modifications. Most commands print their results to standard output automatically, so you don’t need to do anything extra. If your answer is in a variable, you will need to print it yourself using `echo` (most shells) or `print` (many languages, such as Perl and Awk). For example:

__Listing 1__  Set the AppleScript variable mySlug to a date slug in yyyy-mm-dd format.

```
set mySlug to do shell script "date +%Y-%m-%d"
-- see date(1) for details on the format string.
```

__Listing 2__  The same thing, but as a Perl script.

```
set mySlug to do shell script ¬
    "perl -e 'my (undef, undef, undef, $d, $m, $y) = localtime;
              my $date = sprintf("%4d-%02d-%02d", $y+1900, $m+1, $d);
              print $date'"
```

By default, `do shell script` transforms all the line endings in the result to classic Mac OS-style carriage returns ("\r" or ASCII character 13), and removes a single trailing line ending, if one exists. This means, for example, that the result of `do shell script "echo foo; echo bar"` is `"foo\rbar"`, not the `"foo\nbar\n"` that echo actually returned. You can suppress both of these behaviors by adding the `without altering line endings` parameter. For dealing with non-ASCII data, see [Dealing with Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4zq).

### How does do shell script report errors?

All shell commands return an integer status when they finish: zero means success; anything else means failure. If the script exits with a non-zero status, `do shell script` throws an AppleScript error with the status as the error number. (The man page for a command should tell you what status codes it can return. Most commands simply use 1 for all errors.) If the script printed something to the standard error stream, that text becomes the error message in AppleScript. If there was no error text, the normal output (if any) is used as the error message.

### When I run my command in Terminal, I get a bunch of output, but when using do shell script, some of it is missing.

When running in Terminal, standard output and standard error are both sent to the same place, so it is difficult to tell them apart. `do shell script`, on the other hand, keeps the two streams separate. If you want to combine them, follow the command with `2>&1` like this:

```
do shell script "command 2>&1"
```

See the `sh` man page under "Redirection" for more details.

### How much output can a command return?

A single command can return up to 2 GiB of data on a 32-bit system, or up to 4 TiB on a 64-bit system.

[Back to Top](#)

## Dealing with Text

### My command doesn’t work right when a parameter has spaces or certain punctuation — parentheses, $, \*, etc.

Because the shell separates parameters with spaces, and some punctuation marks have special meanings, you must take special steps to make the shell treat your string as one parameter with literal spaces, parentheses, etc. This is called "quoting," and there are several ways to do it, but the simplest and most effective is to use the `quoted form` property of strings.

For example, consider this (buggy) handler, which takes a string and appends it to a file named "stuff" in your home directory:

```
to append_message(s)
    do shell script "echo " & s & " >> ~/stuff"
end append_message
```

It works fine for most strings, but if we call it with a string like "$100", the string that ends up in the file is "00", because the shell thinks that "$1" is a variable whose value is an empty string. (Variables in `sh` begin with a dollar sign.) To fix the script, change it like this:

```
do shell script "echo " & quoted form of s & " >> ~/stuff"
```

The `quoted form` property gives the string in a form that is safe from further interpretation by the shell, no matter what its contents are. For more details on quoting, see the `sh` man page under “Quoting.”

### I need to put double quotes and backslashes in my shell command, but AppleScript gives me a syntax error when I try.

Strings in AppleScript go from an opening double quote to a closing double quote. To put a literal double quote in your string you must "escape" it with a backslash character, like this:

```
"a \"quote\" mark"
```

The backslash means "treat the next character specially." This means that getting a literal backslash requires two backslashes, like this:

```
"a back\\slash"
```

Putting this all together, you might have something like this:

```
set s to "this is a test."
do shell script "echo " & quoted form of s & " | perl -n -e 'print \"\\U$_\"'"
-- result: "THIS IS A TEST."
```

Despite all the extra backslashes in the script, the actual string passed to perl’s -e option is

```
print "\U$_"
```

### Whenever my shell script returns a double quote or backslash, it comes out with an extra backslash in front of it.

The result window in Script Editor shows you the result in “source” form, such that you could paste it into a script and compile it. This means that string results have quotes around them, and special characters such as double quotes and backslashes are escaped as described above. The extra backslash is not really part of the string, it’s merely how it’s displayed. If you pass the string to `display dialog` or write it to a file, you will see it without the extra backslashes.

### What does do shell script do with non-ASCII text (accented characters, Japanese, etc.)?

From AppleScript’s point of view, `do shell script` accepts and produces Unicode text. `do shell script` passes the commands to the shell and interprets their output using UTF-8. If a command produces bytes that are not valid UTF-8, `do shell script` will interpret them using the primary system encoding.

Realize that most shell commands are completely ignorant of Unicode and UTF-8. UTF-8 looks like ASCII for ASCII characters — for example, `A` is the byte 0x41 in both ASCII and UTF-8 — but any non-ASCII character is represented as a sequence of bytes. As far as the shell commands are concerned, however, one byte equals one character, and they make no attempt to interpret anything outside the ASCII range. This means that they will preserve UTF-8 sequences and can do exact byte-for-byte matches: for example, `echo ™` will produce a trademark symbol, and `grep ©` will find every line with a copyright symbol. However, they cannot intelligently sort, alter, or compare UTF-8 sequences: for example, character-set matching commands like `tr`(1) or the [] construct in `sed`(1) will attempt to match each byte of the sequence independently, `sort`(1) will sort accented characters out of order, and `grep -i` or `find -iname` will not match “é” against “É”. Perl is a notable exception to this; see `perlunicode`(1) for more details.

### What are the rules for line endings?

In general, macOS uses the Unix-style line ending of linefeed (“\n” or `character id 10`), which matches what Unix-based shell commands expect. However, older applications and files may use the classic Mac OS-style line ending of return (“\r” or `character id 13`), which shell commands may interpret in less-than-useful ways. For example, `grep`(1) would consider the entire input to have only one line, so you would get at most one match.

If your classic Mac OS-style data is coming from AppleScript, you can transform the line endings there or generate line feeds in the first place — `"\n"`, `linefeed`, or `character id 10` all yield a line feed. If the data is coming from a file, you can make the shell script transform the line endings by using `tr`(1). For example, the following will find lines that contain “something” in any plain text file, regardless of line-ending style. (The “quoted form of POSIX path of f” idiom is discussed under [Dealing with Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi42a).)

```
set f to choose file
do shell script "tr '\r' '\n' < " & quoted form of POSIX path of f & " | grep something"
```

AppleScript itself is line ending-agnostic — the `paragraph` element of string objects considers classic Mac OS- and Unix-style line endings to be equivalent, along with Windows-style (“\r\n”) and the Unicode paragraph separator and line separator characters. There is generally no need to use `text item delimiters` to get lines of text; `paragraph n` or `every paragraph` will work just as well. (However, if you wanted to consider only a particular line ending style, `text item delimiters` would be the proper solution.)

[Back to Top](#)

## Dealing with Files

### I have an AppleScript file or alias object; how do I pass it to a shell command?

The shell specifies files using POSIX path names, which are strings with slashes separating the path components (for example, `/folder1/folder2/file`). To get the POSIX path of an AppleScript file or alias object, use the `POSIX path` property. (However, see the following question.) For example:

```
POSIX path of file "HD:Users:me:Documents:Welcome.txt"
-- result: "/Users/me/Documents/Welcome.txt"
```

To go the other way — say your shell command returns a POSIX path as a result — use the `POSIX file` class. `POSIX file` with a path name evaluates to a normal file object that you can then pass to other AppleScript commands. For example:

```
set p to do shell script "echo ~"
POSIX file p
-- result: file "HD:Users:me:"
```

### POSIX path doesn’t work right if the file has certain characters in its name — spaces, parentheses, $, \*, etc.

This is a special case of quoting: you must quote the path to make the shell interpret all the punctuation literally. To do this, use the quoted form of the path. For example, this will work with any file, no matter what its name is:

```
choose file
do shell script "ls -l " & quoted form of the POSIX path of the result
-- result: "-rw-r--r-- 1 me unknown 1 Oct 25 17:48 Look! a file!"
```

### Why doesn’t POSIX path just quote everything for me?

For two reasons: first, there are uses for POSIX paths that have nothing to do with shell parameters, and quoting the path would be wrong in such cases. Second, quoted form is useful for things other than file paths. Therefore, there are two orthogonal operations instead of one combined one.

[Back to Top](#)

## Other Concerns

### How do I control an interactive tool like ftp or telnet with do shell script?

The short answer is that you don’t. `do shell script` is designed to start the command and then let it run with no interaction until it completes, much like the backquote operator in Perl and most Unix shells.

However, there are ways around this. You can script Terminal and send a series of commands to the same window, or you could use a Unix package designed for scripting interactive tools, such as [expect](http://expect.nist.gov/). Also, many interactive commands have non-interactive equivalents. For example, `curl` can substitute for `ftp` in most cases.

### My script will produce output over a long time. How do I read the results as they come in?

Again, the short answer is that you don’t — `do shell script` will not return until the command is done. In Unix terms, it cannot be used to create a pipe. What you can do, however, is to put the command into the background (see the next question), send its output to a file, and then read the file as it fills up.

### I want to start a background server process; how do I make do shell script not wait until the command completes?

Use `do shell script "command &> file_path &"`. `do shell script` will return immediately with no result and your AppleScript script will be running in parallel with your shell script. The shell script’s output will go into file_path; if you don’t care about the output, use `/dev/null`. There is no direct support for getting or manipulating the background process from AppleScript, but see the next question.

__Note:__ Saying `&> file_path` is semantically equivalent to `> file_path 2>&1`, and will direct both standard output and standard error to `file_path`. If you need them to go to different places, direct standard output using `>` and standard error using `2>`. For example, to send standard error to a file but ignore standard output, do this:

```
do shell script "command > /dev/null 2> file_path
```

See the `sh`(1) man page under “Redirection” for more details.

### I have started a background process; how do I get its process ID so I can control it with other shell commands?

You can use a feature of `sh` to do this: the special variable `$!` is the ID of the most recent background command, so you can echo it as the last command in your shell script, like this:

```
do shell script "my_command &> /dev/null & echo $!"
-- result: 621
set pid to the result
do shell script "renice +20 -p " & pid
-- change my_command's scheduling priority.
do shell script "kill " & pid
-- my_command is terminated.
```

### I’m trying to use top, but it fails saying “can’t get terminal attributes” or “error opening terminal: unknown.”

`top`(1) in its default mode does all sorts of clever things to create a dynamically updating display, none of which work if the output device does not support cursor control, as `do shell script` does not. However, `top` has an option that makes it run in logging mode, which works with file-like devices like `do shell script`. Use `top -l1` instead, or see the `top`(1) man page for more options.

This same problem will apply to any other command that assumes the presence of a terminal. Fortunately, most of them are interactive front ends to more primitive commands that do not assume a terminal.

### What’s the default working directory for do shell script commands?

`do shell script` inherits the working directory of its parent process. For most applications, such as Script Editor, this is /. For `osascript`(1), it is the working directory of the shell when you launched `osascript`. You should not rely on the default working directory being anything in particular; if you need the working directory to be someplace specific, set it to that yourself.

### Does it make a difference which application I tell to do shell script?

For the most part, no. For security reasons, `do shell script` always runs as a child of the process running the script, regardless of what application is the current “tell” target. However, AppleScript must perform some extra work to redirect `do shell script` commands sent to other applications, so for optimal results always put `do shell script` calls outside of any `tell` block, or use `tell me`.

[Back to Top](#)

## Gory Details

This section is for those who want to know all the niggling details of how `do shell script` works. If you just want to make your script work right, you probably don’t need to read it.

### What shell does do shell script use, really?

`do shell script` always calls /bin/sh. However, in macOS, /bin/sh is really `bash` emulating `sh`.

### How long can my command be, really?

Calling `do shell script` creates a new `sh` process, and is therefore subject to the system’s normal limits on passing data to new processes: the arguments (in this case, the text of your command plus about 40 bytes of overhead) and any environment variables may not be larger than kern.argmax, which is currently 262,144 bytes. Because `do shell script` inherits its parent’s environment (see the next question), the exact amount of space available for command text depends on the calling environment. In practical terms, this comes out to somewhat more than 261,000 bytes, but unusual environment settings might reduce that substantially.

### Where does the shell environment come from — environment variables, working directory, and so on?

`do shell script` inherits the environment of its parent process, which is always the process running the script. The environment covers the working directory, any environment variables, and several other attributes — see `execve`(2) for a complete list. As mentioned in [Issuing Commands](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbzgmwugsbrfvke4vcbi4yq), `do shell script` does not read the configuration files that an interactive shell running in Terminal would.

Any application launched from the Finder gets the same default environment: a working directory of / and the environment variables HOME, LANG, PATH, SHELL, and USER. Most applications do not change their environment, but relying on this is a maintenance risk.

`osascript`(1) inherits its environment from the shell it is run from: the working directory is the working directory of the shell; any environment variables defined in the shell will also be defined in `osascript`, and therefore in `do shell script`. For example:

```shell
$ export VAR=something
$ osascript -e 'do shell script "echo $VAR"'
something
```

[Back to Top](#)

## Historical Notes

The above documents `do shell script` as it behaves on versions of macOS since Mac OS X 10.6 Snow Leopard. Prior to that, some differences applied:

10.1: `do shell script` introduced. Input and output are interpreted using the primary system encoding. `sh` emulation is provided by `zsh`(1). `with administrator privileges` is implemented using `sudo`(8) and has some issues:

- Successful authentication of a script caches the credentials, allowing use of `sudo`(8) anywhere else in the system for a period of time (normally five minutes). Scripts can use `sudo -k` to manually invalidate the cached credentials.
- Scripts with multiple commands will not work correctly with `with administrator privileges`. Scripts can work around this by turning the script into a single invocation of `sh`(1): `do shell script "sh -c " & quoted form of my script`

10.1 update (AppleScript 1.8.3): Input and output are now interpreted using UTF-8, and only UTF-8. Output that is not valid UTF-8 will produce the error “can’t make some data into the expected type.” Workarounds include writing the output to a file and then reading it using AppleScript’s `read` command or piping through `vis`(1).

10.2: `sh` emulation is now provided by `bash`(1).

10.4: Output that is not valid UTF-8 will be interpreted using the primary encoding. Telling another application to `do shell script with administrator privileges` will result in an error. `with administrator privileges` is re-implemented using the system Authentication framework, fixing the issues described in 10.1. However:

In Mac OS X 10.4.0 and 10.4.1 `with administrator privileges` executes the command with only the effective user id set to root. This causes trouble for some commands that rely on the real user id — for example, Perl will turn on its “taint mode” security checks, and `sudo`(8) will hang. To work around the problem (assuming you cannot simply remove a use of `sudo`), preface your command with a small Perl script to set the real user id, like this:

```
do shell script "/usr/bin/perl -Ue '$< = $>; system(@ARGV)' my_command" with administrator privileges
```

Mac OS X 10.4.2 and later sets both the real and effective user ids; the above workaround is unnecessary, but harmless.

10.6: `do shell script` may no longer be sent to other applications. AppleScript silently redirects commands to other applications back to the process running the script, so existing scripts run without an error.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-05-11 | Move antiquated information to its own section. |
| 2006-03-23 | Document security restriction on telling other applications with administrator privileges. |
| 2005-07-20 | Updated "administrator privileges" question to reflect changes in 10.4.2. |
| 2005-05-06 | Changes for Mac OS X 10.4 (Tiger). |
| 2003-01-27 | New document that frequently Asked Questions about the AppleScript "do shell script" command. |

