---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/ShellScriptSecurity/ShellScriptSecurity.html
archived_at: '2026-07-18T01:39:30.243783Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Command%20Line%20Primer.md)[Previous](Performance%20Tuning.md)

# Shell Script Security

Security is often overlooked when writing shell scripts. Many programmers ignore shell script security under the assumption that anything an attacker can do by attacking a script can be achieved more easily by simply executing the commands themselves. This is not true, however, when the script takes input from an untrusted third party:

- Shell scripts running as CGI scripts on a web server take input from the network.
- Shell scripts that read files and take actions based on their contents may take input from untrusted files.
- Shell scripts that perform web queries (with `curl`, for example) or other network requests may take input from untrusted servers or clients.

Further, most security problems are also correctness bugs even if someone is not trying to attack your code.

This chapter describes a few common mistakes in scripting, shows how these vulnerabilities can be exploited, and explains how to prevent these attacks in your scripts.

This chapter also describes how UNIX permissions and POSIX access control lists (ACLs) affect your scripts and how to manipulate those permissions and ACLs in your scripts.

Environment variable attacks are the most common way to manipulate script behavior. By manipulating the environment of a script, you can change its behavior if the script depends on the values of those environment variables.

Although they are less harmful for scripts these days (because scripts cannot be run setuid in any modern OS), they can still cause incorrect behavior. For setuid binaries, they are even more dangerous. These attacks can also be harmful in a multiuser setting if one user gains the ability to modify the login scripts of another user through a bug or incorrect configuration.

The most common environment attack is modifying the `PATH` environment variable. This variable controls what gets executed when you type a command without giving the full path.

Consider the following code:

```
#!/bin/sh

ls /tmp
```

__The attack:__

Create an executable binary or script that does something harmful and name it “ls”. Then do this:

```
export PATH=/path/to/malicious/binary:$PATH
/path/to/above/script
```

Because the path to the malicious binary is first in the search path, the malicious `ls` command gets executed instead of the real one.

__Mitigation:__

Always specify absolute or relative paths when executing binaries or other scripts. If your script runs other scripts or binaries that do not use absolute or relative paths internally, you should explicitly set the value of the `PATH` environment variable in your scripts to prevent problems.

Files in publicly writable directories, including temporary files, are vulnerable to attack by substituting a malicious file in place of the file your script intended to read or write.

The simplest example of this attack is a tool storing secret information into a temporary file.

Consider the following code:

```
#!/bin/sh

SECRETDATA="My password is 12345."
echo > /tmp/mysecretdata
chmod og-rwx /tmp/mysecretdata
echo "$SECRETDATA" >> /tmp/mysecretdata
```

__The attack:__

Create a tool that watches for the file `/tmp/mysecretdata` to appear. (Although this can be done with a shell script, it probably won’t be fast enough to work very often. Use the File System Events API in C instead.)

Upon detecting the existence of the path, do this:

```
FILE *fp=fopen("/tmp/mysecretdata", "r");
```

If the attacker manages to open the file before the script executes the `chmod` command, it can continue to read data from the file for as long as it keeps the file open.

__Mitigation:__

There are two things you must do to fix this:

- Always use the `umask` command to specify initial permissions on the file when you create it.
- Always create temporary files with the `mktemp` command. This creates a new file with the specified template, ensuring that a file or symbolic link with that name does not already exist.

For example:

```
#!/bin/sh

SECRETDATA="My password is 12345."
umask 0177
FILENAME="$(mktemp /tmp/mytempfile.XXXXXX)"
echo "$SECRETDATA" >> "$FILENAME"
```

However, assuming you actually intend to use the data again in the future, this mitigation is probably not sufficient either, for the reasons described in the next attack.

A similar attack can be performed on files used as inputs to shell scripts.

Consider a script that executes the following code:

```
#!/bin/sh

echo "My password is secret!" > /tmp/mypublicdata

...

PUBLICDATA="$(cat /tmp/mypublicdata)"

echo "$PUBLICDATA" | nc 192.168.1.102 3333
```

This script sends the contents of a temporary file to port 3333 of another computer at IP number 192.168.1.102 using the `nc` utility.

__The attack:__

Create a tool that watches for the file `/tmp/mydata` to appear. (Although this can be done with a shell script, it probably won’t be fast enough to work very often. Use the File System Events API in C instead.)

Upon detecting the existence of the path, do this:

```
unlink("/tmp/mypublicdata");
unlink("/etc/myscretdata", "/tmp/mypublicdata");
```

If the attacker manages to do this before the script reads the file, then your secret password (presumably 12345, from the previous script) is sent unencrypted over port 3333. The attacker can then sniff for traffic on that port, and can log into your account (or at least unlock your luggage).

__Mitigation:__

This is particularly troublesome to mitigate because UNIX tools inherently follow symbolic links. The only way to solve the problem is to avoid writing the actual files into public directories. You should do this as follows:

- Always create temporary _directories_ with the `mktemp` command, then create your actual temporary files _inside_ those directories. By doing this, you can set restrictive permissions on the directory that will prevent an attacker from deleting your files and replacing them.

  If you specify the `-d` flag, the `mktemp` command creates a new directory with the specified template, ensuring that a file or directory with that name does not already exist.
- Always use the `umask` command to specify initial permissions on files and directories when you create them.

For example:

```
#!/bin/sh

umask 0177
TMPDIR="$(mktemp -d /tmp/mytempfile.XXXXXX)"
echo "My password is secret!" > "$TMPDIR"/mypublicdata

...

PUBLICDATA="$(cat "$TMPDIR"/mypublicdata)"

echo "$PUBLICDATA" | nc 192.168.1.102 3333
```


The most common type of attack in shell scripts is the injection attack. This type of attack occurs when arguments stored in user-provided variables are passed to commands without proper quoting.

Consider the following example:

```
read FOO
read BAR
if [ x$FOO = xfoo ] ; then
    echo $FOO
    eval $BAR
fi
```

This code has two security holes. Can you spot them?

- `if [ x$FOO = xfoo ] ; then`

  This statement allows for an injection attack on `FOO`.

  __The attack:__

  Pass “`foo = xfoo -o x`” as the value for `FOO`.

  Despite the fact that the value of `FOO` is not “foo”, the statement executes anyway. Depending on what this test does, this could potentially cause unexpected behavior.

  __Mitigation:__

  To fix this bug, change the if statement to read:

```
if [ "$FOO" = "foo" ] ; then
```
- `eval $BAR`

  This is a no-no. Never run eval on data passed in by a user unless you have very, very carefully sanitized it (and if possible, use a whitelist to limit the allowed values).

  __The attack:__

  Pass a dangerous command for `BAR`.

  __Mitigation:__

  Just don’t do that.

The following example is more subtle. Instead of running `eval`, it writes data to a script, but does so without protecting the values:

```
#!/bin/sh

read FOO

# ...

echo ls $FOO >> myscript.sh

# ...

chmod a+x myscript.sh
./myscript.sh
```

__The attack:__

Pass the value “`; rm randomfile`” to cause this script to delete a file.

__The Wrong Mitigation:__

You might be tempted to fix this bug by changing the echo and execution lines to read:

```
echo ls "\"$FOO\"" >> myscript.sh
export FOO
```

However, this still does not solve the problem because `FOO` is expanded immediately, which means that if the value of `FOO` contains a quotation mark—for example, “`";rm randomfile ; echo "`”, you now have a different (but equally bad) security hole.

__Correct Mitigation #1:__

One way to fix this bug is to change the echo line to read:

```
echo ls "\"\$FOO\"" >> myscript.sh
```

This causes the variable `FOO` to be expanded when the script is executed. However, this works only if the variable `FOO` is exported, because otherwise the variable `FOO` would expand to nothing in the second script.

__Correct Mitigation #2:__

Another way to fix this bug is to change the echo line to read:

```
QUOTFOO="$(echo "$FOO" | sed "s/'/'\"'\"'/g")"
echo ls "'$QUOTFOO'" >> myscript.sh
```

By using single quotes around the string in the secondary script, the only character relevant to the shell is the single quote character. The `sed` command then replaces any single quote characters in the string with a closing single quote followed by a single quote wrapped in double quotes followed by an opening single quote.

The following example is not dangerous in modern shells, but is dangerous in older Bourne shells:

```
#!/bin/sh

read FOO
echo $FOO
```

__The attack:__

Pass the value “`; rm randomfile`” to cause this script to delete a file in older shells.

Most modern shells parse the statement prior to any variable substitution, and are thus unaffected by this attack. However, for proper security when your script is run on older systems (not to mention avoiding a syntax error if the filename contains spaces), you should still surround the variable with double quotes.

__Mitigation:__

To fix this bug, change the echo line to read:

```
echo "$FOO"
```


In general, you should not rely on a script to determine whether a user does or does not have permission to do something. It is clumsy and error-prone. It is possible to do so, however, and there are right and wrong ways to do it.

The wrong way:

```
if [ $UID = 100 -a $USER = "myusername" ] ; then
    cd $HOME
fi
```

This code has three security bugs, and they’re all caused by using variables in ways that are unsafe. For historical compatibility, the OS provides the `UID`, `USER`, and `HOME` environment variables. They are quite useful as long as you aren’t using them for security reasons.

__The attack:__

```shell
$ tcsh
% setenv UID 100
% setenv USER myusername
% setenv HOME $HOME/.ssh
% /path/to/script.sh
```

Even though most modern Bourne shells protect against modifying `UID`, the `USER` variable is unprotected, and not all shells protect the `UID` variable, either.

Fortunately, the script just changed into a directory. Combined with another exploitable attack such as an injection attack, however, this could be exploited in bad ways.

__Mitigation:__

To obtain the user ID:

```
# Effective UID
MYEUID="$(/usr/bin/id -u)"

# Real UID
MYUID="$(/usr/bin/id -u -r)"
```

To obtain the username:

```
MYUID="$(/usr/bin/id -u -n)"
```

To obtain the actual home directory:

```
HOMEDIR="$(dscl . -read /Users/dg NFSHomeDirectory | sed 's/^NFSHomeDirectory: //')"
```

Note that this method for obtaining the home directory is specific to OS X.

OS X uses the UNIX permissions model, extended by POSIX access control lists. These permissions models are described in detail in the [OS X File System Security](../File%20Management/File%20System%20Programming%20Guide/File%20System%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqobnknlts) section of _[File System Programming Guide](../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_. This section assumes that you are already at least peripherally familiar with the concept of users and groups.

UNIX permissions are visible to users in Terminal and in the Finder’s Get Info window. In Terminal, you can easily look at the permissions in a human-readable format by using the `ls` command as follows:

```
$ ls -ld filename dirname
drwxr-xr-x  2 username  groupname  68 Jun 16 13:40 dirname
-rw-r--r--  1 username  groupname   0 Jun 16 13:40 filename
```

The left character indicates whether the file system object is a file (`-`), directory (`d`), symbolic link (`l`), block (`b`) or character (`c`) special file, named pipe (`p`), or UNIX domain socket (`s`).

The next three characters show the Owner permissions, followed by the Group permissions, and finally, the Other permissions as listed in the following table:

| Permissions flag | Octal Bit Value | Meaning |
| --- | --- | --- |
| - | n/a | No permission |
| r | 4 | Read permission |
| w | 2 | Write permission |
| x | 1 | Execute permission |
| s | In the optional first octal digit:   - 4—setuid - 2—setgid | Setuid or setgid with execute permission |
| S | See above. | Setuid or setgid `without` execute permission |
| t | In optional first octal digit:  1 | Sticky bit |

The complete set of permissions is often expressed in octal, as defined by the bits in the table above. The first digit includes the sticky bit and setuid and setgid bits. If zero, you may omit it when passing the value to most commands. The remaining three digits contain the Owner (user), Group, and Other permissions, respectively.

For example, a file that is setuid and setgid, with read/write/execute Owner permissions and read/execute Group and Other permissions, the octal equivalent is 6755:

- The leading special permissions value is 6, which is the bitwise OR of setuid (4) and setgid (2).
- The Owner permission is 7, which is the bitwise OR of the read (4), write (2), and execute (1) bits.
- The Group and Other permissions are both 5, which is the bitwise OR of the read (4) and execute (1) permissions.

To show the UNIX permissions of a file, use the stat command as follows:

```
stat -f "%p" filename
```

Ignore all but the last four digits returned.

The ability to change file ownership and permissions is limited by the operating system for security and quota reasons. Users can:

- Change the permissions for any file that they own.
- Change the group for any file that they own to any group that they are a member of.

Non-root users cannot:

- Change permissions on files owned by anyone else.
- Change the group of a file to a group that they are not a member of.
- Change the owner of any file.

The root user can change permissions and ownership arbitrarily except when blocked by BSD file system flags.

With those restrictions in mind, the sections that follow describe how to change permissions and change user and group ownership of files and directories.

You can change the owner of a file or directory with the `chown` command:

```
# Change the owner of a file or directory
sudo chown newowner filename_or_dirname

# Change the owner of a directory and everything in it recursively
sudo chown -R newowner dirname
```

You can change the group for a file with either the `chown` command or the `chgrp` command:

```
# Change the group by itself
chown :newgroup filename_or_dirname
chgrp newgroup filename_or_dirname

# Change the group of a directory and everything in it recursively
chown -R :newgroup dirname
chgrp -R newgroup dirname
```

You can also change both owner and group simultaneously:

```
# Change the owner and the group
sudo chown newowner:newgroup filename_or_dirname

# Change the group of a directory and everything in it recursively
sudo chown -R newowner:newgroup dirname
```

For more information, see the manual pages for `chown` and `chgrp`.

OS X (and other UNIX-based operating systems) provide the `chmod` command for changing the permissions of files and directories.

The `chmod` command, short for “change mode”, is so named because it allows you to modify file or directory __modes__. A mode is a three-digit or four-digit octal representation of the UNIX permissions for a file (or 4-5 digits in languages that require a leading zero, such as C).

There are two basic ways you can use the `chmod` command: numeric modes and human-readable flags.

Most users use `chmod` in its human-readable form:

```
chmod a+rw world_writable_file
```

This command tells `chmod` to add read (`r`) and write (`w`) access to the existing set of permissions for all users (`a`). So if the permissions were originally `r-x--x-w-`, the resulting permissions would be `rwxrwxrw-`.

You can also add and subtract permissions for the owning user (`u`), the group (`g`), or other users (`o`) separately. For example, to add read (`r`), write (`w`), and execute (`x`) permission for the owning user and take it away from members of the owning group and everyone else, you could issue either of the following commands:

```
chmod u+rwx,g-rwx,o-rwx filename
chmod u+rwx,go-rwx filename
chmod a-rwx,u+rwx filename
```

Similarly, you can set the User, Group, or Other permissions without regard to what bits were set before by using equals. For example, to set group permissions to read, no-write, no-execute, you could issue the following command:

```
chmod g=r filename
```

Finally, to make an executable run setuid (`u+s`) and setgid (`g+s`), you might execute a command like one of the following:

```
chmod a+rx,ug+s filename
chmod a+rxs filename    # Note: o+s is ignored.
```

Alternatively, if you know the numeric file mode you want to apply (see [Examining File Permissions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqobnknlts) for details), you can pass the `chmod` command either a three-digit or four-digit mode value:

```
chmod 666 world_writable_file
chmod 0666 world_writable_file
```

The chmod command can also be used to modify POSIX access control lists (ACLs). This use is described later, in [Use chmod to Modify Access Control Lists](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqobnknltcma).

In addition to the standard permission flags, OS X has a few special permission flags that can be set using the `chflags` or [lchflags](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/lchflags.3.html#//apple_ref/doc/man/3/lchflags) command (or with the [chflags](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/chflags.2.html#//apple_ref/doc/man/2/chflags) or [fchflags](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fchflags.2.html#//apple_ref/doc/man/2/fchflags) API in C). These flags are described in the [OS X File System Security](../File%20Management/File%20System%20Programming%20Guide/File%20System%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqobnknlts) section of _[File System Programming Guide](../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

The permissions flags set with `chflags` take precedence over any permissions granted by normal UNIX permissions or access control lists.

The usage of the `chflags` command is fairly straightforward. For example, to make a file immutable (so that it cannot be moved, renamed, deleted, or modified), you can issue one of the following commands:

```
chflags uchg filename # user flag
sudo chflags schg filename # system flag
```

Notice that the flag comes in two variants: the user flag and the system flag. The user flag can be changed by the file’s owner and `root` (just like normal permissions). The system flag can be changed solely by `root`.

To undo this change, you would issue one of the following commands:

```
chflags nouchg filename # user flag
sudo chflags noschg filename # system flag
```

For cross-platform compatibility and readability reasons, OS X supports two other variations on each of these flags: `uchange`, `uimmutable`, `schange`, and `simmutable`. These variants behave identically to their shortened forms.

There are several other flags you can set with the `chflags` command, the most common being the user and system append-only flags (`uappnd`/`uappend` and `sappnd`/`sappend`, respectively).

For more information, read the `chflags` and [lchflags](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/lchflags.3.html#//apple_ref/doc/man/3/lchflags) manual pages and the [OS X File System Security](../File%20Management/File%20System%20Programming%20Guide/File%20System%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqobnknlts) section of _[Security Overview](../Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_.

The `chmod` command is most commonly known for its ability to modify UNIX permissions. However, in OS X, it also does double duty, providing the scripting interfaces for modifying a file’s POSIX access control lists (ACLs).

The basic concept of ACLs is fairly straightforward. An access control list is a list of rules (access control entries, or ACEs).

- Each entry grants or denies the right to access a file or directory in a particular way (the right to read the file, for example).
- For any given right, the first entry in the list that matches against the current user’s user ID or group membership wins.
- If the end of the list is reached without matching anything, the file or directory’s UNIX permissions are used to determine access.

This is a greatly simplified explanation; for full details, read the OS X File System Security section of _[Security Overview](../Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_.

Each ACL entry looks like this:

```
username grant rightname
groupname grant rightname
username deny rightname
groupname deny rightname
```

where _username_ and _groupname_ are the names of a user or group, respectively, and _rightname_ is the name of an access right (`read`, for example).

You can add an access control entry with the `+a` flag to `chmod`. For example, to deny read access on a file to the MySQL user, you would type:

```
chmod +a "_mysql deny read" filename
```

To see the results of your changes, type:

```
ls -le filename
```

By default, new access control list entries are appended to the end of the list. If you need to insert an access control elsewhere in the list, you can use the `+a#` flag. For example, to insert a new rule at position zero (the top of the list), you would issue a command like this one:

```
chmod +a# 0 "_www deny read" filename
```

You can delete an access control entry with the `-a` flag like this:

```
chmod -a "_mysql deny read" filename
```

This command deletes any entry that is an exact match for the specified rule.

Finally, you can replace an entry with another entry using the `=a#` flag. For example, to change the username in the rule inserted above from `_www` to `_mdnsresponder`, you would type:

```
chmod =a# 0 "_mdnsresponder deny read" filename
```

In addition to the basic rules described above, the ACL system in OS X supports inheritance. Any inherited ACL entries for a directory are automatically copied to any new files created within that directory at the time of creation.

You can specify:

- whether an ACL should be inherited by:

  - enclosed files—`file_inherit` right
  - directories—`directory_inherit` right
  - both—`file_inherit,directory_inherit` right
  - neither (the default).
- whether an ACL should be inherited by the children of enclosed directories (the default) or not (`limit_inherit` right).
- whether an ACL should apply to the directory itself (the default) or merely be inherited by things inside it (`only_inherit` right).

You can specify any combination of these flags in an access control entry for a directory by passing the flags as part of the rights list.

For example:

```
chmod +a "_www deny list,search,directory_inherit" dirname
```

This rule prevents the `_www` user from listing the directory’s contents. It also prevents the `_www` user from accessing any files within the specified directory even with an exact name lookup (search). The rule is inherited by any new directory created inside the specified directory (and any directory created inside that one, and so on), but is not inherited by ordinary files.

For more information about the ACL scheme in OS X is described in OS X File System Security section of _[Security Overview](../Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_. For more information about the command-line flags for getting and setting ACLs, see the manual page for `chmod`.

Because the temporary directories in OS X and other UNIX-based operating systems are world-writable, you must take care to ensure that you are modifying the file you think you are modifying.

For example, the following code has two serious bugs:

```
if [ ! -f /tmp/mytempfile ] ; then
    # Race condition here

    touch /tmp/mytempfile

    chmod u=rw,og= /tmp/mytempfile
    # Missing error check here

    echo My secret password is omnibus > /tmp/mytempfile
fi
```

An application that happens to get the timing right can create a file called `/tmp/mytempfile` right after the script checks for its existence, wait for the script to write data into it, and subsequently steal the password. The `chmod` command would produce an error in this case, but because the script doesn’t check the result code, the error is moot.

To solve this problem, always use the `mktemp` command to create temporary files. The `mktemp` command creates files with initial permissions of 0600, and never returns an existing file. (Using `mktemp` also provides an easy way to obtain a known-unique filename, potentially avoiding unexpected behavior caused by temp file collisions.)

The `set` builtin (described in the `sh` man page) sets a number of shell features that can be used to reduce the risk posed by certain types of common programming mistakes. These flags allow your scripts to automatically exit if an unset variable is expanded, automatically exit if any simple commands fail, or automatically export variables.

In addition, the BASH shell provides a flag that causes pipes to return a nonzero exit status when any command in the chain of pipes exits with an error instead of always returning the exit status of the last command. It also supports a flag that limits the effect of environment variables on the interpreter, intended for use in scripts that are expected to be run as a privileged user (for example, the `root` user).

By default, the Bourne shell treats unset variables as empty (unlike `csh`). If your script expects that unset variable to contain a value, this can lead to incorrect script execution and, depending on the script, may even result in a security hole. To guard against this, you can issue the following command:

```
set -u
```

With this flag set, if your script tries to use an empty variable, the shell prints an error message, and the entire script exits immediately with a nonzero exit status.

If desired, you can later restore the default behavior with the following command:

```
set +u
```


For very simple scripts, checking the exit status of each command can be tedious. You can greatly simplify these scripts by instead issuing the following command:

```
set -e
```

With this flag set, if any simple command exits with a nonzero exit status, the shell terminates with that command’s exit status. A simple command is defined as a command that includes no pipes or lists, that is not executed as part of a control statement, and whose exit status is not inverted with an exclamation point.

If desired, you can later restore the default behavior with the following command:

```
set +e
```


It is not always necessary to export variables that your script uses internally. However, if a child process depends on the values of those variables, they must be exported. In some cases, failing to export a variable could even result in a security hole if it causes the child to grant a user access that he or she would otherwise not have. For example, if a CGI script running in a web server environment provides additional limits on what files a remote user can access, a bug in that script might give the user access to other files.

You can, if desired, tell the shell to automatically export any variable that your script sets by issuing the following command:

```
set -a
```

If desired, you can later restore the default behavior with the following command:

```
set +a
```


The exit status of a series of commands connected by pipes is, by default, the exit status of the rightmost command. If you do not examine the output from the final command to ensure that it makes sense, this default behavior can potentially mask errors that might lead to security problems.

For example, consider the following code:

```
ls nonexistentfile | cat
echo $?
```

In the first command, even though the `ls` command fails, the cat command does not care whether it received any input or not, and thus exits with a zero exit status. As a result, the pipe’s exit status is zero. If it is critical to know whether the first command failed (for example, if it performs an operation with an important side effect, such as removing a file on disk), then this is potentially unsafe.

There are many ways that you can fix this problem. The most obvious fix is to store the results of the first command into a variable temporarily, check the result code of the first command, and then use `echo` to pipe the results to the second command. This technique is often less than ideal for commands that take a long time to execute or produce large amounts of output, however, because the second command does not receive any data until after the first command exits. The performance impact is particularly noticeable if the output of the final command is expected to be read by the user.

As an alternative, in BASH, you can issue the following command before issuing the commands above:

```
set -o pipefail
```

After issuing this command, the pipe’s exit status is provided by the rightmost command that failed with a nonzero exit status, or zero if every command in the chain of pipes exited successfully. In the earlier example, the final `echo` command would print the number `1` (the exit status of the `ls` command).

If desired, you can later restore the default behavior with the following command:

```
set +o pipefail
```


For BASH shell scripts (or Bourne shell scripts running in BASH) that must run in a privileged environment (as the `root` user, for example), it is a good idea to tell the shell to not automatically execute any “run commands” files (`.bashrc`, `.profile`, and so on) that may contain alias commands that affect script execution, functions that may override commands in your script, or even malicious commands that an attacker wants your script to execute while running as the `root` user.

To sanitize the script’s environment in this way, you should change your script’s interpreter line to the following:

```
#!/bin/bash -p
```

In this mode, the scripts referenced by the `ENV` and `BASH_ENV` environment variables are not executed, shell functions are not inherited, and the `SHELLOPTS` environment variable is ignored.

[Next](Command%20Line%20Primer.md)[Previous](Performance%20Tuning.md)

